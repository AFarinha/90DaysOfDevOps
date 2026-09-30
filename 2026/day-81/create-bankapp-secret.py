"""Create private lab credentials; never apply the upstream plaintext Secret."""
import json
import secrets
import subprocess

context = subprocess.run(["kubectl", "config", "current-context"], capture_output=True, text=True, check=True).stdout.strip()
if "bankapp-eks" not in context:
    raise RuntimeError("Select the intended bankapp-eks kubeconfig before creating cloud credentials")
namespace = {"apiVersion": "v1", "kind": "Namespace", "metadata": {"name": "bankapp"}}
subprocess.run(["kubectl", "apply", "-f", "-"], input=json.dumps(namespace), text=True, check=True)
existing = subprocess.run(["kubectl", "get", "secret", "bankapp-secret", "-n", "bankapp",
                           "--ignore-not-found", "-o", "name"], capture_output=True, text=True, check=True)
if existing.stdout.strip():
    print("Existing Secret preserved")
else:
    password = secrets.token_urlsafe(24)
    secret = {"apiVersion": "v1", "kind": "Secret",
              "metadata": {"name": "bankapp-secret", "namespace": "bankapp"},
              "stringData": {"MYSQL_ROOT_PASSWORD": password,
                             "MYSQL_USER": "root", "MYSQL_PASSWORD": password}}
    subprocess.run(["kubectl", "apply", "-f", "-"], input=json.dumps(secret), text=True, check=True)
