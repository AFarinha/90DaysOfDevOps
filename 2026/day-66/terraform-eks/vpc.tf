data "aws_availability_zones" "available" {
  state = "available"
}
locals {
  common_tags = { Project = "TerraWeek", Environment = "dev", ManagedBy = "Terraform" }
}
module "vpc" {
  source                  = "terraform-aws-modules/vpc/aws"
  version                 = "5.21.0"
  name                    = format("%s-vpc", var.cluster_name)
  cidr                    = var.vpc_cidr
  azs                     = slice(data.aws_availability_zones.available.names, 0, 2)
  public_subnets          = [cidrsubnet(var.vpc_cidr, 8, 1), cidrsubnet(var.vpc_cidr, 8, 2)]
  private_subnets         = [cidrsubnet(var.vpc_cidr, 8, 3), cidrsubnet(var.vpc_cidr, 8, 4)]
  enable_nat_gateway      = true
  single_nat_gateway      = true
  public_subnet_tags      = { "kubernetes.io/role/elb" = "1" }
  private_subnet_tags     = { "kubernetes.io/role/internal-elb" = "1" }
  enable_dns_hostnames    = true
  map_public_ip_on_launch = true
  tags                    = local.common_tags
}
