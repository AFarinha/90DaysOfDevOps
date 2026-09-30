variable "region" {
  type    = string
  default = "ap-south-1"
}
variable "key_name" {
  type = string
}
variable "ssh_cidr" {
  type = string
  validation {
    condition     = can(cidrnetmask(var.ssh_cidr)) && endswith(var.ssh_cidr, "/32")
    error_message = "Use the control node public IPv4 address with /32."
  }
}
