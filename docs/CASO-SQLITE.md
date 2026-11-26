<!-- Gerado por scripts/gerar_docs.py a partir de data/. Edite os JSON, não este arquivo. -->

# Ficha canônica: Lote de CVEs fabricados citando o repositório programmervuln/cveadvisory- (jul/2026)

**Primeiro caso identificado nesta pesquisa.** Busca em fontes abertas (imprensa técnica, listas de segurança, literatura acadêmica e cinzenta, bases de vulnerabilidade) feita para esta linha até 26/11/2026. Não é um levantamento exaustivo: outro caso anterior pode existir fora desse escopo.

## As quatro perguntas

### Quantos avisos foram publicados e quantos foram examinados?

O repositório tinha 55 avisos (auditoria posterior da JFrog, que diz que 54 eram totalmente fabricados e um continha um bug real; o post não diz se todos foram checados um a um). Na lista oficial de CVEs, 32 registros citando o repositório foram publicados entre 27 e 30/07/2026 no bloco 51xxx: 13 sobre SQLite, 18 sobre ESP32-audioI2S e 1 sobre LibRaw. A JFrog examinou em detalhe seis, todos de SQLite.

*Certeza: Alta para os 32 e os seis (registros oficiais e relatório técnico); moderada para os 55 e os 54 (afirmação da JFrog sem método detalhado).*

### Quais registros chegaram às bases oficiais e receberam enriquecimento?

Todos os 32 foram publicados na lista oficial (CNA: MITRE), que a NVD espelha. 28 receberam enriquecimento CISA-ADP (Vulnrichment) com nota CVSS, mediana de cerca de 3 horas depois da publicação; 15 chegaram a 9,0 ou mais em algum momento. As notas vieram da CISA, não da CNA (que não deu nota) nem do NIST (páginas da NVD mostram “NVD assessment not yet provided”). Os seis examinados pela JFrog: 51296 (7,5), 51297 (8,8), 51300 (9,1), 51302 (9,8, revista para 7,5 em 30/07), 51303 (9,8) e 51304 (7,5). A Red Hat chegou a 10,0 em 51302 e rebaixou para 7,6.

*Certeza: Alta: histórico de commits da lista oficial (uma linha por registro na tabela abaixo).*

### Qual é a evidência de geração por IA?

Suspeita, não fato. A JFrog escreve que os avisos “parecem” gerados por IA e que o GPTZero os marcou; o título do post é uma pergunta. O que é fato é a fabricação: o código citado não existe nas versões afetadas, o autor do SQLite chamou os CVEs de fictícios no fórum oficial (29/07) e a Red Hat repete isso nas páginas que atualizou.

*Certeza: Fabricação: alta. Geração por IA: baixa a moderada (detector de texto e julgamento de analista).*

### O que se sabe sobre a motivação do autor?

Nada. A JFrog não atribui intenção e nenhuma fonte identificou o autor. Recompensa, currículo, reputação, teste do sistema e influência sobre scanners são explicações a investigar, não conclusões.

*Certeza: Desconhecida.*

## Linha do tempo

| Data | O quê | Fonte |
|---|---|---|
| 2026-06-07 | Identificadores reservados (dateReserved). | lista oficial |
| 2026-07-27 | Nove registros publicados: sete de SQLite (entre eles os seis que a JFrog examinou), um de LibRaw e um de ESP32-audioI2S. A CISA começa a enriquecer em horas. | lista oficial |
| 2026-07-28 | Mais 16 registros de ESP32-audioI2S publicados. | lista oficial |
| 2026-07-28 | Um mantenedor do Fedora escreve no Bugzilla que 51296 e 51298 são relatos completamente falsos: o código nem existe na versão citada. | Bugzilla da Red Hat |
| 2026-07-29 | Richard Hipp abre no fórum oficial do SQLite o tópico “Fake CVEs against SQLite”. | fórum do SQLite |
| 2026-07-30 | Ainda saem sete registros: seis de SQLite (51290 a 51295) e um de ESP32-audioI2S, depois de o autor do SQLite já ter chamado os anteriores de fictícios. A JFrog publica a análise. A CISA rebaixa 51302 de 9,8 para 7,5. | lista oficial; JFrog |
| 2026-07-31 | A CNA rejeita os 32 registros (motivo: “não era um problema de segurança”). | lista oficial; OSS-Security |
| 2026-08-03 | The Register publica o caso. | imprensa |
| 2026-08-04 | Bugs de falha da Red Hat para 51302, 51303 e 51304 ainda abertos (status NEW) na última modificação indexada. | piloto de retratações |
| 2026-08-17 | Trackers do Fedora para 51303 ainda abertos na última modificação indexada. | piloto de retratações |


## Os registros na lista oficial

Fonte: https://github.com/CVEProject/cvelistV5, commit 2233e247ef. Datas são as dos commits da lista oficial (UTC). Enriquecimento = contêiner ADP da CISA (Vulnrichment) com nota CVSS. O escopo é o bloco 51xxx; registros do mesmo lote em outros blocos não entram. Reproduza com `python3 scripts/caso_cve.py`.

| Registro | Produto | Examinado pela JFrog | Publicado (UTC) | Nota da CISA | Horas até a nota | Rejeitado (UTC) | Horas publicado |
|---|---|---|---|---|---|---|---|
| CVE-2026-51235 | LibRaw |  | 2026-07-27 17:33 | 8.8 | 1.2 | 2026-07-31 14:43 | 93.2 |
| CVE-2026-51244 | ESP32-audioI2S |  | 2026-07-27 18:44 | 7.5 | 0.5 | 2026-07-31 14:43 | 92.0 |
| CVE-2026-51251 | ESP32-audioI2S |  | 2026-07-28 14:33 | 7.5 | 4.3 | 2026-07-31 14:43 | 72.2 |
| CVE-2026-51252 | ESP32-audioI2S |  | 2026-07-28 14:33 | 9.8 | 4.3 | 2026-07-31 14:43 | 72.2 |
| CVE-2026-51254 | ESP32-audioI2S |  | 2026-07-28 14:33 | 7.8 | 4.3 | 2026-07-31 14:43 | 72.2 |
| CVE-2026-51259 | ESP32-audioI2S |  | 2026-07-28 14:33 | 9.8 | 4.3 | 2026-07-31 14:43 | 72.2 |
| CVE-2026-51260 | ESP32-audioI2S |  | 2026-07-28 14:33 | 9.4 | 4.3 | 2026-07-31 14:43 | 72.2 |
| CVE-2026-51261 | ESP32-audioI2S |  | 2026-07-28 14:33 | 9.8 | 51.3 | 2026-07-31 14:43 | 72.2 |
| CVE-2026-51263 | ESP32-audioI2S |  | 2026-07-28 15:25 | 9.8 | 2.9 | 2026-07-31 14:43 | 71.3 |
| CVE-2026-51266 | ESP32-audioI2S |  | 2026-07-28 15:25 | 9.8 | 2.9 | 2026-07-31 14:43 | 71.3 |
| CVE-2026-51267 | ESP32-audioI2S |  | 2026-07-28 15:25 | 9.8 | 2.9 | 2026-07-31 14:43 | 71.3 |
| CVE-2026-51268 | ESP32-audioI2S |  | 2026-07-28 15:25 | 9.8 | 50.4 | 2026-07-31 14:43 | 71.3 |
| CVE-2026-51269 | ESP32-audioI2S |  | 2026-07-28 15:25 | 8.8 | 2.4 | 2026-07-31 14:43 | 71.3 |
| CVE-2026-51270 | ESP32-audioI2S |  | 2026-07-28 15:25 | 8.8 | 50.4 | 2026-07-31 14:43 | 71.3 |
| CVE-2026-51271 | ESP32-audioI2S |  | 2026-07-28 16:10 | 9.6 | 2.2 | 2026-07-31 14:43 | 70.5 |
| CVE-2026-51272 | ESP32-audioI2S |  | 2026-07-30 17:51 | 9.8 | 2.2 | 2026-07-31 14:43 | 20.9 |
| CVE-2026-51273 | ESP32-audioI2S |  | 2026-07-28 16:48 | 7.8 | 1.5 | 2026-07-31 14:43 | 69.9 |
| CVE-2026-51274 | ESP32-audioI2S |  | 2026-07-28 16:48 | 8.8 | 1.1 | 2026-07-31 14:43 | 69.9 |
| CVE-2026-51275 | ESP32-audioI2S |  | 2026-07-28 16:48 | 8.8 | 1.1 | 2026-07-31 14:43 | 69.9 |
| CVE-2026-51290 | SQLite |  | 2026-07-30 16:45 | 9.1 | 2.7 | 2026-07-31 14:43 | 22.0 |
| CVE-2026-51291 | SQLite |  | 2026-07-30 16:45 | 9.8 | 2.7 | 2026-07-31 14:43 | 22.0 |
| CVE-2026-51292 | SQLite |  | 2026-07-30 16:45 | sem nota | — | 2026-07-31 14:43 | 22.0 |
| CVE-2026-51293 | SQLite |  | 2026-07-30 16:45 | sem nota | — | 2026-07-31 14:43 | 22.0 |
| CVE-2026-51294 | SQLite |  | 2026-07-30 16:45 | sem nota | — | 2026-07-31 14:43 | 22.0 |
| CVE-2026-51295 | SQLite |  | 2026-07-30 16:45 | sem nota | — | 2026-07-31 14:43 | 22.0 |
| CVE-2026-51296 | SQLite | sim | 2026-07-27 15:25 | 7.5 | 23.1 | 2026-07-31 14:43 | 95.3 |
| CVE-2026-51297 | SQLite | sim | 2026-07-27 15:25 | 8.8 | 3.3 | 2026-07-31 14:43 | 95.3 |
| CVE-2026-51298 | SQLite |  | 2026-07-27 15:25 | 6.2 | 3.3 | 2026-07-31 14:43 | 95.3 |
| CVE-2026-51300 | SQLite | sim | 2026-07-27 15:25 | 9.1 | 22.3 | 2026-07-31 14:43 | 95.3 |
| CVE-2026-51302 | SQLite | sim | 2026-07-27 15:25 | 9.8 → 7.5 | 22.3 | 2026-07-31 14:43 | 95.3 |
| CVE-2026-51303 | SQLite | sim | 2026-07-27 15:25 | 9.8 | 3.3 | 2026-07-31 14:43 | 95.3 |
| CVE-2026-51304 | SQLite | sim | 2026-07-27 15:25 | 7.5 | 2.7 | 2026-07-31 14:43 | 95.3 |


## Que evidência futura distinguiria H7

- O mesmo autor ou conta reaparece com lotes em outros projetos (padrão de volume, típico de incentivo).
- Os avisos aparecem ligados a pedidos de recompensa, currículo, perfil ou portfólio.
- Nenhuma exploração, nenhum produto ou cliente específico e nenhuma narrativa favorecida pelos registros (contra H3 e contra uma campanha dirigida).
- Os alvos são escolhidos por popularidade (SQLite, bibliotecas muito usadas), não por relevância para um setor ou um adversário.

## Correções feitas

- “54 CVEs falsos entraram no NVD” estava errado: 54 é a estimativa da JFrog para o repositório; 32 viraram registros oficiais; seis foram examinados.
- “Notas de até 9,8 dadas pelo NVD” estava impreciso: as notas vieram da CISA (ADP), não do NIST nem da CNA.
- “Gerados por IA” passou a “com suspeita de geração por IA”; a fabricação é que está confirmada.
- “Primeiro caso público” passou a “primeiro caso identificado nesta pesquisa”, com escopo e data da busca.

## Piloto de retratações (versão 0, 2026-11-26)

Versão 0, por índice de busca: para cada um dos seis registros de SQLite examinados pela JFrog, buscas pelo identificador e classificação da cópia indexada de cada página em quatro estados (ainda apresentado como válido, rejeição visível, removido, indisponível para consulta), mais “misto” (rejeição visível com nota crítica ainda exibida), “não afetado” e “inconclusivo”. Uma página que preserva o registro e mostra a rejeição conta como correção propagada, não como falha. Quando a página exibe a data da última modificação, ela delimita o atraso conhecido; sem essa data, não se sabe quando a cópia foi feita.

**Limites:** Cópias de índice de busca, não páginas consultadas ao vivo: uma página marcada como válida pode já ter sido corrigida. A consulta direta às páginas ficou pendente nesta rodada; o script scripts/zumbis.py faz essa captura com data e hora. A lista de fontes é a que o índice devolveu, não uma amostra planejada.

| Registro | Fonte | Estado | Última modificação exibida | O que a cópia mostra |
|---|---|---|---|---|
| CVE-2026-51296 | [Lista oficial de CVEs (CVE Program)](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/51xxx/CVE-2026-51296.json) | rejeição visível | 2026-07-31 | Estado REJECTED desde 31/07; referência para medir atraso. Coletado do repositório oficial. |
| CVE-2026-51297 | [Lista oficial de CVEs (CVE Program)](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/51xxx/CVE-2026-51297.json) | rejeição visível | 2026-07-31 | Estado REJECTED desde 31/07; referência para medir atraso. Coletado do repositório oficial. |
| CVE-2026-51300 | [Lista oficial de CVEs (CVE Program)](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/51xxx/CVE-2026-51300.json) | rejeição visível | 2026-07-31 | Estado REJECTED desde 31/07; referência para medir atraso. Coletado do repositório oficial. |
| CVE-2026-51302 | [Lista oficial de CVEs (CVE Program)](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/51xxx/CVE-2026-51302.json) | rejeição visível | 2026-07-31 | Estado REJECTED desde 31/07; referência para medir atraso. Coletado do repositório oficial. |
| CVE-2026-51303 | [Lista oficial de CVEs (CVE Program)](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/51xxx/CVE-2026-51303.json) | rejeição visível | 2026-07-31 | Estado REJECTED desde 31/07; referência para medir atraso. Coletado do repositório oficial. |
| CVE-2026-51304 | [Lista oficial de CVEs (CVE Program)](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/51xxx/CVE-2026-51304.json) | rejeição visível | 2026-07-31 | Estado REJECTED desde 31/07; referência para medir atraso. Coletado do repositório oficial. |
| CVE-2026-51296 | [Red Hat (página do CVE)](https://access.redhat.com/security/cve/CVE-2026-51296) | rejeição visível | não exibida | Diz que o upstream confirmou o CVE como fictício e que a CNA o rejeitou. |
| CVE-2026-51296 | [Red Hat Bugzilla (falha 2507546)](https://bugzilla.redhat.com/show_bug.cgi?id=2507546) | ainda apresentado como válido | não exibida | Status NEW, com a descrição original da falha. |
| CVE-2026-51296 | [Fedora (tracker 2507909)](https://bugzilla.redhat.com/show_bug.cgi?id=2507909) | misto | 2026-07-28 | Um mantenedor comentou em 28/07 que o relato é completamente falso; o tracker segue com o título da falha. |
| CVE-2026-51296 | [OSV (UBUNTU-CVE-2026-51296)](https://osv.dev/vulnerability/UBUNTU-CVE-2026-51296) | inconclusivo | 2026-07-29 | Cópia indexada anterior à rejeição (gravidade média, pacotes afetados). |
| CVE-2026-51296 | [INCIBE-CERT](https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2026-51296) | ainda apresentado como válido | 2026-07-27 | Descrição da falha, análise pendente. |
| CVE-2026-51296 | [SentinelOne (base de vulnerabilidades)](https://www.sentinelone.com/vulnerability-database/cve-2026-51296/) | ainda apresentado como válido | 2026-07-29 | Artigo técnico tratando a falha como real. |
| CVE-2026-51296 | [cvefeed.io](https://cvefeed.io/vuln/detail/CVE-2026-51296) | ainda apresentado como válido | 2026-07-27 | Orienta atualizar o SQLite. |
| CVE-2026-51296 | [Amazon Linux (ALAS)](https://explore.alas.aws.amazon.com/CVE-2026-51296.html) | inconclusivo | 2026-07-31 | Modificada em 31/07; o trecho indexado não mostra o estado. |
| CVE-2026-51297 | [Red Hat (página do CVE)](https://access.redhat.com/security/cve/CVE-2026-51297) | inconclusivo | não exibida | O trecho indexado só mostra a descrição. |
| CVE-2026-51297 | [INCIBE-CERT](https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2026-51297) | ainda apresentado como válido | 2026-07-27 | Descrição da falha, análise pendente. |
| CVE-2026-51297 | [SentinelOne (base de vulnerabilidades)](https://www.sentinelone.com/vulnerability-database/cve-2026-51297/) | ainda apresentado como válido | 2026-07-29 | Artigo técnico tratando a falha como real. |
| CVE-2026-51300 | [Red Hat Bugzilla (falha 2507549)](https://bugzilla.redhat.com/show_bug.cgi?id=2507549) | ainda apresentado como válido | não exibida | Status NEW, com a descrição original. |
| CVE-2026-51300 | [Feedly (página do CVE)](https://feedly.com/cve/CVE-2026-51300) | ainda apresentado como válido | não exibida | CVSS 9,1 crítico, “Public PoC” e orientação de aplicar patches. |
| CVE-2026-51300 | [Amazon Linux (ALAS)](https://explore.alas.aws.amazon.com/CVE-2026-51300.html) | não afetado (sem citar a rejeição) | não exibida | Amazon Linux 2 e 2023 marcados como não afetados. |
| CVE-2026-51300 | [INCIBE-CERT](https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2026-51300) | ainda apresentado como válido | 2026-07-27 | Análise pendente. |
| CVE-2026-51302 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-51302) | inconclusivo | 2026-07-28 | Cópia indexada anterior à rejeição; outros registros do lote aparecem na NVD com o texto de rejeição. |
| CVE-2026-51302 | [OSV (CVE-2026-51302)](https://osv.dev/vulnerability/CVE-2026-51302) | inconclusivo | 2026-08-01 | Modificada depois da rejeição e ainda com descrição e gravidade 7,5; o trecho não mostra o campo de retirada. |
| CVE-2026-51302 | [Red Hat Bugzilla (falha 2507543)](https://bugzilla.redhat.com/show_bug.cgi?id=2507543) | ainda apresentado como válido | 2026-08-04 | Status NEW, com a descrição original, quatro dias depois da rejeição. |
| CVE-2026-51302 | [OpenCVE](https://app.opencve.io/cve/CVE-2026-51302) | misto | 2026-07-31 | Mostra status REJECTED e, no topo, “CVSS 3.1 · 10.0 Critical”. |
| CVE-2026-51302 | [SentinelOne (base de vulnerabilidades)](https://www.sentinelone.com/vulnerability-database/cve-2026-51302/) | ainda apresentado como válido | 2026-07-30 | Artigo técnico tratando a falha como real. |
| CVE-2026-51302 | [cvefeed.io](https://cvefeed.io/vuln/detail/CVE-2026-51302) | ainda apresentado como válido | 2026-07-27 | Orienta atualizar para 3.41.2 ou posterior. |
| CVE-2026-51302 | [vulert](https://vulert.com/vuln-db/CVE-2026-51302) | ainda apresentado como válido | não exibida | Descrição técnica e instruções de correção. |
| CVE-2026-51302 | [cve.threatint.com](https://cve.threatint.com/CVE/CVE-2026-51302) | ainda apresentado como válido | 2026-07-27 | Estado PUBLISHED. |
| CVE-2026-51303 | [Red Hat Bugzilla (falha 2507555)](https://bugzilla.redhat.com/show_bug.cgi?id=2507555) | ainda apresentado como válido | 2026-08-04 | Status NEW, quatro dias depois da rejeição. |
| CVE-2026-51303 | [Fedora (tracker 2508472, mingw-sqlite)](https://bugzilla.redhat.com/show_bug.cgi?id=2508472) | ainda apresentado como válido | 2026-08-17 | Tracker aberto, gravidade alta, 17 dias depois da rejeição. |
| CVE-2026-51303 | [Fedora (tracker 2508475, fossil)](https://bugzilla.redhat.com/show_bug.cgi?id=2508475) | ainda apresentado como válido | 2026-08-17 | Tracker aberto, 17 dias depois da rejeição. |
| CVE-2026-51303 | [Feedly (página do CVE)](https://feedly.com/cve/CVE-2026-51303) | ainda apresentado como válido | não exibida | CVSS 9,8 crítico, “Public PoC” e detecção no Nessus. |
| CVE-2026-51303 | [OpenCVE](https://app.opencve.io/cve/CVE-2026-51303) | misto | não exibida | Texto “DO NOT USE THIS CVE RECORD” ao lado de “CVSS 3.1 · 9.8 Critical”. |
| CVE-2026-51303 | [averlon](https://research.averlon.ai/vulnerability-intelligence/cve/CVE-2026-51303) | ainda apresentado como válido | não exibida | Gravidade crítica, CVSS 9,8. |
| CVE-2026-51303 | [cve.report](https://cve.report/CVE-2026-51303) | ainda apresentado como válido | 2026-07-27 | Estado PUBLISHED. |
| CVE-2026-51303 | [INCIBE-CERT](https://www.incibe.es/en/incibe-cert/early-warning/vulnerabilities/cve-2026-51303) | ainda apresentado como válido | 2026-07-27 | Análise pendente. |
| CVE-2026-51304 | [Red Hat (página do CVE)](https://access.redhat.com/security/cve/CVE-2026-51304) | rejeição visível | não exibida | Não afeta os produtos; upstream confirmou como fictício; CNA rejeitou. |
| CVE-2026-51304 | [CIRCL vulnerability-lookup](https://cve.circl.lu/cve/CVE-2026-51304) | rejeição visível | 2026-07-31 | Espelha o estado REJECTED da lista oficial. |
| CVE-2026-51304 | [Red Hat Bugzilla (falha 2507560)](https://bugzilla.redhat.com/show_bug.cgi?id=2507560) | ainda apresentado como válido | 2026-08-04 | Status NEW, quatro dias depois da rejeição. |
| CVE-2026-51304 | [Feedly (página do CVE)](https://feedly.com/cve/CVE-2026-51304) | ainda apresentado como válido | não exibida | CVSS 7,5 e “A patch is available” com link para aviso do GitHub. |
| CVE-2026-51304 | [SentinelOne (base de vulnerabilidades)](https://www.sentinelone.com/vulnerability-database/cve-2026-51304/) | ainda apresentado como válido | 2026-07-29 | Artigo técnico com indicadores de comprometimento. |
| CVE-2026-51304 | [OSV (CVE-2026-51304)](https://osv.dev/vulnerability/CVE-2026-51304) | inconclusivo | 2026-07-31 | Modificada às 03h49 UTC de 31/07, antes da rejeição. |
| CVE-2026-51304 | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-51304) | inconclusivo | 2026-07-29 | Cópia indexada anterior à rejeição. |


Captura direta, com data e hora: `python3 scripts/zumbis.py` (acrescenta linhas em `data/zumbis-capturas.csv`).