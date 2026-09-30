# Day 90 - Graduation Review

## Completion status
The challenge reaches its final review day. This report records the learning map and remaining practical gaps; it does not claim that every cloud or AI exercise succeeded. Days 81-83 require AWS credentials and a verified EKS deployment. The end-to-end DockerHub/EKS pipeline and Claude diagnosis also remain pending.

## Timeline
| Period | Topics and connection |
| --- | --- |
| Days 1-13 | Linux files, permissions, processes and storage form the operating foundation |
| Days 14-21 | Networking and shell automation connect systems and repeat operations |
| Days 22-28 | Git/GitHub make changes reviewable and recoverable |
| Days 29-37 | Docker packages applications, networks and persistent data |
| Days 38-49 | CI/CD, Actions, runners, secrets and security checks automate delivery |
| Days 50-58 | Kubernetes schedules workloads and provides services/RBAC |
| Days 59-67 | Terraform expresses infrastructure and tracks resource state |
| Days 68-72 | Ansible manages host configuration |
| Days 73-77 | Metrics, logs, traces and alerts provide operational evidence |
| Days 78-80 | Helm packages BankApp configuration for multiple environments |
| Days 81-83 | EKS adds managed control plane, IAM, zonal storage and public routing |
| Days 84-86 | ArgoCD pulls desired state; CI updates Git rather than pushing to the cluster |
| Days 87-89 | LLM tools, MCP, approval gates and Temporal connect diagnosis to controlled action |
| Day 90 | Review evidence, identify gaps and choose the next practical exercise |

The pipeline is code -> Git -> Actions tests/image -> registry -> desired-state Git commit -> ArgoCD -> Kubernetes -> monitoring -> reviewed remediation. Terraform provisions the infrastructure; Helm renders workloads; Ansible configures appropriate hosts. Prometheus handles metrics, Loki logs and an OpenTelemetry tracing backend handles traces; Grafana visualizes them.

## Five technical insights
1. A successful apply or Synced status is different from a healthy application.
2. Persistence belongs to storage, not the lifetime of a container or Pod.
3. GitOps makes operational drift reviewable but requires attention to multiple controllers owning the same fields.
4. Agent tooling needs bounds, clear descriptions and validated arguments; a model answer is not execution evidence.
5. Durable workflows must preserve approval state and make retries safe.

These are technical observations from the work, not invented personal memories.

## Difficulties and honest reflection
The final block exposed practical obstacles: missing AWS credentials, slow image/model pulls and differences between exercise text and upstream code. The response was to validate available local behavior, keep cloud artifacts intact, record failures and avoid substituting fabricated output.
The participant's personal hardest day and how they experienced it still require their own answer.

## Skills inventory
Confidence is a personal assessment and was not guessed.
| Skill | Days | Confidence 1-5 |
| --- | --- | --- |
| Linux | 1-13 | To be rated by participant |
| Shell | 16-21 | To be rated by participant |
| Git/GitHub | 22-28 | To be rated by participant |
| Docker | 29-37 | To be rated by participant |
| Actions CI/CD | 38-49 | To be rated by participant |
| Kubernetes | 50-58 | To be rated by participant |
| Terraform | 59-67 | To be rated by participant |
| Ansible | 68-72 | To be rated by participant |
| Observability | 73-77 | To be rated by participant |
| Helm | 78-80 | To be rated by participant |
| EKS | 81-83 | To be rated after cloud validation |
| ArgoCD/GitOps | 84-86 | To be rated after end-to-end validation |
| Agentic AI | 87-89 | To be rated after full model-backed execution |

## Next practice
First finish the verified gaps: one short-lived EKS deployment with a cost plan, then a personal registry/fork pipeline, then a scoped Claude diagnosis with human approval. After that, repeat the complete pipeline for a small owned application, add backup/restore and secret-management exercises, and test failure recovery.

Advice for Day 1: keep short factual notes, validate each command, use isolated disposable labs and retain enough evidence to reproduce a failure. Preserve existing data, keep credentials private and distinguish preparation from completed execution.

## Sharing draft
I reached the final review of the #90DaysOfDevOps learning challenge. The strongest lesson was learning how Linux, Git, containers, infrastructure code, GitOps, observability and AI tooling connect into one delivery process.

I documented local validation and the remaining cloud/API-dependent exercises instead of claiming results I had not verified. Next I want to complete those gaps and build an owned application pipeline with backup, recovery and scoped AI diagnosis.

#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham

This is a draft, not a published post. Personal confidence ratings, personal reflections and any screenshot collage remain participant tasks.
