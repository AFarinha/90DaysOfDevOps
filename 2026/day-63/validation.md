# Day 63 Local Validation

| Command | Exit code |
| --- | --- |
| `terraform fmt -recursive` | 0 |
| `terraform init -backend=false -input=false -no-color` | 0 |
| `terraform validate -no-color` | 0 |

Installed provider selections: hashicorp/aws 5.100.0.... Provider selections/checksums are recorded in the dependency lock file.

terraform validate returned: `Success! The configuration is valid.`.


AWS execution is pending: STS could not locate credentials. No AWS resources were created.

## Executed console expressions

```text
upper("terraweek") => "TERRAWEEK"
join("-", ["terra", "week", "2026"]) => "terra-week-2026"
format("arn:aws:s3:::%s", "my-bucket") => "arn:aws:s3:::my-bucket"
length(["a", "b", "c"]) => 3
lookup({dev = "t2.micro", prod = "t3.small"}, "dev") => "t2.micro"
toset(["a", "b", "a"]) => toset([
  "a",
  "b",
])
cidrsubnet("10.0.0.0/16", 8, 1) => "10.0.1.0/24"
TF_VAR_environment=staging, default tfvars => "dev"
-var-file=prod.tfvars => "prod"
-var=instance_type=t2.nano => "t2.nano"
```

Generated .terraform provider/module cache was removed after validation. The dependency lock file is retained. Run init again before repeating validation. User-local installed tools and the shared provider cache are retained.
