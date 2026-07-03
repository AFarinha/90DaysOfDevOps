# Notes - Day 34

Summary: Build a more production-like Docker Compose stack with an app, database and cache.

- The stack uses a custom web app image instead of only pre-built images.
- `depends_on` with `condition: service_healthy` makes the app wait for Postgres readiness.
- Restart policies define how Compose should recover failed services.
- Explicit networks, named volumes and labels make the setup easier to understand and operate.
- Scaling a service with host port mapping can break because replicas cannot all bind the same host port.

