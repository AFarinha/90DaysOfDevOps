"""Create random lab credentials privately, preserving an existing Secret."""
import json
import secrets
import subprocess

context = subprocess.run(["kubectl", "config", "current-context"], capture_output=True, text=True, check=True).stdout.strip()
if context != "kind-days81-90-lab":
    raise RuntimeError("Select the dedicated days81-90-lab kubeconfig")

def apply(manifest):
    subprocess.run(["kubectl", "apply", "-f", "-"],
                   input=json.dumps(manifest), text=True, check=True)

apply({"apiVersion": "v1", "kind": "Namespace", "metadata": {"name": "bankapp-local"}})
existing = subprocess.run(["kubectl", "get", "secret", "bankapp-credentials",
                           "-n", "bankapp-local", "--ignore-not-found", "-o", "name"],
                          capture_output=True, text=True, check=True)
if existing.stdout.strip():
    print("Existing credentials preserved")
else:
    password = secrets.token_urlsafe(24)
    apply({"apiVersion": "v1", "kind": "Secret",
           "metadata": {"name": "bankapp-credentials", "namespace": "bankapp-local"},
           "type": "Opaque",
           "stringData": {"MYSQL_ROOT_PASSWORD": password,
                         "MYSQL_USER": "root", "MYSQL_PASSWORD": password}})
