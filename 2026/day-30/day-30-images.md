# Day 30 Images

## Docker Images

Compare image sizes for `ubuntu`, `alpine` and `nginx`. `alpine` is smaller because it is built as a minimal distribution.

## Image Layers

Layers are cached filesystem changes. Docker reuses unchanged layers to speed up builds and downloads.

## Container Lifecycle

Document state after each lifecycle command from `tasks.md`.

## Cleanup

Use `docker system df` before pruning so you understand what will be removed.

