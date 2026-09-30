# Day 85 Validation

- root-app.yaml, project-rbac.yaml, notifications.yaml and all three child Applications passed server dry-run against ArgoCD v3.5.3.
- API warnings included the upstream-style ArgoCD finalizer name and the existing notification ConfigMap's missing client-apply annotation; dry-run did not change the live notification ConfigMap.
- prepare-sync-waves.py generated local wave manifests from the reviewed reference, omitted plaintext Secrets and placed WaitForFirstConsumer PVCs with their consuming workloads.
- The day-84 local app demonstrated manual sync: drift remained for 15s with automation disabled and explicit sync restored replicas in 8.0s. Automation was restored afterward.
- App of Apps was prepared, not bootstrapped from an unpublished Git path.
- Historical rollback, notification delivery, real SSO/RBAC identity restrictions and wave-order runtime validation remain pending.
- No webhook message was sent and no project destination was broadened as an alleged restriction test.

## Final scope and cleanup
The task-created days81-90-lab cluster and days87-broken, days87-ollama and days89-temporal containers were removed successfully. Only the pre-existing devops-cluster remains; its default context is unchanged and its node was verified Ready.

Sources, virtual environments, model cache and private test history remain only in ignored local directories for reproducibility. No AWS resources were created. Final Python/YAML syntax, Terraform formatting, whitespace, credential-pattern and Git scope checks passed; no README or file outside days 81-90 was changed. No commit, push or social post was performed.
