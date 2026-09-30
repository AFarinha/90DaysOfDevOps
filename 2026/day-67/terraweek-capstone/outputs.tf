output "environment" {
  value = local.environment
}
output "vpc_id" {
  value = module.vpc.vpc_id
}
output "instance_id" {
  value = module.server.instance_id
}
output "public_ip" {
  value = module.server.public_ip
}
