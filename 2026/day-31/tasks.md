# Tasks - Day 31

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-31/my-first-image` | Changes into the target directory before running the exercise commands. |
| `docker build -t my-ubuntu:v1 .` | Builds a Docker image from the current build context. |
| `docker run --rm my-ubuntu:v1` | Creates and starts a container from the specified image. |
| `cd ../instructions-demo` | Changes into the target directory before running the exercise commands. |
| `docker build -t dockerfile-instructions:v1 .` | Builds a Docker image from the current build context. |
| `docker run --rm -p 8081:8080 dockerfile-instructions:v1` | Creates and starts a container from the specified image. |
| `cd ../cmd-entrypoint/cmd` | Changes into the target directory before running the exercise commands. |
| `docker build -t cmd-demo:v1 .` | Builds a Docker image from the current build context. |
| `docker run --rm cmd-demo:v1` | Creates and starts a container from the specified image. |
| `docker run --rm cmd-demo:v1 echo custom command` | Creates and starts a container from the specified image. |
| `cd ../entrypoint` | Changes into the target directory before running the exercise commands. |
| `docker build -t entrypoint-demo:v1 .` | Builds a Docker image from the current build context. |
| `docker run --rm entrypoint-demo:v1 hello from entrypoint` | Creates and starts a container from the specified image. |
| `cd ../../web-app` | Changes into the target directory before running the exercise commands. |
| `docker build -t my-website:v1 .` | Builds a Docker image from the current build context. |
| `docker run --rm -d --name my-website -p 8080:80 my-website:v1` | Creates and starts a container from the specified image. |
