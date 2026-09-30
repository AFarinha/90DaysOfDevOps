"""Render a disposable MySQL Secret from environment variables, never from disk."""
import json
import os
import subprocess

secret = {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {"name": "mysql-secret", "namespace": "capstone"},
    "type": "Opaque",
    "stringData": {
        "MYSQL_DATABASE": "wordpress",
        "MYSQL_USER": "wordpress",
        "MYSQL_ROOT_PASSWORD": os.environ["MYSQL_ROOT_PASSWORD"],
        "MYSQL_PASSWORD": os.environ["MYSQL_PASSWORD"],
    },
}
payload = json.dumps(secret)
for mode in ("client", "server"):
    subprocess.run(
        ["kubectl", "apply", "--dry-run=" + mode, "-f", "-"],
        input=payload, text=True, check=True,
    )
subprocess.run(["kubectl", "apply", "-f", "-"], input=payload, text=True, check=True)
