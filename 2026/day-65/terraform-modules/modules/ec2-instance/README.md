# ec2-instance module

Inputs:

- ami_id (string): required
- instance_type (string): default "t2.micro"
- subnet_id (string): required
- security_group_ids (list(string)): required
- instance_name (string): required
- tags (map(string)): default {}

Outputs: instance_id, public_ip, private_ip. The root supplies the AWS provider. Public TCP ingress is intended for a disposable lab; restrict SSH before use.
