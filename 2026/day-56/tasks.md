# Day 56 Tasks

Run from `2026/day-56/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `kubectl apply --dry-run=client -f comparison-deployment.yaml` | Validate comparison-deployment.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f comparison-deployment.yaml` | Validate comparison-deployment.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f comparison-deployment.yaml` | Apply comparison-deployment.yaml. |
| `kubectl rollout status deployment/comparison -n default --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods -l app=comparison -o jsonpath='{.items[0].metadata.name}'` | Read random Deployment Pod name. |
| `pod=$(kubectl get pods -l app=comparison -o jsonpath='{.items[0].metadata.name}'); kubectl delete pod "$pod"` | Test replacement with a different name. Deletes exercise resources; approval required. |
| `kubectl rollout status deployment/comparison -n default --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods -l app=comparison` | Inspect replacement names. |
| `kubectl delete -f comparison-deployment.yaml` | Remove comparison Deployment before StatefulSet. Deletes exercise resources; approval required. |
| `kubectl apply --dry-run=client -f headless-service.yaml` | Validate headless-service.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f headless-service.yaml` | Validate headless-service.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f headless-service.yaml` | Apply headless-service.yaml. |
| `kubectl apply --dry-run=client -f statefulset.yaml` | Validate statefulset.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f statefulset.yaml` | Validate statefulset.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f statefulset.yaml` | Apply statefulset.yaml. |
| `kubectl rollout status statefulset/web -n default --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods -l app=web -o wide; kubectl get pvc; kubectl get service web-headless` | Inspect ordered Pod names, per-replica PVCs and headless Service. |
| `kubectl run stateful-dns --image=busybox:1.36 --restart=Never --attach --rm -- sh -c 'for i in 0 1 2; do nslookup web-$i.web-headless.default.svc.cluster.local; done'` | Resolve all three stable Pod DNS names; remove temporary client. |
| `kubectl exec web-0 -- sh -c "echo Data-from-web-0 > /usr/share/nginx/html/index.html"` | Write unique data to web-0 PVC. |
| `kubectl exec web-1 -- sh -c "echo Data-from-web-1 > /usr/share/nginx/html/index.html"` | Write unique data to web-1 PVC. |
| `kubectl exec web-2 -- sh -c "echo Data-from-web-2 > /usr/share/nginx/html/index.html"` | Write unique data to web-2 PVC. |
| `kubectl delete pod web-0` | Delete StatefulSet Pod while preserving identity and PVC. Deletes exercise resources; approval required. |
| `kubectl wait --for=condition=Ready pod/web-0 --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl exec web-0 -- cat /usr/share/nginx/html/index.html` | Verify identical stored data after replacement. |
| `kubectl scale statefulset web --replicas=5` | Scale StatefulSet to 5; creation uses ascending ordinals and removal descending. |
| `kubectl rollout status statefulset/web -n default --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods -l app=web; kubectl get pvc` | Verify retained claims after scaling. |
| `kubectl scale statefulset web --replicas=3` | Scale StatefulSet to 3; creation uses ascending ordinals and removal descending. |
| `kubectl rollout status statefulset/web -n default --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods -l app=web; kubectl get pvc` | Verify retained claims after scaling. |
| `kubectl delete -f statefulset.yaml -f headless-service.yaml` | Remove StatefulSet and headless Service. Deletes exercise resources; approval required. |
| `kubectl get pvc` | Verify five claims are retained after controller deletion. |
| `kubectl delete pvc web-data-web-0 web-data-web-1 web-data-web-2 web-data-web-3 web-data-web-4` | Remove only StatefulSet exercise claims and dynamically provisioned data. Deletes exercise resources; approval required. |

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-56/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 56 - Completed - Verify StatefulSet identity and storage"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
