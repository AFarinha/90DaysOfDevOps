resource "aws_s3_bucket" "first" {
  bucket = var.bucket_name
}
resource "aws_instance" "main" {
  ami           = var.ami_id
  instance_type = "t2.micro"
  tags          = { Name = var.instance_name }
}
