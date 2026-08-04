# Day 50 Tasks - Kubernetes Architecture and Cluster Setup

Commands below assume Linux on `amd64`, Docker is running, and `~/.local/bin` is on `PATH` for the current shell.

## Install kubectl

| Command | What it does |
| --- | --- |
| `mkdir -p "$HOME/.local/bin"` | Creates a user-owned directory for executable files without requiring `sudo`. |
| `KUBECTL_VERSION="$(curl -fsSL https://dl.k8s.io/release/stable.txt)"` | Reads the current stable kubectl release identifier from the official Kubernetes download site. |
| `curl -fsSLo /tmp/kubectl "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"` | Downloads the Linux amd64 kubectl binary to a temporary path and fails on HTTP errors. |
| `curl -fsSLo /tmp/kubectl.sha256 "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl.sha256"` | Downloads the official SHA-256 checksum for that kubectl release. |
| `printf '%s  %s\n' "$(cat /tmp/kubectl.sha256)" /tmp/kubectl \| sha256sum --check` | Verifies that the downloaded kubectl binary matches the official checksum before installation. |
| `install -m 0755 /tmp/kubectl "$HOME/.local/bin/kubectl"` | Installs kubectl for the current user and marks it as executable. |
| `export PATH="$HOME/.local/bin:$PATH"` | Makes executables in `~/.local/bin` available by name in the current shell. |
| `kubectl version --client` | Prints the installed kubectl client version without requiring a cluster connection. |

## Install kind

| Command | What it does |
| --- | --- |
| `KIND_VERSION="v0.32.0"` | Selects the kind release used for this exercise. |
| `curl -fsSLo /tmp/kind-linux-amd64 "https://kind.sigs.k8s.io/dl/${KIND_VERSION}/kind-linux-amd64"` | Downloads the official kind binary for Linux amd64. |
| `curl -fsSLo /tmp/kind.sha256sum "https://github.com/kubernetes-sigs/kind/releases/download/${KIND_VERSION}/kind-linux-amd64.sha256sum"` | Downloads the checksum published with the selected kind release. |
| `(cd /tmp && sha256sum --check kind.sha256sum)` | Verifies the kind download from the directory expected by the checksum file. |
| `install -m 0755 /tmp/kind-linux-amd64 "$HOME/.local/bin/kind"` | Installs kind for the current user and marks it as executable. |
| `kind version` | Prints the installed kind version. |

## Create and Explore the Cluster

| Command | What it does |
| --- | --- |
| `docker version` | Confirms that both the Docker client and daemon are available before kind creates node containers. |
| `kind create cluster --name devops-cluster --wait 120s` | Creates a kind cluster named `devops-cluster`, writes its kubeconfig context, and waits up to two minutes for readiness. |
| `kind get clusters` | Lists clusters managed by kind and helps diagnose a missing cluster. |
| `kubectl cluster-info` | Shows the API server and core service endpoints for the current cluster. |
| `kubectl get nodes` | Lists cluster nodes and their readiness state. |
| `kubectl get nodes -o wide` | Lists nodes with additional details such as internal IP, OS, kernel, and container runtime. |
| `kubectl describe node devops-cluster-control-plane` | Shows detailed conditions, capacity, allocated resources, labels, and events for the kind node. |
| `kubectl get namespaces` | Lists all namespaces in the cluster. |
| `kubectl get pods -A` | Lists Pods across every namespace; `-A` means `--all-namespaces`. |
| `kubectl get pods -n kube-system` | Lists the Kubernetes system Pods in the `kube-system` namespace. |
| `kubectl get pods -n kube-system -o wide` | Shows system Pods together with their IP addresses and assigned nodes. |

## Practise the Cluster Lifecycle

| Command | What it does |
| --- | --- |
| `kind delete cluster --name devops-cluster` | Deletes the named kind cluster and removes its generated kubeconfig entries. |
| `kubectl config get-contexts` | Confirms which contexts remain after deletion or are available after recreation. |
| `kind create cluster --name devops-cluster --wait 120s` | Recreates the local cluster and waits until its control-plane node is ready. |
| `kubectl get nodes` | Confirms that the recreated node exists and reports `Ready`. |
| `kubectl config current-context` | Prints the context currently selected by kubectl. |
| `kubectl config get-contexts` | Lists configured contexts and marks the current one with an asterisk. |
| `kubectl config view` | Displays the merged kubeconfig while redacting sensitive certificate and key data by default. |
| `kubectl config view --minify` | Displays only the cluster, user, and context information associated with the current context. |

## Commit the Day 50 Work

Day 50 does not require a separate branch or changes to `github-actions-practice`, so these commands apply only to the `90DaysOfDevOps` repository on `master`.

| Command | What it does |
| --- | --- |
| `cd ~/git/90DaysOfDevOps` | Moves to the root of the parent challenge repository. |
| `git switch master` | Selects the repository's required `master` branch. |
| `git add 2026/day-50/notes.md 2026/day-50/tasks.md 2026/day-50/day-50-k8s-setup.md` | Stages only the Day 50 documentation created for the exercise. |
| `git commit -m "Day 50 - Completed - Set up a local Kubernetes cluster"` | Creates the Day 50 completion commit using the requested message format. |
| `git push origin master` | Pushes the new commit from the local `master` branch to the fork's `master` branch. |
