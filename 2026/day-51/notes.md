# Day 51 Notes - Kubernetes Manifests and Pods

## Summary

- A Kubernetes manifest declares a resource through `apiVersion`, `kind`, `metadata`, and `spec`.
- A Pod is the smallest deployable Kubernetes unit and can contain one or more containers that share networking and storage.
- Declarative commands apply version-controlled YAML, while imperative commands create or change resources directly from the command line.
- Labels organize resources and allow `kubectl` and controllers to select matching objects.

## Practical Results

- Created `nginx-pod`, `busybox-pod`, and `team-pod` from hand-written manifests.
- Created `redis-pod` imperatively with `kubectl run`.
- All four Pods reached `Running` with `1/1` containers ready.
- `curl localhost:80` inside `nginx-pod` returned the Nginx welcome page.
- `kubectl logs busybox-pod` returned `Hello from BusyBox`.
- Filters for `app=nginx`, `environment=dev`, and `team=platform` selected the expected Pods.
- Added and removed `environment=production` on `nginx-pod`.

## Validation Lessons

- Client and server dry-runs accepted all three valid manifests.
- A client dry-run accepted a Pod container without an `image`, but server-side validation rejected it with `spec.containers[0].image: Required value`.
- Dry-run generation provides a useful starting point, but generated YAML still needs review and customization.
- Deleting a standalone Pod removes it permanently because no controller exists to recreate it.
