<!-- Gerado por scripts/gerar_docs.py a partir de data/. Edite os JSON, não este arquivo. -->

# Dossiê 7 por score da dissertação

Score da dissertação (0 a 100) = metade do score de leitura geral (até 50) + 10 por ponto de relevância para o portão de admissão (0 a 3, até 30) + 10 se o dossiê 7 põe o trabalho na ordem de leitura + 10 se o trabalho mede o custo ou o limite de uma defesa (inteligência legítima descartada, sucesso residual, benchmark fraco). Relevância 3: muda o desenho do portão ou do experimento; 2: ataque ou defesa que o experimento precisa incluir; 1: contexto da família. Classes: 70 ou mais, núcleo da dissertação; 50 a 69, ler no semestre; abaixo de 50, consulta.

Componentes: geral ÷ 2 + relevância + ordem do dossiê + custo ou limite.

| Score | Classe | Trabalho | Família | Componentes | Ordem | Nota | Por que ler |
|---|---|---|---|---|---|---|---|
| 93 | Núcleo da dissertação | [Safeguarding RAG Pipelines with GMTP: A Gradient-based Masked Token Probability Method for Poisoned Document Detection](https://aclanthology.org/2025.findings-acl.1263.pdf) | Defesa: detecção | 43 + 30 + 10 + 10 | passo 3 | A | Depende da pergunta; descartou 22,3% do limpo. |
| 91 | Núcleo da dissertação | [TrustRAG: Enhancing Robustness and Trustworthiness in Retrieval-Augmented Generation](https://arxiv.org/pdf/2501.00879) | Defesa: recuperação | 41 + 30 + 10 + 10 | passo 3 | A | Removeu 85,8% do veneno e 44% do limpo. |
| 88 | Núcleo da dissertação | [Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval](https://arxiv.org/pdf/2608.16044) | Defesa: proveniência na ingestão | 38 + 30 + 10 + 10 | passo 4 | A | Prova o limite da admissão contra envenenamento coordenado. |
| 86 | Núcleo da dissertação | [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](https://usenix.org/system/files/usenixsecurity25-zou-poisonedrag.pdf) | Ataque: base do RAG | 46 + 30 + 10 + 0 | passo 1 | A | O seu método de ataque; cinco textos por pergunta, 90%. |
| 84 | Núcleo da dissertação | [RAG-H: A RAG-Hardened SOC Framework for Trustworthy Threat Intelligence and AI Defence](https://papers.academic-conferences.org/index.php/eccws/article/view/4741) | Defesa: proveniência na ingestão | 44 + 30 + 10 + 0 | passo 4 | A | O mais próximo do seu tema: CTI, 300 documentos, 90 envenenados. |
| 82 | Núcleo da dissertação | [RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.13010) | Defesa: detecção | 32 + 30 + 10 + 10 | passo 3 | A | A comparação independente, e um detector sem pergunta. |
| 79 | Núcleo da dissertação | [Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses](https://arxiv.org/pdf/2610.33849) | Defesa: detecção | 29 + 30 + 10 + 10 | passo 3 | A | Leia antes de declarar qualquer defesa eficaz. |
| 79 | Núcleo da dissertação | [RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2604.00387) | Defesa: proveniência na ingestão | 29 + 30 + 10 + 10 | passo 4 | A | Atestação na ingestão; o insider ainda alcança 17,5%. |
| 75 | Núcleo da dissertação | [Practical Poisoning Attacks against Retrieval-Augmented Generation (CorruptRAG)](https://arxiv.org/html/2504.03957v2) | Ataque: base do RAG | 35 + 30 + 10 + 0 | passo 1 | A | A crítica que mais muda o método: um texto basta, rotulando o verdadeiro como desatualizado. |
| 75 | Núcleo da dissertação | [Certifiably Robust RAG against Retrieval Corruption (RobustRAG)](https://arxiv.org/pdf/2405.15556) | Defesa: recuperação | 35 + 20 + 10 + 10 | passo 3 | A | Robustez certificada, com custo em acurácia limpa. |
| 75 | Núcleo da dissertação | [CTIConnect: A Benchmark for Retrieval-Augmented LLMs over Heterogeneous Cyber Threat Intelligence](https://arxiv.org/pdf/2510.11974) | Benchmark de CTI | 35 + 30 + 10 + 0 | passo 5 | A | A base do CTIConnect envenenado. |
| 74 | Núcleo da dissertação | [GraphRAG under Fire](https://arxiv.org/pdf/2501.14050) | Ataque: base do RAG | 44 + 30 + 0 + 0 | — | A | Análogo do PoisonedRAG para grafo de CTI: várias perguntas de uma vez. |
| 74 | Núcleo da dissertação | [AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases](https://arxiv.org/pdf/2407.12784) | Ataque: memória | 44 + 20 + 10 + 0 | passo 2 | A | Modela o insider ou a fonte comprometida. |
| 74 | Núcleo da dissertação | [Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking](https://arxiv.org/pdf/2608.21230) | Ataque: memória | 34 + 30 + 0 + 10 | — | A | Testa triagem de conteúdo e ranking por proveniência: as defesas desta linha. |
| 73 | Núcleo da dissertação | [Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173) | Ataque: injeção | 43 + 20 + 10 + 0 | passo 1 | A | Fundação: injeção usa instrução, PoisonedRAG fabrica conhecimento. |
| 68 | Ler no semestre | [Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?](https://arxiv.org/abs/2510.05244v2) | Ataque: injeção | 28 + 20 + 10 + 10 | passo 6 | A | Defesa perfeita quase sempre é benchmark fraco. |
| 65 | Ler no semestre | [CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://arxiv.org/pdf/2406.07599) | Benchmark de CTI | 35 + 20 + 10 + 0 | passo 5 | A | Livro fechado: mede memória, não recuperação. |
| 63 | Ler no semestre | [A Practical Memory Injection Attack against LLM Agents (MINJA)](https://arxiv.org/abs/2503.03704) | Ataque: memória | 33 + 20 + 10 + 0 | passo 2 | A | Atacante que só conversa com o assistente. |
| 62 | Ler no semestre | [Benchmarking Poisoning Attacks against Retrieval-Augmented Generation (RSB)](https://arxiv.org/abs/2505.18543) | Ataque: base do RAG | 32 + 20 + 0 + 10 | — | A | 13 ataques contra 7 defesas: base para comparar. |
| 60 | Ler no semestre | [AuthRank: Scoring Source Credibility to Counter Poisoning in CTI LLM Pipelines](https://arxiv.org/pdf/2510.20768) | Defesa: recuperação | 30 + 20 + 0 + 10 | — | A | Credibilidade por citação; admite suprimir o novo. |
| 57 | Ler no semestre | [TriShieldRAG: A Three-Ring Defense-in-Depth Framework Against Knowledge Corruption in Retrieval-Augmented Generation](https://www.alphaxiv.org/abs/2607.23838) | Defesa: proveniência na ingestão | 27 + 20 + 0 + 10 | — | A | Resultado negativo honesto sobre três anéis. |
| 56 | Ler no semestre | [Retrieval-Augmented Generation with Estimation of Source Reliability (RA-RAG)](https://arxiv.org/abs/2410.22954) | Defesa: recuperação | 26 + 20 + 0 + 10 | — | A | Confiabilidade aprendida por cruzamento de fontes: corroboração com o mesmo risco. |
| 55 | Ler no semestre | ragsec: pipeline de defesa em camadas sob ataque adaptativo | Defesa: proveniência na ingestão | 25 + 20 + 0 + 10 | — | B | Assinatura vence conteúdo sob ataque adaptativo. |
| 54 | Ler no semestre | [From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence](https://arxiv.org/pdf/2610.20417) | Benchmark de CTI | 34 + 20 + 0 + 0 | — | A | Sinais de confiança na extração de entidades. |
| 53 | Ler no semestre | [One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems (AuthChain)](https://arxiv.org/html/2505.11548v4) | Ataque: base do RAG | 33 + 20 + 0 + 0 | — | A | Autoridade fabricada num só documento. |
| 53 | Ler no semestre | [Phantom: General Trigger Attacks on Retrieval Augmented Language Generation](https://arxiv.org/abs/2405.20485) | Ataque: base do RAG | 33 + 20 + 0 + 0 | — | A | Inerte na admissão, ativo na pergunta certa. |
| 53 | Ler no semestre | [Benign Alone, Harmful Together (EvoBreak)](https://arxiv.org/pdf/2608.01759) | Ataque: memória | 33 + 20 + 0 + 0 | — | A | Nenhum filtro por item pega: o portão precisa olhar o lote. |
| 50 | Ler no semestre | [Architecture Matters: comparação de arquiteturas de RAG sob envenenamento](https://arxiv.org/pdf/2605.05632) | Ataque: base do RAG | 30 + 20 + 0 + 0 | — | A | Confirma que ninguém testou arquiteturas agênticas. |
| 49 | Consulta | [Mnemonic Sovereignty: survey de segurança de memória de longo prazo em agentes](https://arxiv.org/html/2604.16548v1) | Ataque: memória | 29 + 10 + 10 + 0 | passo 2 | A | Porta de entrada da família de memória. |
| 48 | Consulta | [Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives](https://arxiv.org/pdf/2604.27202) | Ataque: injeção | 38 + 10 + 0 + 0 | — | A | Ponte entre laboratório e campo. |
| 48 | Consulta | [BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models](https://arxiv.org/abs/2406.00083) | Ataque: base do RAG | 28 + 20 + 0 + 0 | — | A | Ataque por tema: um ator ou uma família inteira contaminados. |
| 48 | Consulta | [A-MemGuard: A Proactive Defense Framework for LLM-Based Agent Memory](https://proceedings.mlr.press/v306/wei26ac.html) | Ataque: memória | 28 + 10 + 0 + 10 | — | A | Detectores com LLM deixam passar 66% do veneno. |
| 48 | Consulta | [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://arxiv.org/pdf/2509.23519v2) | Defesa: recuperação | 28 + 20 + 0 + 0 | — | A | Reputação acumulada da fonte como sinal difícil de manipular. |
| 46 | Consulta | Auditoria de saturação de benchmarks de injeção indireta | Ataque: injeção | 26 + 10 + 0 + 10 | — | B | Use mais de um benchmark. |
| 45 | Consulta | [MEMSAD: detecção de anomalia semântica contra envenenamento de memória](https://arxiv.org/pdf/2605.03482) | Ataque: memória | 25 + 10 + 0 + 10 | — | A | Avaliação frouxa subestima o ataque em quatro vezes. |
| 43 | Consulta | Benchmark scores are pipeline-dependent: auditoria de benchmarks de LLM em cibersegurança | Benchmark de CTI | 23 + 10 + 0 + 10 | — | B | Notas de benchmark dependem do pipeline. |
| 40 | Consulta | [Memory Poisoning Attack and Defense on Memory Based LLM-Agents](https://arxiv.org/abs/2601.05504) | Ataque: memória | 30 + 10 + 0 + 0 | — | A | MINJA em condições menos idealizadas. |
| 40 | Consulta | [Traceback of Poisoning Attacks to Retrieval-Augmented Generation (RAGForensics)](https://arxiv.org/pdf/2504.21668v2) | Defesa: detecção | 30 + 10 + 0 + 0 | — | A | Forense depois da falha. |
| 39 | Consulta | [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/pdf/2406.13352) | Ataque: injeção | 29 + 10 + 0 + 0 | — | A | Padrão para avaliar defesas de agentes. |
| 39 | Consulta | [Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models (BIPIA)](https://arxiv.org/abs/2312.14197) | Ataque: injeção | 29 + 10 + 0 + 0 | — | A | Cenário de resumo, o mais exposto. |
| 38 | Consulta | [TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models](https://arxiv.org/abs/2405.13401) | Ataque: base do RAG | 28 + 10 + 0 + 0 | — | A | Backdoor no recuperador, não no corpus. |
| 38 | Consulta | [GhostWriter: envenenamento de memórias de produção (Letta, Mem0, Zep)](https://arxiv.org/pdf/2607.06595) | Ataque: memória | 28 + 10 + 0 + 0 | — | B | Memórias de produção vulneráveis. |
| 38 | Consulta | [AthenaBench: A Dynamic Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://arxiv.org/pdf/2511.01144) | Benchmark de CTI | 28 + 10 + 0 + 0 | — | A | Dinâmico, reduz contaminação de treino. |
| 38 | Consulta | [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/pdf/2403.02691v2) | Ataque: injeção | 28 + 10 + 0 + 0 | — | A | Injeção em agentes com ferramentas. |
| 37 | Consulta | Topic-FlipRAG, DeRAG, HijackRAG e PoisonedEye (família de ataques a RAG) | Ataque: base do RAG | 27 + 10 + 0 + 0 | — | B | Família ampla; PoisonedEye abre o caso multimodal. |
| 37 | Consulta | WASP: benchmark de injeção contra agentes web autônomos | Ataque: injeção | 27 + 10 + 0 + 0 | — | B | O coletor de OSINT é um agente web. |
| 37 | Consulta | [RADAR: defesa dinâmica contra corrupção da recuperação em busca web](https://arxiv.org/pdf/2605.22041) | Defesa: recuperação | 27 + 10 + 0 + 0 | — | A | Busca web, o cenário de OSINT. |
| 37 | Consulta | [ExCyTIn-Bench: benchmark de investigação de ameaças com agentes](https://arxiv.org/pdf/2507.14201) | Benchmark de CTI | 27 + 10 + 0 + 0 | — | A | Investigação por agentes. |
| 36 | Consulta | SeCon-RAG: filtragem semântica em dois estágios e geração sem conflito | Defesa: recuperação | 26 + 10 + 0 + 0 | — | A | Comparar com TrustRAG; caro. |
| 36 | Consulta | [SEvenLLM: Benchmarking, Eliciting, and Enhancing Abilities of Large Language Models in Cyber Threat Intelligence](https://arxiv.org/abs/2405.03446) | Benchmark de CTI | 26 + 10 + 0 + 0 | — | A | Corpus bilíngue de tarefas de CTI. |
| 35 | Consulta | [Cyber Defense Benchmark](https://arxiv.org/pdf/2604.19533) | Benchmark de CTI | 25 + 10 + 0 + 0 | — | A | Caçada por agentes. |
| 35 | Consulta | [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](https://arxiv.org/abs/2606.25721) | Defesa: detecção | 25 + 10 + 0 + 0 | — | A | Forense por influência de tokens. |
| 35 | Consulta | [Minerva: aprendizado por reforço com recompensas verificáveis para LLMs de CTI](https://arxiv.org/pdf/2602.00513) | Benchmark de CTI | 25 + 10 + 0 + 0 | — | A | Tarefas de CTI como sinais verificáveis. |
| 34 | Consulta | [Defeating Prompt Injections by Design (CaMeL)](https://arxiv.org/abs/2503.18813) | Ataque: injeção | 24 + 10 + 0 + 0 | — | A | Defesa por desenho, cara de implementar. |
| 33 | Consulta | CyberSOCEval: análise de malware e raciocínio de CTI | Benchmark de CTI | 23 + 10 + 0 + 0 | — | B | Tarefas de SOC. |
| 27 | Consulta | AgentFlayer: injeção indireta sem clique em agentes corporativos | Ataque: injeção | 17 + 10 + 0 + 0 | — | B | Injeção sem clique em agentes corporativos. |


## Ordem de leitura sugerida pelo dossiê 7

1. Greshake → PoisonedRAG → CorruptRAG
2. AgentPoison → MINJA → survey de memória
3. RobustRAG → TrustRAG → GMTP → RAGSieve → Ranking Is Not Deciding
4. RAG-H → RAGShield → Coverage Is Not Containment
5. CTIBench → CTIConnect
6. Are Firewalls All You Need, or Stronger Benchmarks?