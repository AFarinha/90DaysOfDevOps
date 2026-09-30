# Day 56 - StatefulSets

## Stable identity for stateful workloads

Use Deployments for replaceable stateless replicas and StatefulSets when replicas need stable identity, ordered operations and individual storage. This Nginx exercise demonstrates those mechanics; StatefulSets do not themselves replicate database data or configure a database cluster.

| Feature | Deployment | StatefulSet in this exercise |
| --- | --- | --- |
| Names | Generated ReplicaSet and Pod suffixes | web-0, web-1, web-2 |
| Creation | Replicas can start concurrently | OrderedReady: ascending ordinals |
| Storage | Configured explicitly; no automatic per-replica claim | One PVC per ordinal through volumeClaimTemplates |
| Network | Usually reached through a shared Service | Stable per-Pod DNS under a headless Service |
| Scale-down | No application identity ordering | Highest ordinal terminates first |

Deleting a comparison Deployment Pod changed its generated name. Deleting web-0 recreated web-0 with the same stored Data-from-web-0 content.

## Service and claim templates

[headless-service.yaml](headless-service.yaml) sets clusterIP: None and selects app=web. [statefulset.yaml](statefulset.yaml) sets serviceName to web-headless, three nginx:1.25 replicas and a web-data volumeClaimTemplate requesting 100Mi from standard. Each claim mounts at /usr/share/nginx/html.

The claims were web-data-web-0, web-data-web-1 and web-data-web-2. DNS names web-0.web-headless.default.svc.cluster.local through web-2 resolved to 10.244.0.40, 10.244.0.43 and 10.244.0.45, respectively, matching Pod IPs at that moment. Stable DNS names persist across recreation, while IP addresses can change.

## Ordered scaling and retention

Scaling to five created web-3 and web-4 with separate PVCs. Scaling back to three terminated the higher ordinals and retained all five PVCs. An immediate rollout-status response can overlap with terminating Pods, so inspect actual Pod listings as well.

Deleting the StatefulSet and Service still left five claims. The manifests use default claim retention: Retain. StatefulSet PVC retention can be configured explicitly in newer Kubernetes; retention is not an unconditional rule for every StatefulSet.

## Validation and cleanup

Deployment comparison, headless Service and StatefulSet passed client and server dry-runs. Three Pod DNS checks and storage recovery succeeded. The comparison Deployment, StatefulSet, headless Service, temporary DNS client and all five exercise claims were removed. See [tasks.md](tasks.md) and [validation.md](validation.md).
