#!/usr/bin/env python3
"""Piloto CVEs-zumbis: captura direta, com data e hora, do estado de registros rejeitados em várias fontes.
Só biblioteca padrão. Rode na sua máquina (precisa de acesso à internet):

  python3 scripts/zumbis.py                 # seis registros de SQLite, fontes padrão
  python3 scripts/zumbis.py CVE-2026-51302  # um registro

Acrescenta uma linha por registro × fonte em data/zumbis-capturas.csv, com o estado classificado:
  rejeição visível · ainda apresentado como válido · misto · removido · indisponível para consulta · inconclusivo
Uma página que preserva o registro e mostra a rejeição conta como correção propagada, não como falha.
A classificação é por palavras-chave; confira à mão as linhas "inconclusivo" e "misto".
"""
import csv, re, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "data" / "zumbis-capturas.csv"
PADRAO = ["CVE-2026-51296", "CVE-2026-51297", "CVE-2026-51300", "CVE-2026-51302", "CVE-2026-51303", "CVE-2026-51304"]
FONTES = {
    "CVE Program (API)": "https://cveawg.mitre.org/api/cve/{id}",
    "NVD (API 2.0)": "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={id}",
    "OSV (API)": "https://api.osv.dev/v1/vulns/{id}",
    "GitHub Advisories": "https://github.com/advisories?query={id}",
    "Red Hat (API)": "https://access.redhat.com/hydra/rest/securitydata/cve/{id}.json",
    "Debian": "https://security-tracker.debian.org/tracker/{id}",
    "Ubuntu": "https://ubuntu.com/security/{id}",
    "SUSE": "https://www.suse.com/security/cve/{id}.html",
    "INCIBE-CERT": "https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/{idl}",
    "OpenCVE": "https://app.opencve.io/cve/{id}",
    "Feedly": "https://feedly.com/cve/{id}",
    "SentinelOne": "https://www.sentinelone.com/vulnerability-database/{idl}/",
    "cvefeed.io": "https://cvefeed.io/vuln/detail/{id}",
}
REJ = re.compile(r'REJECTED|DO NOT USE THIS CVE RECORD|"withdrawn"\s*:|\bwithdrawn\b|fictitious|Rejected reason|"vulnStatus"\s*:\s*"Rejected"', re.I)
VAL = re.compile(r"CVSS|use-after-free|baseScore|severity|Critical|High\b", re.I)
NAO = re.compile(r"not affected|não afetado", re.I)


def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "poisonAI-piloto-zumbis/0.1 (pesquisa acadêmica)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # rede, TLS, tempo
        return None, str(e)


def classificar(status, corpo, cve):
    if status in (404, 410):
        return "removido"
    if status is None or status >= 400:
        return "indisponível para consulta"
    if cve not in corpo:
        return "inconclusivo"
    rej, val = bool(REJ.search(corpo)), bool(VAL.search(corpo))
    if rej and re.search(r"Critical|9\.\d|10\.0", corpo):
        return "misto"
    if rej:
        return "rejeição visível"
    if NAO.search(corpo):
        return "não afetado (sem citar a rejeição)"
    return "ainda apresentado como válido" if val else "inconclusivo"


def main():
    ids = [a for a in sys.argv[1:] if a.upper().startswith("CVE-")] or PADRAO
    novo = not SAIDA.exists()
    with SAIDA.open("a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if novo:
            w.writerow(["capturado_em_utc", "cve", "fonte", "url", "http", "estado", "bytes"])
        for cve in ids:
            for nome, modelo in FONTES.items():
                url = modelo.format(id=cve, idl=cve.lower())
                st, corpo = baixar(url)
                estado = classificar(st, corpo, cve)
                agora = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                w.writerow([agora, cve, nome, url, st or "", estado, len(corpo)])
                print(f"{cve}  {nome:22} {st or '-':>4}  {estado}")
                time.sleep(1.5)  # gentileza com os servidores
    print(f"\nCapturas acrescentadas a {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
