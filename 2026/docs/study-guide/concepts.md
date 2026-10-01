# Conceitos independentes das ferramentas

[Entrada do guia](README.md) · [Tecnologias](technologies.md) · [Fluxos](architecture.md)

## Sistemas, isolamento e armazenamento

**Fontes:** dias 02-15, 29-37 e 50-60. Uma máquina virtual virtualiza uma máquina com sistema operativo próprio; um container isola processos que partilham o kernel do host. A imagem empacota ficheiros e dependências, não uma garantia de comportamento igual em qualquer kernel ou arquitetura.

Persistência separa o ciclo de vida dos dados do processo. Há três perguntas: onde estão os dados, que falhas sobrevivem e quem os remove? Filesystem do container, emptyDir, volume Docker, hostPath e EBS respondem de formas diferentes. Persistência não substitui backup e um backup só tem valor operacional se houver recuperação verificada.

Alta disponibilidade reduz dependência de um único componente. Réplicas de app, control plane gerido e várias AZs ajudam, mas uma base de dados de réplica única, um volume zonal ou sessões apenas em memória continuam a ser pontos frágeis.

## Networking, routing e descoberta

**Fontes:** dias 14-15, 32-34, 53 e 82. O modelo OSI (Open Systems Interconnection) organiza diagnóstico em sete camadas; TCP/IP agrupa ligação, Internet, transporte e aplicação. IP endereça, TCP/UDP transportam, portas identificam serviços e DNS traduz nomes. HTTP descreve pedidos/respostas; HTTPS acrescenta proteção TLS.

CIDR (Classless Inter-Domain Routing) define tamanho do prefixo. `/24` representa 256 endereços; numa subnet IPv4 convencional, 254 são utilizáveis após rede/broadcast. Subnets cloud podem reservar mais. As gamas privadas IPv4 são 10.0.0.0/8, 172.16.0.0/12 e 192.168.0.0/16.

| Conceito | Responsabilidade |
| --- | --- |
| Service discovery | Encontrar o destino por nome/identidade sem fixar IPs efémeros |
| Routing | Selecionar caminho/backend segundo regras |
| Load balancing | Distribuir tráfego por backends disponíveis |
| Reverse proxy | Receber pedidos em nome da aplicação e encaminhá-los |
| Session affinity | Tentar manter pedidos do mesmo cliente no mesmo backend |
| Firewall / Security Group | Controlar tráfego autorizado |

Uma resposta ping não prova TCP acessível; TCP acessível não prova HTTP correto. Num incidente, seguir nome → IP → rota → porta → listener → aplicação → dependências.

## Versionamento, revisão e rastreabilidade

**Fontes:** dias 22-28 e 84-86. Versionar código, infraestrutura e configuração permite comparar, rever e regressar a estados conhecidos. PR e checks ligam colaboração a controlo de alterações. Documentação e portefólio dos dias 01/27/90 tornam decisões e evidência comunicáveis.

SHA de commit liga build a fonte, mas uma tag de imagem continua mutável se o registry permitir. Identidade de fonte, identidade do artefacto e revisão da configuração de deploy são três referências que precisam de ligação explícita.

## CI, delivery e deployment

**Fontes:** dias 39-49. Continuous Integration (CI) integra mudanças frequentemente e automatiza build/testes para detetar incompatibilidades cedo. Continuous Delivery mantém alterações aprovadas prontas a instalar, com uma decisão de release quando necessário. Continuous Deployment promove automaticamente alterações que passam as condições definidas.

Um pipeline liga evento → build → testes → artefacto → entrega/deploy. Build produz algo executável; testes verificam expectativas; publicação distribui; deploy muda o sistema de destino. O artifact pode ser binário, imagem ou relatório, com consumidores distintos.

**Princípios a reter:**

- Falha deve bloquear a etapa que depende da garantia falhada.
- Testes de PR e publicação da branch principal têm permissões e efeitos diferentes.
- Cache acelera execução; artifacts conservam resultados; um não substitui o outro.
- Reutilizar workflows reduz duplicação, mas exige interfaces de inputs/secrets/outputs claras.
- Environment distingue configuração e política de promoção, não só um nome escrito no log.

## DevSecOps e segredos

**Fontes:** dias 44/49, 54, 71, 80 e 85. DevSecOps integra segurança no mesmo ciclo de entrega: dependências, imagens, identidade, revisão e permissões mínimas. Scans reduzem risco conhecido sem provar ausência de falhas.

Segredo é um dado que exige confidencialidade; variável de ambiente é um mecanismo de configuração, não um cofre. Base64 é codificação reversível. Um ficheiro Vault cifrado requer proteção da chave; depois de renderizado, o valor pode ficar exposto a acesso, logs ou diffs.

IAM autoriza operações AWS; RBAC autoriza operações segundo roles, por exemplo em Kubernetes ou Argo CD. Security Groups tratam rede. Namespace, branch ou label não são isolamentos de segurança completos por si só.

## Infrastructure as Code antes de Terraform

**Fontes:** dias 61-67. Infrastructure as Code (IaC) descreve infraestrutura em ficheiros versionados para criar, rever e reproduzir recursos. O modo declarativo descreve intenção; um motor calcula operações para chegar a ela.

Terraform compara configuração, state e recursos consultados. State não substitui código: associa endereços lógicos a objetos reais. Drift é divergência provocada fora do contrato de gestão. Reconciliar pode restaurar a intenção ou aceitar uma mudança através de revisão do código.

Um plan é previsão no contexto observado; não garante que apply posterior terá o mesmo resultado. Dependências ordenam recursos. create_before_destroy ajuda substituição, mas exige capacidade e não transfere dados/sessões automaticamente.

Backend remoto, locking e versionamento resolvem colaboração, concorrência e recuperação do estado. Workspaces separam estados; módulos reutilizam definições. Isolamento forte de produção pode exigir também identidades, políticas, redes e contas próprias.

## Configuration Management antes de Ansible

**Fontes:** dias 68-72. Gestão de configuração mantém pacotes, ficheiros, utilizadores e serviços num estado conhecido. Pode ser executada sobre VMs provisionadas por Terraform. Idempotência significa que repetir a operação converge para o mesmo resultado pretendido sem mudanças desnecessárias.

Provisionar cria recursos; configurar prepara o seu funcionamento. A separação não é absoluta: Terraform pode gerir recursos Kubernetes/Helm e Ansible pode provisionar. O mais importante é definir ownership, ciclo de vida e ferramenta responsável por cada objeto.

Idempotência não significa ausência de falhas ou de efeitos laterais. Um módulo de estado, um handler condicionado e uma tarefa shell que reinicia sempre têm comportamentos distintos.

## Orquestração e reconciliação

**Fontes:** dias 50-60. Orquestração coordena colocação, execução, rede e substituição de workloads. Reconciliação compara continuamente intenção e observação. O scheduler escolhe nó; controller cria/atualiza objetos; runtime executa containers.

Labels/seletores ligam recursos. Deployment mantém réplicas e estratégias de atualização; Service dá endpoint estável; StatefulSet associa identidade/volume a réplicas; StorageClass traduz claims em armazenamento. O estado Running refere execução, não necessariamente prontidão.

Rollout substitui versões segundo estratégia. Rollback restaura configuração anterior, não dados anteriores. Init containers preparam dependências antes dos containers principais; lifecycle hooks acompanham transições de containers. Não confundir esses mecanismos com hooks Helm ou sync hooks Argo CD.

## Capacidade, saúde e scaling

**Fontes:** dias 34, 52, 57-58 e 82. Scaling horizontal aumenta réplicas; vertical aumenta recursos por instância. Requests orientam colocação; limits delimitam consumo. Capacidade allocatable é o que sobra para workloads após reservas do sistema.

HPA aumenta réplicas segundo métricas, enquanto o aumento de nodes exige outro mecanismo. Aumentar réplicas não resolve dependências saturadas nem estado local inconsistente. Percentagem CPU HPA é relativa a requests, não necessariamente à capacidade total do nó.

| Probe | Pergunta | Efeito típico de falha |
| --- | --- | --- |
| Startup | A inicialização terminou? | Pode reiniciar após exceder o orçamento; adia outras probes |
| Readiness | Pode receber tráfego agora? | Retira o Pod dos backends prontos, sem reiniciar |
| Liveness | Está bloqueado e precisa de restart? | Reinicia o container após o limiar |

Uma probe mal dimensionada pode provocar a falha que tenta detetar. Rolling update depende de readiness, estratégia, capacidade e comportamento da aplicação para preservar serviço.

## GitOps e ownership

**Fontes:** dias 84-86. GitOps combina estado declarativo, versionado/imutável, obtido automaticamente e continuamente reconciliado. CI produz artefactos e atualiza a versão desejada; um controlador faz pull dessa configuração e aplica-a.

Automated sync define aplicação automática de alterações; selfHeal corrige drift; prune remove objetos retirados da fonte. São políticas relacionadas, mas não sinónimos.

Argo CD e HPA não devem disputar replicas; Helm CLI e Argo CD não devem instalar independentemente os mesmos recursos. O contrato de ownership precisa de explicar campos geridos por outros controladores. Patches diretos de um agente podem ser revertidos pelo GitOps.

Waves ordenam recursos segundo saúde. PVC WaitForFirstConsumer precisa de consumidor para avançar; colocá-los em waves incompatíveis cria espera circular. Um rollback operacional sem mudança de Git pode ser temporário; revert é uma mudança auditável do estado desejado.

## Observabilidade, monitoring e alerting

**Fontes:** dias 73-77 e 83. Monitoring acompanha condições conhecidas. Observabilidade permite investigar estado interno a partir de sinais externos e relações entre eles, incluindo causas que não foram previstas num dashboard.

| Sinal | O que representa | Pergunta útil | Percurso estudado |
| --- | --- | --- | --- |
| Métricas | Medidas agregáveis ao longo do tempo | Quanto, com que taxa, desde quando? | Exporters/OTel → Prometheus → Grafana |
| Logs | Eventos com contexto textual/estruturado | Que erro ocorreu neste momento? | Containers → Promtail → Loki → Grafana |
| Traces | Operações e relações de um pedido | Em que serviço/operação se gastou tempo? | OTLP → Collector → debug no laboratório |

Histogramas e counters permitem taxas/distribuições; logs dão contexto; traces ligam operações. Correlacionar exige tempo e identificadores coerentes. Muitos labels distintos aumentam cardinalidade e custo.

Alertas precisam de condição, duração, severidade, destinatário e ação esperada. Pending evita disparar em picos breves; firing é estado de regra, não confirmação de mensagem entregue. Sem routing/canal real, um alerta pode existir apenas na UI.

## Troubleshooting, runbooks e recuperação

**Fontes:** dias 04-05, 19-20, 51-58 e 87-89. Um runbook torna investigação repetível: sintomas → evidência → hipótese → verificação → ação limitada → validação do resultado.

Distinguir causas de sintomas: CrashLoopBackOff descreve restarts repetidos; pode resultar de comando que termina, configuração errada ou falha da aplicação. ImagePullBackOff aponta à obtenção da imagem; Pending pode ser capacidade, scheduling ou armazenamento. OOMKilled exige evidência do motivo de terminação.

Limpeza é parte do ciclo de vida: conhecer o âmbito e o efeito sobre dados, remover consumidores antes de infraestrutura e verificar recursos remanescentes. A tarefa deste guia não executa essas operações.

## Agentes, MCP, AIOps e execução durável

**Fontes:** dias 87-89. Um agente combina modelo e ferramentas; MCP normaliza a interface dessas ferramentas; AIOps aplica análise/automação assistida por IA à operação. Temporal acrescenta execução durável, não inteligência.

Usar regras fixas para causas/ações conhecidas; diagnóstico por modelo pode ajudar quando há várias hipóteses. A resposta precisa de evidência, limites e validação. Aprovação humana, âmbito, auditoria, reversibilidade, limites de retries e escalada são os seis controlos do dia 89.

Replay reconstitui decisões a partir da história; activities externas podem ser repetidas quando interrompidas. Operações idempotentes, chaves de deduplicação e confirmação de resultado evitam efeitos duplicados. Temperatura, system prompt e docstrings melhoram comportamento, mas não substituem estes controlos.
