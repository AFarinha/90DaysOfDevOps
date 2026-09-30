# Day 80 - Multi-Environment Helm and CI/CD

## Environments

The day includes a self-contained copy of the day-79 chart, versioned 0.2.0 with appVersion 1.1.0. The appVersion is package metadata; use a verified image commit tag for deployment rather than assuming a matching Docker tag exists.

| Setting | Dev | Staging | Production |
| --- | --- | --- | --- |
| App replicas | 1 fixed | HPA 2-3 | HPA 2-4 |
| Requested example image tag | latest | v1.2.0 | v1.2.0 |
| MySQL PVC | 2Gi standard | 5Gi gp3 | 20Gi gp3 |
| Ollama model | tinyllama | tinyllama | tinyllama |
| Ollama PVC | 5Gi standard | 10Gi gp3 | 10Gi gp3 |
| Gateway | disabled | disabled | enabled, example hostname |

The dev MySQL memory limit was raised from the README's 256Mi to 512Mi after a real OOMKilled event. The BankApp also has a startup probe after a measured 116-second boot exceeded its original liveness window.

All environments use an existing credential Secret; none contain a real password. Dev can be run on Kind. Staging/production require EBS CSI, metrics-server for HPA and Gateway API/controller prerequisites. The production hostname is a placeholder. Rendering these environments locally does not validate those external prerequisites or the example image tags.

Do not install environments that each claim the same cluster-scoped `gp3` StorageClass on one cluster; normally platform infrastructure should own it and set `storageClass.create=false` in workload charts. Upgrading an existing 5Gi PVC with the 2Gi dev override is rejected by Kubernetes; retain its current size or use a fresh namespace/release. Never delete real data merely to make an environment override fit.

## Hooks and tests

`db-ready-job.yaml` uses post-install and post-upgrade, with weight 0, a 180-second deadline and before-hook-creation/hook-succeeded cleanup policies. The README's pre-install hook would wait for the chart's own MySQL before Helm had created it, deadlocking first installation. The app's init container remains the readiness gate before app startup; the post hook validates the deployed database endpoint. This TCP check verifies a listener, not credentials or schema migrations. [Helm hook lifecycle](https://helm.sh/docs/topics/charts_hooks/).

The Helm test Pod requests the actual release-scoped app service and health path. The optional namespace quota is disabled by default and uses limits that can accommodate the provided component resources. Enable it only after reviewing all namespace consumers.

## Packaging and validation

Both 0.1.0 and 0.2.0 packages were generated in ignored runtime storage and a repository index was created locally. Archives and rendered manifests containing potential future secrets are not committed. `helm lint` and `helm template` passed for dev, staging and production. Counts before optional quota: dev 11, staging 13 and production 15 resources. Gateway manifests were rendered but not applied to a cluster lacking that API.

`helm upgrade --install` provides one entry point. `--wait` waits for readiness, `--timeout` bounds execution, and `--atomic` rolls back a failed upgrade. Helm diff is an optional plugin; it was not installed because introducing additional tools is unnecessary to this exercise's validation. The complete dev stack deployed successfully at revision 5, including MySQL and Ollama with tinyllama. The database readiness hook completed and `helm test` reported Succeeded. Existing PVC sizes were explicitly retained (MySQL 5Gi, Ollama 10Gi) on upgrade. HTTP health/login evidence and the failure history are in `validation.md`.

## GitOps integration

The upstream workflow builds/tests a Java app, publishes an image tagged with commit SHA, edits the raw deployment image and pushes the manifest change. `gitops-ci-step.yaml` is a reference fragment showing the corresponding Helm values update with `yq` and an environment-provided SHA, followed by a scoped commit. It is not installed as an active root workflow and no image publication is triggered.

`argocd-application.yaml` points at this chart and production values. ArgoCD renders Helm templates and reconciles their Kubernetes resources; it does not normally use Helm as a release manager or call `helm upgrade` for reconciliation. Values files provide reviewed environment changes, configurable components and drift comparison. Manual Helm management and ArgoCD ownership of the same resources should not compete.

| Approach | Suitable use |
| --- | --- |
| Raw manifests | Small, explicit single-environment deployments |
| Helm | Versioned parameterized packages and optional components |
| Kustomize | Structured overlays/patches on existing manifests |

Production secrets should come from an external secret controller, Vault or Sealed Secrets; base64 encoding does not protect them. Configure namespaces, CSI classes, quotas, TLS, backups and immutable images before enabling automated production synchronization.

## Scope

No ArgoCD controller was installed, no production/staging resources were deployed and no active CI workflow was changed. All local resources are disposable and cleanup is restricted to their namespace and explicitly named containers.
