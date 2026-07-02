import json

cloud_services = {
    "aws": "ec2",
    "azure": "VM",
    "gcp": "compute engine"
}

with open("cloud_services.json", "w") as file:
    json.dump(cloud_services, file, indent=4)

print("JSON file created successfully.")
