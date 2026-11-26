#!/usr/bin/env python3
"""Gera os documentos em docs/ a partir de data/. Só biblioteca padrão.

    python3 scripts/gerar_docs.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS, DOCS = RAIZ / "data", RAIZ / "docs"
AVISO = "<!-- Gerado por scripts/gerar_docs.py a partir de data/. Edite os JSON, não este arquivo. -->\n\n"


def ler(nome):
    return json.loads((DADOS / nome).read_text(encoding="utf-8"))


def cel(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def tabela(cab, linhas):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    out += ["| " + " | ".join(cel(c) for c in l) + " |" for l in linhas]
    return "\n".join(out) + "\n"


def link(it):
    return f"[{it['tit']}]({it['links'][0]['url']})" if it["links"] else it["tit"]


def escrever(nome, texto):
    (DOCS / nome).write_text(AVISO + texto, encoding="utf-8")
    print("docs/" + nome)


def pontuar():
    """Reusa o cálculo do score de construir.py para manter uma só fórmula."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("construir", RAIZ / "scripts" / "construir.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    _, itens, erros = mod.montar()
    if erros:
        raise SystemExit("\n".join(erros))
    return itens


def main():
    DOCS.mkdir(exist_ok=True)
    itens = pontuar()
    tax, agenda, intel = ler("taxonomia.json"), ler("agenda.json"), ler("inteligencia.json")
    conf, pautas, atores = ler("conferencias.json"), ler("pautas.json"), ler("atores.json")
    por = {i["key"]: i for i in itens}
    peso = {t["n"]: t["p"] for t in tax["tipos_de_estudo"]}

    # catálogo por tipo de estudo
    t = ["# Catálogo por tipo de estudo\n",
         f"{len(itens)} trabalhos. O peso (1 a 5) mede a força para afirmar algo sobre o mundo real; veja [METODOLOGIA.md](../METODOLOGIA.md).\n"]
    for tipo in sorted(tax["tipos_de_estudo"], key=lambda x: -x["p"]):
        its = sorted([i for i in itens if i["met"] == tipo["n"]], key=lambda i: (-i["ano"], i["tit"]))
        if not its:
            continue
        t.append(f"\n## {tipo['n']} · peso {tipo['p']} · {len(its)} trabalhos\n")
        t.append(f"Prova: {tipo['prova']} Não prova: {tipo['nao']}\n")
        t.append(tabela(["Score", "Ano", "Trabalho", "Veículo", "Lado", "Nota", "Status"],
                        [[i["score"], i["ano"], link(i), i["veic"], tax["lados"][i["lado"]], i["nota_fonte"], i["st"]] for i in its]))
    escrever("CATALOGO.md", "\n".join(t))

    # ordem de leitura
    t = ["# Ordem de leitura\n",
         "Score de 0 a 100 calculado por `scripts/construir.py`; a fórmula está em [METODOLOGIA.md](../METODOLOGIA.md). É uma régua para decidir a ordem, não uma nota de qualidade.\n"]
    for classe in ("Leia primeiro", "Leia depois", "Consulta"):
        its = sorted([i for i in itens if i["classe"] == classe], key=lambda i: (-i["score"], -i["ano"]))
        t.append(f"\n## {classe} ({len(its)})\n")
        t.append(tabela(["Score", "Trabalho", "Ano", "Tipo de estudo", "Nota", "Por quê"],
                        [[i["score"], link(i), i["ano"], i["met"], i["nota_fonte"],
                          ", ".join(f"{k} {v}" for k, v in i["score_partes"].items() if v)] for i in its]))
    escrever("LEITURA.md", "\n".join(t))

    # hipóteses concorrentes e julgamentos
    I = intel["intel"]
    hs = [h[0] for h in I["hip"]]
    t = ["# Hipóteses concorrentes, indicadores e julgamentos\n", f"**Pergunta:** {I['pergunta']}\n", "## Hipóteses\n"]
    t += [f"- **{h[0]}.** {h[1]}" for h in I["hip"]]
    t.append("\n## Matriz (C consistente, N neutra, I inconsistente)\n")
    t.append(tabela(["Evidência"] + hs, [[f"{e[0]}. {e[1]}"] + list(e[2]) for e in I["ev"]]))
    inc = [sum(1 for e in I["ev"] if e[2][j] == "I") for j in range(len(hs))]
    t.append("Inconsistências por hipótese: " + ", ".join(f"{h} = {n}" for h, n in zip(hs, inc)) + ". Pela regra de Heuer, mais inconsistência é hipótese mais fraca.\n")
    t.append(f"\n## Leitura\n\n{I['leitura']}\n")
    t += [f"- {j}" for j in I["julgamento"]]
    t.append("\n## Julgamentos-chave\n")
    t.append(tabela(["#", "Julgamento", "Probabilidade", "Confiança", "Base"], I["jcs"]))
    t.append("\n## Indicadores e alertas\n")
    t.append(tabela(["#", "Indicador", "Favorece", "Onde observar"], I["indic"]))
    t.append("\n## Cenários (12 a 24 meses)\n")
    t.append(tabela(["Cenário", "Descrição", "Probabilidade", "Sinais"], I["cenarios"]))
    t.append("\n## Premissas-chave\n")
    t.append(tabela(["#", "Premissa", "Sustentação", "Se estiver errada"], I["premissas"]))
    escrever("HIPOTESES.md", "\n".join(t))

    # Brasil
    br = sorted([i for i in itens if "br" in i["tags"]], key=lambda i: (-i["ano"], i["tit"]))
    t = ["# Brasil e lusofonia\n"] + [f"- {x}" for x in I["brleit"]]
    t.append("\n## Trabalhos\n")
    t.append(tabela(["Ano", "Trabalho", "Tipo de estudo", "Status", "Nota"], [[i["ano"], link(i), i["met"], i["st"], i["nota"]] for i in br]))
    t.append("\n## Intenção, capacidade e oportunidade para defensores no Brasil\n")
    t.append(tabela(["Ator", "Intenção", "Capacidade", "Oportunidade", "Prioridade"], I["ico"]))
    t.append("\n## Correspondência de nomes\n")
    t.append(tabela(["Cluster", "Quem rastreia", "Relação", "Observação"], I["corresp"]))
    escrever("BRASIL.md", "\n".join(t))

    # agenda
    t = ["# Agenda de pesquisa\n", "## Tese\n"] + [f"- {x}" for x in agenda["tese"]]
    t.append("\n## Perguntas prioritárias\n")
    t += [f"- **{p[0]}.** {p[1]} (ligadas: {', '.join(p[2])})" for p in I["pirs"]]
    t.append("\n## Banco de perguntas\n")
    t.append(tabela(["#", "Pergunta", "Hipótese", "Como testar", "Origem", "Tema", "Prioridade", "Relação"], agenda["perguntas"]))
    t.append("\n## Lacunas confirmadas\n")
    t.append(tabela(["Lacuna", "Evidência", "Origem"], agenda["lacunas"]))
    t.append("\n## Fases\n")
    for f in agenda["fases"]:
        t.append(f"\n### {f[0]}\n")
        t += [f"- [ ] {x}" for x in f[1]]
    escrever("AGENDA.md", "\n".join(t))

    # conferências
    t = ["# Conferência das fontes\n", "Registro de correções. Zero correção não é a meta; honestidade é.\n",
         "## Afirmações do artigo âncora e do dossiê 1\n", tabela(["Afirmação", "Veredito", "Nota"], conf["ancora"]),
         "\n## Afirmações dos dossiês 2 a 5\n", tabela(["Afirmação", "Veredito", "Nota"], conf["dossies"]),
         "\n## Pistas ainda não promovidas\n",
         tabela(["Categoria", "Ano", "Pista", "Onde", "Nota"], [[p["cat"], p["ano"] or "—", p["tit"], p["onde"], p["nota"]] for p in conf["pistas"]]),
         "\n## Status por trabalho\n"]
    cont = {}
    for i in itens:
        cont[i["st"]] = cont.get(i["st"], 0) + 1
    t.append(tabela(["Status", "Trabalhos"], sorted(cont.items(), key=lambda x: -x[1])))
    escrever("CONFERENCIA.md", "\n".join(t))

    # pautas
    t = ["# Pautas de episódios\n"]
    for s, nome in pautas["series"].items():
        t.append(f"\n## {nome}\n")
        for p in [p for p in pautas["pautas"] if p[0] == s]:
            fontes = "; ".join(link(por[k]) for k in p[3] if k in por)
            t.append(f"- [ ] **{p[1]}.** {p[2]} Fontes: {fontes}")
    escrever("PAUTAS.md", "\n".join(t))

    # atores
    t = ["# Atores\n", "Rótulos de fornecedores mantidos como publicados; sobreposição não é sinônimo.\n"]
    t.append(tabela(["Ator", "Também", "Origem", "Tipo", "Confiança", "Prioridade", "O que fez"],
                    [[a["nome"], a.get("aka", ""), a["origem"], a["tipo"], a.get("conf", ""), a.get("prio") or "—", a["oque"]] for a in atores]))
    escrever("ATORES.md", "\n".join(t))
    # a virada (dossiê 6) e o desenho do dossiê 7
    I = intel["intel"]; V = I.get("virada")
    if V:
        t = ["# A virada: o envenenamento já aconteceu, e não foi espião\n", f"**Antes:** {V['antes']}\n", f"**Agora:** {V['agora']}\n", f"> {V['frase']} ({V['frase_fonte']})\n"]
        t += [f"{n}. **{c[0]}.** {c[1]}" for n, c in enumerate(V["consequencias"], 1)]
        t.append("\n## Correções aos dossiês 1 a 5\n")
        t.append(tabela(["Onde", "Como estava", "Correção"], I["correcoes"]))
        t.append("\n## Cinco projetos com dados públicos\n")
        t.append(tabela(["#", "Projeto", "Por que", "Como", "Prazo e cuidado", "Pergunta"], I["projetos"]))
        D7 = I["desenho"]
        t.append(f"\n## Desenho experimental do dossiê 7\n\n**Pergunta:** {D7['pergunta']}\n\n**Base:** {D7['base']}\n")
        t.append(tabela(["Fator", "Níveis"], D7["fatores"]))
        for tit, k in [("Métricas", "metricas"), ("Hipóteses", "hipoteses"), ("Regras", "regras")]:
            t.append(f"\n**{tit}**\n"); t += [f"- {x}" for x in D7[k]]
        t.append("\n**Ler antes:** " + ", ".join(link(por[k]) for k in D7["itens"] if k in por))
        escrever("VIRADA.md", "\n".join(t))
    # dossiê 7 por score da dissertação
    D7 = intel["intel"].get("dossie7")
    if D7:
        rows = []
        for k, fam, rel, passo, custo, porq in D7["itens"]:
            it = por.get(k)
            if not it:
                continue
            base = int(it["score"] / 2 + 0.5)
            tot = base + rel * 10 + (10 if passo else 0) + (10 if custo else 0)
            cl = "Núcleo da dissertação" if tot >= 70 else "Ler no semestre" if tot >= 50 else "Consulta"
            rows.append((tot, it["score"], [str(tot), cl, link(it), fam, f"{base} + {rel*10} + {10 if passo else 0} + {10 if custo else 0}", f"passo {passo}" if passo else "—", it.get("nota_fonte", "—"), porq]))
        rows.sort(key=lambda r: (-r[0], -r[1]))
        t = ["# Dossiê 7 por score da dissertação\n", D7["regra"] + "\n", "Componentes: geral ÷ 2 + relevância + ordem do dossiê + custo ou limite.\n"]
        t.append(tabela(["Score", "Classe", "Trabalho", "Família", "Componentes", "Ordem", "Nota", "Por que ler"], [r[2] for r in rows]))
        t.append("\n## Ordem de leitura sugerida pelo dossiê 7\n")
        t += [f"{n}. {o}" for n, o in enumerate(D7["ordem"], 1)]
        escrever("DOSSIE7.md", "\n".join(t))
    # ficha canônica do caso SQLite e piloto de retratações
    def opc(nome):
        f = DOCS.parent / "data" / nome
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None
    C, R, P = opc("caso-sqlite.json"), opc("caso-sqlite-registros.json"), opc("piloto-retratacao.json")
    if C and R:
        t = [f"# Ficha canônica: {C['titulo']}\n", f"**{C['rotulo']}.** {C['escopo_busca']}\n", "## As quatro perguntas\n"]
        for q in C["perguntas"]:
            t.append(f"### {q['q']}\n\n{q['r']}\n\n*Certeza: {q['certeza']}*\n")
        t.append("## Linha do tempo\n")
        t.append(tabela(["Data", "O quê", "Fonte"], C["linha_do_tempo"]))
        t.append(f"\n## Os registros na lista oficial\n\nFonte: {R['fonte']}, commit {R['commit'][:10]}. {R['nota']} Reproduza com `python3 scripts/caso_cve.py`.\n")
        t.append(tabela(["Registro", "Produto", "Examinado pela JFrog", "Publicado (UTC)", "Nota da CISA", "Horas até a nota", "Rejeitado (UTC)", "Horas publicado"],
                        [[r["cve"], r["produto"], "sim" if r["examinado_jfrog"] else "", r["publicado"][:16].replace("T", " "),
                          " → ".join(str(c[1]) for c in r["cisa_adp"]) or "sem nota", str(r["horas_ate_cisa"] or "—"), (r["rejeitado"] or "")[:16].replace("T", " "), str(r["horas_publicado"])] for r in R["registros"]]))
        t.append("\n## Que evidência futura distinguiria H7\n")
        t += [f"- {x}" for x in C["discriminar_h7"]]
        t.append("\n## Correções feitas\n")
        t += [f"- {x}" for x in C["correcoes"]]
        if P:
            t.append(f"\n## Piloto de retratações (versão 0, {P['observado_em']})\n\n{P['metodo']}\n\n**Limites:** {P['limites']}\n")
            t.append(tabela(["Registro", "Fonte", "Estado", "Última modificação exibida", "O que a cópia mostra"],
                            [[o["cve"], f"[{o['fonte']}]({o['url']})", o["estado"], o["ultima_mod"] or "não exibida", o["nota"]] for o in P["obs"]]))
            t.append("\nCaptura direta, com data e hora: `python3 scripts/zumbis.py` (acrescenta linhas em `data/zumbis-capturas.csv`).")
        escrever("CASO-SQLITE.md", "\n".join(t))


if __name__ == "__main__":
    main()
