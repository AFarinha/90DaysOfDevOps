# security-group module

Inputs:

- vpc_id (string): required
- sg_name (string): required
- ingress_ports (list(number)): default [22, 80]
- tags (map(string)): default {}

Outputs: sg_id. The root supplies the AWS provider. Public TCP ingress is intended for a disposable lab; restrict SSH before use.

Additional required inputs: environment and project_name. These tags are enforced by the capstone child modules.
