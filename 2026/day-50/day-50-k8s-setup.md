# Day 50 - Kubernetes Architecture and Cluster Setup

## Kubernetes Story

Docker runs and packages containers well, but it does not by itself coordinate large groups of containers across multiple machines. Kubernetes adds scheduling, service discovery, scaling, recovery, and continuous reconciliation of declared state. Google open-sourced Kubernetes in 2014 after drawing on lessons from its Borg system. The name comes from the Greek word for helmsman or pilot, and `K8s` is its common abbreviation.

## Architecture

```text
                       kubectl and other clients
                                  |
                                  v
+------------------------------------------------------------------+
| Control plane                                                    |
|                                                                  |
|  +----------------+       +-----------------------------------+   |
|  | kube-apiserver |<----->| etcd: persistent cluster state   |   |
|  +-------+--------+       +-----------------------------------+   |
|          ^                                                       |
|          | watches and updates API objects                       |
|  +-------+----------------+       +---------------------------+   |
|  | kube-scheduler         |       | kube-controller-manager   |   |
|  | selects a node for Pods|       | reconciles desired state  |   |
|  +------------------------+       +---------------------------+   |
+----------------------------------+-------------------------------+
                                   |
                                   v
+------------------------------------------------------------------+
| Worker node                                                      |
|                                                                  |
|  +-----------+   +------------+   +---------------------------+   |
|  | kubelet   |   | kube-proxy |   | container runtime         |   |
|  | runs Pods |   | networking |   | runs containers           |   |
|  +-----------+   +------------+   +---------------------------+   |
+------------------------------------------------------------------+
```

A production cluster normally separates control-plane and worker roles. This single-node kind cluster runs both roles in one Docker container, which is appropriate for local learning and testing.

## What Happens During `kubectl apply`

1. `kubectl` reads the manifest and kubeconfig, then sends the requested object to the API server.
2. The API server authenticates and authorizes the request, validates the object, and persists the desired state in etcd.
3. Controllers observe the new desired state and create or update the required dependent objects.
4. For a Pod without a node assignment, the scheduler selects a suitable node and records that binding through the API server.
5. The kubelet on the selected node observes the Pod, asks the container runtime to prepare and run its containers, and reports status through the API server.
6. Cluster networking and kube-proxy rules make the workload reachable where Services require it.

## Local Cluster Choice

I chose kind because Docker was already running on the machine. kind creates Kubernetes nodes as Docker containers, is quick to create and remove, and needs no additional virtual-machine driver.

Installed and verified versions:

```text
kubectl Client Version: v1.36.3
kind v0.32.0
Kubernetes node version: v1.36.1
```

## Verification

After creation, `kubectl get nodes -o wide` reported:

```text
NAME                           STATUS   ROLES           VERSION   CONTAINER-RUNTIME
devops-cluster-control-plane   Ready    control-plane   v1.36.1   containerd://2.3.1
```

The active context is `kind-devops-cluster`. The cluster was then deleted and recreated as requested, and the recreated control plane reached `Ready` after 17 seconds. Screenshots were intentionally omitted; the relevant command output is recorded as text.

## `kube-system` Pods

The first cluster inspection showed all of these Pods in `Running` state:

| Pod | Purpose |
| --- | --- |
| `kube-apiserver-*` | Exposes the Kubernetes API and coordinates access to cluster state. |
| `etcd-*` | Stores the authoritative configuration and state of the cluster. |
| `kube-scheduler-*` | Selects a node for each newly created, unscheduled Pod. |
| `kube-controller-manager-*` | Runs controllers that reconcile resources toward their desired state. |
| `kube-proxy-*` | Maintains node network rules used to implement Kubernetes Services. |
| `coredns-*` | Provides DNS-based service discovery inside the cluster. |
| `kindnet-*` | Provides the container network interface used for Pod networking in this kind cluster. |

The kubelet and container runtime are node processes rather than Pods listed in `kube-system`.

## Failure Scenarios

If the API server goes down, existing containers generally keep running because kubelet and the runtime do not immediately stop them. However, `kubectl` requests fail and controllers, schedulers, and kubelets cannot reliably coordinate new state until API access returns.

If a worker node goes down, the Pods on it stop serving traffic. The control plane marks the node unhealthy and controllers can replace managed Pods on other healthy nodes, subject to detection time, scheduling constraints, available capacity, and storage requirements. A single-node development cluster has nowhere else to reschedule those Pods.

## Kubeconfig

A kubeconfig tells `kubectl` which API server to contact, which credentials to use, and which cluster/user combination a context selects. The default file is `~/.kube/config`; kind added the `kind-devops-cluster` cluster, user, and context entries and selected that context during cluster creation.

## Official References

- [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/)
- [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
- [Install kubectl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/)
