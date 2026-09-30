# Day 84 Validation

## Local deployment
- Created kind-days81-90-lab with its own ignored kubeconfig.
- Installed argo-cd chart 10.9.5, ArgoCD v3.5.3; all controller Pods became Ready.
- ArgoCD fetched 2026/day-80/bankapp from AFarinha/90DaysOfDevOps master, using dev values with Ollama disabled.
- bankapp-local became Synced and Healthy; BankApp and MySQL Pods were 1/1 Ready; the local 2Gi PVC was Bound.
- Credentials were randomly generated and retained privately. An initial mismatch between the two root-password references was corrected in this task's generated Secret; the helper now uses one shared value.

## HTTP and reconciliation
```text
/actuator/health: HTTP 200, status UP
/login: HTTP 200
/actuator/prometheus: HTTP 200
Scale 2 -> Git desired 1 restored after 6.7s
Deleted ConfigMap recreated after 10.6s
Manual database ConfigMap field restored after 55.2s
Manual sync: replicas remained 2 for 15s with automation disabled
Explicit manual sync restored replicas to 1 after 8.0s
Envoy /login: HTTP 200; BANKAPP_AFFINITY cookie present
```

An initial test adding an unknown ConfigMap key did not converge within 120s. The successful test changed the existing managed MYSQL_DATABASE field instead. Port forwards initially needed an explicit readiness wait rather than a fixed two-second sleep. The final validate-gitops.py records results incrementally and waits for its local ports.

This demonstrates local Helm-backed GitOps. EKS deployment of the upstream raw-manifest application, a fork-backed code change and cloud access remain pending.

## Final scope and cleanup
The task-created days81-90-lab cluster and days87-broken, days87-ollama and days89-temporal containers were removed successfully. Only the pre-existing devops-cluster remains; its default context is unchanged and its node was verified Ready.

Sources, virtual environments, model cache and private test history remain only in ignored local directories for reproducibility. No AWS resources were created. Final Python/YAML syntax, Terraform formatting, whitespace, credential-pattern and Git scope checks passed; no README or file outside days 81-90 was changed. No commit, push or social post was performed.
