#!/usr/bin/env python3
"""Valida os dados e gera o site (site/index.html) e a bibliografia (data/referencias.bib).

Só biblioteca padrão. Uso:
    python3 scripts/construir.py            # valida e gera
    python3 scripts/construir.py --checar   # só valida
"""
import json, re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data"
STATUS = ("Conferido na fonte", "Conferido via cobertura", "Preprint conferido",
          "Dossiê A", "Dossiê B", "Alegação (C)", "A conferir")


def ler(nome):
    return json.loads((DADOS / nome).read_text(encoding="utf-8"))


def tex(s):
    rep = {"á": "{\\'a}", "é": "{\\'e}", "í": "{\\'\\i}", "ó": "{\\'o}", "ú": "{\\'u}", "ã": "{\\~a}", "õ": "{\\~o}",
           "ç": "{\\c c}", "è": "{\\`e}", "ê": "{\\^e}", "â": "{\\^a}", "ô": "{\\^o}", "ñ": "{\\~n}", "&": "\\&",
           "–": "--", "—": "---"}
    return "".join(rep.get(c, c) for c in s)


def bib(it):
    typ = {"Conferência": "inproceedings", "Periódico": "article", "Periódico (revisão)": "article",
           "Revisão sistemática": "misc", "Preprint": "misc"}.get(it["tipo"], "techreport" if it["ft"] != "AC" else "misc")
    au = " and ".join(tex(a) for a in it["aut"]) or "{a conferir}"
    f = [f"  author    = {{{au}}}", f"  title     = {{{{{tex(it['tit'])}}}}}", f"  year      = {{{it['ano']}}}"]
    venue = tex(it["veic"])
    campo = {"article": "journal", "inproceedings": "booktitle", "techreport": "institution"}.get(typ, "howpublished")
    f.append(f"  {campo} = {{{venue}}}")
    if it.get("doi"):
        f.append(f"  doi       = {{{it['doi']}}}")
    if it["links"]:
        f.append(f"  url       = {{{it['links'][0]['url']}}}")
    m = re.search(r"arXiv (\d{4}\.\d{4,5})", it["veic"]) or re.search(r"arXiv\.(\d{4}\.\d{4,5})", it.get("doi", ""))
    if m:
        f += [f"  eprint    = {{{m.group(1)}}}", "  archiveprefix = {arXiv}"]
    f.append(f"  keywords  = {{eixo{it['eixo']}, {it['met']}, {it['st']}}}")
    return f"@{typ}{{{it['key']},\n" + ",\n".join(f) + "\n}\n"


NUCLEO = {"aluc", "valid", "poison", "rag", "mem", "inj", "soc", "osintia", "humano", "desinf", "br", "admissao"}
NOTA = {"Conferido na fonte": "A", "Preprint conferido": "A", "Dossiê A": "A", "Conferido via cobertura": "B",
        "Dossiê B": "B", "Alegação (C)": "D", "A conferir": "—"}
PESO_NOTA = {"A": 10, "B": 6, "C": 4, "D": 2, "—": 0}
PESO_REV = {"Revisado por pares": 10, "Preprint": 6, "Literatura cinzenta": 3}


def nota_fonte(it):
    """Escala do LLmInjection (A a E). Cobertura de imprensa vale C."""
    n = it.get("grade") or NOTA[it["st"]]
    if n == "B" and it["ft"] == "IM":
        n = "C"
    return n


def score_leitura(it, peso, refs, trilha):
    """Score de leitura de 0 a 100. A fórmula está em METODOLOGIA.md."""
    rec = 10 if it["ano"] >= 2026 else 8 if it["ano"] == 2025 else 6 if it["ano"] == 2024 else 4 if it["ano"] >= 2021 else 2
    partes = {
        "evidencia": peso * 6,
        "nucleo": min(len(NUCLEO & set(it["tags"])), 3) * 5,
        "conexoes": min(refs, 5) * 3,
        "verificacao": PESO_NOTA[it["nota_fonte"]],
        "revisao": PESO_REV[it["pr"]],
        "recencia": rec,
        "trilha": 10 if it["key"] in trilha else 0,
    }
    total = sum(partes.values())
    classe = "Leia primeiro" if total >= 70 else "Leia depois" if total >= 50 else "Consulta"
    return total, classe, partes


def opcional(nome):
    """JSON gerado por scripts próprios (caso, piloto, medição); ausente vira None."""
    f = RAIZ / "data" / nome
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None


def resumo_registros(d):
    """Tira o histórico completo de cada registro para o site (fica no JSON do repositório)."""
    if not d:
        return None
    return dict(fonte=d["fonte"], commit=d["commit"][:10], nota=d["nota"],
                registros=[{k: r[k] for k in ("cve", "produto", "examinado_jfrog", "publicado", "cisa_adp", "horas_ate_cisa", "rejeitado", "horas_publicado")} for r in d["registros"]])


def montar():
    tax = ler("taxonomia.json")
    itens_brutos = ler("itens.json")
    agenda = ler("agenda.json")
    intel = ler("inteligencia.json")
    off = ler("ofensiva.json")
    defe = ler("defesa.json")
    pautas = ler("pautas.json")
    conf = ler("conferencias.json")
    rec = ler("recursos.json")
    atores = ler("atores.json")
    cadeia = ler("cadeia.json")
    tempo = ler("linha-do-tempo.json")
    metodos = [t["n"] for t in tax["tipos_de_estudo"]]
    erros = []

    itens, chaves = [], set()
    for i, bruto in enumerate(itens_brutos, 1):
        it = dict(bruto)
        it["id"] = i
        k = it["key"]
        if k in chaves:
            erros.append(f"chave repetida: {k}")
        chaves.add(k)
        for t in it["tags"]:
            if t not in tax["temas"]:
                erros.append(f"{k}: tema desconhecido {t}")
        if it["met"] not in metodos:
            erros.append(f"{k}: tipo de estudo desconhecido {it['met']}")
        if it["lado"] not in tax["lados"]:
            erros.append(f"{k}: lado desconhecido {it['lado']}")
        if it["st"] not in STATUS:
            erros.append(f"{k}: status desconhecido {it['st']}")
        if str(it["eixo"]) not in tax["eixos"]:
            erros.append(f"{k}: eixo desconhecido {it['eixo']}")
        for l in it["links"]:
            if not l["url"].startswith("https://"):
                erros.append(f"{k}: link sem https {l['url']}")
        it.setdefault("doi", ""); it.setdefault("repo", []); it.setdefault("num", [])
        it["url"] = ""; it["cit"] = ""
        tipos = [l["kind"] for l in it["links"]]
        it["acc"] = next((x for x in ["pdf", "aberto", "dados", "editor", "registro"] if x in tipos), "busca")
        it["dos"] = it.get("dos") or [0]
        it["org"] = "; ".join(tax["origens"][str(d)] for d in it["dos"])
        it["pr"] = ("Revisado por pares" if it["tipo"] in ("Conferência", "Periódico", "Periódico (revisão)")
                    else "Preprint" if it["tipo"] in ("Preprint", "Revisão sistemática") else "Literatura cinzenta")
        it["bib"] = bib(it)
        itens.append(it)

    refs = []
    refs += list(agenda["qp_itens"].values())
    refs += [s["itens"] for s in cadeia] + [a["fontes"] for a in atores] + [g["keys"] for g in rec["familias"]]
    refs += [[t["key"]] for t in rec["trilha"]] + [[t["item"]] for t in tempo] + [p[3] for p in pautas["pautas"]]
    refs += [e[4] for e in off["estagios"]] + [[e[2]] for e in off["efeitos"]] + [[e[2]] for e in off["escada"]]
    refs += [[p[2]] for p in defe["passos"]] + [[e[3]] for e in intel["intel"]["ev"]]
    for ks in refs:
        for k in ks:
            if k not in chaves:
                erros.append(f"referência a item inexistente: {k}")
    for q in agenda["qps"]:
        q["itens"] = agenda["qp_itens"][q["id"]]

    contagem = {}
    for ks in refs:
        for k in ks:
            contagem[k] = contagem.get(k, 0) + 1
    trilha = {t["key"] for t in rec["trilha"]}
    pesos = {t["n"]: t["p"] for t in tax["tipos_de_estudo"]}
    for it in itens:
        it["nota_fonte"] = nota_fonte(it)
        it["score"], it["classe"], it["score_partes"] = score_leitura(it, pesos[it["met"]], contagem.get(it["key"], 0), trilha)

    payload = dict(
        items=itens, eixos=tax["eixos"], ft=tax["tipos_de_fonte"], topics=tax["temas"], topicOrder=tax["ordem_temas"],
        methods=metodos, topicInfo=tax["info_temas"], pairNotes=tax["notas_pares"], actors=atores, stages=cadeia,
        qps=agenda["qps"], metrics=agenda["metricas"], venues=agenda["veiculos"], checks=conf["ancora"],
        pistas=conf["pistas"], groups=rec["familias"], trail=rec["trilha"], frameworks=rec["frameworks"],
        study=tax["tipos_de_estudo"], lados=tax["lados"], orig=tax["origens"],
        tl=[dict(d=t["data"], t=t["titulo"], x=t["texto"], c=t["categoria"], k=t["item"]) for t in tempo],
        tlcat=tax["categorias_tempo"], off=off, defe=defe, rq=agenda["perguntas"], lacunas=agenda["lacunas"],
        fases=agenda["fases"], tese=agenda["tese"], epis=pautas["pautas"], episSer=pautas["series"],
        dchecks=conf["dossies"], grupos=rec["grupos_acompanhar"], intel=intel["intel"], crit=intel["critica"],
        repo=rec["llminjection"], repos=rec["repositorios"], queries=rec["consultas"],
        caso=opcional("caso-sqlite.json"), casoReg=resumo_registros(opcional("caso-sqlite-registros.json")),
        piloto=opcional("piloto-retratacao.json"), medicao=opcional("medicao-portao.json"),
        code=(RAIZ / "scripts" / "dose_resposta.py").read_text(encoding="utf-8"),
        updated=(RAIZ / "data" / "ATUALIZADO").read_text(encoding="utf-8").strip())
    return payload, itens, erros


def main():
    payload, itens, erros = montar()
    if erros:
        print("\n".join(erros))
        sys.exit(1)
    print(f"ok: {len(itens)} trabalhos, {len(payload['actors'])} atores, {len(payload['rq'])} perguntas")
    if "--checar" in sys.argv:
        return
    js = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = (RAIZ / "site" / "template.html").read_text(encoding="utf-8").replace("__DATA__", js)
    (RAIZ / "site" / "index.html").write_text(html, encoding="utf-8")
    (RAIZ / "data" / "referencias.bib").write_text("\n".join(i["bib"] for i in itens), encoding="utf-8")
    print(f"site/index.html ({len(html) // 1024} KiB) e data/referencias.bib gerados")


if __name__ == "__main__":
    main()
