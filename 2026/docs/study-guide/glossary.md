# Glossário de consulta rápida

[Entrada do guia](README.md) · [Revisão rápida](cheat-sheet.md)

Os termos pertencem ao núcleo e às extensões relevantes identificadas em 2026. Os detalhes e fontes por dia estão em [tecnologias](technologies.md) e no [índice](day-index.md).

## Sistemas, redes e automação

| Termo | Significado |
| --- | --- |
| Kernel | Núcleo que gere processos, memória, dispositivos e rede |
| User space | Espaço onde correm aplicações e ferramentas |
| PID | Process Identifier, identificador de processo |
| Serviço / unit | Processo operacional e unidade de gestão systemd |
| journald | Recolha de eventos do sistema; journalctl consulta-os |
| Ownership | Utilizador e grupo associados a ficheiro/diretório |
| LVM | Logical Volume Manager, gestão de volumes lógicos |
| PV / VG / LV em LVM | Physical Volume / Volume Group / Logical Volume |
| Filesystem | Organização de ficheiros num dispositivo/volume |
| Mount | Associação de filesystem a caminho acessível |
| VM | Virtual Machine, máquina virtual com sistema próprio |
| SSH | Secure Shell, administração remota autenticada e cifrada |
| OSI | Open Systems Interconnection, modelo de sete camadas |
| TCP/IP | Transmission Control Protocol / Internet Protocol, família de protocolos e modelo de rede |
| UDP | User Datagram Protocol, transporte de datagramas |
| ICMP | Internet Control Message Protocol, controlo/diagnóstico de rede |
| DNS | Domain Name System, resolução de nomes e outros registos |
| TTL | Time To Live, validade temporal de dados como registos DNS |
| CIDR | Classless Inter-Domain Routing, prefixo de rede/tamanho do bloco |
| Porta | Identificador de endpoint de transporte para um serviço |
| HTTP / HTTPS | Hypertext Transfer Protocol / HTTP protegido por TLS |
| TLS | Transport Layer Security, proteção da comunicação |
| Reverse proxy | Intermediário que recebe pedidos em nome dos backends |
| Load balancing | Distribuição de tráfego por backends |
| Service discovery | Descoberta de destinos por identidade/nome |
| Afinidade | Política que associa pedidos de cliente ao mesmo backend |
| Shebang | Linha que indica interpretador ao executar um script |
| Quoting | Preservação/expansão controlada de argumentos shell |
| Pipe | Ligação de stdout de um processo a stdin de outro |
| Exit code | Estado numérico de terminação do comando |
| Trap | Tratamento shell de sinais/eventos como saída |
| Cron | Agendador de tarefas por expressões temporais |
| Runbook | Procedimento repetível de investigação/operação |
| Retenção | Política de conservação e eliminação de dados antigos |
| Backup | Cópia destinada à recuperação; requer teste de restauro |

## Git, containers e entrega

| Termo | Significado |
| --- | --- |
| Working tree | Ficheiros do checkout em trabalho |
| Staging / index | Seleção de conteúdo para o próximo commit |
| Commit / SHA | Snapshot versionado / identificador de commit |
| HEAD | Referência do checkout atual |
| Branch | Referência móvel numa linha de desenvolvimento |
| Remote | Repositório de troca de referências/commits |
| Fork / clone | Repositório associado na plataforma / cópia local |
| PR | Pull Request, proposta de alteração para revisão |
| Merge / rebase | Integração de históricos / reaplicação de commits |
| Revert / reset | Inversão por commit / reposicionamento de referência e eventualmente ficheiros |
| Stash | Guarda temporária de trabalho não consolidado |
| Cherry-pick | Aplicação da alteração de um commit selecionado |
| Reflog | Registo local de movimentos de referências |
| Imagem | Artefacto de ficheiros e metadados que serve de base a containers |
| Container | Instância de processos isolados baseada numa imagem |
| Dockerfile | Instruções para construir uma imagem |
| Build context | Ficheiros disponíveis ao processo de build |
| Layer | Camada reutilizável da imagem |
| Multi-stage | Separação de fases de build e runtime numa imagem |
| Tag / digest | Referência nomeada potencialmente mutável / identificador do conteúdo |
| Registry | Serviço de armazenamento e distribuição de imagens |
| Volume / bind mount | Armazenamento gerido / montagem de caminho do host |
| CI | Continuous Integration, integração e verificação frequentes |
| Continuous Delivery | Alterações verificadas prontas para release |
| Continuous Deployment | Instalação automática após condições de sucesso |
| Workflow / job / step | Fluxo de automação / unidade executada / operação dessa unidade |
| Trigger | Evento que inicia automação |
| Runner | Ambiente/máquina que executa um job |
| Matrix | Expansão de combinações de parâmetros de execução |
| Artifact | Resultado produzido e conservado para utilização |
| Cache | Dados reutilizados para acelerar execução |
| Environment | Destino/configuração com políticas de promoção |
| DevSecOps | Segurança integrada no desenvolvimento, entrega e operação |
| CVE | Common Vulnerabilities and Exposures, identificador de vulnerabilidade conhecida |
| OIDC | OpenID Connect, identidade federada usada para credenciais temporárias |
| SARIF | Static Analysis Results Interchange Format, formato de resultados de análise |

## Infraestrutura, configuração e Kubernetes

| Termo | Significado |
| --- | --- |
| IaC | Infrastructure as Code, infraestrutura declarada em ficheiros versionados |
| HCL | HashiCorp Configuration Language, linguagem Terraform |
| Provider | Integração Terraform com APIs de recursos |
| Resource / data source | Objeto gerido / informação consultada |
| State | Associação Terraform entre endereços lógicos e objetos reais |
| Backend / locking | Armazenamento de state / controlo de escrita concorrente |
| Drift | Diferença entre intenção gerida e estado observado |
| Import | Associação de recurso existente à gestão Terraform |
| Module / workspace | Definição reutilizável / instância separada de estado |
| Idempotência | Repetição que converge para o estado desejado sem alterações desnecessárias |
| Inventory | Hosts e grupos alvo de Ansible |
| Playbook / play / task | Documento Ansible / tarefas para hosts / operação individual |
| Handler | Task acionada por notificação de mudança |
| Facts / register | Informação dos hosts / resultado de tarefa guardado |
| Role / template / Vault Ansible | Organização reutilizável / geração de ficheiro / cifragem de conteúdo |
| AWS | Amazon Web Services |
| EC2 / AMI | Elastic Compute Cloud / Amazon Machine Image |
| VPC | Virtual Private Cloud, rede lógica de recursos AWS |
| Subnet / AZ | Segmento de endereços / Availability Zone |
| IAM | Identity and Access Management, identidades e políticas AWS |
| NAT | Network Address Translation, tradução de endereços, usada para saída privada |
| S3 / EBS | Simple Storage Service, objetos / Elastic Block Store, volumes de blocos |
| NLB | Network Load Balancer, balanceador AWS de transporte |
| EKS | Elastic Kubernetes Service, Kubernetes gerido AWS |
| Control plane | Componentes que armazenam e coordenam estado do cluster |
| Node | Máquina que executa workloads Kubernetes |
| Pod | Unidade de execução de containers com rede/volumes partilhados |
| Manifest | Declaração de recurso para a API Kubernetes |
| Kubeconfig / context | Configuração de acesso / seleção de cluster, identidade e namespace |
| Label / selector | Metadado de organização / critério de seleção de recursos |
| Namespace | Âmbito lógico de recursos namespaced |
| Deployment / ReplicaSet | Gestão de rollout / manutenção de réplicas de Pods |
| StatefulSet | Gestão de Pods com identidade estável e volumes por réplica |
| Service / endpoint | Abstração de acesso / destino concreto do tráfego |
| Headless Service | Descoberta de endpoints sem ClusterIP virtual |
| ConfigMap / Secret | Configuração não sensível / dados sensíveis sujeitos a controlos |
| PV / PVC Kubernetes | PersistentVolume / PersistentVolumeClaim, oferta e pedido de armazenamento |
| StorageClass | Política/implementação de provisionamento de volumes |
| CSI / CNI | Container Storage Interface / Container Network Interface |
| RWO | ReadWriteOnce, montagem de leitura/escrita por um nó |
| Reclaim policy | Política Retain/Delete após libertação da claim |
| Requests / limits | Recursos pedidos para scheduling / restrições de consumo |
| QoS | Quality of Service, classificação Kubernetes de recursos dos Pods |
| HPA | Horizontal Pod Autoscaler, ajusta réplicas por métricas |
| Probe | Teste de startup, readiness ou liveness |
| OOMKilled | Terminação por falta/excesso de memória segundo evidência do runtime |
| CrashLoopBackOff | Espera crescente entre restarts repetidos |
| Init container | Preparação executada antes dos containers principais |
| RollingUpdate / Recreate | Substituição gradual / terminar versão antiga antes de iniciar nova |
| Chart / values / release | Pacote Helm / parâmetros / instalação |
| GatewayClass / Gateway / HTTPRoute | Controlador de tráfego / listeners / regras para backends |
| CRD | CustomResourceDefinition, extensão de tipos da API Kubernetes |
| RBAC | Role-Based Access Control, autorização por roles |

## GitOps, telemetria e IA

| Termo | Significado |
| --- | --- |
| GitOps | Entrega por estado declarativo versionado e reconciliação contínua |
| Application / AppProject | Fonte e destino Argo CD / fronteiras de gestão |
| Sync / health | Alinhamento do estado / avaliação de saúde |
| Prune / selfHeal | Eliminar objetos retirados da fonte / corrigir drift automaticamente |
| Sync wave | Grupo ordenado de recursos numa sincronização |
| App of Apps | Application pai que gere Applications filhas |
| Métrica / série temporal | Medida numérica / amostras identificadas por nome e labels |
| Scrape / exporter | Recolha periódica / exposição de métricas |
| Counter / gauge | Acumulação de eventos / medida do estado atual |
| Histogram / summary | Distribuição por buckets / sumário com quantis calculados na origem |
| PromQL / LogQL | Linguagens de consulta Prometheus / Loki |
| Cardinalidade | Número de séries/streams decorrente das combinações de labels |
| TSDB | Time-Series Database, base de séries temporais |
| Trace / span | Percurso de pedido / operação e relação dentro desse percurso |
| OTel / OTLP | OpenTelemetry / OpenTelemetry Protocol |
| Receiver / processor / exporter OTel | Receção / transformação / saída de telemetria |
| ServiceMonitor | Recurso Prometheus Operator para descoberta/scrape de Services |
| Pending / firing | Condição de alerta à espera de duração / condição ativa |
| LLM | Large Language Model, modelo de linguagem |
| ReAct | Ciclo de raciocínio, ação e observação com ferramentas |
| Tool | Capacidade executável com argumentos e resultados definidos |
| MCP | Model Context Protocol, descoberta/chamada de ferramentas |
| AIOps | Operações assistidas por análise e automação de IA |
| Guardrail | Limite/controlos sobre ações do agente |
| Workflow / activity / signal Temporal | Coordenação durável / operação externa / evento recebido |
| Replay | Reconstituição do workflow com história/resultados registados |
| Escalada | Transferência para intervenção humana quando não há resolução autorizada |
