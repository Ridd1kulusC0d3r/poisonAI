<!-- Gerado por scripts/gerar_docs.py a partir de data/. Edite os JSON, não este arquivo. -->

# Conferência das fontes

Registro de correções. Zero correção não é a meta; honestidade é.

## Afirmações do artigo âncora e do dossiê 1

| Afirmação | Veredito | Nota |
|---|---|---|
| 74 estudos e taxonomia de 11 categorias | Confere | Revisão de Palmieri et al. |
| Alucinação citada em mais de 20 estudos e medida em um (4%) | Confere | Monografia de graduação (LUISS), não revisada, base curada. |
| Allam: falha de conclusão de 11% | Implícito | A revisão dá 89% de conclusão, 92% de acurácia factual e 96% de citação. |
| Ranade: caçadores julgaram CTI falso como verdadeiro | Confere, com nuance | 78,5% das falsas e 73,6% das verdadeiras foram julgadas verdadeiras; acurácia reportada (36,8%) não bate com a matriz (47,5%). |
| Niu: 9% de desinformação em 1,96 milhão de tweets de 48 comunidades | Corrigir | Fonte primária: quase 2 milhões de tweets de cerca de 1.040 usuários (conferido); “48 comunidades” não aparece; os 9% vêm de classificadores sem verdade-terreno (dossiê 1). |
| Srikanth: analistas seniores com familiaridade 2/5 com LLM | Confere, com ressalva | Experiência é familiaridade autodeclarada; o artigo tem erros factuais graves. |
| Kobayashi e Yamaguchi: viés político transmitido a análises | Corrigir | O predecessor só mede se o modelo emite opinião. Troque por estudos de viés medido diretamente. |
| Pervez: automação agêntica de reconhecimento | Corrigir | OSINT manual com Shodan e Maltego, sem IA. |
| Shafee: défice de 25% em NER de “biosferas cibernéticas” | Corrigir | Dados de cibersegurança do Twitter (LASIGE), com sete chatbots. |
| “Shen et al. / Univ. Tsinghua” | Corrigir | A revisão cita o sistema só como [5]. |
| Mukhopadhyay e Luther definem os checkpoints | Parcial | Só posição geral; sem desenho nem avaliação. |
| Metodologia do âncora | Ressalva | Segundo o dossiê 1: triagem por um revisor, sem κ; primeiro autor também assina o Estudo 1 (conflito não declarado). |
| Efeito cascata 9% + viés + 4% | Corrigir | Soma grandezas incompatíveis. Use a calculadora da aba Agenda e lembre que, sob envenenamento dirigido, a independência não vale. |


## Afirmações dos dossiês 2 a 5

| Afirmação | Veredito | Nota |
|---|---|---|
| Storm-0940: 2.900 logins por minuto em 2.250 tenants | Corrigir | 2.250 é mínimo de tenants; o pico de 2.900 falhas por minuto foi numa campanha separada de password spray (327 contas, 8 organizações). |
| Watchtower: sequestro de persona foi o ataque mais forte | Corrigir | O mais forte foi a manipulação de contexto (96% sem defesa); persona suprimiu 68% dos logs maliciosos; comando direto teve 0%. |
| ToxicSkills: 36% com injeção e 1.467 payloads maliciosos | Corrigir | 36,82% (1.467 skills) com alguma falha; 13,4% (534) críticas; 76 payloads maliciosos confirmados. |
| Injeções na web: 54 modelos explicam 95%; 13 exfiltrações | Parcial | URLs, hosts, 15,3 mil injeções, 11,7 mil páginas e ~70% não renderizado conferidos; os outros números não estão no resumo. |
| Lazarus: menos de dez neurônios; 91,4% com 9,7% de falso positivo | Confere | Sete neurônios no Nemotron-Terminal-8B, ≥98,8% de disparo com gatilho. Título: “Lazare, veni foras”. |
| AISI: 19 ações em 10 de 122 execuções | Confere | 17 do Mythos 5 e 2 do GPT-5.6 Sol; internet ligada e classificadores desligados de propósito. |
| GuardBreaker do UAC-0099 | Confere | ESET, VBS com MATCHBOIL; grupo entrega alvos ao Sandworm. |
| MadPot capturou a memória de agentes ARTEX | Confere | 3/out a 5/nov/2026; confiança moderada; resultados não verificados pela Amazon. |
| GTG-1002: o Claude fabricou dados | Confere | Citação da Anthropic reproduzida em cobertura: credenciais que não funcionavam e achados públicos. |
| Halcyon: quase 4.000 posts | Confere | Via Axios; acrescenta a alta de anúncios de menos de 50 para mais de 1.400 por mês. |
| Al Jazeera: 5% | Confere | E o estudo revisado da mesma equipe (HKS): 5% repetiram, 8% citaram sites do Kremlin. |
| DFRLab: Pravda no Common Crawl | Confere | Inclui também Glassbridge e RT; inclusão no arquivo não garante treino. |
| Kaspersky: cerca de 85% da América Latina; ransomware −18% (448 mil); phishing +5% (583 milhões) | Corrigir | 1,7 milhão, +15% e seis de oito famílias conferidos no comunicado; os demais números não estão nele. Procure no relatório completo antes de citar. |
| Data Privacy Brasil: 88% envolveram imagem ou voz | Corrigir | São 336 casos, cerca de 81%. Os 413 casos, 1,8 por dia, 63% sem indicação e 40% de desinformação conferem. |
| TSE: a resolução exige rotulagem e veda deepfake para prejudicar ou favorecer | Parcial | Definição e placar (5 a 2, em 1º/set) conferem. A notícia não trata da rotulagem, e a vedação pressupõe que o conteúdo seja propaganda eleitoral. |
| VigIA: 920 mídias, 554 deepfakes, 371 rotuladas | Confere | Via Terra: 1.941 posts suspeitos; 525 publicações manipuladas de cidadãos comuns e anônimos. |
| Bouwman et al.: 2,5% a 4,0% para 22 atores | Confere | Página da USENIX; 14 entrevistas; atraso médio de cerca de um mês. |
| Storm-0940, UNC7228 e VAPOR PANDA como um só esforço | Corrigir | Clusters separados com sobreposição parcial (dossiê 5). O artefato agora os separa na aba Atores. |
| BREEZE COMET só via panorama da Vantico | Corrigir | Fonte primária existe e foi conferida: GTIG e Mandiant, 01/09/2026, ex-UNC5669, Pix, STR e boleto. |
| Slim Spider (CrowdStrike) usa IA contra instituição financeira brasileira | Não confirmado | O nome não aparece no post do GTIG nem no LLmInjection; o GTIG cita sobreposição com Plump Spider (Axur). Fonte única é um blog. |
| Microsoft: envenenamento de recomendação em assistentes | Confere | 50 prompts de 31 organizações em 14 setores em 60 dias; ATLAS AML.T0080. |
| Viaconnect: 14 de 23 modelos manipulados pela telemetria do EDR | Confere via cobertura | AI Agent Security Summit, 21/10/2026; a palestra e o artigo não foram lidos. |
| Viaconnect: só cobertura de imprensa | Corrigir | A agenda oficial da Zenity Labs confirma o resumo: Elastic Security sem modificação; linha de comando, nome de processo e User-Agent; 14 de 23 modelos. |
| CrowdStrike: envenenamento de ferramentas de IA | Confere | 09/01/2026; exemplos hipotéticos, sem incidentes nem números. |


## Pistas ainda não promovidas

| Categoria | Ano | Pista | Onde | Nota |
|---|---|---|---|---|
| Citado na revisão | — | Sistema agêntico com LangChain, Neo4j, memória e Tor (ref. [5]) | Referência [5] de Palmieri et al. 2026 | Arquitetura mais rica do corpus, sem medida de NER no pipeline nem validação na dark web. |
| Citado na revisão | — | Shafee et al.: sete chatbots em CTI do Twitter (ref. [54]) | Referência [54] | NER cerca de 25% abaixo de modelos especializados; F1 0,94 (GPT-4) e 0,90 (GPT4all). |
| Citado na revisão | — | Mukhopadhyay e Luther: arquitetura de checkpoints humanos (ref. [32]) | Referência [32] | Posição de alto nível; desenho e avaliação ficam como lacuna. |
| Citado na revisão | — | Yurtalan: LLMs locais de pesos abertos em OSINT policial (ref. [14]) | Referência [14] | Argumento on-premise; a revisão cita uma decisão italiana de proteção de dados como contexto. |
| Framework | 2025 | OWASP Top 10 for Agentic Applications | OWASP (dez/2025, segundo a Bugcrowd) | Lista própria para agentes, irmã do Top 10 de LLM. |
| Material da aula | 2026 | Áudio “Como hackers envenenam IAs de cibersegurança” (23 min) | Anexo da conversa | Não deu para transcrever aqui. O conteúdo da aula e os quatro dossiês foram conferidos contra as fontes (aba Recursos). |
| Dossiê 2 | 2026 | GTG-20006: ator com nexo russo usando IA para phishing e ferramentas | Relatório da Anthropic (set/2026), via boletim | Abra o original antes de usar. |
| Dossiê 2 | 2026 | TRM Labs: índice de adoção de IA no cripto-crime (54/100 em 2026) | TRM Labs (ago/2026), via cobertura | Plataforma onion DIG virou chat sem censura. |
| Dossiê 2 | 2026 | Linha de vermes de prompt: AgentWorm, Zombie Agents, Mind Viruses, Share-Borne AI Virus (arXiv 2609.35576) | arXiv | Laboratório; nenhum verme confirmado em campo. |
| Dossiê 2 | 2026 | Exposição: 492 servidores MCP sem autenticação (Trend Micro) | Cobertura secundária | Mais dezenas de milhares de instâncias OpenClaw expostas no início de 2026. |
| Dossiê 4 | 2026 | Alerta FLASH do FBI sobre o ARTEX (13/11/2026) | FBI, via cobertura | Fonte de indicadores; confira o original. |
| Dossiê 4 | 2026 | NIST IR 8596: perfil de cibersegurança para IA (rascunho) | NIST | Ainda em rascunho. |
| Dossiê 4 | — | Clássicos de defesa: Detection Maturity Level, Hunting Maturity Model, PEAK, TaHiTI, Pirâmide da Dor, Código do Almirantado, Sigma, D3FEND | Referências consolidadas | Citados de memória nos dossiês: confira edição e link. |
| Dossiê 5 | 2026 | Ler na íntegra o “ARTEX and Friends” do GTIG antes de citar números | Google Cloud Blog | A página existe; o conteúdo não foi lido. |
| Dossiê 5 | — | Mapear CERT.br, CTIR Gov, regulador financeiro e comunidades MISP setoriais | Contatos e regras de uso | Fonte, consumidor e possível vetor de propagação de dado ruim. |
| Dossiê 5 | 2026 | Relatório completo da Kaspersky com ransomware, phishing e participação regional | Kaspersky | O comunicado não traz esses números. |
| LLmInjection | 2026 | Ler a palestra ou artigo da Viaconnect (EDR → SOC com IA) | Zenity AI Agent Security Summit 2026 | Possível parceria de replicação no Brasil. |
| LLmInjection | 2026 | Pistas do panorama Brasil ainda sem fonte primária: Serasa e Banco Central sobre golpes com Pix e deepfake; PixRevolution (Recorded Future) | docs/pt-BR/PANORAMA-BRASIL-LATAM.md | Mantidas fora dos dados pelo próprio repositório. |


## Status por trabalho

| Status | Trabalhos |
|---|---|
| Conferido na fonte | 53 |
| Dossiê A | 47 |
| Dossiê B | 17 |
| A conferir | 14 |
| Preprint conferido | 13 |
| Conferido via cobertura | 7 |
| Alegação (C) | 1 |
