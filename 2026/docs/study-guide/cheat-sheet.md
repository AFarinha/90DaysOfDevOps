# Revisão rápida e comparações

[Entrada do guia](README.md) · [Tecnologias](technologies.md) · [Índice](day-index.md)

## Comparações que evitam erros

| A | B | Diferença a reter / fontes |
| --- | --- | --- |
| VM | Container | VM tem SO/kernel próprio; container isola processos sobre kernel partilhado. Dias 29/50. |
| Imagem | Container | Artefacto de base / instância em execução com estado próprio. Dias 29-30. |
| Docker | Kubernetes | Constrói/executa containers / orquestra workloads num cluster. Dias 29-37/50. |
| Volume Docker | Bind mount | Armazenamento gerido por Docker / caminho explícito do host. Dia 32. |
| Compose | Kubernetes | Coordenação de serviços num host / reconciliação e scheduling de cluster. Dias 33-34/50. |
| CMD | ENTRYPOINT | Comando/argumentos por omissão / executável principal; interagem conforme forma e overrides. Dia 31. |
| Git | GitHub | Motor distribuído de versionamento / plataforma de alojamento e colaboração. Dias 22-26. |
| Fetch | Pull | Obtém referências / obtém e integra alterações. Dia 23. |
| Merge | Rebase | Integra históricos / reaplica commits sobre outra base. Dia 24. |
| Reset | Revert | Reposiciona referências e pode descartar alterações / novo commit de inversão. Dia 25. |
| CI | CD | Verificação frequente de integração / preparação ou instalação da versão. Dia 39. |
| Delivery | Deployment contínuo | Pronto para decisão de release / promoção automática após checks. Dia 39. |
| Artifact | Cache | Resultado para consumir/guardar / otimização reutilizável de execução. Dia 44. |
| Hosted runner | Self-hosted | Plataforma gere ambiente / equipa gere máquina, segurança e resíduos. Dia 42. |
| Reusable workflow | Composite action | Reutiliza jobs / agrupa steps de um job. Dia 46. |
| workflow_call | workflow_run | Chamada explícita / evento de outra execução. Dia 47. |
| Terraform | Ansible | Provisionamento e state / configuração por tarefas e inventário; fronteira flexível. Dias 61/68. |
| Module | Workspace Terraform | Reutiliza definição / separa estado entre instâncias de configuração. Dias 65/67. |
| Variable | Data source Terraform | Entrada definida / informação consultada externamente. Dia 63. |
| Helm | Manifests | Gera/pacota recursos parametrizados / definições explícitas dos recursos. Dias 59/78-80. |
| Helm | Kustomize | Templates/values/packages / overlays e patches sobre manifests. Dia 80. |
| Chart | Release | Pacote reutilizável / instalação desse pacote. Dias 59/78. |
| Kubernetes | EKS | Orquestrador / serviço AWS que gere o control plane e integra serviços. Dias 50/81. |
| Pod | Deployment | Unidade de execução / controlador de réplicas e atualização. Dias 51-52. |
| Deployment | StatefulSet | Réplicas intercambiáveis / identidades e volumes por réplica. Dia 56. |
| Deployment | Service | Mantém workloads / fornece descoberta e encaminhamento. Dias 52-53. |
| Service | Ingress ou Gateway | Endpoint de backends / regras de entrada e routing da aplicação. Dias 53/82. |
| Ingress | Gateway API | Recurso de entrada tradicional / APIs com responsabilidades separadas e routing extensível. Dia 82. |
| ConfigMap | Secret | Configuração não sensível / objeto para dados sensíveis; base64 não cifra. Dia 54. |
| PV | PVC | Recurso de armazenamento / pedido namespaced que o consome. Dia 55. |
| Requests | Limits | Base de scheduling/referência / restrição de consumo. Dia 57. |
| Readiness | Liveness | Pode receber tráfego / deve reiniciar. Dia 57. |
| Horizontal | Vertical scaling | Mais réplicas / mais recursos por instância. Dias 52/58/82. |
| HPA | Capacidade de nodes | Aumenta Pods / capacidade para os agendar precisa de gestão separada. Dias 58/81-82. |
| Metrics Server | Prometheus | Métricas recentes para recursos/HPA / histórico, consultas e alertas. Dias 58/73. |
| Node Exporter | cAdvisor | Métricas do host / dos containers. Dia 74. |
| Prometheus | Grafana | Recolha/armazenamento de métricas / consulta e apresentação. Dias 73-74. |
| Métricas | Logs | Valores agregáveis / eventos com contexto. Dias 73-75. |
| Logs | Traces | Eventos de componentes / relações de operações de um pedido. Dias 75-76. |
| OTel Collector | Trace backend | Recebe/processa/exporta / armazena e permite pesquisa. Dia 76. |
| CI/CD | GitOps | Práticas de verificação/entrega / modelo declarativo de entrega/reconciliação; complementares. Dia 84. |
| Synced | Healthy | Alinhado com Git / avaliação de saúde. Dia 84. |
| Argo rollback | Git revert | Muda cluster para revisão anterior / muda intenção versionada. Dia 85. |
| IAM | RBAC | Permissões AWS / autorização por roles numa API/plataforma. Dias 81/85. |
| Ansible Vault | HashiCorp Vault | Cifra ficheiros / serviço de gestão de segredos. Dias 71/80. |
| Modelo | Agente | Interpreta/gera resposta / usa ferramentas num ciclo de execução. Dia 87. |
| MCP | Temporal | Interface de ferramentas / execução durável de workflows. Dias 88-89. |

Jenkins e GitLab CI/CD são mencionados como alternativas no dia 39; não há base nesta edição para uma comparação operacional aprofundada com Actions. O conceito comum é pipeline; diferem a plataforma e o modelo de gestão.

## O que devo conseguir explicar depois dos 90 dias

Usa cada linha como pergunta oral: explica o conceito, a responsabilidade, uma relação e uma falha que ele não resolve sozinho.

### Sistemas e redes

- Kernel/user space, processo, serviço systemd e logs journald.
- Utilizador, grupo, ownership e permissões de ficheiros/diretórios.
- PV/VG/LV LVM, filesystem e montagem.
- DNS, registos, IP privado/público, CIDR, rotas e portas.
- Porque ping, teste TCP e HTTP respondem a perguntas distintas.
- Papel de SSH, Nginx e Security Groups no primeiro deploy cloud.

### Automação e Git

- Shebang, argumentos, quoting, funções, exit codes e pipes.
- Tratamento de erro, traps, cron, rotação de logs e backup.
- Working tree, staging, commit, HEAD e remotes.
- Branch, PR, merge/rebase, stash/cherry-pick e reset/revert.
- Porque segredos já versionados não desaparecem com gitignore.

### Containers

- Imagem/container, build context, Dockerfile, layers e cache.
- Multi-stage, non-root, tag/digest e registry.
- Volume/bind mount, rede por nome e publicação de portas.
- Compose, configuração externa, healthcheck, dependências e restart.
- Porque persistir base de dados não persiste todos os ficheiros da app.

### CI/CD e segurança

- CI, delivery, deployment, build, testes, artefactos e promoção.
- Trigger/job/step/runner, needs, matrix e condição de sucesso.
- Outputs/artifacts/cache e reusable workflow/composite action.
- Hosted/self-hosted, ambientes/aprovações, secrets e permissões.
- Trivy, dependency review, secret scanning e OIDC como extensão.
- Porque publicar uma imagem difere de instalar essa imagem.

### Kubernetes, Helm e EKS

- Control plane/node, API/etcd/scheduler/controllers/runtime.
- Pod, Deployment, StatefulSet, Service e namespace.
- ConfigMap/Secret, PV/PVC/StorageClass, acesso e reclaim policy.
- Requests/limits, probes, HPA e capacidade allocatable.
- Chart/release/revision, values, templates, hooks e rollback.
- EKS, node group, VPC CNI, CSI, IAM e volumes zonais.
- GatewayClass/Gateway/HTTPRoute, Envoy, TLS e cert-manager.
- Limites de afinidade, alta disponibilidade e rollout.

### Infraestrutura e configuração

- IaC, provider/resource/data source e dependências Terraform.
- State/backend/locking, drift/import e plan/apply.
- Variable/local/output, módulo e workspace.
- Inventory/playbook/task/module/handler/role Ansible.
- Idempotência, facts/register, Jinja2 e Ansible Vault.
- Diferença flexível entre criar infraestrutura e configurar sistemas.

### Observabilidade

- Monitoring/observabilidade, métricas/logs/traces e correlação.
- Counter/gauge/histogram, labels, cardinalidade, rate e agregação.
- Prometheus/exporters/Grafana e Loki/Promtail/LogQL.
- OTel receiver/processor/exporter e OTLP.
- Regra pending/firing, destinatário e validação de entrega.
- Porque exporter de debug não é armazenamento de traces.

### GitOps e IA operacional

- Estado desejado em Git, pull e reconciliação contínua.
- Application/AppProject, sync/health, prune/selfHeal e waves.
- Ownership de replicas com HPA; revert e rollback.
- Ollama/modelo, ReAct, tools, MCP e cliente/servidor.
- Temporal workflow/activity/signal, replay e retries idempotentes.
- AIOps, aprovação, âmbito, auditoria, limites e escalada.
- Distinguir evidência real, hipótese do modelo e teste com diagnóstico simulado.

## Ligações que vale a pena memorizar

```text
Linux → executa processos e fornece recursos
systemd → gere serviços; journald → regista eventos
DNS → resolve nomes; portas → identificam serviços
Git → versiona intenção; GitHub → colaboração e eventos
Bash/cron → automatizam rotinas e agendamento
Docker → constrói imagens e executa containers
Docker Hub → distribui imagens; Compose → coordena serviços num host
Actions → build/testes/verificações/publicação
Terraform → provisiona recursos e mantém associação em state
Ansible → configura hosts; Jinja2 → gera ficheiros; Vault → cifra conteúdo
Kubernetes → reconcilia workloads; EKS → control plane gerido pela AWS
Helm → gera e empacota manifests
Gateway/Envoy → recebem e encaminham tráfego
cert-manager → automatiza certificados; EBS CSI → liga claims a volumes
Argo CD → reconcilia estado de Git com Kubernetes
Exporters → expõem métricas; Prometheus → recolhe e consulta
Grafana → apresenta dados e avalia alertas
Promtail → envia logs; Loki → guarda e consulta logs
OTel → instrumenta/transporta; Collector → recebe/processa/exporta
Ollama → executa modelos; agente → usa ferramentas
MCP → normaliza ferramentas; Temporal → preserva execução
KubeHealer → diagnóstico/proposta/aprovação/remediação limitada
```

## Cinco perguntas finais de arquitetura

1. Qual é a identidade do código, da imagem e da configuração atualmente executada?
2. Quem gere este recurso/campo e quem pode alterá-lo?
3. Onde estão os dados e o que acontece se o processo, nó ou zona falhar?
4. Que evidência prova disponibilidade e que alerta chega à pessoa responsável?
5. Como corrigir, verificar e recuperar sem criar drift ou perder dados?
