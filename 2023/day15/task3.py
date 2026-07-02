import json
import yaml

with open("services.yaml", "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

with open("services.json", "w") as json_file:
    json.dump(yaml_data, json_file, indent=4)

print("YAML converted to JSON successfully.")
print(json.dumps(yaml_data, indent=4))
