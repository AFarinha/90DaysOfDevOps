variable "region" {
  type    = string
  default = "ap-south-1"
}

variable "cluster_name" {
  type    = string
  default = "terraweek-eks"
}

variable "cluster_version" {
  type = string
}

variable "node_instance_type" {
  type    = string
  default = "t3.medium"
}

variable "node_desired_count" {
  type    = number
  default = 2
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "endpoint_allowed_cidrs" {
  type = list(string)
}
