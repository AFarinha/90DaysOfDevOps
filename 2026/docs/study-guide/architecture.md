# Arquitetura e fluxos completos

[Entrada do guia](README.md) · [Conceitos](concepts.md) · [Índice](day-index.md)

As setas indicam produção, consulta, controlo ou tráfego conforme a legenda. Os desenhos combinam responsabilidades ensinadas em dias diferentes; não afirmam que todos os componentes foram executados juntos na AWS.

## 1. Do código até produção por GitOps

**Fontes:** dias 45, 49, 80 e 84-86. O registry transporta imagens; Git transporta a referência da versão desejada; Argo CD reconcilia a configuração. A pipeline de referência do dia 86 usa manifests; Helm é a integração alternativa desenvolvida nos dias 79-80.

```mermaid
flowchart LR
    Dev[Alteração de código] --> PR[GitHub: PR e revisão]
    PR --> Teste[Actions: build e testes]
    Teste --> Integracao[Integração na branch de entrega]
    Integracao --> Build[Build Docker e checks de segurança]
    Build --> Hub[Docker Hub: imagem versionada]
    Build --> Config[Commit: imagem no manifest ou values]
    Config --> Argo[Argo CD: leitura e comparação]
    Helm[Chart Helm, quando usado] --> Argo
    Argo --> Deploy[Deployment e ReplicaSet]
    Hub --> Runtime[Runtime obtém imagem]
    Deploy --> Pod[Pod no Kubernetes ou EKS]
    Runtime --> Pod
    Pod --> Saude[Readiness e validação funcional]
```

**O que verificar em cada passagem:** testes bloqueantes; scan da imagem correta; publicação no registry pretendido; referência consistente no Git; sync e health separados; resposta funcional e dados corretos. Tags não são garantias de imutabilidade. O job demonstrativo do dia 48 e testes tolerados no exemplo do dia 86 são limites explicitados nas fontes locais.

## 2. Provisionamento e configuração de uma VM

**Fontes:** dias 61-72. Terraform gere recursos; Ansible prepara o sistema; Nginx recebe o tráfego externo e faz reverse proxy para a porta da app.

```mermaid
flowchart LR
    HCL[Definição HCL em Git] --> TF[Terraform: plan e apply]
    TF --> AWS[AWS: VPC, subnet, SG e EC2]
    TF --> State[State: backend e locking]
    AWS --> Hosts[Hosts no inventário]
    Hosts --> Ansible[Ansible por SSH]
    Roles[Roles e templates Jinja2] --> Ansible
    Vault[Ansible Vault: segredos cifrados] --> Ansible
    Ansible --> Docker[Docker e container da app]
    Ansible --> Proxy[Nginx configurado]
    User[Cliente HTTP] --> Proxy
    Proxy --> Docker
```

A VM tem de existir e ser acessível antes de Ansible a configurar. Inventário, credenciais SSH e permissões de become fazem parte dessa ligação. State sensível e chave do Vault têm de ter acesso controlado. Este fluxo é uma opção completa de entrega; não precisa de EKS ou Argo CD para funcionar.

## 3. Arquitetura consolidada da AI-BankApp

**Fontes:** dias 79-86, com observabilidade dos dias 73-77/83. Plano de controlo é distinto do percurso do tráfego. O control plane EKS é gerido pela AWS; os workloads executam nos worker nodes ligados à VPC do utilizador.

```mermaid
flowchart TB
    TF[Terraform] --> Rede[VPC: subnets, rotas e Security Groups]
    TF --> CP[EKS control plane gerido]
    Rede --> Nodes[Managed node group EC2]
    CP --> Nodes
    CI[GitHub Actions] --> Hub[Docker Hub]
    CI --> Git[Git: estado desejado]
    Git --> Argo[Argo CD]
    Chart[Helm: render opcional] --> Argo
    Argo --> App[Pods Spring Boot]
    Hub --> App
    Nodes --> App
    User[Utilizador] --> DNS[DNS]
    DNS --> LB[Load balancer AWS configurado]
    LB --> Gateway[Envoy Gateway: listeners HTTP e HTTPS]
    Gateway --> Route[HTTPRoute]
    Route --> Service[Service BankApp]
    Service --> App
    Cert[cert-manager e Let's Encrypt] --> TLS[Secret TLS]
    TLS --> Gateway
    App --> DB[MySQL]
    App --> AI[Ollama e TinyLlama]
    DB --> Disco[EBS através de PVC e CSI]
    AI --> Disco
    App --> Metrics[Actuator e Micrometer]
    Metrics --> Prom[Prometheus via ServiceMonitor]
    Prom --> Grafana[Grafana]
    Diagnostico[Equipa ou agente com limites] --> Grafana
    Diagnostico --> Git
```

A seta Nodes → App significa local de execução; não pedido HTTP. O percurso de tráfego não atravessa Terraform nem Argo CD. As duas workloads persistentes usam volumes distintos; o nó Disco agrega apenas o mecanismo.

**Responsabilidades que faltam num desenho simples:** políticas IAM/RBAC, secrets, DNS/TLS válidos, backups, capacidade e proteção de sessões. Afinidade não elimina perda de sessão após falha do Pod. Instalar monitorização exige capacidade adicional.

## 4. Rede Kubernetes e armazenamento EBS

**Fonte:** dias 53-56 e 82. O controlador implementa routing; o driver CSI liga claims a volumes reais. Um LoadBalancer Service depende da implementação cloud; Gateway não garante por si só um NLB.

```mermaid
flowchart LR
    Classe[GatewayClass] --> Controlador[Envoy Gateway controller]
    Controlador --> Gateway[Gateway e listeners]
    Gateway --> Route[HTTPRoute: regra e backend]
    Route --> Service[Service e endpoints prontos]
    Service --> Pod[Pod consumidor]
    SC[StorageClass gp3 e política] --> CSI[EBS CSI driver]
    Claim[PVC: pedido de capacidade] --> CSI
    Pod --> Claim
    CSI --> PV[PV associado à claim]
    PV --> EBS[Volume EBS na AZ do consumidor]
```

WaitForFirstConsumer adia provisionamento até conhecer colocação do consumidor. Não colocar essa claim numa sync wave que só avança depois de Bound se o consumidor está numa wave posterior. Retain/Delete define o destino do armazenamento quando libertado; não é política de backup.

## 5. Observabilidade: três percursos distintos

**Fontes:** dias 73-77. As setas representam movimento/consulta dos dados; Prometheus faz pull dos endpoints, enquanto OTLP e o envio de logs são push.

```mermaid
flowchart LR
    Host[Host] --> NE[Node Exporter]
    Containers[Containers] --> CA[cAdvisor]
    NE --> Prom[Prometheus recolhe por scrape]
    CA --> Prom
    App[Aplicação instrumentada] --> OTel[OTel Collector: receiver e processor]
    OTel --> Expo[Exporter com endpoint de métricas]
    Expo --> Prom
    Containers --> Tail[Promtail lê logs]
    Tail --> Loki[Loki]
    OTel --> Debug[Exporter debug: traces e logs OTLP]
    Prom --> Grafana[Grafana consulta métricas e logs]
    Loki --> Grafana
    Prom --> Regras[Regras e estado de alertas]
    Grafana --> Contactos[Alerting e contact points]
    Regras -.-> AM[Alertmanager: extensão para notificações]
    OTel -.-> Traces[Tempo ou Jaeger: extensão de armazenamento]
```

As setas tracejadas são extensões propostas, não serviços integrados no laboratório base. A stack completa inclui Notes App, Prometheus, Node Exporter, cAdvisor, Grafana, Loki, Promtail e Collector. Os snapshots locais podem ter mais targets por incluírem a app como endpoint direto.

## 6. Diagnóstico, MCP e remediação durável

**Fontes:** dias 87-89. MCP uniformiza ferramentas; Temporal preserva progresso; o modelo interpreta resultados. O controlo de execução permanece fora das decisões livres do modelo.

```mermaid
flowchart LR
    Q[Pergunta ou problema observado] --> Agent[Agente: modelo e ciclo ReAct]
    Agent --> Client[Cliente MCP]
    Client --> Server[Servidor FastMCP]
    Server --> Tools[Ferramentas limitadas: docker, kubectl, gh]
    Tools --> Evidence[Logs, eventos e estado]
    Evidence --> Agent
    Agent --> Proposta[Diagnóstico e proposta]
    Proposta --> Humano[Aprovação ou rejeição]
    Humano --> Workflow[Workflow Temporal: sinal de aprovação]
    Workflow --> Activity[Activity: correção idempotente e limitada]
    Activity --> Verifica[Verificar saúde e registar resultado]
    Verifica --> Escala[Escalar casos não resolvidos]
```

No KubeHealer, Temporal coordena scan, diagnóstico e espera de aprovação desde o início; o sinal permite avançar para a activity de correção. Este diagrama reúne padrões dos três dias: não afirma que KubeHealer usa obrigatoriamente MCP. No dia 88 MCP serve ferramentas; no dia 89 Temporal coordena o percurso de remediação. O laboratório Temporal local usa diagnóstico simulado para testar durabilidade/aprovação, separadamente do desempenho de Claude.

## Contratos a memorizar

| Fronteira | Contrato |
| --- | --- |
| Fonte → build | Dependências e instruções reprodutíveis |
| Build → registry | Artefacto identificado e verificado |
| Registry → Git desejado | Referência da imagem efetivamente publicada |
| Git → Argo CD | Fonte/path/revisão e permissões corretas |
| Controller → workload | Ownership e estratégia de reconciliação |
| Workload → armazenamento | Claim, classe, zona e política de dados |
| Workload → tráfego | Porta, readiness, endpoints e routing |
| Telemetria → equipa | Dados interpretáveis, alerta entregue e runbook |
| Proposta → ação | Âmbito, aprovação, auditoria e verificação |
