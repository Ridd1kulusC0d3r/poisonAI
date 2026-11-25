# Metodologia

## Tipos de estudo e peso da evidência

O peso mede a força de um tipo de estudo para afirmar algo sobre o mundo real. É uma régua desta linha, não uma nota de qualidade do trabalho.

| Peso | Tipos |
|:---:|---|
| 5 | Medição em escala com dados reais |
| 4 | Experimento de ataque em laboratório · Avaliação empírica de modelos · Benchmark ou dataset · Estudo com humanos |
| 3 | Auditoria de sociedade civil · Defesa ou método · Incidente documentado · Relatório de ameaça (autorrelato) · Revisão |
| 2 | Prova de conceito · Arquitetura · Padrão, framework ou guia |
| 1 | Análise ou opinião · Monografia |

O que cada tipo prova e não prova está em `data/taxonomia.json` e no site.

## Status de verificação

| Status | Significado |
|---|---|
| Conferido na fonte | Lido na fonte primária nesta linha |
| Conferido via cobertura | Número confirmado em reportagem ou resumo, não no original |
| Preprint conferido | Resumo do preprint conferido; sem revisão por pares |
| Dossiê A | Fonte primária lida por um dossiê ou pelo LLmInjection, não reconferida aqui |
| Dossiê B | Cobertura secundária |
| Alegação (C) | Afirmação de fórum ou de vendedor |
| A conferir | Citado de memória ou ainda sem fonte localizada |

Equivalência aproximada com a escala do LLmInjection ([SOURCE-GRADING](https://github.com/Ridd1kulusC0d3r/LLmInjection/blob/main/docs/SOURCE-GRADING.md)): Conferido na fonte e Dossiê A ≈ A; Conferido via cobertura e Dossiê B ≈ B ou C; Alegação ≈ D ou E. Unificar as duas escalas é trabalho pendente.

## Probabilidade e confiança

Os julgamentos usam linguagem estimativa (quase nula, muito improvável, improvável, tão provável quanto não, provável, muito provável, quase certo) e confiança analítica separada (baixa, moderada, alta), no padrão da ICD 203. Dá para julgar algo provável com confiança baixa.

## Hipóteses concorrentes

A pergunta central (“por que não há caso público de pipeline de CTI envenenado?”) é analisada com ACH: seis hipóteses, onze evidências, e a hipótese com mais inconsistências é a mais fraca. A matriz é de um só analista; ela rende mais com divergência real. Edite a sua no site.

## Origem do material

Artigo âncora (Palmieri et al., arXiv 2607.03233), cinco dossiês produzidos com assistência de IA, a crítica aos quatro primeiros, o repositório LLmInjection e buscas em 25/11/2026. Tudo o que veio dos dossiês carrega a origem no campo `dos`.
