# Day 67 Local Validation

| Command | Exit code |
| --- | --- |
| `terraform fmt -recursive` | 0 |
| `terraform init -backend=false -input=false -no-color` | 0 |
| `terraform validate -no-color` | 0 |

Installed provider selections: hashicorp/aws 5.100.0.... Provider selections/checksums are recorded in the dependency lock file.

terraform validate returned: `Success! The configuration is valid.`.


AWS execution is pending: STS could not locate credentials. No AWS resources were created.

## Executed local workspace checks

```text
[32m[1mSuccess![0m The configuration is valid.
[0m
[0m[32m[1mCreated and switched to workspace "dev"![0m[32m

You're now on a new, empty workspace. Workspaces isolate their state,
so if you run "terraform plan" Terraform will not see any existing state
for this configuration.[0m
dev: [
  "dev",
  "dev",
  "t2.micro",
  "10.0.0.0/16",
]
[0m[32m[1mCreated and switched to workspace "staging"![0m[32m

You're now on a new, empty workspace. Workspaces isolate their state,
so if you run "terraform plan" Terraform will not see any existing state
for this configuration.[0m
staging: [
  "staging",
  "staging",
  "t2.small",
  "10.1.0.0/16",
]
[0m[32m[1mCreated and switched to workspace "prod"![0m[32m

You're now on a new, empty workspace. Workspaces isolate their state,
so if you run "terraform plan" Terraform will not see any existing state
for this configuration.[0m
prod: [
  "prod",
  "prod",
  "t3.small",
  "10.2.0.0/16",
]
[0m[32mDeleted workspace "prod"![0m
[0m[32mDeleted workspace "staging"![0m
[0m[32mDeleted workspace "dev"![0m
* default
```

No apply ran. Empty exercise workspace metadata was deleted and default restored.

Generated .terraform provider/module cache was removed after validation. The dependency lock file is retained. Run init again before repeating validation. User-local installed tools and the shared provider cache are retained.
