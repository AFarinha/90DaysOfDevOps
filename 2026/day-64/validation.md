# Day 64 Local Validation

| Command | Exit code |
| --- | --- |
| `terraform fmt -recursive` | 0 |
| `terraform init -backend=false -input=false -no-color` | 0 |
| `terraform validate -no-color` | 0 |

Installed provider selections: hashicorp/aws 5.100.0.... Provider selections/checksums are recorded in the dependency lock file.

terraform validate returned: `Success! The configuration is valid.`.


AWS execution is pending: STS could not locate credentials. No AWS resources were created.

Generated .terraform provider/module cache was removed after validation. The dependency lock file is retained. Run init again before repeating validation. User-local installed tools and the shared provider cache are retained.
