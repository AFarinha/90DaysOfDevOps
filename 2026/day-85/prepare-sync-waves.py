"""Generate reviewed sync-wave manifests from the reference, excluding plaintext Secrets."""
import argparse
from pathlib import Path
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
args = parser.parse_args()
target = Path(".runtime/waved-k8s")
target.mkdir(parents=True, exist_ok=True)
waves = {"Namespace": -2, "StorageClass": -2, "ConfigMap": -1,
         "PersistentVolumeClaim": 0, "Service": 0, "HorizontalPodAutoscaler": 2}
for source in sorted(args.source.glob("*.yml")):
    output = []
    for manifest in yaml.safe_load_all(source.read_text()):
        if not manifest or manifest["kind"] in {"Secret", "Gateway", "HTTPRoute", "GatewayClass",
                                                 "BackendTrafficPolicy", "ClusterIssuer"}:
            continue
        metadata = manifest.setdefault("metadata", {})
        wave = waves.get(manifest["kind"], 0)
        if manifest["kind"] == "Deployment" and metadata["name"] == "bankapp":
            wave = 1
        metadata.setdefault("annotations", {})["argocd.argoproj.io/sync-wave"] = str(wave)
        output.append(manifest)
    if output:
        (target / source.name).write_text(yaml.safe_dump_all(output, sort_keys=False))
print("Generated manifests in .runtime/waved-k8s; supply credentials privately")
