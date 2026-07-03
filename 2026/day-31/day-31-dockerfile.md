# Day 31 Dockerfile

## Created Images

- `my-ubuntu:v1`
- `dockerfile-instructions:v1`
- `cmd-demo:v1`
- `entrypoint-demo:v1`
- `my-website:v1`

## CMD vs ENTRYPOINT

`CMD` is the default command and is easy to override. `ENTRYPOINT` is better when the image should always run the same executable and accept arguments.

## Build Optimization

Put slow, stable layers before frequently changing files so Docker can reuse cache.

