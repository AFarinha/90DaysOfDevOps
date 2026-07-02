import json

with open("services.json", "r") as file:
    data = json.load(file)

services = data["services"]

for provider, details in services.items():
    if provider != "debug":
        print(f"{provider} : {details['name']}")
