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

## Score de leitura

Cada trabalho recebe um score de 0 a 100 para decidir a ordem de leitura. Não é nota de qualidade.

| Componente | Pontos | Como |
|---|:---:|---|
| Evidência | até 30 | peso do tipo de estudo × 6 |
| Núcleo da linha | até 15 | 5 por tema central (alucinação, validação, envenenamento, RAG, memória, injeção, SOC, OSINT com IA, humano, desinformação, Brasil), no máximo 3 |
| Conexões | até 15 | 3 por vez que o trabalho sustenta a cadeia, um ator, uma pergunta, a linha do tempo, uma pauta, a ofensiva, a defesa ou a análise de hipóteses, no máximo 5 |
| Verificação | até 10 | nota da fonte A = 10, B = 6, C = 4, D = 2, sem fonte conferida = 0 |
| Revisão | até 10 | revisado por pares = 10, preprint = 6, literatura cinzenta = 3 |
| Recência | até 10 | 2026 = 10, 2025 = 8, 2024 = 6, 2021–2023 = 4, antes = 2 |
| Trilha | 10 | está na trilha de leitura |

Classes: **70 ou mais, leia primeiro**; 50 a 69, leia depois; abaixo de 50, consulta. Clássicos de método (Heuer, Kent) caem em consulta porque estão “a conferir” e são antigos: leia-os quando for escrever o método, não para mapear o campo.

## Nota da fonte (escala do LLmInjection)

Derivada do status: conferido na fonte, preprint conferido e Dossiê A valem **A**; via cobertura e Dossiê B valem **B** (cobertura de imprensa vale **C**); alegação vale **D**; “a conferir” fica sem nota até alguém abrir a fonte.

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

Equivalência aproximada com a escala do LLmInjection ([SOURCE-GRADING](https://github.com/Ridd1kulusC0d3r/LLmInjection/blob/main/docs/SOURCE-GRADING.md)): Conferido na fonte e Dossiê A ≈ A; Conferido via cobertura e Dossiê B ≈ B ou C; Alegação ≈ D ou E. A nota A a E agora é calculada para cada trabalho (abaixo).

## Probabilidade e confiança

Os julgamentos usam linguagem estimativa (quase nula, muito improvável, improvável, tão provável quanto não, provável, muito provável, quase certo) e confiança analítica separada (baixa, moderada, alta), no padrão da ICD 203. Dá para julgar algo provável com confiança baixa.

## Hipóteses concorrentes

A pergunta central (por que o primeiro caso identificado nesta pesquisa de fonte contaminada por conteúdo fabricado, os 32 CVEs do lote de julho de 2026, não veio de um adversário mirando pipelines de CTI) é analisada com ACH: sete hipóteses, dezessete evidências, e a hipótese com mais inconsistências é a mais fraca. A matriz é de um só analista; ela rende mais com divergência real. Edite a sua no site.

## Origem do material

Artigo âncora (Palmieri et al., arXiv 2607.03233), cinco dossiês produzidos com assistência de IA, a crítica aos quatro primeiros, o repositório LLmInjection, o relatório completo do GTG-1002 e buscas científicas em 25/11/2026. Tudo o que veio dos dossiês carrega a origem no campo `dos`.


## Identidade visual

O site usa a identidade do repositório LLmInjection: papel, tinta e uma única cor de sinal (#b43c0e), Inter e JetBrains Mono, cartões com profundidade suave, abas em pílula fixas com vidro fosco, tema claro e escuro. Todos os gráficos (cadeia, linhas de assunto, linha do tempo, curva dose-resposta, matriz de hipóteses) foram mantidos.

## Medições próprias

- **Ficha canônica do caso SQLite** (`data/caso-sqlite.json`, `data/caso-sqlite-registros.json`, `scripts/caso_cve.py`): toda contagem do caso sai do histórico de commits da lista oficial de CVEs. README, matriz de hipóteses e página usam a mesma ficha.
- **Piloto de retratações** (`data/piloto-retratacao.json`, `scripts/zumbis.py`): estados por registro × fonte (ainda apresentado como válido, rejeição visível, removido, indisponível), mais “misto” e “inconclusivo”. Preservar o registro mostrando a rejeição conta como correção. A versão 0 usa cópias de índice de busca; a data só é conhecida quando a página exibe a última modificação.
- **Medição do portão** (`scripts/medir_portao.py`): separa documento legítimo rejeitado de fato legítimo perdido (o fato perde todas as fontes) e de decisão final correta, com e sem o portão, nos mesmos dados sintéticos.
