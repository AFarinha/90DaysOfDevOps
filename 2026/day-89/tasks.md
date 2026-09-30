# Day 89 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `git clone --depth 1 https://github.com/TrainWithShubham/kubehealer.git .runtime/kubehealer; python3 -m venv .venv` | First run only: obtain reviewed upstream source and create a private environment. |
| `.venv/bin/pip install -r requirements.txt; .venv/bin/pip check` | Install authorized Temporal/Anthropic/Kubernetes dependencies. |
| `export KUBECONFIG="$PWD/../day-84/.runtime/kubeconfig"` | Select only the dedicated disposable cluster. |
| `kubectl create namespace days89-lab; kubectl apply --dry-run=server -f broken-apps.yaml; kubectl apply -f broken-apps.yaml` | Create and validate the three intentionally broken Deployment fixtures. |
| `kubectl get pods -n days89-lab` | Verify all three failure modes before diagnosis. |
| `docker run -d --name days89-temporal -p 127.0.0.1:7233:7233 -p 127.0.0.1:8233:8233 temporalio/temporal server start-dev --ip 0.0.0.0` | Run the local Temporal dev server; host ports remain loopback-only. |
| `.venv/bin/python validate-durability.py` | Integration test with deterministic diagnosis fixture: real scan/Temporal crash-recovery/approval/Deployment patches; explicitly not a Claude test. |
| `read -rs -p 'Anthropic key: ' ANTHROPIC_API_KEY; export ANTHROPIC_API_KEY` | Configure API credential privately; do not echo/store it in Git. |
| `.venv/bin/python lab-worker.py` | Start the scoped real-Claude worker; fails explicitly without a local key. |
| `.venv/bin/python start-with-approval.py start; .venv/bin/python start-with-approval.py status` | Start a stable-ID workflow with auto_approve=False, then inspect proposed plans. |
| `.venv/bin/python start-with-approval.py approve --pod <verified-pod-name>` | Only after reviewing a specific diagnosis, record explicit approval. |
| `.venv/bin/python start-with-approval.py reject --pod <verified-pod-name>` | Reject unresolved or unwanted changes, including missing ConfigMap. |
| `kubectl rollout status deployment/web-app -n days89-lab --timeout=120s; kubectl rollout status deployment/memory-app -n days89-lab --timeout=120s` | Verify actual corrected workload readiness; patch success alone is insufficient. |
| `kubectl delete namespace days89-lab; docker rm -f days89-temporal` | Destructive lab cleanup; stop worker first and retain any needed private history. |
| `kind delete cluster --name days81-90-lab` | Final cleanup of the dedicated cluster only after all local tests; preserves devops-cluster. |
