<!-- Gerado por scripts/medir_portao.py. -->

# Medição do portão: documento rejeitado não é fato perdido

Dados sintéticos, determinísticos. Reproduza com `python3 scripts/medir_portao.py`.

## Cenário

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

## Resultado

| Ataque | Portão | Docs legítimos rejeitados | Fatos novos perdidos (1 / 3 / 8 fontes) | Veneno admitido | Acerto: alvos | Acerto: fatos novos | Acerto: controle | Acerto total |
|---|---|---|---|---|---|---|---|---|
| Fonte nova, 3 relatórios por alvo | Sem portão | 0.0% | 0.0% (0.0 / 0.0 / 0.0) | 100.0% | 0.0% | 100.0% | 100.0% | 80.0% |
| Fonte nova, 3 relatórios por alvo | Proveniência + idade | 42.9% | 16.7% (50.0 / 0.0 / 0.0) | 0.0% | 100.0% | 83.3% | 100.0% | 90.0% |
| Fonte nova, 3 relatórios por alvo | Proveniência + idade + rajada | 60.7% | 33.3% (50.0 / 30.0 / 20.0) | 0.0% | 100.0% | 66.7% | 100.0% | 80.0% |
| Fonte nova, 3 relatórios por alvo | Só corroboração na base | 85.7% | 100.0% (100.0 / 100.0 / 100.0) | 0.0% | 100.0% | 0.0% | 100.0% | 40.0% |
| Fonte nova, 3 relatórios por alvo | Só corroboração na base ou no lote | 7.1% | 33.3% (100.0 / 0.0 / 0.0) | 0.0% | 100.0% | 66.7% | 100.0% | 80.0% |
| Fonte nova, 3 relatórios por alvo | Tudo (com corroboração na base ou no lote) | 64.3% | 50.0% (100.0 / 30.0 / 20.0) | 0.0% | 100.0% | 50.0% | 100.0% | 70.0% |
| Reputação comprada, 3 por alvo | Sem portão | 0.0% | 0.0% (0.0 / 0.0 / 0.0) | 100.0% | 0.0% | 100.0% | 100.0% | 80.0% |
| Reputação comprada, 3 por alvo | Proveniência + idade | 42.9% | 16.7% (50.0 / 0.0 / 0.0) | 100.0% | 0.0% | 83.3% | 100.0% | 70.0% |
| Reputação comprada, 3 por alvo | Proveniência + idade + rajada | 60.7% | 33.3% (50.0 / 30.0 / 20.0) | 0.0% | 100.0% | 66.7% | 100.0% | 80.0% |
| Reputação comprada, 3 por alvo | Só corroboração na base | 85.7% | 100.0% (100.0 / 100.0 / 100.0) | 0.0% | 100.0% | 0.0% | 100.0% | 40.0% |
| Reputação comprada, 3 por alvo | Só corroboração na base ou no lote | 7.1% | 33.3% (100.0 / 0.0 / 0.0) | 0.0% | 100.0% | 66.7% | 100.0% | 80.0% |
| Reputação comprada, 3 por alvo | Tudo (com corroboração na base ou no lote) | 64.3% | 50.0% (100.0 / 30.0 / 20.0) | 0.0% | 100.0% | 50.0% | 100.0% | 70.0% |
| Espalhado, 3 autores diferentes por alvo | Sem portão | 0.0% | 0.0% (0.0 / 0.0 / 0.0) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Espalhado, 3 autores diferentes por alvo | Proveniência + idade | 42.9% | 16.7% (50.0 / 0.0 / 0.0) | 0.0% | 100.0% | 83.3% | 100.0% | 90.0% |
| Espalhado, 3 autores diferentes por alvo | Proveniência + idade + rajada | 60.7% | 33.3% (50.0 / 30.0 / 20.0) | 0.0% | 100.0% | 66.7% | 100.0% | 80.0% |
| Espalhado, 3 autores diferentes por alvo | Só corroboração na base | 85.7% | 100.0% (100.0 / 100.0 / 100.0) | 0.0% | 100.0% | 0.0% | 100.0% | 40.0% |
| Espalhado, 3 autores diferentes por alvo | Só corroboração na base ou no lote | 7.1% | 33.3% (100.0 / 0.0 / 0.0) | 100.0% | 100.0% | 66.7% | 100.0% | 80.0% |
| Espalhado, 3 autores diferentes por alvo | Tudo (com corroboração na base ou no lote) | 64.3% | 50.0% (100.0 / 30.0 / 20.0) | 0.0% | 100.0% | 50.0% | 100.0% | 70.0% |

Dados sintéticos; a resposta é a maioria entre 5 documentos e a busca é BM25. Um LLM real e um atacante adaptativo mudam os números; o que esta tabela mostra é a diferença entre documento rejeitado e fato perdido.
