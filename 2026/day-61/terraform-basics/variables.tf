variable "region" {
  type    = string
  default = "ap-south-1"
}

variable "bucket_name" {
  type = string
}

variable "ami_id" {
  type = string
}

variable "instance_name" {
  type    = string
  default = "TerraWeek-Modified"
}
