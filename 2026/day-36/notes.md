# Notes - Day 36

Summary: Dockerize a complete application end to end.

- The chosen app is a small Flask task API backed by Postgres.
- The app image uses a multi-stage Dockerfile and runs as a non-root user.
- Docker Compose defines the app, database, persistent volume, custom network and database healthcheck.
- Runtime configuration is externalized through environment variables.
- A Docker Hub-oriented Compose file is included for the "pull and run" verification flow.

