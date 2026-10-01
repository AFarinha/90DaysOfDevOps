# Tecnologias: responsabilidade e conhecimentos a reter

[Entrada do guia](README.md) · [Conceitos](concepts.md) · [Comparações](cheat-sheet.md)

Os dias remetem para o [índice](day-index.md). Alternativas e extensões recebem cobertura proporcional ao que foi desenvolvido no curso.

## Linux, systemd e journald

**Fonte:** dias 02-12. Linux fornece kernel, processos, memória, dispositivos, rede e filesystem. O kernel gere recursos; user space executa aplicações. systemd organiza serviços e dependências de arranque; journald recolhe registos. São a base da operação antes de qualquer orquestrador.

**Conceitos:** PID, estados running/sleeping/zombie, sinais, serviço, unit, arranque, logs, utilizador, grupo e permissões. Ubuntu, Amazon Linux e Alpine representam distribuições/imagens de base diferentes.

**No fluxo:** aplicação → processo Linux → recursos do host; ajuda a interpretar VMs, containers e nós Kubernetes.

**Recordar:**

- Estado do processo, estado do serviço e resposta HTTP são evidências distintas.
- Serviço ativo não implica enabled no arranque; enabled não implica ativo agora.
- `/etc` concentra configuração; `/var/log`, registos; `/home`, dados pessoais; `/tmp`, temporários; `/opt`, aplicações adicionais.
- chmod muda permissões; chown/chgrp mudam ownership. Permissões de diretório controlam listagem, alteração e travessia.
- Zombie significa processo terminado ainda não recolhido pelo pai.

**Confusão:** usar root ultrapassa uma barreira, mas não explica se as permissões estão corretas.

## LVM e armazenamento Linux

**Fonte:** dia 13. Logical Volume Manager (LVM) acrescenta uma camada flexível entre discos e filesystems para agregar e dimensionar capacidade.

**Conceitos:** Physical Volume (PV) → Volume Group (VG) → Logical Volume (LV) → filesystem → ponto de montagem. Loop devices simulam discos; ext4 é o filesystem exemplificado.

**Recordar:**

- Aumentar LV e aumentar filesystem são operações distintas.
- Montar torna o filesystem acessível num caminho; não copia dados para esse caminho.
- Capacidade livre no grupo, volume e filesystem são medidas diferentes.

**Confusão:** PV do LVM é Physical Volume; PV Kubernetes é PersistentVolume.

## SSH, DNS e ferramentas de rede

**Fonte:** dias 03, 08, 14-15 e 68. Secure Shell (SSH) permite administração remota autenticada e cifrada. Domain Name System (DNS) resolve nomes. As ferramentas observam camadas diferentes do serviço.

| Ferramenta | Sinal que fornece |
| --- | --- |
| ip, hostname | Endereços e identidade de rede |
| ping | Resposta ICMP, latência e perda; não testa a aplicação |
| traceroute/tracepath | Percurso observado entre redes |
| ss/netstat | Sockets, listeners e ligações |
| dig/nslookup | Resolução DNS e registos |
| curl/wget | Resposta de protocolo/aplicação e transferência |
| nc | Teste de porta/conectividade |
| PuTTY | Cliente SSH exemplificado para Windows |

**Recordar:**

- Resolver o nome não prova porta acessível; porta acessível não prova aplicação saudável.
- A/AAAA associam nomes a IPv4/IPv6; CNAME cria alias; MX indica correio; NS identifica servidores de nomes; TTL limita validade em cache.
- localhost é o próprio contexto de rede, incluindo o container onde corre o comando.

## Bash, cron e processamento de texto

**Fonte:** dias 16-21. Bash combina programas para automatizar tarefas operacionais; cron agenda execuções. grep, awk, sed, cut, sort, uniq, tr e wc processam texto; find seleciona ficheiros; tar e gzip arquivam/comprimem dados.

**Problema resolvido:** rotinas verificáveis de diagnóstico, rotação de logs e backup.

**Conceitos:** shebang, quoting, variáveis, argumentos, condições, loops, funções, stdin/stdout/stderr, pipes, exit codes, trap e âmbito local.

**Recordar:**

- Aspas duplas expandem variáveis; simples preservam texto literal. Quoting evita dividir caminhos e argumentos.
- return de função comunica estado; stdout pode transportar o resultado.
- `set -euo pipefail` ajuda a detetar falhas, mas não substitui tratamento explícito; `-e` tem exceções contextuais.
- Agendamento precisa de caminhos, ambiente e registos previsíveis, sem depender da sessão interativa.
- Backup criado não prova recuperação. Compressão e rotação controlam retenção.

## Git, GitHub e GitHub CLI

**Fonte:** dias 22-28, CI/CD e GitOps. Git versiona snapshots e histórico distribuído; GitHub aloja repositórios e suporta revisão/Actions. GitHub CLI (gh) automatiza a plataforma.

**Conceitos:** working tree, staging/index, commit, HEAD, branch, remote, clone, fork, pull request (PR), merge, rebase, squash, stash, cherry-pick, reset, revert e reflog.

**No fluxo:** revisão e verificações antecedem entrega; Git também versiona estado desejado.

**Recordar:**

- Commit é local; push publica commits num remote.
- Fetch obtém referências; pull também integra alterações.
- Branch é uma referência móvel; HEAD identifica o checkout atual.
- Merge integra históricos; rebase reaplica commits e muda a sua identidade.
- Revert cria um commit de inversão; reset reposiciona referências e pode afetar index/working tree.
- `.gitignore` não elimina segredos já existentes no histórico.
- GitFlow, GitHub Flow e trunk-based development organizam duração de branches e integração.

**Confusão:** clone é cópia local; fork é um repositório associado na plataforma. PR é um processo de colaboração, não um comando Git.

## Docker e Docker Hub

**Fonte:** dias 29-37 e 45-49. Docker constrói/executa containers; Docker Hub armazena/distribui imagens. Resolvem diferenças de dependências e distribuição do mesmo artefacto entre ambientes.

**Conceitos:** imagem, container, Dockerfile, build context, layers, cache, tag, digest, registry, portas, volumes, bind mounts e bridge networks.

**No fluxo:** fonte + Dockerfile → build → imagem → registry → runtime local ou Kubernetes.

**Recordar:**

- Imagem é o artefacto de base; container é uma instância com processos e camada gravável.
- Parar preserva a camada gravável; remover elimina-a. Volumes têm ciclo separado.
- EXPOSE documenta uma porta; não a publica no host.
- Multi-stage separa ferramentas de build do runtime. Alpine, slim, distroless e scratch têm requisitos distintos.
- Cache depende das instruções/entradas; mudar uma camada pode invalidar as seguintes.
- `.dockerignore` reduz contexto; não protege segredos já copiados.
- latest e tags baseadas em SHA podem ser movidas; digest identifica conteúdo.
- Bridge criada pelo utilizador permite resolução por nome; publicação de portas dá o acesso pretendido pelo host.

**Confusões:** Docker não gere sozinho um cluster; imagem pequena não prova segurança; registry de imagens difere de repository de charts.

## Docker Compose

**Fonte:** dias 33-37 e 72-77. Compose descreve serviços, redes, volumes e configuração de uma aplicação num host, coordenando app, base de dados, cache ou telemetria.

**Recordar:**

- Nomes de serviços funcionam como nomes de rede do projeto.
- depends_on simples ordena arranque; service_healthy exige healthcheck. A app deve tolerar falhas posteriores.
- `.env` alimenta interpolação; não injeta automaticamente tudo em cada container.
- Restart policy e healthcheck são distintos; unhealthy não implica sempre restart.
- Réplicas não podem todas publicar a mesma porta fixa do host.
- Desligar serviços e eliminar volumes/dados são decisões separadas.

## YAML e ferramentas de edição

**Fonte:** dia 38 e configurações posteriores. YAML representa dados de Compose, Actions, Kubernetes e Ansible. HCL configura Terraform; Go templates e Jinja2 geram configuração em contextos diferentes.

**Recordar:**

- Indentação define estrutura; booleanos diferem de strings com o mesmo texto.
- `|` preserva quebras de linha; `>` dobra linhas segundo regras YAML.
- YAML válido pode violar o schema da ferramenta.
- yamllint verifica estilo/sintaxe; yq edita estrutura; sed substitui texto.
- Vim é editor dos exercícios Linux, não componente da arquitetura.

## GitHub Actions e runners

**Fonte:** dias 40-48 e 86. Actions executa workflows associados a eventos; runners executam jobs. Actions empacotam operações reutilizáveis.

**Conceitos:** trigger, job, step, needs, matrix, context, env, output, artifact, cache, secret, environment e aprovação.

**Recordar:**

- Steps do mesmo job partilham ambiente; jobs não partilham automaticamente ficheiros/processos.
- Outputs passam valores; artifacts transportam ficheiros; cache acelera execuções.
- Matrix expande combinações de runtime/sistema; fail-fast controla cancelamentos após falha.
- Reusable workflow reutiliza jobs; composite action reutiliza steps.
- workflow_call invoca implementação; workflow_run reage a uma execução; repository_dispatch recebe eventos externos.
- Self-hosted exige atualizações, isolamento, credenciais e limpeza; labels selecionam máquinas, não garantem segurança.
- Aprovação de environment exige proteção configurada; chamar ao job deploy não instala software.
- Filtros de paths ajudam a evitar loops quando CI escreve em Git.

## Trivy e segurança GitHub

**Fonte:** dia 49. Trivy procura vulnerabilidades conhecidas nas imagens; dependency review avalia dependências de PR; secret scanning deteta credenciais; push protection pode bloquear publicação.

**Conceitos:** CVE (Common Vulnerabilities and Exposures), severidade, security gate, permissões mínimas, supply chain e SARIF, formato de resultados de análise.

**Recordar:**

- Scan é limitado pela cobertura, configuração e base de vulnerabilidades.
- Verificar uma tag mutável diferente do build pode analisar a imagem errada.
- Mascaramento não autoriza imprimir segredos; fuga exige revogação/rotação.
- Fixar actions por commit reduz dependência de tags móveis, sem dispensar atualizações deliberadas.
- OpenID Connect (OIDC), extensão do dia 49, permite identidade federada e credenciais temporárias.

## Kubernetes, kubectl, kind e minikube

**Fonte:** dias 50-60 e 78-89. Kubernetes mantém workloads declarativos através de scheduling e reconciliação. kubectl comunica com a API; kind usa containers Docker como nós; minikube é alternativa local com vários drivers.

**Conceitos:** control plane, node, Pod, API Server, etcd, scheduler, controllers, kubelet, runtime, kube-proxy, DNS, manifest e kubeconfig.

**Recordar:**

- API Server valida/expõe recursos; etcd persiste estado; scheduler atribui nós; controllers aproximam estado observado e desejado.
- kubelet gere execução através do runtime, como containerd ou CRI-O. Kubernetes não exige Docker Engine.
- Pod agrupa containers com rede e volumes partilhados; não é uma VM.
- Kubeconfig associa clusters, credenciais e contexts; context seleciona alvo e namespace.
- Deployment gere ReplicaSets e substituição de Pods; Pod isolado não tem essa garantia.
- StatefulSet acrescenta identidade e armazenamento por réplica; não implementa replicação dos dados da app.
- Namespace organiza recursos; isolamento de rede/acesso exige políticas adicionais.
- Client dry-run, server dry-run e teste funcional respondem a perguntas distintas.

**Confusão:** manter o número de Pods não resolve uma configuração errada em todas as réplicas.

## Recursos Kubernetes: rede, dados e configuração

**Fonte:** dias 51-60. São interfaces do Kubernetes, não ferramentas concorrentes.

| Recurso | Responsabilidade |
| --- | --- |
| Deployment / ReplicaSet | Atualizações e réplicas de Pods intercambiáveis |
| StatefulSet | Identidade estável e volumes por réplica |
| Service | Endpoint e seleção de backends por labels |
| Headless Service | Descoberta direta de endpoints, útil para StatefulSets |
| ConfigMap | Configuração não secreta por ficheiro ou variável de ambiente |
| Secret | Dados sensíveis com controlos de acesso; base64 não é cifragem |
| PersistentVolume / PersistentVolumeClaim | Oferta / pedido de armazenamento |
| StorageClass | Provisionamento dinâmico e ciclo de vida de volumes |
| HPA | Réplicas de acordo com métricas |
| ResourceQuota | Limite agregado no namespace, exemplificado no dia 80 |

**Recordar:**

- Selector deve corresponder às labels; port, targetPort e nodePort são camadas diferentes.
- ClusterIP é interno; NodePort expõe porta de nó; LoadBalancer depende de implementação de infraestrutura.
- Variáveis de ambiente ficam fixadas no arranque; volumes projetados podem atualizar-se, com exceções como subPath e latência de propagação.
- emptyDir acompanha o Pod: sobrevive a restart de container, não à eliminação do Pod.
- ReadWriteOnce (RWO) refere um nó com leitura/escrita, não necessariamente um único Pod.
- Retain/Delete determinam tratamento do armazenamento após libertar a claim; persistência não substitui backup.

## Metrics Server e HPA

**Fonte:** dias 57-58 e 81-83. Quality of Service (QoS) classifica Pods: Guaranteed exige requests/limits de CPU e memória iguais em todos os containers; BestEffort não tem esses valores; os restantes são Burstable. Metrics Server disponibiliza métricas recentes para kubectl top e autoscaling. Horizontal Pod Autoscaler (HPA) altera réplicas; não é uma base histórica como Prometheus.

**Recordar:**

- Requests ajudam scheduling e dão referência para utilização percentual de CPU; limits restringem consumo.
- Uso observado, request e limit são valores diferentes.
- HPA precisa de métricas e capacidade para novas réplicas; Pods podem ficar Pending.
- Estabilização/políticas reduzem oscilações; scaling não é instantâneo.
- Liveness pode reiniciar; readiness controla tráfego; startup protege inicialização lenta.
- Memória excessiva pode causar OOMKilled; CPU limitada tende a ser throttled. Confirmar reason/eventos, não inferir OOM só de exit 137.

## Helm e repositórios de charts

**Fonte:** dia 59 e dias 78-80. Helm empacota manifests em charts parametrizáveis, evitando repetição entre instalações/ambientes. Bitnami fornece charts usados nos exercícios.

**Conceitos:** Chart.yaml, values, Go templates, release, revision, dependencies, repository/OCI, hook, lint, render e rollback.

**Recordar:**

- Chart é pacote; release é instalação; revision regista operação sobre a release.
- version identifica chart; appVersion descreve app e não define automaticamente a tag da imagem.
- Values posteriores sobrepõem anteriores; templates precisam de utilizar esses valores.
- Lint/render não provam APIs, capacidade, volumes ou segredos disponíveis no cluster.
- Hook pré-instalação não pode esperar por um recurso que a instalação ainda não criou.
- Rollback de manifests não desfaz automaticamente migrações ou dados.
- Argo CD usa Helm para renderizar e gere os recursos, sem manter necessariamente uma release da CLI Helm.

**Apoio:** Kustomize, comparado no dia 80, aplica overlays/patches a manifests; helm diff é plugin mencionado, não dependência do guia.

## Terraform

**Fonte:** dias 61-67 e 81. Terraform provisiona infraestrutura declarativa através de providers e associa código a recursos reais.

**Conceitos:** HCL (HashiCorp Configuration Language), provider, resource, data source, variable, local, output, dependency, lifecycle, state, backend, locking, import, module e workspace.

**Recordar:**

- Init prepara providers/módulos/backend; validate verifica configuração; plan calcula alterações; apply executa-as.
- Resource gere objeto; data source consulta; variable recebe entrada; local deriva valores; output expõe resultados.
- Referências criam dependências implícitas; depends_on cobre relações não expressas pelos valores.
- State associa endereços Terraform a objetos; pode conter segredos mesmo com outputs sensitive.
- Backend remoto partilha estado; locking evita writers concorrentes; versionamento ajuda recuperação. O laboratório do dia 64 combina S3/DynamoDB.
- Import não garante configuração correta; state rm deixa o objeto real e pode levar plan a propor outro.
- Módulo encapsula recursos; workspace separa estado, não fronteiras completas de permissões/contas.
- Precedência conceptual: defaults < TF_VAR < ficheiros automáticos < flags explícitas, considerando ordem entre ficheiros/flags. `-var-file` não impede carregar terraform.tfvars.

**Confusão:** suporte a várias clouds não torna configuração AWS automaticamente portável.

## AWS: infraestrutura, identidade e armazenamento

**Fonte:** dia 08, dias 61-68 e 81-83. Amazon Web Services (AWS) disponibiliza infraestrutura por API; AWS CLI fornece operação e autenticação no curso.

| Componente | Problema resolvido / lugar no sistema |
| --- | --- |
| EC2 e AMI | Máquina virtual e imagem de sistema, para servidores ou worker nodes |
| VPC e subnets | Rede privada lógica e segmentação por zona |
| Route table / Internet Gateway | Percursos e ligação apropriada à Internet |
| NAT Gateway | Saída de redes privadas; não publica serviços privados |
| Security Group | Regras de tráfego associadas aos recursos |
| IAM | Identidades, roles e políticas de acesso a APIs AWS |
| S3 | Armazenamento de objetos, buckets e backend Terraform |
| DynamoDB | Locking no backend exemplificado; não é a base da BankApp |
| EBS / gp3 | Volumes de blocos para dados/modelos, com restrições de zona |
| Load balancer / NLB | Entrada/distribuição de tráfego conforme controlador e configuração |

**Recordar:**

- Subnet pública exige rotas e acesso coerentes, não apenas nome ou IP.
- IAM autoriza APIs; Security Groups autorizam tráfego. SSH exige ainda autenticação do sistema.
- Região, Availability Zone (AZ), AMI e capacidade devem ser compatíveis; várias zonas não garantem dados replicados.
- Remover cluster não prova remoção de todos os volumes/balanceadores criados por controladores.
- Entender componentes faturáveis e verificar recursos remanescentes vale mais que memorizar preços do enunciado.

**Alternativa:** Utho é opção de VM nos dias 08/42, sem o percurso aprofundado de serviços AWS.

## Amazon EKS e add-ons

**Fonte:** dias 66 e 81-83. Elastic Kubernetes Service (EKS) fornece control plane Kubernetes gerido na AWS. A equipa mantém responsabilidade por workloads, acesso, rede, dados e capacidade.

| Componente | Papel |
| --- | --- |
| Managed node group | Worker nodes EC2 com ciclo de vida integrado |
| CoreDNS | Resolução de Services |
| VPC CNI | Rede/IPs de Pods integrados na VPC |
| kube-proxy | Encaminhamento de Services no modelo estudado |
| EBS CSI driver | Provisionamento/montagem de EBS a partir de claims |
| Metrics Server | Métricas para top/HPA |
| IRSA / Pod Identity | Mecanismos distintos de acesso AWS para workloads |

CNI significa Container Network Interface; CSI, Container Storage Interface; IRSA, IAM Roles for Service Accounts. Identidade AWS de workload difere de RBAC, que autoriza operações na API Kubernetes.

**Recordar:**

- Kubernetes é o orquestrador; EKS é uma forma de o operar.
- Endereços/IPs, recursos allocatable e overhead condicionam Pods por nó.
- HPA aumenta Pods; dimensionar nodes é outra responsabilidade. Min/max num node group não prova um controlador a reagir a Pods Pending.
- EBS é zonal; WaitForFirstConsumer associa provisionamento à colocação inicial, sem tornar volume multizona.
- Self-managed nodes/Fargate são alternativas apresentadas, não implementação principal do laboratório.

## Ansible, Jinja2, Galaxy e Vault

**Fonte:** dias 68-72. Ansible configura sistemas existentes por tarefas e módulos, normalmente via SSH, sem daemon Ansible permanente nos alvos. Resolve deriva e repetição manual na instalação de pacotes, ficheiros, utilizadores e serviços.

**Conceitos:** control node, managed node, inventory, playbook, play, task, module, handler, become, facts, register, when, loop, role, template e vault.

**No fluxo:** Terraform cria VM → inventário identifica host → Ansible configura Docker/Nginx → container serve aplicação através do proxy.

**Recordar:**

- Inventory define alvos/grupos; play associa tarefas a hosts; role organiza automação reutilizável.
- Módulos orientados a estado ajudam idempotência; shell arbitrário não a garante.
- Handlers respondem a notify quando uma task mudou e evitam reloads desnecessários.
- Facts descrevem hosts; register guarda resultados; group_vars/host_vars separam configuração de implementação.
- Precedência depende da origem; play/task vars podem prevalecer sobre inventory vars e extra vars têm prioridade elevada. Defaults de role devem ser fáceis de substituir.
- Jinja2 gera ficheiros dinâmicos; Galaxy distribui roles/collections, como community.docker.
- Ansible Vault cifra conteúdo em repouso; a password do vault deve ficar separada e no alvo os dados podem ser texto simples.
- Check/diff ajuda revisão, mas depende do suporte de cada módulo e pode expor valores sensíveis.

**Confusões:** ping Ansible valida acesso/execução, não ICMP. Agentless não significa ausência de requisitos no alvo. Ansible Vault e HashiCorp Vault são produtos diferentes.

## Gateway API, Envoy Gateway e cert-manager

**Fonte:** dias 79-83. Gateway API separa responsabilidades de tráfego; Envoy Gateway materializa as regras; cert-manager automatiza certificados.

**Conceitos:** GatewayClass escolhe controlador; Gateway define listeners; HTTPRoute define regras/backends; BackendTrafficPolicy é extensão Envoy para políticas como afinidade por cookie. TLS (Transport Layer Security) protege HTTPS; Let's Encrypt é a autoridade de certificação exemplificada via ACME (Automatic Certificate Management Environment).

**Recordar:**

- APIs declaram intenção; controlador e infraestrutura fazem-na funcionar.
- Gateway API e Ingress coexistem; versões da Gateway API não são versões do Kubernetes.
- Service é backend estável; Gateway/HTTPRoute tratam entrada e routing de aplicação.
- cert-manager pode criar rota temporária HTTP-01 e guardar certificado/chave num Secret; DNS e alcance externo têm de funcionar.
- nip.io é DNS de laboratório baseado em IP; não converte arbitrariamente um hostname NLB num domínio válido.
- Afinidade associa pedidos ao Pod, mas não salva uma sessão em memória depois de perder esse Pod.

## Prometheus, PromQL, Node Exporter e cAdvisor

**Fonte:** dias 73-74, 76-77 e 83. Prometheus recolhe métricas por scrape, armazena séries temporais e avalia queries/regras. PromQL é a linguagem de consulta; Node Exporter expõe métricas do host e cAdvisor expõe métricas de containers.

**Conceitos:** target, scrape, time series, labels, counter, gauge, histogram, summary, rate, agregação e retenção.

**Recordar:**

- Exporter expõe; Prometheus recolhe/armazena; Grafana consulta/apresenta.
- Counter acumula eventos; gauge mede estado atual; histogram distribui observações por buckets; summary pode expor quantis calculados na origem.
- Rate sobre counters transforma crescimento em taxa; agregar depois de rate preserva tratamento de resets por série.
- Labels multiplicam séries: IDs de pedidos/utilizadores criam cardinalidade elevada.
- up=1 prova scrape bem-sucedido, não saúde funcional da aplicação.
- Persistência e retenção da base de séries temporais determinam histórico disponível.

**Kubernetes:** kube-prometheus-stack reúne monitorização; Prometheus Operator interpreta recursos como ServiceMonitor para discovery/scrape de Services. ServiceMonitor exige operador e selectors compatíveis.

## Grafana

**Fonte:** dias 74-77 e 83. Grafana reúne queries, dashboards e alertas sobre datasources, sem substituir os backends que armazenam os sinais.

**Recordar:**

- Datasource aponta para Prometheus/Loki/outro backend; dashboard combina queries e visualizações.
- Provisionamento e JSON de dashboards permitem gerir configuração como código.
- Tempo e labels incorretos podem produzir No data com recolha funcional.
- Regra e contact point configurados não provam entrega; verificar o canal real.

## Loki, Promtail e LogQL

**Fonte:** dias 75-77. Loki agrega logs e indexa principalmente labels; Promtail recolhe/envia linhas; LogQL seleciona streams, filtra mensagens e deriva métricas de logs.

**Recordar:**

- Positions acompanha leitura; perder checkpoints pode provocar releitura.
- Labels estáveis permitem seleção; conteúdo livre é filtrado nas linhas.
- Correlacionar hora, serviço e versão entre logs/métricas acelera investigação.
- Retenção e volume influenciam armazenamento e consulta.
- O relatório local do dia 75 assinala a transição de Promtail para Grafana Alloy. Alloy é aí mencionado como evolução da recolha; não integra a stack executada nesta formação.

**Comparação mencionada:** ELK (Elasticsearch, Logstash, Kibana) é alternativa orientada a pesquisa/indexação de texto; a implementação do curso usa Loki.

## OpenTelemetry e alertas

**Fonte:** dias 76-77. OpenTelemetry (OTel) normaliza instrumentação, recolha/exportação de métricas, logs e traces. Collector recebe, processa e envia dados; OpenTelemetry Protocol (OTLP) transporta-os por HTTP ou gRPC.

**Recordar:**

- OTel não é backend de armazenamento nem interface de pesquisa de traces.
- Receiver recebe; processor aplica batching/filtros; exporter envia ou expõe dados.
- Trace representa pedido distribuído; spans representam operações e parentesco.
- No laboratório, métricas seguem para Prometheus e traces/logs OTLP para debug; logs de containers usam a rota separada Promtail/Loki.
- Regras Prometheus podem ficar pending/firing; envio requer integração como Alertmanager ou alerting Grafana configurado.
- Jaeger/Tempo são backends de traces mencionados como extensão, não armazenamento integrado no exercício base.

## Aplicações, runtimes e dependências

**Fonte:** dias 15, 29-36, 48, 60, 73-83 e 87-89. São workloads e ferramentas de apoio, não alternativas aos componentes DevOps.

| Tecnologia | Problema resolvido / lugar no sistema |
| --- | --- |
| Nginx | Servidor HTTP, ficheiros estáticos e reverse proxy; liga-se aos containers no dia 72 |
| WordPress | Aplicação com dados na base de dados e ficheiros próprios |
| MySQL / MariaDB / Postgres | Bases relacionais; volumes e recuperação protegem os dados |
| Redis | Cache no exercício de três serviços; distinto da fonte persistente |
| MongoDB | Base documental, opção de aplicação no dia 36 e referência de porta |
| Python, Flask, Django, FastAPI | Linguagem/frameworks de aplicações; Python também implementa ferramentas dos agentes |
| Node.js / Express | Runtime/framework alternativos para apps e CI |
| Java / Spring Boot / Maven | Runtime, aplicação e build da AI-BankApp |
| Spring Security | Autenticação/sessões da BankApp, contexto da afinidade |
| Actuator / Micrometer | Endpoints de saúde e instrumentação JVM/HTTP para Prometheus |
| Go | Opção de aplicação compilada no exercício multi-stage |
| BusyBox / stress / PHP-Apache | Diagnóstico, pressão de recursos e teste HPA |

**Recordar:**

- Nginx recebe/encaminha tráfego; não substitui aplicação nem base de dados.
- Persistir MySQL não persiste automaticamente uploads de WordPress.
- Cache melhora acesso; disponibilidade/correção dos dados dependem da política da aplicação.
- Framework da app, runtime e ferramenta de build têm ciclos de vida distintos.

## Ollama e agentes LangChain/LangGraph

**Fonte:** dias 79-83 e 87-88. Ollama executa modelos localmente. TinyLlama serve o chatbot da BankApp; Gemma exemplifica os agentes locais. Um Large Language Model (LLM) interpreta informação; ferramentas dão acesso limitado à evidência.

LangChain fornece integrações/ferramentas; LangGraph organiza execução em fluxo/grafo. ReAct alterna Reason, Act e Observe: escolher ferramenta, executar e usar resultado para decidir o próximo passo.

**Recordar:**

- Explicador faz uma chamada ao modelo; agente consulta ferramentas e decide sequência.
- Prompt/docstring influenciam escolha, mas não autorizam operações.
- Temperatura baixa reduz variabilidade, sem garantir exatidão ou determinismo.
- Execução local pode dispensar API externa, mas exige recursos e obtenção inicial de modelos.
- Logs podem conter segredos/instruções maliciosas; são dados, não autoridade.
- Validar argumentos e limitar namespaces, tempo e saída evita shell irrestrito.

## MCP e FastMCP

**Fonte:** dia 88. Model Context Protocol (MCP) define descoberta/chamada de ferramentas. FastMCP implementa o servidor do exercício; langchain-mcp-adapters liga ferramentas descobertas ao agente.

**Recordar:**

- Servidor expõe capacidades; cliente descobre/chama; modelo escolhe uso dentro dos limites.
- stdio liga processos locais; HTTP permite outro transporte.
- MCP não fornece por si só inteligência, autorização de produção ou execução durável.
- Claude Desktop, Copilot/VS Code, Cursor e Claude Code são exemplos de clientes, sem exercícios aprofundados sobre cada um.

## Temporal, Claude e KubeHealer

**Fonte:** dia 89. Temporal preserva história de workflows e coordena activities/retries; Claude é o modelo remoto indicado; KubeHealer combina scan, diagnóstico, proposta, aprovação e correção Kubernetes.

**Problema:** retomar após falha do worker mantendo progresso, aprovação e auditoria.

**Recordar:**

- Workflow coordena; activity executa operações externas; signal transporta eventos como aprovação.
- Replay usa resultados registados; activity interrompida pode repetir-se: mutações precisam de idempotência.
- Persistência da história é essencial; reiniciar worker difere de perder a base do serviço.
- Diagnóstico/aprovação antecedem mudanças; casos fora do âmbito são escalados.
- Correções locais incidem em Deployments conhecidos; diagnóstico simulado não prova desempenho de Claude.
- Argo CD pode anular remediação direta; alterar estado desejado em Git quando esse é o contrato.

## Argo CD

**Fonte:** dias 84-86. Argo CD implementa entrega GitOps Kubernetes, comparando recursos desejados com observados e reconciliando conforme política.

**Conceitos:** Application, AppProject, sync, health, diff, prune, selfHeal, waves, hooks, App of Apps, notifications e Role-Based Access Control (RBAC).

**Recordar:**

- Application associa fonte/revisão/path ou chart a cluster/namespace.
- Synced significa alinhamento; Healthy significa avaliação de saúde.
- Sync automático aplica mudanças; manual mantém aprovação por operação.
- selfHeal corrige drift; prune pode eliminar recursos retirados da fonte.
- Waves ordenam e esperam saúde; dependências circulares bloqueiam progresso.
- App of Apps centraliza Applications filhas, sem eliminar governação individual.
- Projects delimitam fontes/destinos/tipos; RBAC delimita ações. Permissões cluster-wide exigem cuidado adicional.
- Rollback não altera Git; revert versionado evita reinstalar a versão problemática.

## Ferramentas de apoio presentes nos artefactos

- **Docker Buildx/BuildKit:** backend e interface de build usados com Actions nos dias 45/49/86; suportam cache e construção/publicação de imagens. Não são um registry nem o runtime da aplicação.
- **pytest:** executa testes Python nos artefactos CI dos dias 44/48; o resultado e exit code alimentam o gate de qualidade.
- **Graphviz/DOT:** descrevem/visualizam o grafo de dependências Terraform do dia 62; documentam relações, sem criar recursos.

## Alternativas e aprofundamentos mencionados

Não são apresentados como tecnologias praticadas em profundidade:

| Fonte | Tecnologias/conceitos | Papel |
| --- | --- | --- |
| 39 | Jenkins, GitLab CI/CD, CircleCI | Alternativas CI/CD; Actions é o percurso prático |
| 61, 68 | CloudFormation, Pulumi, Chef, Puppet, Salt | Comparar provisionamento/configuração |
| 49, 53 | GCP, Azure | Exemplos de cloud/identidade, sem percurso equivalente a AWS |
| 64 | Terraform Cloud, Consul | Alternativas de backend |
| 77 | Datadog, New Relic, CloudWatch | Comparação com observabilidade gerida |
| 76-77, 85, 89 | Slack, email, PagerDuty, webhooks | Alertas/notificações/aprovações; entrega exige integração |
| 80, 83, 90 | HashiCorp Vault, Secrets Manager, External Secrets Operator, Sealed Secrets | Gestão de segredos além do laboratório |
| 83 | Route 53, ExternalDNS, NetworkPolicy, PodDisruptionBudget | Extensões de DNS, isolamento e disponibilidade |
| 90 | Terragrunt, Istio, Linkerd, Litmus, Chaos Monkey, FinOps | Próximos estudos: IaC, service mesh, caos e custos |

Ansible Vault cifra ficheiros; HashiCorp Vault é um serviço de gestão de segredos. Partilhar o nome não lhes dá a mesma arquitetura.
