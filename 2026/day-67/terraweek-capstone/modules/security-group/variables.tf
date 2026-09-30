variable "vpc_id" {
  type = string
}

variable "sg_name" {
  type = string
}

variable "ingress_ports" {
  type    = list(number)
  default = [22, 80]
}

variable "tags" {
  type    = map(string)
  default = {}
}

variable "environment" {
  type = string
}
variable "project_name" {
  type = string
}
