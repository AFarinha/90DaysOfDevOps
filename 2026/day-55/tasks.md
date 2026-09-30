# Day 55 Tasks

Run from `2026/day-55/` using Bash in WSL and context `kind-devops-cluster`. Commands are listed in execution order. Start with `export PATH="$HOME/.local/bin:$PATH"` to expose user-local tools. `-n` selects a namespace, `-A` selects all namespaces, and `-f` reads a manifest. Dry-runs validate without persisting; `--wait` and `--timeout` bound readiness waits. Deletion commands affect only exercise resources and require approval.

| Command | What it does |
| --- | --- |
| `kubectl apply --dry-run=client -f ephemeral-pod.yaml` | Validate ephemeral-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f ephemeral-pod.yaml` | Validate ephemeral-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f ephemeral-pod.yaml` | Apply ephemeral-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/ephemeral --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl exec ephemeral -- cat /data/message.txt` | Read first timestamp in emptyDir. |
| `kubectl delete -f ephemeral-pod.yaml` | Remove ephemeral Pod and its emptyDir. Deletes exercise resources; approval required. |
| `kubectl apply --dry-run=client -f ephemeral-pod.yaml` | Validate ephemeral-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f ephemeral-pod.yaml` | Validate ephemeral-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f ephemeral-pod.yaml` | Apply ephemeral-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/ephemeral --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl exec ephemeral -- cat /data/message.txt` | Read recreated timestamp; previous emptyDir data is gone. |
| `kubectl apply --dry-run=client -f pv.yaml` | Validate pv.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f pv.yaml` | Validate pv.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f pv.yaml` | Apply pv.yaml. |
| `kubectl get pv day55-pv` | Verify static PV is Available. |
| `kubectl apply --dry-run=client -f pvc.yaml` | Validate pvc.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f pvc.yaml` | Validate pvc.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f pvc.yaml` | Apply pvc.yaml. |
| `kubectl get pv day55-pv; kubectl get pvc static-data` | Verify static PVC bound to day55-pv. |
| `kubectl apply --dry-run=client -f persistent-pod.yaml` | Validate persistent-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f persistent-pod.yaml` | Validate persistent-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f persistent-pod.yaml` | Apply persistent-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/persistent --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl exec persistent -- cat /data/message.txt` | Read first persistent timestamp. |
| `kubectl delete -f persistent-pod.yaml` | Delete Pod while retaining PVC. Deletes exercise resources; approval required. |
| `kubectl apply --dry-run=client -f persistent-pod.yaml` | Validate persistent-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f persistent-pod.yaml` | Validate persistent-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f persistent-pod.yaml` | Apply persistent-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/persistent --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl exec persistent -- cat /data/message.txt` | Verify timestamps from both Pods are retained. |
| `kubectl get storageclass; kubectl describe storageclass standard` | Inspect provisioner, Delete reclaim policy and WaitForFirstConsumer binding. |
| `kubectl apply --dry-run=client -f dynamic-pvc.yaml` | Validate dynamic-pvc.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f dynamic-pvc.yaml` | Validate dynamic-pvc.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f dynamic-pvc.yaml` | Apply dynamic-pvc.yaml. |
| `kubectl get pvc dynamic-data` | Observe Pending until a consumer is scheduled. |
| `kubectl apply --dry-run=client -f dynamic-pod.yaml` | Validate dynamic-pod.yaml with client dry-run; do not persist resources. |
| `kubectl apply --dry-run=server -f dynamic-pod.yaml` | Validate dynamic-pod.yaml with server dry-run; do not persist resources. |
| `kubectl apply -f dynamic-pod.yaml` | Apply dynamic-pod.yaml. |
| `kubectl wait --for=condition=Ready pod/dynamic --timeout=180s` | Wait for exercise Pods to become Ready (180-second timeout). |
| `kubectl exec dynamic -- cat /data/message.txt; kubectl get pv; kubectl get pvc` | Verify dynamically provisioned PV and stored data. |
| `kubectl delete -f ephemeral-pod.yaml -f persistent-pod.yaml -f dynamic-pod.yaml` | Delete storage consumers first. Deletes exercise resources; approval required. |
| `kubectl delete -f pvc.yaml -f dynamic-pvc.yaml` | Delete exercise claims and observe reclaim behavior. Deletes exercise resources; approval required. |
| `kubectl get pv` | Inspect retained manual PV versus deleted dynamic PV. |
| `kubectl delete -f pv.yaml` | Delete retained PV object; hostPath data requires separate explicit cleanup. Deletes exercise resources; approval required. |
| `docker exec devops-cluster-control-plane sh -c 'test "$(readlink -f /tmp/k8s-pv-data/message.txt)" = /tmp/k8s-pv-data/message.txt && cat /tmp/k8s-pv-data/message.txt'` | Verify resolved hostPath test file and its two recorded timestamps before removal. |
| `docker exec devops-cluster-control-plane sh -c 'test "$(readlink -f /tmp/k8s-pv-data/message.txt)" = /tmp/k8s-pv-data/message.txt && rm -- /tmp/k8s-pv-data/message.txt && rmdir -- /tmp/k8s-pv-data'` | Remove only verified test file and its empty directory from the kind node. Deletes exercise resources; approval required. |
| `docker exec devops-cluster-control-plane test ! -e /tmp/k8s-pv-data; kubectl get pv` | Verify hostPath removal and final absence of earlier exercise PVs; capstone PV may still exist. |

## Submission

The README requires commit and push to the fork. Run from the repository root after validation; stage only this day. Push publishes the committed work to origin/master.

| Command | What it does |
| --- | --- |
| `cd /home/afarinha/git/90DaysOfDevOps` | Move to repository root. |
| `git add 2026/day-55/` | Stage only this day; do not include unrelated AGENTS.md. |
| `git commit -m "Day 55 - Completed - Verify persistent and ephemeral storage"` | Create the required completion commit. |
| `git push origin master` | Publish completion commits to the fork; changes the remote branch. |
