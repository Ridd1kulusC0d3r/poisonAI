<!-- Gerado por scripts/gerar_docs.py a partir de data/. Edite os JSON, não este arquivo. -->

# Hipóteses concorrentes, indicadores e julgamentos

**Pergunta:** Por que, até 25/11/2026, não há caso público confirmado de pipeline de CTI ou OSINT em produção envenenado por conteúdo gerado por IA?

## Hipóteses

- **H1.** Acontece, mas não é detectado: faltam telemetria e proveniência.
- **H2.** Acontece e é detectado, mas não é divulgado.
- **H3.** Não compensa para o adversário: há caminhos mais baratos para o mesmo efeito.
- **H4.** O ruído natural dos feeds torna o envenenamento pouco eficaz ou desnecessário.
- **H5.** É questão de tempo: a capacidade amadureceu há pouco.
- **H6.** O esforço existe, mas mira outro alvo: assistentes públicos e opinião pública.

## Matriz (C consistente, N neutra, I inconsistente)

| Evidência | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|
| E1. O âncora: quase nenhum sistema registra proveniência ou foi testado sob ataque | C | N | N | N | C | N |
| E2. Envenenamento funciona barato em laboratório (250 documentos; CTI falso aceito) | C | C | I | N | C | N |
| E3. O submundo concentra-se em credenciais e acesso roubados, não em manipulação de dados | N | N | C | N | N | N |
| E4. Feeds já têm sobreposição de 2,5% a 4,0% e falsos positivos frequentes | C | N | C | C | N | N |
| E5. Operações russas investem em escala para chegar a chatbots e buscadores | N | N | N | N | N | C |
| E6. Malware já embute texto para enganar ou travar analisadores de IA (Skynet, GuardBreaker, DUSTMAKER) | C | N | I | N | C | N |
| E7. Atores estatais usam IA sobretudo para acelerar operações, não para enganar defensores | N | N | C | N | N | N |
| E8. Fornecedores publicam com frequência relatórios sobre uso indevido de IA | I | I | N | N | N | N |
| E9. Nenhuma oferta de “serviço de envenenamento de CTI” nos levantamentos do submundo | N | N | C | C | C | N |
| E10. Envenenamento de memória observado em produção, mas com fim comercial e contra assistentes do público (Microsoft, AML.CS0072) | N | I | C | N | C | C |
| E11. Pesquisa brasileira manipula 14 de 23 modelos de SOC pela telemetria do EDR, em laboratório | C | N | I | N | C | N |

Inconsistências por hipótese: H1 = 1, H2 = 2, H3 = 3, H4 = 0, H5 = 0, H6 = 0. Pela regra de Heuer, mais inconsistência é hipótese mais fraca.


## Leitura

H2 tem a maior carga de inconsistência: com tantos relatórios públicos sobre abuso de IA, um caso de CTI envenenado seria valioso de divulgar. H3 e H6 acumulam consistência sem inconsistência forte. H1 não pode ser descartada, porque a falta de telemetria (E1) impede justamente a detecção. E6 é a evidência mais incômoda para H3. Duas evidências novas, vindas do LLmInjection: E10 mostra envenenamento de memória fora do laboratório, mas por motivo comercial e contra o público, o que reforça H3 e H6 e enfraquece H2; E11 mostra que a superfície do SOC é real e barata de atacar, o que pesa contra H3.

- É provável que a ausência de casos se explique principalmente por H3 e H6.
- É tão provável quanto não que manipulações de baixa escala já tenham ocorrido sem detecção (H1).
- Confiança baixa a moderada: autorrelatos de fornecedores e ausência de evidência.

## Julgamentos-chave

| # | Julgamento | Probabilidade | Confiança | Base |
|---|---|---|---|---|
| JC1 | Atores criminosos e estatais continuarão usando IA principalmente para acelerar operações conhecidas, não para criar técnicas novas. | Muito provável | Moderada | Microsoft, GTIG, Elastic e Amazon convergem; todos são fornecedores. |
| JC2 | Pipelines de CTI/OSINT com IA em uso hoje não conseguem reconstituir a origem de suas conclusões. | Provável | Moderada | Âncora; nenhum padrão de proveniência adotado. |
| JC3 | Um ator já estar envenenando de forma sistemática pipelines de CTI. | Improvável | Baixa | Ausência de evidência sob baixa visibilidade. |
| JC4 | No Brasil, a ameaça de IA mais relevante para defensores no curto prazo é a aceleração do cibercrime financeiro local. | Quase certo | Moderada | Telemetria de fornecedores convergente, sem dado oficial independente. |
| JC5 | Agentes de OSINT operando no Brasil durante eleições absorvem conteúdo sintético não rotulado. | Muito provável | Moderada | Data Privacy Brasil e VigIA mostram baixa rotulagem. |
| JC6 | Chatbots respondem pior em português do que em inglês a narrativas de propaganda estatal. | Tão provável quanto não | Baixa | Indícios indiretos; nenhuma auditoria em pt-BR. |


## Indicadores e alertas

| # | Indicador | Favorece | Onde observar |
|---|---|---|---|
| I1 | Primeiro relatório falso ou IOC fabricado identificado em comunidade de compartilhamento (MISP, ISAC) | H1/H5 | Avisos das comunidades; FIRST |
| I2 | Oferta em fórum de serviço de “seeding” de relatórios técnicos ou reputação de indicadores | H5, contra H3 | Monitoramento do submundo |
| I3 | Ferramenta pública que gera relatórios de ameaça falsos em lote | H5 | Repositórios de código; avisos de fornecedores |
| I4 | Fornecedor de CTI publica retratação por inteligência contaminada | H1/H2 | Blogs e boletins de fornecedores |
| I5 | Novas amostras de malware com texto dirigido a analisadores de IA, com taxa de sucesso medida | Contra H3 | ESET, Check Point, GTIG |
| I6 | Contas falsas de OSINT em português ganhando tração em crises | H6 | Agências de checagem; DFRLab |
| I7 | Caso documentado de assistente de IA corporativo ou de SOC enganado em produção (parcialmente visto: o envenenamento de recomendação da Microsoft atinge assistentes do público, não de SOC) | H1/H5 | Divulgações de incidentes; CVEs |
| I8 | Propaganda estatal medida em dados de treino ou em respostas em português | H6 | DFRLab; NewsGuard; pesquisadores lusófonos |


## Cenários (12 a 24 meses)

| Cenário | Descrição | Probabilidade | Sinais |
|---|---|---|---|
| A. Continuidade | Envenenamento de CTI segue em laboratório; o dano real vem de agentes ofensivos e de conteúdo sintético em massa | Provável | Nenhum de I1 a I4; crescimento de I5 e I6 |
| B. Primeiro caso | Um caso público de pipeline de CTI ou de assistente de SOC manipulado em produção | Improvável em 12 meses; tão provável quanto não em 24 | I1, I4 ou I7 |
| C. Industrialização | Serviço de envenenamento oferecido no submundo, com clientes | Muito improvável em 12 meses | I2, I3 |


## Premissas-chave

| # | Premissa | Sustentação | Se estiver errada |
|---|---|---|---|
| P1 | Adversários querem moldar as conclusões de analistas de CTI | Fraca | A linha vale mais como robustez geral do que como defesa contra ameaça ativa |
| P2 | Pipelines de CTI com IA são usados em decisões relevantes | Moderada | O dano de um envenenamento seria menor do que o suposto |
| P3 | O revisor humano é o último controle eficaz | Fraca | O modelo copiloto pode dar falsa segurança |
| P4 | O que vale em laboratório vale em produção | Fraca | Riscos super ou subestimados, sem saber em qual direção |
| P5 | Relatórios de fornecedores são confiáveis sobre técnicas | Moderada para técnica; baixa para atribuição | Atribuições citadas podem cair |
| P6 | O problema é igual no Brasil e no eixo anglófono | Não testada | O recorte local muda prioridades (aba Brasil) |
