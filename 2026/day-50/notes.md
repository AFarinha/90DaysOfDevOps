# Day 50 Notes - Kubernetes Architecture and Cluster Setup

## Summary

- Kubernetes orchestrates containers across one or more nodes and continuously reconciles the running state with the declared desired state.
- Google open-sourced Kubernetes in 2014, drawing on experience from its Borg cluster-management system. The name comes from the Greek word for helmsman or pilot; `K8s` abbreviates the eight letters between `K` and `s`.
- The control plane stores and coordinates cluster state, while node components run workloads and provide networking.
- `kubectl` communicates with the API server using connection and authentication details from a kubeconfig file.

## Local Setup

- Tool: kind, chosen because Docker was already available and kind runs Kubernetes nodes as Docker containers.
- kubectl: `v1.36.3`.
- kind: `v0.32.0`.
- Cluster: `devops-cluster` using Kubernetes `v1.36.1`.
- Context: `kind-devops-cluster`.
- Node: `devops-cluster-control-plane`, verified as `Ready` with containerd as its runtime.
- Lifecycle: the cluster was created, inspected, deleted, recreated, and verified again.

## Key Lessons

- The API server is the entry point for cluster operations; etcd stores cluster state.
- The scheduler assigns unscheduled Pods to nodes, and controllers drive the actual state toward the desired state.
- The kubelet manages Pods on a node, while kube-proxy and the cluster network support service and Pod communication.
- The default kubeconfig path is `~/.kube/config`. A kubeconfig contains clusters, credentials, contexts, and the selected current context.

## Failure Behaviour

- If the API server is unavailable, existing workloads can continue running, but clients and control-plane components cannot reliably read or change cluster state through the API.
- If a worker node fails, its Pods become unavailable. The control plane detects the failure and can create replacement Pods on healthy nodes when controllers manage those workloads and capacity is available.
