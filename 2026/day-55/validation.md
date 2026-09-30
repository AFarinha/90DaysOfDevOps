# Day 55 Validation

Executed on 2026-09-30 against kind Kubernetes v1.36.1. Concise output and selected excerpts replace screenshots under the repository working agreements.

## Validate ephemeral-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/ephemeral created (dry run)
```

## Validate ephemeral-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/ephemeral created (server dry run)
```

## Apply ephemeral-pod.yaml.

Exit code: 0

```text
pod/ephemeral created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/ephemeral condition met
```

## Read first timestamp in emptyDir.

Exit code: 0

```text
Wed Sep 30 12:30:23 UTC 2026
```

## Remove ephemeral Pod and its emptyDir. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "ephemeral" deleted from default namespace
```

## Validate ephemeral-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/ephemeral created (dry run)
```

## Validate ephemeral-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/ephemeral created (server dry run)
```

## Apply ephemeral-pod.yaml.

Exit code: 0

```text
pod/ephemeral created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/ephemeral condition met
```

## Read recreated timestamp; previous emptyDir data is gone.

Exit code: 0

```text
Wed Sep 30 12:30:56 UTC 2026
```

## Validate pv.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
persistentvolume/day55-pv created (dry run)
```

## Validate pv.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
persistentvolume/day55-pv created (server dry run)
```

## Apply pv.yaml.

Exit code: 0

```text
persistentvolume/day55-pv created
```

## Verify static PV is Available.

Exit code: 0

```text
NAME       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
day55-pv   1Gi        RWO            Retain           Available                          <unset>                          0s
```

## Validate pvc.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
persistentvolumeclaim/static-data created (dry run)
```

## Validate pvc.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
persistentvolumeclaim/static-data created (server dry run)
```

## Apply pvc.yaml.

Exit code: 0

```text
persistentvolumeclaim/static-data created
```

## Verify static PVC bound to day55-pv.

Exit code: 0

```text
NAME       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                 STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
day55-pv   1Gi        RWO            Retain           Bound    default/static-data                  <unset>                          2s
NAME          STATUS   VOLUME     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
static-data   Bound    day55-pv   1Gi        RWO                           <unset>                 1s
```

## Validate persistent-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/persistent created (dry run)
```

## Validate persistent-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/persistent created (server dry run)
```

## Apply persistent-pod.yaml.

Exit code: 0

```text
pod/persistent created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/persistent condition met
```

## Read first persistent timestamp.

Exit code: 0

```text
Wed Sep 30 12:31:00 UTC 2026
```

## Delete Pod while retaining PVC. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "persistent" deleted from default namespace
```

## Validate persistent-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/persistent created (dry run)
```

## Validate persistent-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/persistent created (server dry run)
```

## Apply persistent-pod.yaml.

Exit code: 0

```text
pod/persistent created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/persistent condition met
```

## Verify timestamps from both Pods are retained.

Exit code: 0

```text
Wed Sep 30 12:31:00 UTC 2026
Wed Sep 30 12:31:34 UTC 2026
```

## Inspect provisioner, Delete reclaim policy and WaitForFirstConsumer binding.

Exit code: 0

```text
NAME                 PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
standard (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  56d
Name:            standard
IsDefaultClass:  Yes
Annotations:     kubectl.kubernetes.io/last-applied-configuration={"apiVersion":"storage.k8s.io/v1","kind":"StorageClass","metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"true"},"name":"standard"},"provisioner":"rancher.io/local-path","reclaimPolicy":"Delete","volumeBindingMode":"WaitForFirstConsumer"}
,storageclass.kubernetes.io/is-default-class=true
Provisioner:           rancher.io/local-path
Parameters:            <none>
AllowVolumeExpansion:  <unset>
MountOptions:          <none>
ReclaimPolicy:         Delete
VolumeBindingMode:     WaitForFirstConsumer
Events:                <none>
```

## Validate dynamic-pvc.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
persistentvolumeclaim/dynamic-data created (dry run)
```

## Validate dynamic-pvc.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
persistentvolumeclaim/dynamic-data created (server dry run)
```

## Apply dynamic-pvc.yaml.

Exit code: 0

```text
persistentvolumeclaim/dynamic-data created
```

## Observe Pending until a consumer is scheduled.

Exit code: 0

```text
NAME           STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
dynamic-data   Pending                                      standard       <unset>                 0s
```

## Validate dynamic-pod.yaml with client dry-run; do not persist resources.

Exit code: 0

```text
pod/dynamic created (dry run)
```

## Validate dynamic-pod.yaml with server dry-run; do not persist resources.

Exit code: 0

```text
pod/dynamic created (server dry run)
```

## Apply dynamic-pod.yaml.

Exit code: 0

```text
pod/dynamic created
```

## Wait for exercise Pods to become Ready (180-second timeout).

Exit code: 0

```text
pod/dynamic condition met
```

## Verify dynamically provisioned PV and stored data.

Exit code: 0

```text
Dynamic storage works
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                  STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
day55-pv                                   1Gi        RWO            Retain           Bound    default/static-data                   <unset>                          46s
pvc-0bd5f24e-115a-46d6-bfeb-d382137f507e   500Mi      RWO            Delete           Bound    default/dynamic-data   standard       <unset>                          3s
NAME           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
dynamic-data   Bound    pvc-0bd5f24e-115a-46d6-bfeb-d382137f507e   500Mi      RWO            standard       <unset>                 7s
static-data    Bound    day55-pv                                   1Gi        RWO                           <unset>                 45s
```

## Delete storage consumers first. Deletes exercise resources; approval required.

Exit code: 0

```text
pod "ephemeral" deleted from default namespace
pod "persistent" deleted from default namespace
pod "dynamic" deleted from default namespace
```

## Delete exercise claims and observe reclaim behavior. Deletes exercise resources; approval required.

Exit code: 0

```text
persistentvolumeclaim "static-data" deleted from default namespace
persistentvolumeclaim "dynamic-data" deleted from default namespace
```

## Inspect retained manual PV versus deleted dynamic PV.

Exit code: 0

```text
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS     CLAIM                  STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
day55-pv                                   1Gi        RWO            Retain           Released   default/static-data                   <unset>                          100s
pvc-0bd5f24e-115a-46d6-bfeb-d382137f507e   500Mi      RWO            Delete           Released   default/dynamic-data   standard       <unset>                          57s
```

## Delete retained PV object; hostPath data requires separate explicit cleanup. Deletes exercise resources; approval required.

Exit code: 0

```text
persistentvolume "day55-pv" deleted
```

## Verify resolved hostPath test file and its two recorded timestamps before removal.

Exit code: 0

```text
Wed Sep 30 12:31:00 UTC 2026
Wed Sep 30 12:31:34 UTC 2026
```

## Remove only verified test file and its empty directory from the kind node. Deletes exercise resources; approval required.

Exit code: 0

```text

```

## Verify hostPath removal and final absence of earlier exercise PVs; capstone PV may still exist.

Exit code: 0

```text
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                  STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
pvc-47b0fb8f-628a-4183-b83a-63641b314f52   1Gi        RWO            Delete           Bound    capstone/mysql-data-mysql-0            standard       <unset>                          13m
pvc-598d9449-a953-427f-9ad1-02d3036e79c4   10Gi       RWO            Delete           Bound    capstone-helm/wp-helm-wordpress        standard       <unset>                          74s
pvc-bab3f630-fab9-458a-9fd7-0b2855c5afb4   8Gi        RWO            Delete           Bound    capstone-helm/data-wp-helm-mariadb-0   standard       <unset>                          74s
```
