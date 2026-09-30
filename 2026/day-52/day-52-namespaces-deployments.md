# Day 52 - Namespaces and Deployments

## Namespaces and isolation

Namespaces organize namespaced resources into environments such as dev and staging. The same resource name can exist in different namespaces. Namespaces alone do not isolate network traffic: use RBAC, quotas and NetworkPolicies for access, capacity and traffic controls. PVs and Nodes are cluster-scoped.

The cluster initially had eight kube-system Pods. After the separately authorized Metrics Server installation it had nine. Standalone nginx-dev and nginx-staging ran in their respective namespaces; the default Pod listing did not include them, while -A did.

## Deployment manifest

See [nginx-deployment.yaml](nginx-deployment.yaml). apiVersion apps/v1 and kind Deployment choose the controller API. metadata identifies nginx-deployment in dev. spec.replicas requests three copies. selector.matchLabels matches the Pod template labels app=nginx-deployment. template.spec declares the nginx container, nginx:1.24 image and port 80. A declared containerPort describes the port; it does not expose the workload externally.

A Deployment manages ReplicaSets, which maintain Pod counts. Deleting a managed Pod produced a replacement with a different name; deleting a standalone Pod leaves it absent. READY compares ready with desired replicas, UP-TO-DATE counts replicas using the latest template, and AVAILABLE counts replicas satisfying availability requirements.

## Scaling and revisions

Imperative scale changed replicas from three to five, then two. Extra Pods terminated on scale-down. Declaratively, edit spec.replicas and reapply the manifest; the committed initial manifest deliberately remains at three replicas. Reapplying it can overwrite imperative changes.

Changing the image to nginx:1.25 created rollout revision two. The rolling update completed and rollback restored nginx:1.24. Rollback changes the Pod template, not the manually scaled replica count. kubectl warned that rollout undo does not update the last-applied annotation; keep declarative source consistent before future applies.

The default RollingUpdate strategy permits a controlled overlap of old and new Pods. A successful rollout alone does not prove zero downtime: meaningful readiness probes and continuous traffic testing are needed for that claim.

## Evidence and cleanup

Client and server dry-runs passed. The Deployment reached 3/3, 5/5 and 2/2 ready replicas. All three new namespaces and their resources were deleted. Exact command results are in [validation.md](validation.md); the repeatable commands are in [tasks.md](tasks.md). Text evidence replaces screenshots under the working agreements.
