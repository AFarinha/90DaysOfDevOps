# Day 57 Tasks

Run from `2026/day-57/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `kubectl apply --dry-run=client -f resources-pod.yaml` | Validate resources-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f resources-pod.yaml` | Validate resources-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f resources-pod.yaml` | Apply resources-pod.yaml. |
| `kubectl apply --dry-run=client -f oom-pod.yaml` | Validate oom-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f oom-pod.yaml` | Validate oom-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f oom-pod.yaml` | Apply oom-pod.yaml. |
| `kubectl apply --dry-run=client -f pending-pod.yaml` | Validate pending-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f pending-pod.yaml` | Validate pending-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f pending-pod.yaml` | Apply pending-pod.yaml. |
| `kubectl apply --dry-run=client -f liveness-pod.yaml` | Validate liveness-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f liveness-pod.yaml` | Validate liveness-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f liveness-pod.yaml` | Apply liveness-pod.yaml. |
| `kubectl apply --dry-run=client -f readiness-pod.yaml` | Validate readiness-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f readiness-pod.yaml` | Validate readiness-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f readiness-pod.yaml` | Apply readiness-pod.yaml. |
| `kubectl apply --dry-run=client -f startup-pod.yaml` | Validate startup-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f startup-pod.yaml` | Validate startup-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f startup-pod.yaml` | Apply startup-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/resources pod/readiness pod/startup --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl describe pod resources` | Inspect requests, limits and Burstable QoS. |
| `for attempt in {1..24}; do reason=$(kubectl get pod oom -o jsonpath='{.status.containerStatuses[0].lastState.terminated.reason}'); [ "$reason" = OOMKilled ] && break; sleep 5; done; test "$reason" = OOMKilled; kubectl describe pod oom` | Wait for OOMKilled and verify exit 137. |
| `kubectl describe pod pending` | Inspect insufficient CPU and memory scheduling events. |
| `kubectl expose pod readiness --port=80 --name=readiness-svc` | Expose readiness Pod through Service. |
| `kubectl get endpointslices -l kubernetes.io/service-name=readiness-svc -o yaml` | Record ready endpoint before probe failure. |
| `kubectl exec readiness -- rm /usr/share/nginx/html/index.html` | Remove disposable container index page to make readiness return HTTP 403. |
| `kubectl wait --for=condition=Ready=false pod/readiness --timeout=60s; kubectl get pod readiness; kubectl get endpointslices -l kubernetes.io/service-name=readiness-svc -o yaml` | Verify readiness false and endpoint ready=false without restart. |
| `for attempt in {1..18}; do count=$(kubectl get pod liveness -o jsonpath='{.status.containerStatuses[0].restartCount}'); [ "$count" -ge 1 ] && break; sleep 5; done; test "$count" -ge 1; kubectl describe pod liveness; kubectl describe pod startup` | Verify liveness restarts and startup success within the 60-second budget. |
| `kubectl delete -f resources-pod.yaml -f oom-pod.yaml -f pending-pod.yaml -f liveness-pod.yaml -f readiness-pod.yaml -f startup-pod.yaml; kubectl delete service readiness-svc` | Remove resource/probe Pods and Service. Deletes exercise resources; approval required. |
| `kubectl get pods,services,pvc` | Verify exercises are cleaned up. |

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-57/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 57 - Completed - Test resource limits and health probes"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
