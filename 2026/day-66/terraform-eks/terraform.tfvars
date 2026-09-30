region             = "ap-south-1"
cluster_name       = "terraweek-eks"
node_instance_type = "t3.medium"
node_desired_count = 2
vpc_cidr           = "10.0.0.0/16"
# Supply a supported cluster_version and your public IPv4 /32 at plan time.
