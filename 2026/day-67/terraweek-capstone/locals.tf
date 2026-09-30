locals {
  environment = terraform.workspace
  name_prefix = format("%s-%s", var.project_name, local.environment)
  common_tags = {
    Project     = var.project_name
    Environment = local.environment
    ManagedBy   = "Terraform"
    Workspace   = terraform.workspace
  }
}
