# Day 51 Tasks - Kubernetes Manifests and Pods

Run these commands from `~/git/90DaysOfDevOps/2026/day-51`. They assume the Day 50 `kind` cluster and kubectl context are available.

## Check the Cluster

| Command | What it does |
| --- | --- |
| `kind get clusters` | Lists local kind clusters and confirms that `devops-cluster` exists. |
| `kind create cluster --name devops-cluster --wait 120s` | Recreates the learning cluster when Docker has been restarted or no kind cluster exists, and waits for readiness. |
| `kubectl config current-context` | Shows which kubeconfig context kubectl currently uses; the expected value is `kind-devops-cluster`. |
| `kubectl get nodes` | Confirms that the cluster API is reachable and its node is `Ready`. |

## Validate and Apply the Manifests

Repeat the validation and apply commands for `busybox-pod.yaml` and `team-pod.yaml` after checking `nginx-pod.yaml`.

| Command | What it does |
| --- | --- |
| `kubectl apply -f nginx-pod.yaml --dry-run=client` | Parses and prepares the Nginx resource locally without storing it in the cluster. |
| `kubectl apply -f nginx-pod.yaml --dry-run=server` | Sends a validation-only request to the API server without persisting the Nginx Pod. |
| `kubectl apply -f nginx-pod.yaml` | Creates or updates `nginx-pod` from its declarative manifest. |
| `kubectl apply -f busybox-pod.yaml` | Creates or updates the long-running BusyBox Pod from YAML. |
| `kubectl apply -f team-pod.yaml` | Creates or updates the third Pod containing `app`, `environment`, and `team` labels. |
| `kubectl wait --for=condition=Ready pod/nginx-pod pod/busybox-pod pod/team-pod --timeout=180s` | Waits until all three declarative Pods report the Ready condition or the timeout expires. |

## Explore the Pods

| Command | What it does |
| --- | --- |
| `kubectl get pods` | Lists Pods in the current namespace and shows readiness, status, restarts, and age. |
| `kubectl get pods -o wide` | Adds Pod IP and assigned-node information to the Pod list. |
| `kubectl describe pod nginx-pod` | Shows Nginx Pod configuration, current conditions, container state, and recent events. |
| `kubectl logs nginx-pod` | Reads standard output and standard error from the Nginx container. |
| `kubectl logs busybox-pod` | Shows the `Hello from BusyBox` message emitted by the configured command. |
| `kubectl exec -it nginx-pod -- /bin/bash` | Opens an interactive Bash shell inside the Nginx container. |
| `curl localhost:80` | Requests the Nginx home page from inside the container through its loopback interface. |
| `exit` | Closes the interactive container shell and returns to the host terminal. |
| `kubectl exec nginx-pod -- curl -fsS localhost:80` | Performs the same HTTP verification non-interactively and fails on HTTP or connection errors. |

## Compare Imperative and Generated Resources

| Command | What it does |
| --- | --- |
| `kubectl run redis-pod --image=redis:latest` | Imperatively creates a standalone Redis Pod without a local manifest. |
| `kubectl get pod redis-pod -o yaml` | Displays the complete stored resource, including server defaults, metadata, scheduling data, and status. |
| `kubectl run test-pod --image=nginx --dry-run=client -o yaml` | Generates a Pod manifest on standard output without creating the Pod. |
| `kubectl run test-pod --image=nginx --dry-run=client -o yaml > test-pod.yaml` | Saves the generated manifest to `test-pod.yaml` for review and customization. |

## Validate a Missing Image

Temporarily remove the container's `image` field from a copy of a Pod manifest, then run both commands below. Restore or delete the invalid copy afterward.

| Command | What it does |
| --- | --- |
| `kubectl apply -f invalid-pod.yaml --dry-run=client` | Tests local object generation; with the current kubectl version, this did not reject the missing image. |
| `kubectl apply -f invalid-pod.yaml --dry-run=server` | Asks the API server to validate the Pod and returns `spec.containers[0].image: Required value`. |

## Work with Labels

| Command | What it does |
| --- | --- |
| `kubectl get pods --show-labels` | Lists every Pod together with all of its labels. |
| `kubectl get pods -l app=nginx` | Selects Pods whose `app` label equals `nginx`. |
| `kubectl get pods -l environment=dev` | Selects Pods in the exercise's development environment. |
| `kubectl get pods -l team=platform` | Selects the third Pod by its team label. |
| `kubectl label pod nginx-pod environment=production` | Adds the `environment=production` label to the existing Nginx Pod. |
| `kubectl get pods -l environment=production` | Verifies that the new label selects `nginx-pod`. |
| `kubectl label pod nginx-pod environment-` | Removes the `environment` label; the trailing hyphen means deletion. |

## Clean Up

| Command | What it does |
| --- | --- |
| `kubectl delete pod nginx-pod busybox-pod redis-pod team-pod` | Deletes all Pods created during the practical exercise by name. |
| `kubectl delete -f nginx-pod.yaml` | Alternative declarative deletion for the resource described by the Nginx manifest. Do not run it after deleting the same Pod by name unless `--ignore-not-found` is used. |
| `kubectl get pods` | Verifies that no exercise Pods remain in the current namespace. |

## Commit the Day 51 Work

Day 51 does not request a separate branch or changes to `github-actions-practice`, so commit only to the parent repository's `master` branch.

| Command | What it does |
| --- | --- |
| `cd ~/git/90DaysOfDevOps` | Moves to the root of the challenge repository. |
| `git switch master` | Selects the required branch for `AFarinha/90DaysOfDevOps`. |
| `git add 2026/day-51/notes.md 2026/day-51/tasks.md 2026/day-51/day-51-pods.md 2026/day-51/nginx-pod.yaml 2026/day-51/busybox-pod.yaml 2026/day-51/team-pod.yaml 2026/day-51/test-pod.yaml` | Stages only the Day 51 documentation and manifests. |
| `git commit -m "Day 51 - Completed - Create and explore Kubernetes Pods"` | Creates the completion commit using the requested message format. |
| `git push origin master` | Pushes the Day 51 commit to the fork's `master` branch. |
