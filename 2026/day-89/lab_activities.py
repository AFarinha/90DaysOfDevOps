"""Scope upstream KubeHealer activities to this lab and remove duplicate scan results."""
from temporalio import activity
from activities.k8s_activities import scan_cluster as upstream_scan, execute_fix as upstream_fix
from models import Diagnosis

@activity.defn(name="scan_cluster")
async def scan_cluster(namespace: str):
    if namespace != "days89-lab":
        raise ValueError("Only days89-lab is allowed")
    issues = await upstream_scan(namespace)
    unique = {}
    for issue in issues:
        unique.setdefault((issue.namespace, issue.name), issue)
    return list(unique.values())

@activity.defn(name="execute_fix")
async def execute_fix(diagnosis: Diagnosis):
    if diagnosis.namespace != "days89-lab" or not diagnosis.pod_name.startswith(
            ("web-app-", "memory-app-", "config-app-")):
        raise ValueError("Fix outside lab fixtures is forbidden")
    if diagnosis.action == "patch_resources" and diagnosis.fix_details.get("memory") not in {"128Mi", "256Mi"}:
        raise ValueError("Lab memory fixes are limited to 128Mi or 256Mi")
    if diagnosis.action == "fix_image" and diagnosis.fix_details.get("image") not in {"nginx:latest", "nginx:alpine"}:
        raise ValueError("Only the known lab image correction is allowed")
    return await upstream_fix(diagnosis)
