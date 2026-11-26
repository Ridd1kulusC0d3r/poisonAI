#!/usr/bin/env python3
"""Reconstrói, a partir da lista oficial de CVEs (CVEProject/cvelistV5), o histórico dos
registros que citam um repositório de origem. Só biblioteca padrão + git.

Uso:
  python3 scripts/caso_cve.py                      # clona (parcial) e gera data/caso-sqlite-registros.json
  python3 scripts/caso_cve.py --clone CAMINHO      # reaproveita um clone já feito

O clone é parcial (sem blobs, a partir de 25/07/2026): cerca de 80 MB.
Escopo: o bloco cves/2026/51xxx, onde estão os identificadores do lote. Um registro de outro
bloco que cite o mesmo repositório não entra; o relatório diz isso.
"""
import json, subprocess, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REPO_ORIGEM = "programmervuln"
BLOCO = "cves/2026/51xxx/"
DESDE = "2026-07-25"
JFROG = {"CVE-2026-51296", "CVE-2026-51297", "CVE-2026-51300", "CVE-2026-51302", "CVE-2026-51303", "CVE-2026-51304"}


def git(repo, *a):
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, check=False).stdout


def clonar(destino):
    subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", f"--shallow-since={DESDE}",
                    "--single-branch", "https://github.com/CVEProject/cvelistV5.git", str(destino)], check=True)


def notas(cont):
    return [v.get("baseScore") for m in cont.get("metrics", []) for k, v in m.items() if k.startswith("cvss")]


def produto(desc):
    d = desc.lower()
    if "sqlite" in d: return "SQLite"
    if "libraw" in d: return "LibRaw"
    if "esp32" in d or "audioi2s" in d: return "ESP32-audioI2S"
    return "outro"


def main():
    clone = None
    if "--clone" in sys.argv:
        clone = Path(sys.argv[sys.argv.index("--clone") + 1])
    else:
        clone = Path(tempfile.mkdtemp()) / "cvelist"
        clonar(clone)
    cabeca = git(clone, "rev-parse", "HEAD").strip()
    regs = []
    for f in git(clone, "ls-tree", "--name-only", "HEAD", BLOCO).split():
        log = [l.split(" ", 1) for l in git(clone, "log", "--format=%H %cI", "--", f).splitlines()][::-1]
        if not log or not any(REPO_ORIGEM in git(clone, "show", f"{h}:{f}") for h, _ in log[:1]):
            # o repositório de origem aparece já na primeira versão publicada; versões rejeitadas apagam as referências
            continue
        hist, pub, cisa, rej, desc = [], None, [], None, ""
        for h, t in log:
            d = json.loads(git(clone, "show", f"{h}:{f}"))
            m, c = d["cveMetadata"], d.get("containers", {})
            adp = {a.get("providerMetadata", {}).get("shortName"): notas(a) for a in c.get("adp", [])}
            hist.append(dict(commit=h[:10], quando=t, estado=m["state"], cna=notas(c.get("cna", {})), adp=adp))
            if m["state"] == "PUBLISHED":
                if not pub:
                    pub = t
                    desc = (c["cna"].get("descriptions") or [{}])[0].get("value", "")
                s = adp.get("CISA-ADP") or []
                if s and (not cisa or cisa[-1][1] != s[0]):
                    cisa.append([t, s[0]])
            elif m["state"] == "REJECTED" and not rej:
                rej = t
                motivo = (c.get("cna", {}).get("rejectedReasons") or [{}])[0].get("value", "")
        horas = lambda a, b: round((datetime.fromisoformat(b) - datetime.fromisoformat(a)).total_seconds() / 3600, 1)
        cve = d["cveMetadata"]["cveId"]
        regs.append(dict(cve=cve, produto=produto(desc), examinado_jfrog=cve in JFROG, publicado=pub,
                         cisa_adp=cisa, horas_ate_cisa=horas(pub, cisa[0][0]) if cisa else None,
                         rejeitado=rej, horas_publicado=horas(pub, rej) if rej else None,
                         motivo_rejeicao=motivo if rej else "", historico=hist))
    regs.sort(key=lambda r: r["cve"])
    saida = dict(fonte="https://github.com/CVEProject/cvelistV5", commit=cabeca, bloco=BLOCO, repositorio_citado=REPO_ORIGEM,
                 gerado_em=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), registros=regs,
                 nota="Datas são as dos commits da lista oficial (UTC). Enriquecimento = contêiner ADP da CISA (Vulnrichment) com nota CVSS. "
                      "O escopo é o bloco 51xxx; registros do mesmo lote em outros blocos não entram.")
    (RAIZ / "data" / "caso-sqlite-registros.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    n = len(regs)
    print(f"{n} registros; rejeitados: {sum(1 for r in regs if r['rejeitado'])}; com CISA-ADP: {sum(1 for r in regs if r['cisa_adp'])}")


if __name__ == "__main__":
    main()
