"""Dose-resposta de envenenamento num RAG de CTI de brinquedo. Só biblioteca padrão.

Pergunta: quantos documentos plantados bastam para virar a atribuição
de uma campanha (ator A -> ator B) quando o agente decide pela maioria
dos documentos recuperados?
"""
import math, random, re
from collections import Counter

random.seed(7)
ATORES = ["APT-A", "APT-B", "APT-C"]
CAMPANHAS = [f"campanha-{i:02d}" for i in range(20)]
VERBOS = ["atribuída a", "ligada a", "conduzida por", "associada a"]
RUIDO = "phishing loader c2 credenciais exfiltração dropper powershell".split()

def doc_limpo(camp):
    ator = "APT-A" if int(camp[-2:]) % 2 == 0 else "APT-C"  # verdade-terreno
    extra = " ".join(random.sample(RUIDO, 3))
    return {"camp": camp, "ator": ator, "veneno": False,
            "txt": f"relatório {camp} {random.choice(VERBOS)} {ator} {extra}"}

def doc_veneno(camp):
    # repete termos da pergunta provável para subir no ranking (SEO adversarial)
    return {"camp": camp, "ator": "APT-B", "veneno": True,
            "txt": f"{camp} {camp} atribuição {camp} atribuída a APT-B confirmado relatório {camp}"}

tok = lambda s: re.findall(r"[\w-]+", s.lower())

class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.docs, self.k1, self.b = docs, k1, b
        self.tf = [Counter(tok(d["txt"])) for d in docs]
        self.len = [sum(t.values()) for t in self.tf]
        self.avg = sum(self.len) / len(self.len)
        df = Counter(w for t in self.tf for w in t)
        n = len(docs)
        self.idf = {w: math.log(1 + (n - f + .5) / (f + .5)) for w, f in df.items()}
    def busca(self, q, k=5):
        qs = tok(q)
        def score(i):
            t, L = self.tf[i], self.len[i]
            return sum(self.idf.get(w, 0) * t[w] * (self.k1 + 1) /
                       (t[w] + self.k1 * (1 - self.b + self.b * L / self.avg)) for w in qs)
        return sorted(range(len(self.docs)), key=score, reverse=True)[:k]

base = [doc_limpo(c) for c in CAMPANHAS for _ in range(15)]  # 300 docs limpos
alvo = "campanha-07"
verdade = Counter(d["ator"] for d in base if d["camp"] == alvo).most_common(1)[0][0]

print(f"alvo={alvo}  verdade={verdade}  base limpa={len(base)} docs")
print("dose  topk_envenenado  atribuição_do_agente  virou?")
for dose in [0, 1, 2, 3, 5, 10, 25]:
    corpus = base + [doc_veneno(alvo) for _ in range(dose)]
    idx = BM25(corpus).busca(f"qual ator está por trás da {alvo} atribuição", k=5)
    top = [corpus[i] for i in idx]
    frac = sum(d["veneno"] for d in top) / len(top)
    voto = Counter(d["ator"] for d in top).most_common(1)[0][0]
    print(f"{dose:>4}  {frac:>15.0%}  {voto:>20}  {'SIM' if voto != verdade else 'não'}")
