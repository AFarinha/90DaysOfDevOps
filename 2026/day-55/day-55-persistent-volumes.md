# Day 55 - Persistent Volumes and Claims

## Ephemeral versus persistent data

An emptyDir survives a container restart inside the same Pod, but is removed when that Pod is deleted. [ephemeral-pod.yaml](ephemeral-pod.yaml) wrote 12:30:23 UTC; the recreated Pod wrote 12:30:56 UTC instead. This demonstrated loss across Pod replacement.

A PersistentVolume (PV) represents cluster-wide storage. A namespaced PersistentVolumeClaim (PVC) requests capacity and access mode. A Pod references its claim through persistentVolumeClaim.claimName. Binding connects one claim to an appropriate PV.

## Static and dynamic provisioning

[pv.yaml](pv.yaml) defines day55-pv with 1Gi, ReadWriteOnce, Retain and hostPath /tmp/k8s-pv-data. [pvc.yaml](pvc.yaml) requests 500Mi, explicitly names that PV and sets storageClassName to an empty string to avoid dynamic provisioning. The PV progressed from Available to Bound and the PVC VOLUME column showed day55-pv.

[persistent-pod.yaml](persistent-pod.yaml) appends a timestamp at each Pod creation. After replacement, both 12:31:00 and 12:31:34 UTC entries remained. hostPath is suitable only for this single-node learning cluster: it is tied to a node and does not provide replicated storage.

[dynamic-pvc.yaml](dynamic-pvc.yaml) uses standard, the verified default StorageClass, and [dynamic-pod.yaml](dynamic-pod.yaml) consumes it. The provisioner is rancher.io/local-path, reclaim policy Delete and binding mode WaitForFirstConsumer. The claim was Pending before a consumer existed, then bound to a newly created PV. The Pod read Dynamic storage works.

## Access modes and reclamation

| Mode or policy | Meaning |
| --- | --- |
| ReadWriteOnce | Read-write mount by one node; multiple Pods on that node may share it. |
| ReadOnlyMany | Read-only mounts by multiple nodes, when supported. |
| ReadWriteMany | Read-write mounts by multiple nodes, when supported. |
| Retain | Preserve backing data after releasing a claim; manual reclamation is required. |
| Delete | Ask the provisioner to remove backing storage after the claim is deleted. |

Deleting claims first showed both PVs briefly Released: dynamic cleanup is asynchronous. The retained static PV object was removed explicitly. Deleting a hostPath PV object does not erase its files; their separate cleanup is recorded in validation.md.

## Validation

All six manifests passed client and server dry-runs. Both persistence cases and dynamic provisioning ran on the real cluster. See [tasks.md](tasks.md) and [validation.md](validation.md) for evidence and cleanup results.
