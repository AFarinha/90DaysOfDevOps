# Day 53 - Kubernetes Services

## Stable access to changing Pods

A Deployment maintains Pods whose names and IPs can change. A Service selects Pods by labels and gives clients a stable virtual IP and DNS name for the lifetime of that Service. Recreating the Service can allocate a different IP. [app-deployment.yaml](app-deployment.yaml) requests three nginx:1.25 replicas with app=web-app, which all three Service selectors match.

| Manifest | Type | Access and ports |
| --- | --- | --- |
| [clusterip-service.yaml](clusterip-service.yaml) | ClusterIP | Internal port 80 forwards to Pod port 80. |
| [nodeport-service.yaml](nodeport-service.yaml) | NodePort | Node port 30080 forwards through the Service to Pod port 80. |
| [loadbalancer-service.yaml](loadbalancer-service.yaml) | LoadBalancer | Requests an external provider; also allocates a ClusterIP and, by default, NodePort. |

port is the Service port; targetPort is the backend container port; nodePort is the external node listener. The local kind cluster has no LoadBalancer controller, so the external IP remained pending. NodePort access from WSL to 172.18.0.2:30080 returned the Nginx page.

## DNS and endpoints

CoreDNS resolves web-app-clusterip within default and web-app-clusterip.default.svc.cluster.local as its fully qualified name, assuming the standard cluster.local domain. Both HTTP names returned the welcome page. DNS returned 10.96.245.101, matching the Service ClusterIP. The three backend IPs were 10.244.0.18, 10.244.0.19 and 10.244.0.20.

EndpointSlices describe backend addresses, ports and readiness conditions. Inspect them with the kubernetes.io/service-name label selector. They replace the deprecated Endpoints API for this Kubernetes version. Services route traffic to ready backend addresses. Identical Nginx welcome pages confirm reachability but do not identify which replica answered or prove even traffic distribution.

BusyBox nslookup returned a valid short-name A answer but exited unsuccessfully after additional search-suffix NXDOMAIN responses. Repeating with an explicit FQDN and -type=A succeeded. This was a lookup-tool behavior, not an HTTP Service failure.

## Validation and cleanup

All four manifests passed client and server dry-runs. ClusterIP HTTP, FQDN HTTP, DNS and NodePort HTTP succeeded. LoadBalancer had ClusterIP 10.96.70.103 and NodePort 30718, with no external IP. The Deployment, three Services and temporary clients were removed. See [tasks.md](tasks.md) and [validation.md](validation.md).
