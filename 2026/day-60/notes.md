# Day 60 Notes

- Deployed WordPress and MySQL in capstone with ConfigMap, Secret, StatefulSet, PVC, probes, NodePort and HPA.
- Completed the HTTP installation wizard and created published post ID 5 through the WordPress API.
- The post survived both WordPress and MySQL Pod replacement; HTTP and database checks passed.
- Corrected overly short HTTP probes and deferred HPA until setup finished. Final HPA showed CPU 3%/50%, min 2, max 10.
- Bitnami WordPress chart 34.1.1 succeeded on retry after the initial readiness timeout. Selected resource counts: manual nine, Helm twelve.
- Removed both namespaces and their storage, restored default namespace, and retained only Metrics Server in the cluster.

See [day-60-capstone.md](day-60-capstone.md), [tasks.md](tasks.md) and [validation.md](validation.md). MySQL posts persist; manual WordPress uploads are not shared or persisted. Credentials and screenshots are not stored.
