locals {
  name_prefix = format("%s-%s", var.project_name, var.environment)
  common_tags = merge(var.extra_tags, {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  })
}
