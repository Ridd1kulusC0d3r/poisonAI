#!/usr/bin/env python3
"""Medição reproduzível do portão de admissão em dados sintéticos: documento legítimo rejeitado
não é o mesmo que fato legítimo perdido. Só biblioteca padrão, determinístico.

  python3 scripts/medir_portao.py      # gera data/medicao-portao.json e docs/MEDICAO-PORTAO.md

Cenário
- Base já indexada: 20 campanhas (c01 a c20), 15 relatórios cada, de 8 fontes conhecidas e antigas.
- Lote que chega ao portão:
  * 30 fatos novos e verdadeiros (campanhas c21 a c50), com redundância diferente:
    10 com 1 relatório, 10 com 3 e 10 com 8. Metade dos relatórios vem de fontes conhecidas,
    metade de fontes novas (poucos dias de histórico).
  * 20 atualizações verdadeiras de campanhas antigas, de fontes conhecidas.
  * Veneno: 3 relatórios por alvo contra 10 campanhas antigas (c01 a c10), atribuindo-as ao APT-B,
    no estilo que imita a pergunta do analista.
- Perguntas: as 10 campanhas atacadas, os 30 fatos novos e 10 campanhas de controle (c11 a c20).
- Resposta: busca BM25 filtrada pela campanha da pergunta (como um assistente que liga a pergunta à entidade),
  5 documentos, maioria simples. Sem o filtro, o veneno que imita a pergunta captura também as perguntas
  sobre outras campanhas, e a medição deixa de separar os efeitos.

Métricas por condição
- documentos legítimos rejeitados (% dos 50 legítimos do lote)
- fatos novos perdidos: % dos 30 fatos que perderam todas as fontes (por redundância 1, 3 e 8)
- veneno admitido (% dos relatórios envenenados)
- decisões corretas: alvos, fatos novos, controle e total (50 perguntas)
"""
import json, math, re, unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
STOP = set("a o os as de da do das dos e é em no na nos nas um uma que por com para se ao à".split())


def tok(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return [w for w in re.split(r"[^a-z0-9]+", t) if w and w not in STOP]


class Rng:  # o mesmo LCG do laboratório do site
    def __init__(self, s): self.s = s
    def __call__(self):
        self.s = (self.s * 1103515245 + 12345) % 2147483648
        return self.s / 2147483648


SRC = [("Fornecedor Alfa", 1900), ("CSIRT Nacional", 2600), ("Laboratório Beta", 1400), ("ISAC Financeiro", 1100),
       ("Fornecedor Gama", 900), ("Pesquisador Ômega", 700), ("Boletim Delta", 1600), ("Equipe Sigma", 1250)]
TOOLS = ["um loader em PowerShell", "um RAT modular", "credenciais roubadas", "phishing com anexo ISO", "um webshell em ASPX", "tunelamento DNS"]
INFRA = ["VPS alugadas na Europa", "domínios recém-registrados", "roteadores comprometidos", "serviços de nuvem gratuitos"]
MODELOS = ["{a} observou a campanha-{c} usando {t} e {i}. Atribuição: {x}.",
           "Na campanha-{c}, os operadores recorreram a {t}. Indicadores ligam a atividade ao {x}.",
           "Relatório sobre a campanha-{c}: {i} e {t}; avaliamos o {x} como responsável.",
           "Atualização da campanha-{c}. Sobreposição de infraestrutura ({i}) com operações anteriores do {x}."]


def doc(txt, camp, actor, autor, idade, tipo):
    return dict(txt=txt, camp=camp, actor=actor, autor=autor, idade=idade, tipo=tipo)


def base():
    r, D = Rng(7), []
    for c in range(1, 21):
        cid, x = f"{c:02d}", ("APT-A" if c % 2 == 0 else "APT-C")
        for k in range(15):
            a = SRC[(c + k) % 8]
            D.append(doc(MODELOS[k % 4].format(a=a[0], c=cid, t=TOOLS[int(r() * 6)], i=INFRA[int(r() * 4)], x=x), cid, x, a[0], a[1], "base"))
    return D


def lote(ataque):
    r, B = Rng(11), []
    atores = ["APT-D", "APT-E", "APT-F"]
    for n, c in enumerate(range(21, 51)):
        cid, x = f"{c:02d}", atores[n % 3]
        k = 1 if c <= 30 else 3 if c <= 40 else 8
        for j in range(k):
            if (c + j) % 2 == 0:
                a = SRC[(c + j) % 8]
            else:
                a = (f"Fonte nova {cid}-{j}", 3 + int(r() * 22))
            B.append(doc(MODELOS[j % 4].format(a=a[0], c=cid, t=TOOLS[int(r() * 6)], i=INFRA[int(r() * 4)], x=x), cid, x, a[0], a[1], f"novo{k}"))
    for c in range(1, 21):
        cid, x = f"{c:02d}", ("APT-A" if c % 2 == 0 else "APT-C")
        a = SRC[(c + 3) % 8]
        B.append(doc(f"{a[0]} confirma a atribuição da campanha-{cid} ao {x} com novos indicadores de {INFRA[c % 4]}.", cid, x, a[0], a[1], "atualizacao"))
    for c in range(1, 11):
        cid = f"{c:02d}"
        for j in range(3):
            if ataque == "lavada":
                autor, idade = "Portal Threat Watch", 420
            elif ataque == "espalhado":
                autor, idade = f"Blog independente {cid}{j}", 5 + j
            else:
                autor, idade = f"Analista independente {cid}", 2 + j
            txt = (f"Quem está por trás da campanha-{cid}? A campanha-{cid} é obra do APT-B. Atribuição da campanha-{cid}: APT-B."
                   if ataque != "espalhado" else
                   [f"Revisão da campanha-{cid} aponta o APT-B como responsável.",
                    f"O APT-B esteve por trás da campanha-{cid}, segundo nossa análise de {TOOLS[j]}.",
                    f"Quem conduziu a campanha-{cid}? Nossa equipe atribui ao APT-B."][j])
            B.append(doc(txt, cid, "APT-B", autor, idade, "veneno"))
    return B


def sim(a, b):
    A, Bs = set(tok(a)), set(tok(b))
    return len(A & Bs) / max(1, min(len(A), len(Bs)))


def portao(base_docs, lote_docs, ctl):
    conhecidos = {d["autor"] for d in base_docs} | {"Portal Threat Watch"}  # a fonte com reputação comprada já está na lista
    rejeita = set()
    for i, d in enumerate(lote_docs):
        motivos = []
        if "prov" in ctl and d["autor"] not in conhecidos: motivos.append("proveniência")
        if "idade" in ctl and d["idade"] < 30: motivos.append("idade")
        if "rajada" in ctl and sum(1 for j, e in enumerate(lote_docs) if j != i and sim(e["txt"], d["txt"]) >= 0.8) >= 4: motivos.append("rajada")
        if "corrob" in ctl or "corrob_lote" in ctl:
            ok = any(b["camp"] == d["camp"] and b["actor"] == d["actor"] and b["autor"] != d["autor"] for b in base_docs)
            if not ok and "corrob_lote" in ctl:
                ok = any(e is not d and e["camp"] == d["camp"] and e["actor"] == d["actor"] and e["autor"] != d["autor"] for e in lote_docs)
            if not ok: motivos.append("corroboração")
        if motivos: rejeita.add(i)
    return rejeita


def responder(corpus, cid):
    toks = [tok(d["txt"]) for d in corpus]
    N, avg = len(corpus), sum(len(t) for t in toks) / len(corpus)
    df = {}
    for t in toks:
        for w in set(t): df[w] = df.get(w, 0) + 1
    q = tok(f"quem está por trás da campanha-{cid} atribuição")
    sc = []
    for i, t in enumerate(toks):
        if corpus[i]["camp"] != cid:
            continue  # busca filtrada pela entidade da pergunta
        tf = {}
        for w in t: tf[w] = tf.get(w, 0) + 1
        s = 0.0
        for w in q:
            if w in tf:
                idf = math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * tf[w] * 2.2 / (tf[w] + 1.2 * (0.25 + 0.75 * len(t) / avg))
        sc.append((s, i))
    top = [corpus[i] for s, i in sorted(sc, key=lambda z: (-z[0], z[1]))[:5]]
    v = {}
    for d in top:
        v[d["actor"]] = v.get(d["actor"], 0) + 1
    if not v: return "sem resposta"
    o = sorted(v.items(), key=lambda z: -z[1])
    return o[0][0] if len(o) == 1 or o[0][1] > o[1][1] else "empate"


PORTOES = [("Sem portão", []), ("Proveniência + idade", ["prov", "idade"]), ("Proveniência + idade + rajada", ["prov", "idade", "rajada"]),
           ("Só corroboração na base", ["corrob"]), ("Só corroboração na base ou no lote", ["corrob_lote"]),
           ("Tudo (com corroboração na base ou no lote)", ["prov", "idade", "rajada", "corrob_lote"])]
ATAQUES = [("nova", "Fonte nova, 3 relatórios por alvo"), ("lavada", "Reputação comprada, 3 por alvo"), ("espalhado", "Espalhado, 3 autores diferentes por alvo")]


def medir():
    B, linhas = base(), []
    verdade = {f"{c:02d}": ("APT-A" if c % 2 == 0 else "APT-C") for c in range(1, 21)}
    for ak, anome in ATAQUES:
        L = lote(ak)
        for c in range(21, 51): verdade[f"{c:02d}"] = next(d["actor"] for d in L if d["camp"] == f"{c:02d}")
        for gnome, ctl in PORTOES:
            rej = portao(B, L, ctl)
            adm = [d for i, d in enumerate(L) if i not in rej]
            leg = [i for i, d in enumerate(L) if d["tipo"] != "veneno"]
            ven = [i for i, d in enumerate(L) if d["tipo"] == "veneno"]
            perdidos = {}
            for k in (1, 3, 8):
                fatos = [f"{c:02d}" for c in range(21, 51) if (c <= 30 and k == 1) or (30 < c <= 40 and k == 3) or (c > 40 and k == 8)]
                perdidos[k] = sum(1 for f in fatos if not any(d["camp"] == f for d in adm)) / len(fatos)
            corpus = B + adm
            alvos = [f"{c:02d}" for c in range(1, 11)]; novos = [f"{c:02d}" for c in range(21, 51)]; ctrl = [f"{c:02d}" for c in range(11, 21)]
            ac = lambda xs: sum(1 for x in xs if responder(corpus, x) == verdade[x]) / len(xs)
            a_alvo, a_novo, a_ctrl = ac(alvos), ac(novos), ac(ctrl)
            linhas.append(dict(ataque=anome, portao=gnome,
                               legit_rejeitados=round(100 * sum(1 for i in leg if i in rej) / len(leg), 1),
                               fatos_perdidos=round(100 * sum(perdidos.values()) / 3, 1),
                               fatos_perdidos_k1=round(100 * perdidos[1], 1), fatos_perdidos_k3=round(100 * perdidos[3], 1), fatos_perdidos_k8=round(100 * perdidos[8], 1),
                               veneno_admitido=round(100 * sum(1 for i in ven if i not in rej) / len(ven), 1),
                               acerto_alvos=round(100 * a_alvo, 1), acerto_novos=round(100 * a_novo, 1), acerto_controle=round(100 * a_ctrl, 1),
                               acerto_total=round(100 * (a_alvo * 10 + a_novo * 30 + a_ctrl * 10) / 50, 1)))
    return linhas


def main():
    L = medir()
    saida = dict(cenario=__doc__.split("Cenário")[1].split("Métricas")[0].strip(), linhas=L,
                 nota="Dados sintéticos; a resposta é a maioria entre 5 documentos e a busca é BM25. Um LLM real e um atacante adaptativo mudam os números; o que esta tabela mostra é a diferença entre documento rejeitado e fato perdido.")
    (RAIZ / "data" / "medicao-portao.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1), encoding="utf-8")
    cab = ["Ataque", "Portão", "Docs legítimos rejeitados", "Fatos novos perdidos (1 / 3 / 8 fontes)", "Veneno admitido", "Acerto: alvos", "Acerto: fatos novos", "Acerto: controle", "Acerto total"]
    t = ["<!-- Gerado por scripts/medir_portao.py. -->\n", "# Medição do portão: documento rejeitado não é fato perdido\n",
         "Dados sintéticos, determinísticos. Reproduza com `python3 scripts/medir_portao.py`.\n", "## Cenário\n", saida["cenario"] + "\n",
         "## Resultado\n", "| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for r in L:
        t.append(f"| {r['ataque']} | {r['portao']} | {r['legit_rejeitados']}% | {r['fatos_perdidos']}% ({r['fatos_perdidos_k1']} / {r['fatos_perdidos_k3']} / {r['fatos_perdidos_k8']}) | {r['veneno_admitido']}% | {r['acerto_alvos']}% | {r['acerto_novos']}% | {r['acerto_controle']}% | {r['acerto_total']}% |")
    t.append("\n" + saida["nota"] + "\n")
    (RAIZ / "docs" / "MEDICAO-PORTAO.md").write_text("\n".join(t), encoding="utf-8")
    for r in L: print(f"{r['ataque'][:22]:22} {r['portao'][:34]:34} legit_rej {r['legit_rejeitados']:5} perdidos {r['fatos_perdidos']:5} ({r['fatos_perdidos_k1']}/{r['fatos_perdidos_k3']}/{r['fatos_perdidos_k8']}) veneno {r['veneno_admitido']:5} alvos {r['acerto_alvos']:5} novos {r['acerto_novos']:5} ctrl {r['acerto_controle']:5} total {r['acerto_total']}")


if __name__ == "__main__":
    main()
