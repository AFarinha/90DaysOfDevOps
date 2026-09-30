"""Real local HTTP routing and GitOps drift checks; no cloud result is claimed."""
import json
import os
from pathlib import Path
import subprocess
import time
import socket

BASE = Path(__file__).resolve().parent / ".runtime"
def run(*args):
    return subprocess.run(args, capture_output=True, text=True, timeout=30, check=True).stdout
def kube(*args):
    return run("kubectl", *args)
def object_(kind, name, namespace):
    return json.loads(kube("get", kind, name, "-n", namespace, "-o", "json"))
def wait(predicate, seconds=120):
    start = time.monotonic()
    while time.monotonic()-start < seconds:
        if predicate():
            return round(time.monotonic()-start, 1)
        time.sleep(1)
    raise TimeoutError("Condition not satisfied")
def replicas():
    return object_("deployment", "bankapp-local-bankapp", "bankapp-local")["spec"]["replicas"]

def port_ready(port):
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=1):
            return True
    except OSError:
        return False

if kube("config", "current-context").strip() != "kind-days81-90-lab":
    raise RuntimeError("Select the dedicated days81-90-lab kubeconfig")

class Results(list):
    def append(self, item):
        super().append(item)
        (BASE / "gitops-http-result.txt").write_text("\n".join(self)+"\n")
        print(item, flush=True)
out = Results()
for path in ["/actuator/health", "/login", "/actuator/prometheus"]:
    forward = subprocess.Popen(["kubectl", "port-forward", "svc/bankapp-local-bankapp-service",
                                "-n", "bankapp-local", "18084:8080"],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        wait(lambda: port_ready(18084), seconds=45)
        response = run("curl", "--fail", "--max-time", "15", "-s", "-o", str(BASE / "http-body.txt"),
                       "-w", "%{http_code}", "http://127.0.0.1:18084" + path)
        out.append(path + ": HTTP " + response)
        if path == "/actuator/health":
            body = json.loads((BASE / "http-body.txt").read_text())
            assert body["status"] == "UP", body
    finally:
        forward.terminate()
        forward.wait(timeout=10)

kube("scale", "deployment/bankapp-local-bankapp", "-n", "bankapp-local", "--replicas=2")
out.append("Scale 2 -> Git desired 1 restored after " + str(wait(lambda: replicas()==1)) + "s")
name = "bankapp-local-bankapp-config"
old_uid = object_("configmap", name, "bankapp-local")["metadata"]["uid"]
kube("delete", "configmap", name, "-n", "bankapp-local")
def config_recreated():
    try:
        return object_("configmap", name, "bankapp-local")["metadata"]["uid"] != old_uid
    except subprocess.CalledProcessError:
        return False
out.append("Deleted ConfigMap recreated after " + str(wait(config_recreated)) + "s")
expected_database = object_("configmap", name, "bankapp-local")["data"]["MYSQL_DATABASE"]
kube("patch", "configmap", name, "-n", "bankapp-local", "--type=merge",
     "-p", json.dumps({"data": {"DAY84_DRIFT_TEST": None, "MYSQL_DATABASE": "day84-drift"}}))
out.append("Manual database ConfigMap field restored after " +
           str(wait(lambda: object_("configmap", name, "bankapp-local")["data"]["MYSQL_DATABASE"] == expected_database)) + "s")
# Exercise manual synchronization without publishing invented Git history.
kube("patch", "application", "bankapp-local", "-n", "argocd", "--type=merge",
     "-p", json.dumps({"spec": {"syncPolicy": {"automated": None}}}))
kube("scale", "deployment/bankapp-local-bankapp", "-n", "bankapp-local", "--replicas=2")
time.sleep(15)
assert replicas() == 2, "Manual sync unexpectedly reverted drift"
out.append("Manual sync: replicas remained 2 for 15s with automation disabled")
kube("patch", "application", "bankapp-local", "-n", "argocd", "--type=merge",
     "-p", json.dumps({"operation": {"sync": {}}}))
out.append("Explicit manual sync restored replicas to 1 after " + str(wait(lambda: replicas()==1)) + "s")
kube("apply", "-f", str(BASE.parent / "local-application.yaml"))
# Test Envoy using the generated Service, without needing a Kind external IP.
services = json.loads(kube("get", "svc", "-n", "envoy-gateway-system", "-o", "json"))["items"]
envoy = next(s["metadata"]["name"] for s in services
             if s["metadata"].get("labels", {}).get("gateway.envoyproxy.io/owning-gateway-name") == "bankapp-local-gateway")
forward = subprocess.Popen(["kubectl", "port-forward", "svc/"+envoy, "-n", "envoy-gateway-system", "18082:80"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    wait(lambda: port_ready(18082), seconds=45)
    headers = run("curl", "--fail", "--max-time", "20", "-s", "-D", "-", "-o", "/dev/null",
                  "http://127.0.0.1:18082/login")
    assert "200" in headers.splitlines()[0], headers
    assert "BANKAPP_AFFINITY" in headers, headers
    out.append("Envoy /login: HTTP 200; BANKAPP_AFFINITY cookie present")
finally:
    forward.terminate()
    forward.wait(timeout=10)
print("\n".join(out))
(BASE / "gitops-http-result.txt").write_text("\n".join(out)+"\n")
