"""Create a private Grafana Secret without printing credentials."""
import json
import secrets
import subprocess

context = subprocess.run(["kubectl", "config", "current-context"], capture_output=True, text=True, check=True).stdout.strip()
if context != "kind-days81-90-lab" and "bankapp-eks" not in context:
    raise RuntimeError("Select the intended lab or bankapp-eks kubeconfig")
existing = subprocess.run(["kubectl", "get", "secret", "monitoring-grafana-admin",
                           "-n", "monitoring", "--ignore-not-found", "-o", "name"],
                          capture_output=True, text=True, check=True)
if existing.stdout.strip():
    print("Existing Secret preserved")
else:
    secret = {"apiVersion": "v1", "kind": "Secret",
              "metadata": {"name": "monitoring-grafana-admin", "namespace": "monitoring"},
              "stringData": {"admin-user": "admin", "admin-password": secrets.token_urlsafe(24)}}
    subprocess.run(["kubectl", "apply", "-f", "-"], input=json.dumps(secret), text=True, check=True)
