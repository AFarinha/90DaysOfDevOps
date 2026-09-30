# VPC module

Inputs: cidr, public_subnet_cidr, environment, project_name. Creates VPC, public subnet, internet gateway, route table and association. Outputs: vpc_id and subnet_id. All resources with tag support receive project/environment tags.
