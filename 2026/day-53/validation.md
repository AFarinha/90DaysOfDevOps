# Day 53 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Validate app-deployment.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/web-app created (dry run)
```

## Validate app-deployment.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
deployment.apps/web-app created (server dry run)
```

## Apply app-deployment.yaml.

Exit code: 0

```text
deployment.apps/web-app created
```

## Validate clusterip-service.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
service/web-app-clusterip created (dry run)
```

## Validate clusterip-service.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
service/web-app-clusterip created (server dry run)
```

## Apply clusterip-service.yaml.

Exit code: 0

```text
service/web-app-clusterip created
```

## Validate nodeport-service.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
service/web-app-nodeport created (dry run)
```

## Validate nodeport-service.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
service/web-app-nodeport created (server dry run)
```

## Apply nodeport-service.yaml.

Exit code: 0

```text
service/web-app-nodeport created
```

## Validate loadbalancer-service.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
service/web-app-loadbalancer created (dry run)
```

## Validate loadbalancer-service.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
service/web-app-loadbalancer created (server dry run)
```

## Apply loadbalancer-service.yaml.

Exit code: 0

```text
service/web-app-loadbalancer created
```

## Wait for the controller rollout (180-second timeout).

Exit code: 0

```text
deployment "web-app" successfully rolled out
```

## Inspect Pod IPs, Service types and endpoints.

Exit code: 0

```text
NAME                       READY   STATUS    RESTARTS   AGE   IP            NODE                           NOMINATED NODE   READINESS GATES
web-app-5c44989c65-c2hnb   1/1     Running   0          10s   10.244.0.20   devops-cluster-control-plane   <none>           <none>
web-app-5c44989c65-gk887   1/1     Running   0          10s   10.244.0.18   devops-cluster-control-plane   <none>           <none>
web-app-5c44989c65-vq25g   1/1     Running   0          10s   10.244.0.19   devops-cluster-control-plane   <none>           <none>
NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE   SELECTOR
kubernetes             ClusterIP      10.96.0.1       <none>        443/TCP        56d   <none>
web-app-clusterip      ClusterIP      10.96.245.101   <none>        80/TCP         8s    app=web-app
web-app-loadbalancer   LoadBalancer   10.96.70.103    <pending>     80:30718/TCP   2s    app=web-app
web-app-nodeport       NodePort       10.96.11.76     <none>        80:30080/TCP   4s    app=web-app
NAME                      ADDRESSTYPE   PORTS   ENDPOINTS                             AGE
web-app-clusterip-mncvt   IPv4          80      10.244.0.19,10.244.0.18,10.244.0.20   9s
```

## Verify internal HTTP and short/full DNS; --rm cleans temporary client.

Exit code: 1

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
<title>Welcome to nginx!</title>
<h1>Welcome to nginx!</h1>
<title>Welcome to nginx!</title>
<h1>Welcome to nginx!</h1>
Address:	10.96.0.10:53
Address: 10.96.245.101
pod default/test-client terminated (Error)
```

## Use explicit FQDN and A record to avoid BusyBox search-suffix NXDOMAIN exit despite a valid answer.

Exit code: 0

```text
Server:		10.96.0.10
Address:	10.96.0.10:53

Name:	web-app-clusterip.default.svc.cluster.local
Address: 10.96.245.101

All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
pod "dns-test" deleted from default namespace
```

## Read node internal IP.

Exit code: 0

```text
172.18.0.2
```

## Verify NodePort from WSL.

Exit code: 0

```text
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

## Inspect pending external IP and allocated ClusterIP/NodePort.

Exit code: 0

```text
Name:                     web-app-loadbalancer
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=web-app
Type:                     LoadBalancer
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.96.70.103
IPs:                      10.96.70.103
Port:                     <unset>  80/TCP
TargetPort:               80/TCP
NodePort:                 <unset>  30718/TCP
Endpoints:                10.244.0.18:80,10.244.0.20:80,10.244.0.19:80
Session Affinity:         None
External Traffic Policy:  Cluster
Internal Traffic Policy:  Cluster
Events:                   <none>
```

## Remove Deployment and three Services. Deletes exercise resources; approval required.

Exit code: 0

```text
deployment.apps "web-app" deleted from default namespace
service "web-app-clusterip" deleted from default namespace
service "web-app-nodeport" deleted from default namespace
service "web-app-loadbalancer" deleted from default namespace
```

## Verify day 53 Services are gone.

Exit code: 0

```text
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   56d
```
