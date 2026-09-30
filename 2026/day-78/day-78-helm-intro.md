# Day 78 - Helm Basics and Release Management

## Concepts and source study

A chart is a versioned collection of resource templates and defaults. A release is an installed instance with a name and revision history. A repository distributes charts; values customize a release without modifying its templates. `Chart.yaml` describes the package, `values.yaml` supplies defaults, `templates/` renders resources and `charts/` holds dependencies. `version` is the chart version; `appVersion` describes the application and does not automatically select an image tag.

Studied `TrainWithShubham/AI-BankApp-DevOps` branch `feat/gitops` at commit `d37fe11f2e754fee6d5857cd19d183ba9fdf0c7d`. Its manifests include Namespace, ConfigMap, Secret, StorageClass/PVC, three Deployments/Services, HPA, Gateway and cert-manager resources. Helm makes image tags, resources and storage configurable across environments instead of manually editing each file. The Kind config preserves the three-node reference topology but uses an isolated name without its occupied host port mapping. Runtime testing reused the existing Kind cluster in a new `days71-80-lab` namespace; the existing cluster is never a cleanup target.

## Community charts and values

Installed MySQL from Bitnami chart 14.0.3 (appVersion 9.4.0) and NGINX Ingress from nginx-ingress chart 2.7.3 (controller 5.6.3). The NGINX controller reached Ready. Helm marking a release deployed does not alone prove that its workload is ready.

`mysql-values.yaml` sets database `bankappdb`, an existing credential Secret, primary requests/limits, a 5Gi standard-class volume and a metrics sidecar. ServiceMonitor creation is disabled because the cluster does not have the Prometheus Operator CRDs. `create-lab-secret.py` creates random lab credentials through stdin and preserves an existing Secret; no password is stored in the values file or printed in the output.

The default Bitnami image entered ImagePullBackOff. Public archived `bitnamilegacy` tags were checked and a lab-only retry was attempted; these archived images are not production recommendations. The archived images ran successfully: MySQL and its exporter reached 2/2 Ready and SQL returned bankappdb. A manual lab Pod replacement was needed to apply the changed StatefulSet template after its blocked rollout; PVC data was preserved. Final release readiness and the retry outcome are in `validation.md`.

## Management evidence

The first MySQL install created revision 1. Disabling metrics created revision 2; `helm rollback bankapp-mysql 1` created revision 3 with description Rollback to 1. Rollback creates another revision, rather than deleting history. This validates release-management operations, but does not prove a database connection while its image cannot run.

Raw manifests require coordinating Secret, PVC, Service and Deployment files. The chart packages those concerns and offers configuration plus revision history. Raw Kubernetes Deployments also support rollout undo; Helm extends revision management to a whole release, so the README's blanket claim of no raw-manifest rollback is too broad.

## Limits and cleanup

Public chart/image availability can differ from older README examples. The chart templates were inspected locally in the ignored cache. No database data was supplied by the user. Runtime results, SQL verification status and cleanup are recorded in `validation.md`.
