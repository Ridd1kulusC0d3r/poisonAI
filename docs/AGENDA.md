<!-- Gerado por scripts/gerar_docs.py a partir de data/. Edite os JSON, não este arquivo. -->

# Agenda de pesquisa

## Tese

- O copiloto humano–IA é a hipótese de implantação mais prudente, mas sua eficácia contra conteúdo adversarial é desconhecida, e a melhor evidência disponível (n=10) sugere que ela é baixa.
- Use o âncora como mapa, não como fonte de números: três dos números que ele usa como pilares não batem com as fontes primárias.

## Perguntas prioritárias

- **PIR-1.** Algum ator com intenção e capacidade está tentando, ou deve tentar nos próximos 12 meses, manipular as conclusões de pipelines de CTI/OSINT com IA? Com que sinais saberíamos? (ligadas: RQ1, RQ13, RQ19)
- **PIR-2.** Quais das nossas fontes são ao mesmo tempo baratas de falsificar e decisivas nas nossas conclusões? (ligadas: RQ5, RQ24, QP6)
- **PIR-3.** Como o cibercrime brasileiro está incorporando IA, e o que muda para quem defende instituições financeiras e de pagamento? (ligadas: RQ22)
- **PIR-4.** Como conteúdo sintético e propaganda em português contaminam fontes abertas e assistentes de IA usados no Brasil? (ligadas: RQ7, QP5, RQ15, RQ23)
- **PIR-5.** Quais frameworks agênticos ofensivos estão em uso contra alvos na América Latina, e que telemetria os revela? (ligadas: RQ22, RQ17)

## Banco de perguntas

| # | Pergunta | Hipótese | Como testar | Origem | Tema | Prioridade | Relação |
|---|---|---|---|---|---|---|---|
| QP1 | Quanto um agente OSINT alucina, etapa por etapa? | A taxa cresce da extração para o relatório. | Verdade-terreno STIX; anotação por afirmação | Artefato | Alucinação | alta | ≈ RQ2 |
| QP2 | Quantos documentos viram uma atribuição? | Poucos, se imitam a pergunta. | Curva dose-resposta em RAG e GraphRAG | Artefato | Envenenamento | alta | ≈ RQ1 e E1 |
| QP3 | O RAG transforma veneno em confiança? | A citação aumenta a aceitação do erro. | Experimento entre grupos com analistas | Artefato | Humano | alta | complementa RQ4 |
| QP4 | O checkpoint humano pega CTI falso de LLM atual? | Aceitação acima de 50%. | Replicar Ranade com n maior | Artefato | Humano | alta | ≈ RQ4 e RQ19 |
| QP5 | LLM grooming em português | Perguntas enviesadas puxam mais fontes de influência. | Bateria em pt-BR no molde do ISD | Artefato | Multilíngue | média | ≈ RQ7 |
| QP6 | Detectar veneno pela ausência de corroboração | Ausência de segunda fonte separa nós plantados. | Contagem de fontes independentes por nó | Artefato | Envenenamento | média | complementa RQ5 e RQ17 |
| QP7 | Ferramenta envenenada no agente OSINT | Saídas de ferramenta funcionam como injeção. | Servidores MCP de teste | Artefato | Ferramentas | média | ≈ RQ10 |
| RQ1 | Quanto CTI falso de LLM é preciso para inverter uma atribuição feita por um agente ReAct com RAG? | Número quase constante e pequeno. | Sandbox fechado; geração controlada; curva dose-resposta (AnnoCTR, CTIBench, CTIConnect, RSB) | Dossiê 1 | Envenenamento | alta |  |
| RQ2 | Como o erro se propaga entre coleta, NER, grafo, RAG e relatório? | Amplificação superlinear na etapa de grafo. | Contaminação controlada de 0 a 20%; rastreio por afirmação; reanotação do dataset de Niu et al.; gabarito possível no CTI-HAL e métrica no HalluVision | Dossiê 1 | Alucinação | alta |  |
| RQ3 | MISP, OpenCTI e STIX/TAXII propagam IOCs envenenados entre organizações? | Sim, por correlações e sightings automáticos. | Testbed federado com instâncias isoladas | Dossiê 1 | Envenenamento | média |  |
| RQ4 | Checkpoints humanos detectam conteúdo adversarial? | Perto do acaso sem proveniência; melhora com nota de fonte. | Experimento com n≥30 e itens semeados; alfabetização em LLM e pressão de tempo; desenho de referência em Horowitz e Kahn (n≈9.000) e no estudo cruzado de correções assistidas por LLM | Dossiê 1 | Humano | alta |  |
| RQ5 | Notas de confiabilidade (Almirantado, AuthRank) reduzem o envenenamento sem suprimir inteligência nova? | Há trade-off mensurável. | Ataque × supressão de relatórios legítimos novos (zero-days) | Dossiê 1 | Defesa | média |  |
| RQ6 | Analisadores de malware por LLM resistem a injeções imperativas, narrativas e de gatilho de recusa? | Narrativas e gatilhos de recusa superam as imperativas. | Avaliação cruzada; amostras Skynet e GuardBreaker; protocolo ALIBI | Dossiê 1 | IA no SOC | média |  |
| RQ7 | Chatbots em pt-BR repetem narrativas da Pravda mais que em inglês? | Sim, por vazios de dados em português. | Auditoria longitudinal com perguntas amplas e estreitas | Dossiê 1 | Multilíngue | média |  |
| RQ8 | LLMs com busca verificam mídia de crise gerada por IA? | Falham nas primeiras 72 horas. | Coorte de crises (Israel–Irã 2025, Índia–Paquistão 2025) | Dossiê 1 | Multimodal | média |  |
| RQ9 | O enquadramento do LLM enviesa a atribuição de ameaças entre Estados? | Sim, e muda com o idioma. | Troca contrafactual de atores em relatórios idênticos | Dossiê 1 | Viés | média |  |
| RQ10 | Agentes de CTI com skills e MCP de terceiros já chegam comprometidos? | Sim; a camada de ferramentas é o elo mais fraco. | Auditoria de dependências de agentes abertos; skills adulteradas em sandbox | Dossiê 2 | Ferramentas | alta |  |
| RQ11 | Quanto da triagem por LLM cai sob injeção em logs, com modelos e logs atuais? | Sumarização segue vulnerável em 2026. | Replicar LogInject e Watchtower com logs reais anonimizados; corpus pronto em Yeagerist0/prompt-injection-soc-telemetry | Dossiê 2 | IA no SOC | alta | Viaconnect (Brasil) é o caso mais próximo |
| RQ12 | Iscas de inferência extraem ou corrompem a memória de agentes ofensivos? Com que limites legais? | Extração passiva é viável e defensável; corrupção ativa não. | Bancada com frameworks abertos apontados para iscas; análise jurídica (LGPD, Marco Civil) | Dossiê 2 | Engano | média |  |
| RQ13 | Com que frequência um agente de OSINT encontra injeções na web e com que efeito? | Frequentes e “defensivas”; efeito é degradação. | Agente de coleta instrumentado, cruzado com os modelos de 15,3 mil instâncias | Dossiê 2 | Injeção | alta |  |
| RQ14 | Como verificar a integridade de pesos abertos usados em inteligência? | Com referência, edições mínimas aparecem; sem referência, detecção imperfeita. | Reproduzir as defesas do Lazarus em modelos de CTI local | Dossiê 2 | Integridade de modelo | média |  |
| RQ15 | Agentes multimodais detectam imagem de satélite fabricada? | Perto do acaso sem metadados de proveniência. | Pares autênticos e gerados; medir falso positivo nos autênticos | Dossiê 2 | Multimodal | média |  |
| RQ16 | Artefatos de agentes autônomos já contaminam coletas de OSINT? | Sim, em volume pequeno e crescente. | Buscar indicadores do relatório do AISI em corpora de coleta | Dossiê 2 | Agentes | baixa |  |
| RQ17 | Em qual estágio da campanha a detecção é mais barata? | Autoridade e semeadura, antes do modelo. | Bancada instrumentada por estágio; custo por detecção | Dossiê 3 | Defesa | média |  |
| RQ18 | Quanto tempo uma isca contra agentes dura depois que sua assinatura vaza? | Queda abrupta. | Repetir Rouxii com iscas renovadas | Dossiê 3 | Engano | média |  |
| RQ19 | O revisor humano detecta falsa bandeira plantada em grafo de CTI? | Não, sem proveniência por afirmação. | Exercício E1 com revisão cega, n≥30 | Dossiê 3 | Humano | alta |  |
| RQ20 | Iscas de inferência distinguem agente malicioso de agente legítimo mal configurado? | Mal; falso positivo cresce com a adoção de agentes. | Tráfego misto controlado | Dossiê 3 | Engano | baixa |  |
| RQ21 | A memória capturada de um agente adversário é fonte confiável? | Parcialmente: contém alucinações. | Comparar relato do agente com o que ocorreu em alvos de laboratório | Dossiê 3 | Engano | média |  |
| RQ22 | Que telemetria distingue uma intrusão conduzida por agente em ambiente financeiro brasileiro? | Ritmo de máquina e laço de planejamento aparecem também em fraude contra Pix. | Aplicar as detecções da aba Defesa a logs de instituição parceira | Dossiê 5 | Brasil | alta | PIR-3 e PIR-5 |
| RQ23 | Quanto erra o modelo copiloto (software mais checagem humana) na eleição de 2026? | Software sozinho erra muito; a checagem humana corrige, com custo de tempo. | Reanalisar amostra do VigIA: acerto e falso positivo por etapa | Dossiê 5 | Humano | média | PIR-4; complementa RQ4 |
| RQ24 | Qual a taxa de discordância natural entre as fontes de CTI que usamos? | Alta, como em Bouwman et al. | Medir sobreposição e atraso entre os feeds da casa antes de qualquer bancada adversarial | Dossiê 5 | Método | alta | linha de base de RQ1 e RQ2 |
| RQ25 | Envenenamento de memória por links (como o da Microsoft) atinge assistentes usados por analistas de CTI? | Sim, se o analista usa assistente com memória e clica em links de fontes abertas. | Bancada com assistentes de memória e links de relatórios; medir o que persiste | LLmInjection | Envenenamento | média | ATLAS AML.CS0072; complementa QP7 |
| RQ26 | Recuperadores híbridos e defesas como TrustRAG resistem a relatórios de CTI semeados sem conhecer a pergunta (modelo MIRAGE)? | Resistem melhor que RAG puro, mas não quando os falsos são maioria. | Bancada da RQ1 com MIRAGE, TrustRAG, RobustRAG e BM25 híbrido | Busca científica | Envenenamento | alta | complementa RQ1 e RQ5 |


## Lacunas confirmadas

| Lacuna | Evidência | Origem |
|---|---|---|
| Não existe benchmark adversarial para agentes de CTI/OSINT | RSB e MCPTox são genéricos; CTIBench e CyberThreat-Eval são benignos. | Dossiê 1 |
| Erro composto ao longo do pipeline nunca foi medido | “No paper attempts to quantify the combined error rate.” | Âncora |
| Envenenamento de grafo de CTI medido só com um exemplo | Ranade 2021, demonstração qualitativa. O ataque ROAR (2023) mira raciocínio sobre grafos de CTI: confira e reavalie a lacuna. | Dossiê 1 |
| Eficácia do checkpoint humano não testada | Estudos com n=10, n=3 e n=10; nenhum com n≥30. Fora de CTI há estudos grandes (Horowitz e Kahn, n≈9.000), mas não com analistas de inteligência. | Âncora |
| Triagem de malware por LLM sem métricas de campo | ALIBI e GuardBreaker sem taxa de sucesso pública. | Dossiê 1 |
| Grooming não medido em português | Nem em outras línguas fora do eixo ocidental. | Dossiê 1 |
| Proveniência sem medida de supressão de inteligência nova | Limitação admitida pelo AuthRank. | Dossiê 1 |
| A camada de ferramentas chega comprometida | Skills e MCP de terceiros antes de qualquer dado. | Dossiê 2 |
| Logs como canal de instrução, testados com modelos de 2024 | Resultados atuais desconhecidos. | Dossiê 2 |
| Nenhum benchmark multimodal para agentes de inteligência | E detectores com falso positivo alto. | Dossiê 2 |
| Nenhum feed ou grafo de produção comprovadamente envenenado em público | A ausência é a justificativa central da linha. | Dossiês 1 a 3 |
| Nenhuma série oficial independente sobre IA no cibercrime brasileiro | Só telemetria de fornecedores. | Dossiê 5 |
| Ecossistema brasileiro de compartilhamento sem mapeamento para IA | CERT.br, CTIR Gov, regulador financeiro e MISP setoriais: coleta pendente. | Dossiê 5 |


## Fases


### Curto prazo (0 a 6 meses)

- [ ] Revisão sistemática reprodutível: busca booleana registrada, dois revisores, κ
- [ ] Corrigir as citações herdadas do âncora
- [ ] Testbed fechado de RAG e agente de CTI
- [ ] RQ1 e RQ6 em pequena escala
- [ ] Protocolo ético: nenhum CTI falso sai do laboratório

### Médio prazo (6 a 18 meses)

- [ ] RQ2, RQ3, RQ5 e RQ7
- [ ] Publicar um benchmark de envenenamento em CTI com divulgação responsável
- [ ] Estudo com analistas (RQ4) com um CSIRT ou SOC parceiro

### Longo prazo (18 a 36 meses)

- [ ] Padrão de proveniência por afirmação integrável ao STIX
- [ ] Currículo de alfabetização em IA para analistas, com proficiência medida
- [ ] Monitoramento contínuo de grooming multilíngue
- [ ] Propor controles específicos de CTI para OWASP e ATLAS