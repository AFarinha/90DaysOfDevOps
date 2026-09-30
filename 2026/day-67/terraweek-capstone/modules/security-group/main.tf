resource "aws_security_group" "web" {
  name_prefix = format("%s-", var.sg_name)
  vpc_id      = var.vpc_id
  dynamic "ingress" {
    for_each = toset(var.ingress_ports)
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = merge(var.tags, { Project = var.project_name, Environment = var.environment }, { Name = var.sg_name })
}
