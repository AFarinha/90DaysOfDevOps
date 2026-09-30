# Day 66 Local Validation

| Command | Exit code |
| --- | --- |
| `terraform fmt -recursive` | 0 |
| `terraform init -backend=false -input=false -no-color` | 0 |
| `terraform validate -no-color` | 0 |

Installed provider selections: hashicorp/kubernetes 2.38.0..., hashicorp/aws 5.100.0..., hashicorp/tls 4.4.1..., hashicorp/time 0.14.2..., hashicorp/cloudinit 2.4.1..., hashicorp/null 3.3.2.... Provider selections/checksums are recorded in the dependency lock file.

terraform validate returned: `Success! The configuration is valid.`.


AWS execution is pending: STS could not locate credentials. No AWS resources were created.

## Kubernetes manifest validation

Client-side and server-side kubectl apply dry-runs both passed on existing context `kind-devops-cluster`. Deployment nginx-terraweek and Service nginx-service were not persisted. This validates the manifest against the local cluster, not an EKS deployment.

Generated .terraform provider/module cache was removed after validation. The dependency lock file is retained. Run init again before repeating validation. User-local installed tools and the shared provider cache are retained.
