# Day 52 Tasks

Run from `2026/day-52/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `kubectl get namespaces; kubectl get pods -n kube-system` | Inspect built-in namespaces and system Pods; eight existed before Metrics Server installation. |
| `kubectl create namespace dev` | Create dev namespace. |
| `kubectl create namespace staging` | Create staging namespace. |
| `kubectl apply --dry-run=client -f namespace.yaml` | Validate namespace.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f namespace.yaml` | Validate namespace.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f namespace.yaml` | Apply namespace.yaml. |
| `kubectl run nginx-dev --image=nginx:latest -n dev` | Create standalone Pod in dev namespace. |
| `kubectl run nginx-staging --image=nginx:latest -n staging` | Create standalone Pod in staging namespace. |
| `kubectl apply --dry-run=client -f nginx-deployment.yaml` | Validate nginx-deployment.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f nginx-deployment.yaml` | Validate nginx-deployment.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f nginx-deployment.yaml` | Apply nginx-deployment.yaml. |
| `kubectl rollout status deployment/nginx-deployment -n dev --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods; kubectl get deployments,pods -A` | Compare default namespace output with all namespaces (-A). |
| `kubectl get pods -n dev -l app=nginx-deployment -o jsonpath='{.items[0].metadata.name}'` | Choose managed Pod for replacement. |
| `pod=$(kubectl get pods -n dev -l app=nginx-deployment -o jsonpath='{.items[0].metadata.name}'); kubectl delete pod "$pod" -n dev` | Delete one managed Pod to test self-healing. Deletes exercise resources; approval required. |
| `kubectl rollout status deployment/nginx-deployment -n dev --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get pods -n dev` | Verify replacement has a new name. |
| `kubectl scale deployment nginx-deployment --replicas=5 -n dev` | Scale desired replicas to 5. |
| `kubectl rollout status deployment/nginx-deployment -n dev --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get deployment,pods -n dev` | Inspect ready replica count. |
| `kubectl scale deployment nginx-deployment --replicas=2 -n dev` | Scale desired replicas to 2. |
| `kubectl rollout status deployment/nginx-deployment -n dev --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get deployment,pods -n dev` | Inspect ready replica count. |
| `kubectl set image deployment/nginx-deployment nginx=nginx:1.25 -n dev` | Trigger rolling update to nginx:1.25. |
| `kubectl rollout status deployment/nginx-deployment -n dev --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl rollout history deployment/nginx-deployment -n dev` | Inspect rollout revisions. |
| `kubectl rollout undo deployment/nginx-deployment -n dev` | Roll back the Pod template. |
| `kubectl rollout status deployment/nginx-deployment -n dev --timeout=180s` | Wait for the controller rollout (180-second timeout). |
| `kubectl get deployment nginx-deployment -n dev -o jsonpath='{.spec.template.spec.containers[0].image}'` | Verify rollback image. |
| `kubectl delete namespace dev staging production` | Remove newly created namespaces and exercise resources. Deletes exercise resources; approval required. |
| `kubectl get namespaces` | Verify namespaces are gone. |

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-52/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 52 - Completed - Explore namespaces and Deployment recovery"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
