# Day 89 Validation

## Environment and faults
- Isolated .venv installed Temporal, Anthropic and Kubernetes SDK dependencies; pip check passed.
- temporalio/temporal dev server ran with loopback host ports 7233 and 8233.
- broken-apps.yaml passed server dry-run; web-app showed ImagePullBackOff, memory-app showed OOMKilled and config-app showed CreateContainerConfigError.
- lab-worker.py failed explicitly because ANTHROPIC_API_KEY was not configured. Full Claude diagnosis remains pending.

## Real integration test with simulated diagnosis
validate-durability.py used real upstream HealerWorkflow, real Temporal history, real Kubernetes scans/details and scoped real Deployment patches. Only the diagnosis activity was replaced by an explicit deterministic fixture.

```text
Worker killed during diagnosis after one completed activity
Replay reused completed diagnosis; awaiting approval; no fixes applied
Healed 2/3 pods:
config-app: skipped -- deterministic fixture, not an AI diagnosis
memory-app: patch_resources -- memory limit changed to 256Mi
web-app: fix_image -- image changed to nginx:alpine
```

After fixes, web-app and memory-app Deployments were 1/1 Ready; config-app remained 0/1. The test asserts three unique diagnoses, no fixes before approval and one execution of the already-completed diagnosis after worker recovery. An initial run exposed duplicate upstream scan results; the scoped adapter deduplicates them before the passing repeat.

The workflow history remains in ignored local storage. No Anthropic call, generated Claude answer or human terminal screenshot is claimed.

## Final scope and cleanup
The task-created days81-90-lab cluster and days87-broken, days87-ollama and days89-temporal containers were removed successfully. Only the pre-existing devops-cluster remains; its default context is unchanged and its node was verified Ready.

Sources, virtual environments, model cache and private test history remain only in ignored local directories for reproducibility. No AWS resources were created. Final Python/YAML syntax, Terraform formatting, whitespace, credential-pattern and Git scope checks passed; no README or file outside days 81-90 was changed. No commit, push or social post was performed.
