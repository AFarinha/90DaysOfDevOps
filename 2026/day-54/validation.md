# Day 54 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Create plaintext config from literals.

Exit code: 0

```text
configmap/app-config created
```

## Verify configuration keys.

Exit code: 0

```text
[Selected excerpt; unrelated metadata and repetitive output omitted]
Name:         app-config
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
APP_DEBUG:
----
false

APP_ENV:
  APP_PORT: "8080"
kind: ConfigMap
metadata:
  creationTimestamp: "2026-09-30T12:31:42Z"
  name: app-config
  namespace: default
  resourceVersion: "80581"
  uid: 5a82862e-9da9-454c-bbe4-9fb86883f01b
```

## Create file-backed ConfigMap.

Exit code: 0

```text
configmap/nginx-config created
```

## Inspect Nginx configuration.

Exit code: 0

```text
apiVersion: v1
data:
  default.conf: |
    server {
        listen 80;
        location /health {
            default_type text/plain;
            return 200 "healthy\n";
        }
    }
kind: ConfigMap
metadata:
  creationTimestamp: "2026-09-30T12:31:43Z"
  name: nginx-config
  namespace: default
  resourceVersion: "80597"
  uid: bbb46230-47e9-44be-863b-0d0723c70999
```

## Validate config-env-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/config-env created (dry run)
```

## Validate config-env-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/config-env created (server dry run)
```

## Apply config-env-pod.yaml.

Exit code: 0

```text
pod/config-env created
```

## Validate nginx-config-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/config-nginx created (dry run)
```

## Validate nginx-config-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/config-nginx created (server dry run)
```

## Apply nginx-config-pod.yaml.

Exit code: 0

```text
pod/config-nginx created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/config-env condition met
pod/config-nginx condition met
```

## Verify environment injection and health response.

Exit code: 0

```text
production
false
8080
healthy
```

## Generate temporary password in memory and create Secret without printing it.

Exit code: 0

```text
secret/db-credentials created
```

## Validate secret-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/secret-consumer created (dry run)
```

## Validate secret-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/secret-consumer created (server dry run)
```

## Apply secret-pod.yaml.

Exit code: 0

```text
pod/secret-consumer created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/secret-consumer condition met
```

## Verify Secret env and plaintext mounted files.

Exit code: 0

```text
Secret env and plaintext files verified; password not printed
```

## Decode Secret in memory to verify encoding.

Exit code: 0

```text
Base64 decoding verified without printing credentials
```

## Create live configuration.

Exit code: 0

```text
configmap/live-config created
```

## Validate live-config-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/live-config-reader created (dry run)
```

## Validate live-config-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/live-config-reader created (server dry run)
```

## Apply live-config-pod.yaml.

Exit code: 0

```text
pod/live-config-reader created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/live-config-reader condition met
```

## Update message with JSON merge patch.

Exit code: 0

```text
configmap/live-config patched
```

## Wait up to 150 seconds for volume propagation; verify no restart.

Exit code: 0

```text
NAME                 READY   STATUS    RESTARTS   AGE
live-config-reader   1/1     Running   0          7s
hello
world
```

## Remove Pods, ConfigMaps and temporary Secret. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "config-env" deleted from default namespace
pod "config-nginx" deleted from default namespace
pod "secret-consumer" deleted from default namespace
pod "live-config-reader" deleted from default namespace
configmap "app-config" deleted from default namespace
configmap "nginx-config" deleted from default namespace
configmap "live-config" deleted from default namespace
secret "db-credentials" deleted from default namespace
```
