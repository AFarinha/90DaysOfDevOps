# Day 58 Tasks

Run from `2026/day-58/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `kubectl apply --dry-run=client -f metrics-server.yaml` | Validate metrics-server.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f metrics-server.yaml` | Validate metrics-server.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f metrics-server.yaml` | Apply metrics-server.yaml. |
| `kubectl rollout status deployment/metrics-server -n kube-system --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl top nodes; kubectl top pods -A --sort-by=cpu` | Verify metrics API and inspect actual CPU/memory usage sorted by CPU. |
| `kubectl apply --dry-run=client -f php-apache-deployment.yaml` | Validate php-apache-deployment.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f php-apache-deployment.yaml` | Validate php-apache-deployment.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f php-apache-deployment.yaml` | Apply php-apache-deployment.yaml. |
| `kubectl apply --dry-run=client -f service.yaml` | Validate service.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f service.yaml` | Validate service.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f service.yaml` | Apply service.yaml. |
| `kubectl rollout status deployment/php-apache -n default --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl top pods -l app=php-apache` | Read initial PHP server usage. |
| `kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10` | Create imperative CPU HPA; target 50% of 200m requests, bounded 1-10 replicas. |
| `kubectl get hpa; kubectl describe hpa php-apache` | Inspect initial target and HPA conditions. |
| `kubectl run load-generator --image=busybox:1.36 --restart=Never -- sh -c 'while true; do wget -q -O- http://php-apache >/dev/null; done'` | Generate continuous HTTP load without storing response bodies. |
| `for attempt in {1..36}; do kubectl get hpa php-apache; count=$(kubectl get deployment php-apache -o jsonpath='{.spec.replicas}'); [ "$count" -gt 1 ] && break; sleep 5; done; test "$count" -gt 1; kubectl get deployment,pods -l app=php-apache; kubectl describe hpa php-apache` | Observe autoscaling for up to 180 seconds and require increased replicas. |
| `kubectl delete pod load-generator` | Stop load generator. Deletes exercise resources; approval required. |
| `kubectl delete hpa php-apache` | Remove imperative HPA before declarative replacement. Deletes exercise resources; approval required. |
| `kubectl apply --dry-run=client -f hpa.yaml` | Validate hpa.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f hpa.yaml` | Validate hpa.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f hpa.yaml` | Apply hpa.yaml. |
| `kubectl describe hpa php-apache` | Verify autoscaling/v2 policies: immediate scale-up, 300-second scale-down stabilization. |
| `kubectl delete -f hpa.yaml -f service.yaml -f php-apache-deployment.yaml` | Remove workload and HPA; leave authorized Metrics Server installed. Deletes exercise resources; approval required. |
| `kubectl get deployment metrics-server -n kube-system; kubectl top nodes` | Verify Metrics Server remains operational after cleanup. |

The committed Metrics Server manifest is the official v0.9.0 release with the local-kind-only `--kubelet-insecure-tls` argument added. Use this reviewed file directly; downloading the upstream file over it would remove that adjustment. Do not use the adjustment in production. `--cpu=50%` is the current alternative to deprecated `--cpu-percent=50`.

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-58/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 58 - Completed - Install metrics and verify CPU autoscaling"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
