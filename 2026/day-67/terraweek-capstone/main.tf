module "vpc" {
  source             = "./modules/vpc"
  cidr               = var.vpc_cidr
  public_subnet_cidr = var.subnet_cidr
  environment        = local.environment
  project_name       = var.project_name
}
module "web_sg" {
  source        = "./modules/security-group"
  environment   = local.environment
  project_name  = var.project_name
  vpc_id        = module.vpc.vpc_id
  sg_name       = format("%s-sg", local.name_prefix)
  ingress_ports = var.ingress_ports
  tags          = local.common_tags
}
module "server" {
  source             = "./modules/ec2-instance"
  environment        = local.environment
  project_name       = var.project_name
  ami_id             = data.aws_ami.amazon_linux.id
  instance_type      = var.instance_type
  subnet_id          = module.vpc.subnet_id
  security_group_ids = [module.web_sg.sg_id]
  instance_name      = format("%s-server", local.name_prefix)
  tags               = local.common_tags
  depends_on         = [module.vpc]
}
resource "terraform_data" "workspace_guard" {
  lifecycle {
    precondition {
      condition     = terraform.workspace == var.environment
      error_message = "Select the workspace matching the environment tfvars file."
    }
  }
}
