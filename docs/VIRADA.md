<!-- Gerado por scripts/gerar_docs.py a partir de data/. Edite os JSON, não este arquivo. -->

# A virada: o envenenamento já aconteceu, e não foi espião

**Antes:** Agentes de CTI/OSINT têm um gap de validação porque foram testados só em ambiente benigno, e adversários podem explorar isso.

**Agora:** O ecossistema de inteligência de segurança inteiro opera no sistema de honra, e a IA generativa quebrou a premissa econômica desse sistema: produzir uma afirmação plausível ficou quase gratuito, verificá-la custa o mesmo de sempre. Os agentes de CTI herdam e ampliam essa assimetria, porque consomem automaticamente os registros que o humano já não consegue verificar.

> A IA generativa reduziu a quase zero o esforço de produzir um aviso plausível; o esforço de verificar (revisar o código, compilar a versão, reproduzir a prova de conceito) continua o mesmo. (Afek Berger, JFrog, segundo o The Register)

1. **O adversário relevante não é só o Estado.** Há um terceiro tipo de ator que faltava em todas as tabelas: o produtor movido a incentivo. Ele não quer enganar ninguém em particular. Quer volume. E o volume contamina.
2. **O envenenamento não precisa mirar o agente.** Basta mirar a fonte autoritativa que o agente trata como verdade.
3. **O controle que falta é uma etapa de reprodução.** Não um filtro no modelo: um ponto da cadeia em que a afirmação é reproduzida antes de virar verdade.

## Correções aos dossiês 1 a 5

| Onde | Como estava | Correção |
|---|---|---|
| Dossiês 1, 2, 3 e 5; página (ressalvas, cenários) | “Não há incidente público em que um feed ou base de CTI tenha sido envenenado por conteúdo gerado por IA” | Há ao menos um, identificado nesta pesquisa: 32 registros CVE fabricados, citando um repositório obscuro, foram publicados na lista oficial entre 27 e 30/07/2026; 28 receberam nota da CISA (até 9,8) e todos foram rejeitados em 31/07, com suspeita de geração por IA. O que segue sem caso identificado é o envenenamento dirigido por ator estatal contra pipeline de CTI. |
| Dossiê 5, análise de hipóteses | Seis hipóteses (H1 a H6) | Acrescentada H7: a contaminação acontece por produtores movidos a incentivo. É a hipótese mais bem sustentada pela evidência nova. |
| Dossiê 5, julgamento JC3 | “Improvável que alguém esteja envenenando sistematicamente pipelines de CTI” | Dividido: é quase certo que fontes autoritativas já recebem e às vezes publicam conteúdo falso de IA; segue improvável, com confiança baixa, que isso seja campanha dirigida. |
| Dossiê 5, cenário B (“primeiro caso”) | Improvável em 12 meses | Realizado em forma não prevista: o caso veio pela base de vulnerabilidades, não pelo feed de CTI. |
| Dossiê 2, tabela de atores | Só Estados, cibercrime e operações de influência | Acrescentado o produtor movido a incentivo (aba Atores, tipo Incentivo). |
| Dossiê 4, modelagem de ameaças | Fontes externas tratadas como feeds e fóruns | NVD, CVE e bases de avisos entram como fonte não verificada por padrão (cadeia, etapa S1). |
| Página e README (26/11/2026) | “54 CVEs falsos entraram no NVD com enriquecimento da CISA” | 32 registros oficiais, 28 com nota da CISA, seis examinados pela JFrog; 54 é a estimativa da JFrog para o repositório inteiro. |


## Cinco projetos com dados públicos

| # | Projeto | Por que | Como | Prazo e cuidado | Pergunta |
|---|---|---|---|---|---|
| P1 | CVEs-zumbis: depois da retratação, por quanto tempo um analista ainda encontra o aviso apresentado como válido? | Experimento natural de propagação de erro, com data de injeção e de retratação conhecidas. Mede o erro composto (RQ2) e a retratação. Uma base que preserva o registro e mostra “rejeitado” já propagou a correção: medir só a presença da página puniria boa prática. | Para cada registro × fonte: ainda apresentado como válido, rejeição visível, removido ou indisponível. Resultado: tempo entre a rejeição oficial e a primeira observação da correção em cada fonte; se a observação começou tarde, publicar o intervalo conhecido. Piloto v0 com os seis registros de SQLite nesta aba; captura direta com scripts/zumbis.py. | Semanas. O piloto v0 já é publicável como nota curta, com os limites declarados. | RQ28 |
| P2 | Quanto da inteligência de vulnerabilidade já é escrita por IA? | Primeira medida populacional desse tipo em segurança, com método validado (Liang et al.). | Estimador distribucional aplicado ao repositório público de registros CVE em JSON e ao banco de avisos do GitHub, por ano, por CNA e por tipo de produto, de 2020 a 2026. Cruzar com taxa de rejeição e disputa por CNA. | Meses; maior visibilidade. Mede exposição, não fraude: texto com IA não é texto falso. | RQ29 |
| P3 | Triagem de CVEs fantasmas com sinais simples | Os sinais da JFrog bastam para priorizar a verificação humana em escala? | Pontuação com os sinais (fornecedor não corroborou, sem hash de commit, metadados suspeitos, funções inexistentes) aplicada a registros recentes de relatores novos; verificação manual de amostra estratificada; precisão e revocação. | Semanas. Suspeitas vão para a CNA por divulgação coordenada, nunca para publicação nominal. | RQ30 |
| P4 | Agentes e chatbots ainda “lembram” dos CVEs falsos? | Liga o caso real ao eixo de grooming sem propaganda estatal, e pode ser feito em português. | Bateria fixa de perguntas sobre os registros rejeitados, repetida todo mês, em vários assistentes e idiomas, com registro das fontes citadas. | Trilha contínua. | RQ31 |
| P5 | Etapa de reprodução e selo de verificação | Que mudança mínima no formato e no processo dos registros fecharia o buraco? | Campo de estado de verificação (não verificado, reproduzido pelo fornecedor, reproduzido por terceiro, disputado, rejeitado), com equivalente em taxonomia MISP e rótulo de confiança STIX; encaminhar ao grupo de qualidade do CVE Program e à OSS-Security. | Depois de ter números de P1 a P3. É a única que muda o sistema diretamente. | RQ32 |


## Desenho experimental do dossiê 7

**Pergunta:** Quanto a corrupção de conhecimento (PoisonedRAG, CorruptRAG) e a injeção indireta degradam tarefas reais de CTI com recuperação, e quais defesas reduzem o dano sem suprimir inteligência legítima?

**Base:** Tarefas de recuperação do CTIConnect, com prioridade para atribuição de ator e ligação CVE↔CWE↔ATT&CK, que têm resposta verificável.

| Fator | Níveis |
|---|---|
| Ataque | Nenhum · PoisonedRAG (5 textos por alvo) · CorruptRAG (1 texto) · Injeção indireta (instrução no relatório) · Grafo (relações compartilhadas) · Braço natural: os 32 registros fabricados de jul/2026 |
| Dose | 1, 3, 5 e 10 documentos por alvo |
| Defesa | Nenhuma · RobustRAG · TrustRAG · GMTP · Proveniência assinada na ingestão (RAG-H/RAGShield) · Combinação |
| Arquitetura | RAG simples · Agente com ferramentas e memória |


**Métricas**

- Taxa de sucesso do ataque (resposta-alvo produzida, julgada por LLM e não só por texto)
- Acurácia limpa, sem ataque
- Taxa de supressão de evidência legítima: fração de documentos verdadeiros descartados pela defesa
- No agente: propagação para a memória e persistência entre sessões

**Hipóteses**

- CorruptRAG com um documento supera PoisonedRAG em tarefas de CTI, porque a evidência correta costuma ter várias fontes.
- GMTP perde eficácia contra veneno fluente reescrito por LLM.
- Proveniência assinada reduz o sucesso mais que qualquer defesa por conteúdo, com a menor supressão, mas não protege contra fonte legítima comprometida.

**Regras**

- Tudo em ambiente fechado; nenhum documento envenenado sai da bancada.
- Avaliar cada defesa contra ataque adaptativo (Ranking Is Not Deciding; paper dos firewalls).
- Pelo menos dois modelos, com a variação relatada.
- Tarefas dependentes de recuperação, não só tarefas que o modelo já sabe (Retrieval-Robustness Paradox).

**Ler antes:** [CTIConnect: A Benchmark for Retrieval-Augmented LLMs over Heterogeneous Cyber Threat Intelligence](https://arxiv.org/pdf/2510.11974), [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf), [Practical Poisoning Attacks against Retrieval-Augmented Generation (CorruptRAG)](https://arxiv.org/html/2504.03957v2), [Certifiably Robust RAG against Retrieval Corruption (RobustRAG)](https://arxiv.org/pdf/2405.15556), [TrustRAG: Enhancing Robustness and Trustworthiness in Retrieval-Augmented Generation](https://arxiv.org/pdf/2501.00879), [Safeguarding RAG Pipelines with GMTP: A Gradient-based Masked Token Probability Method for Poisoned Document Detection](https://aclanthology.org/2025.findings-acl.1263.pdf), [RAG-H: A RAG-Hardened SOC Framework for Trustworthy Threat Intelligence and AI Defence](https://papers.academic-conferences.org/index.php/eccws/article/view/4741), [RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2604.00387), [RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.13010), [Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses](https://arxiv.org/pdf/2610.33849), [The Retrieval-Robustness Paradox: Data Poisoning in Retrieval-Dependent Domains](https://neurips.cc/virtual/2026/178250), [AI slop pollutes the CVE pipeline with fake vulns](https://www.theregister.com/security/2026/08/03/ai-slop-pollutes-the-cve-pipeline-with-fake-vulns/5282462)