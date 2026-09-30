# Day 59 - Helm

## Packages and releases

A chart packages Kubernetes templates and default values. A release is one installation of a chart with its own name, values and history. A repository indexes available charts; OCI registries are another distribution mechanism.

Helm v4.3.0 was installed in ~/.local/bin without sudo after verifying the official archive SHA256. The initial sha256sum command failed because the archive had a temporary filename different from the checksum entry; direct SHA256 comparison then succeeded. A first helm invocation also lacked ~/.local/bin in PATH; explicitly adding it resolved the issue.

The Bitnami repository search returned 144 charts. Nginx chart 25.2.1 declared app version 1.31.6. All installations used that chart version, although its upstream image tag was latest and remains mutable. This is a learning configuration, not a fully pinned production deployment.

## Installation, customization and rollback

my-nginx initially had one ready Pod and a LoadBalancer Service. nginx-cli used --set replicaCount=3 and --set service.type=NodePort. nginx-values used [custom-values.yaml](custom-values.yaml), and reached three ready replicas with a NodePort Service.

| Value | Purpose |
| --- | --- |
| replicaCount: 3 | Request three application replicas. |
| service.type: NodePort | Expose the application through node ports allocated by Kubernetes. |
| resources.requests: 100m CPU, 128Mi | Provide scheduling requests per container. |
| resources.limits: 250m CPU, 256Mi | Bound runtime CPU and memory. |

Upgrading my-nginx to five replicas produced revision two and 5/5 readiness. Rolling back to revision one restored one replica and created revision three. History preserves both upgrade and rollback; it does not overwrite revision two. Helm manages the release's whole collection of manifests, while a Deployment rollout changes its Pod template.

## Custom chart

The my-app directory was generated with helm create. Chart.yaml contains package metadata; values.yaml specifies three replicas and nginx:1.25; templates contain Go templates for the Deployment, Service, ServiceAccount and optional resources. _helpers.tpl centralizes names and labels. .Values.replicaCount reads user-overridable values, .Chart.Name reads chart metadata, and .Release.Name identifies the installation. Conditional templates include optional resources only when enabled.

helm lint passed and helm template rendered manifests accepted by client and server dry-runs. my-release installed with 3/3 ready replicas, then upgraded to 5/5. The generated HTTP connection test is recorded in validation.md.

## Cleanup and sources

Exercise releases are uninstalled after verification. The custom chart and required custom-values.yaml are retained as reproducible source deliverables rather than removed with the runtime resources; no downloaded chart archives, binaries or caches are committed. See [tasks.md](tasks.md), [validation.md](validation.md), [official Helm documentation](https://docs.helm.sh/) and [Bitnami charts](https://github.com/bitnami/charts).
