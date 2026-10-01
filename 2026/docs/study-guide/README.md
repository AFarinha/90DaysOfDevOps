# Manual de estudo - 90DaysOfDevOps 2026

Síntese conceptual dos 90 dias existentes em `2026`, em português de Portugal. Recorda responsabilidades, diferenças e relações entre componentes, sem reproduzir os exercícios.

## Como consultar

| Documento | Pergunta a que responde |
| --- | --- |
| [Visão geral](devops-overview.md) | Porque existe DevOps e como progride a formação? |
| [Tecnologias](technologies.md) | Para que serve cada ferramenta e onde entra no sistema? |
| [Conceitos](concepts.md) | Que princípios se mantêm quando mudam as ferramentas? |
| [Arquitetura e fluxos](architecture.md) | Como passam código, tráfego, dados e telemetria entre componentes? |
| [Revisão rápida](cheat-sheet.md) | Que diferenças e ligações devo conseguir explicar? |
| [Glossário](glossary.md) | O que significa este termo? |
| [Índice dos 90 dias](day-index.md) | Em que exercício posso aprofundar este assunto? |

Para uma revisão curta, começa pela revisão rápida. Para reconstruir o modelo completo, lê visão geral, conceitos e arquitetura; consulta tecnologias conforme necessário.

## Fontes e critérios

Foram analisados os 90 enunciados dos dias 01-90, as notas locais de todos os dias e os relatórios e artefactos relevantes em `2026`. O [índice original](../../README.md) localiza os blocos; o índice deste guia liga a cada enunciado.

Só foi considerado conteúdo formativo de **2026**. As pastas de outras edições não foram usadas. Os projetos externos citados são identificados pelo papel que os materiais locais lhes atribuem; este guia não depende de novas consultas ou clones desses projetos.

Distinguem-se três níveis:

- **Núcleo desenvolvido:** ferramentas e conceitos com exercícios próprios.
- **Alternativa ou apoio:** opções de aplicação, ambiente, biblioteca ou implementação, apresentadas proporcionalmente ao curso.
- **Extensão mencionada:** sugestões de aprofundamento ou produção, sem as apresentar como exercícios concluídos.

Os diagramas são modelos de estudo, não provas de execução. Usam Mermaid, compatível com Markdown no GitHub; num leitor sem esse suporte, o bloco permanece legível como texto.

## Limites e ambiguidades das fontes

Todos os dias têm enunciado. O currículo é identificável, mas existem simplificações e diferenças face aos relatórios locais:

| Dias | Ponto a interpretar com cuidado |
| --- | --- |
| 05 | Pede pelo menos oito comandos, mas enumera seis categorias com dois comandos cada. Reter o diagnóstico por camadas. |
| 08 | O título inclui Docker; as notas e tarefas concentram-se sobretudo em VM, SSH, Nginx e acesso web. |
| 40 | O nome do repositório aparece como `git `; os dias seguintes usam `github-actions-practice`. |
| 45 | Um trigger limitado a `main` não testa builds em feature branches sem ser alargado. |
| 48 | O deploy proposto imprime uma mensagem; isso não demonstra uma aplicação instalada em produção. |
| 49 | Scan sem deteções não prova ausência de vulnerabilidades; analisar o artefacto que será efetivamente publicado. |
| 51-58 | Nem todos os recursos têm `spec`; dry-run local e estado Running não provam validade no servidor ou prontidão. Código 137, isoladamente, não prova OOM. |
| 52, 78 | Rolling update não garante indisponibilidade zero; rollback de workload existe sem Helm, mas difere do histórico de uma release completa. |
| 63, 67, 70 | Há indicações contraditórias sobre precedência de variáveis e carregamento de ficheiros; os relatórios locais registam correções. |
| 75-77 | Promtail integra a stack de estudo; traces no exporter de debug não equivalem a armazenamento pesquisável nem a prontidão de produção. |
| 79-80 | O chart não converte necessariamente toda a infraestrutura. Um hook pré-instalação não pode esperar por uma base de dados que a mesma instalação ainda não criou. |
| 81-83 | EKS, TLS, balanceador e EBS dependem de AWS e controladores reais. Ensaios em kind não validam essas integrações. Preços e capacidades dos enunciados não são garantias atuais. |
| 82 | Gateway API tem versões próprias. Criar Gateway não garante NLB; afinidade não preserva sessões após a morte do Pod. |
| 85 | PVC com WaitForFirstConsumer numa wave anterior ao consumidor pode bloquear o sync. Wave do pai não garante prontidão das aplicações filhas. |
| 86 | O exemplo de referência tolera falhas de testes; o workflow local torna-os bloqueantes. HPA e Argo CD precisam de ownership coerente sobre réplicas. |
| 87-89 | Modelos e bibliotecas são exemplos. Temperatura baixa não garante determinismo; os relatórios distinguem diagnóstico real de respostas simuladas. |
| 90 | Uma tabela agrupa os dias 59-60 com Terraform, apesar de serem Helm e o capstone Kubernetes. O índice deste guia segue os enunciados individuais. |

Os registos locais indicam preparação sem execução AWS nos dias 61-70 e 81-83, validação parcial nos dias 85-86 e diagnóstico Claude pendente no dia 89. Neste último houve validação real de Temporal e correções Kubernetes com diagnóstico simulado. Estes são limites da evidência anterior, não resultados obtidos durante a criação do guia.

## Âmbito desta documentação

Não foram alterados exercícios, enunciados, configurações ou resultados anteriores. Não foram executados deploys, operações cloud ou agentes de remediação para escrever o manual. O pedido explícito de documentação complementar em PT-PT determina a língua e localização deste guia; as convenções das resoluções diárias mantêm-se nos dias originais.

## Validação desta documentação

A revisão final confirmou 90 enunciados, 90 notas e 220 outros ficheiros Markdown ao nível das pastas diárias. O índice liga os 90 dias; os 119 links locais resolvem para ficheiros existentes. Os sete diagramas passaram parsing e geração de SVG com Mermaid num browser local offline. Não foram guardados screenshots ou SVGs.

Foram verificados fences, tabelas e whitespace. A comparação de hashes de 557 ficheiros originais das pastas diárias não detetou alterações; a diferença face ao estado Git inicial acrescenta apenas esta pasta de documentação. Esta validação diz respeito ao guia, não à execução dos exercícios.
