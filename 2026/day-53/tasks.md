# Day 53 Tasks

Run from `2026/day-53/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `kubectl apply --dry-run=client -f app-deployment.yaml` | Validate app-deployment.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f app-deployment.yaml` | Validate app-deployment.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f app-deployment.yaml` | Apply app-deployment.yaml. |
| `kubectl apply --dry-run=client -f clusterip-service.yaml` | Validate clusterip-service.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f clusterip-service.yaml` | Validate clusterip-service.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f clusterip-service.yaml` | Apply clusterip-service.yaml. |
| `kubectl apply --dry-run=client -f nodeport-service.yaml` | Validate nodeport-service.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f nodeport-service.yaml` | Validate nodeport-service.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f nodeport-service.yaml` | Apply nodeport-service.yaml. |
| `kubectl apply --dry-run=client -f loadbalancer-service.yaml` | Validate loadbalancer-service.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f loadbalancer-service.yaml` | Validate loadbalancer-service.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f loadbalancer-service.yaml` | Apply loadbalancer-service.yaml. |
| `kubectl rollout status deployment/web-app -n default --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods -o wide; kubectl get services -o wide; kubectl get endpointslices -l kubernetes.io/service-name=web-app-clusterip` | Inspect Pod IPs, Service types and endpoints. |
| `kubectl run test-client --image=busybox:1.36 --restart=Never --attach --rm -- sh -c 'wget -qO- http://web-app-clusterip; wget -qO- http://web-app-clusterip.default.svc.cluster.local; nslookup web-app-clusterip'` | Verify internal HTTP and short/full DNS; --rm cleans temporary client. |
| `kubectl run dns-test --image=busybox:1.36 --restart=Never --attach --rm -- nslookup -type=A web-app-clusterip.default.svc.cluster.local` | Use explicit FQDN and A record to avoid BusyBox search-suffix NXDOMAIN exit despite a valid answer. |
| `kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}'` | Read node internal IP. |
| `curl -fsS http://172.18.0.2:30080` | Verify NodePort from WSL. |
| `kubectl describe service web-app-loadbalancer` | Inspect pending external IP and allocated ClusterIP/NodePort. |
| `kubectl delete -f app-deployment.yaml -f clusterip-service.yaml -f nodeport-service.yaml -f loadbalancer-service.yaml` | Remove Deployment and three Services. Deletes exercise resources; approval required. |
| `kubectl get services` | Verify day 53 Services are gone. |

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-53/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 53 - Completed - Expose Kubernetes workloads with Services"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
