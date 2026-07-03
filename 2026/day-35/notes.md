# Notes - Day 35

Summary: Build optimized Docker images with multi-stage builds and prepare them for Docker Hub.

- A single-stage image keeps the compiler and build tools in the final runtime image.
- A multi-stage image uses one stage to build the app and another minimal stage to run only the final artifact.
- Smaller images reduce attack surface, pull time and storage usage.
- Docker Hub requires tagging images as `username/repository:tag` before pushing.
- Good image hygiene includes specific base image tags, fewer layers and running as a non-root user.

