# Day 51 - Kubernetes Manifests and Pods

## Manifest Structure

| Field | Purpose |
| --- | --- |
| `apiVersion` | Selects the Kubernetes API version used to represent the resource. A core Pod uses `v1`. |
| `kind` | Identifies the resource type, which is `Pod` in these exercises. |
| `metadata` | Gives the resource its identity and organizational data, including its name and labels. |
| `spec` | Declares the desired state, including containers, images, commands, and exposed container ports. |

Kubernetes adds fields such as `status`, timestamps, UIDs, resource versions, defaults, and scheduling information after a resource is submitted.

## Nginx Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```

The container starts the Nginx server and declares port 80. Executing `curl localhost:80` inside the Pod returned the Nginx welcome page.

## BusyBox Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox-pod
  labels:
    app: busybox
    environment: dev
spec:
  containers:
    - name: busybox
      image: busybox:latest
      command: ["sh", "-c", "echo Hello from BusyBox && sleep 3600"]
```

BusyBox has no long-running server by default. The shell prints a message and then sleeps so that the container remains running. Its logs contained `Hello from BusyBox`.

## Third Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: team-pod
  labels:
    app: nginx
    environment: staging
    team: platform
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```

This Pod supplies the three requested labels. Filtering with `app=nginx` selected `nginx-pod` and `team-pod`; `team=platform` selected only `team-pod`.

## Imperative and Declarative Approaches

The declarative approach stores the desired state in files and uses `kubectl apply -f`. The manifest can be reviewed, versioned, repeated, and updated consistently. It is the preferred approach for maintained environments.

The imperative approach uses commands such as `kubectl run redis-pod --image=redis:latest`. It is useful for quick experiments and diagnostics, but the command itself is not a complete version-controlled record unless it is documented separately.

The live Redis YAML contained the same core fields as the hand-written files, but Kubernetes added defaults and runtime data such as:

- `namespace`, `uid`, `resourceVersion`, and `creationTimestamp`;
- `imagePullPolicy`, `dnsPolicy`, `restartPolicy`, and scheduler settings;
- service-account volumes and mounts;
- node assignment, Pod IP, conditions, container state, and full `status`.

## Generated Dry-Run Manifest

`test-pod.yaml` was generated without creating a Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: test-pod
  name: test-pod
spec:
  containers:
    - image: nginx
      name: test-pod
      resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```

It shares `apiVersion`, `kind`, `metadata`, `spec`, a container name, and an image with the hand-written manifest. Unlike `nginx-pod.yaml`, it adds generated defaults and an empty `status`, uses the `run` label, and does not declare `containerPort: 80`.

## Validation

All three hand-written manifests passed both client-side and server-side dry-runs. When `image` was removed from a temporary Pod manifest, the results differed:

```text
Client dry-run: pod/invalid-pod created (dry run)
Server dry-run: spec.containers[0].image: Required value
```

The client assembled the object without submitting it, while the API server enforced the required Pod field. Server-side validation is therefore the authoritative check when a cluster is available.

## Running Pods

The practical verification produced four ready Pods:

```text
NAME          READY   STATUS
busybox-pod   1/1     Running
nginx-pod     1/1     Running
redis-pod     1/1     Running
team-pod      1/1     Running
```

Screenshots were intentionally omitted; the relevant command results are recorded as text.

## Standalone Pod Deletion

A standalone Pod has no Deployment, ReplicaSet, or other controller maintaining its desired state. After `kubectl delete pod` or `kubectl delete -f`, the API object and its containers are removed and nothing recreates them. Production workloads normally use controllers so failed or deleted Pods can be replaced.
