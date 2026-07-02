# Day 19 - Docker Compose, Volumes and Networks Commands

## Start Docker Compose environment

```bash
docker compose up -d
```

This command starts all services defined in the `docker-compose.yaml` file in detached mode.

## Check running containers

```bash
docker compose ps
```

This command shows the status of the containers created by Docker Compose.

```bash
docker ps
```

This command shows all running Docker containers.

## Check all containers

```bash
docker ps -a
```

This command shows all containers, including stopped containers.

## Check logs

```bash
docker compose logs
```

This command shows logs from all services.

```bash
docker compose logs web
```

This command shows logs only from the `web` service.

```bash
docker compose logs db
```

This command shows logs only from the `db` service.

## Test web container

```bash
curl http://localhost:8081
```

This command tests if the web service is responding.

Port `8081` was used because port `8080` was already being used by Jenkins.

## Stop and remove Compose environment

```bash
docker compose down
```

This command stops and removes the containers and networks created by Docker Compose.

## Stop and remove Compose environment including volumes

```bash
docker compose down -v
```

This command also removes the volumes created by Docker Compose.

## Scale the web service

```bash
docker compose up -d --scale web=3
```

This command tries to run 3 replicas of the `web` service.

When using scaling, a fixed port like `8081:80` causes conflicts because multiple containers cannot use the same host port.

To scale correctly, the Compose file should use:

```yaml
ports:
  - "80"
```

This allows Docker to assign random available host ports.

## Check scaled containers

```bash
docker compose ps
```

Example result:

```text
day19-web-1   0.0.0.0:32768->80/tcp
day19-web-2   0.0.0.0:32769->80/tcp
day19-web-3   0.0.0.0:32770->80/tcp
```

## Test one scaled container

```bash
curl http://localhost:32768
```

The port number should be replaced with the port shown by `docker compose ps`.

## Summary

In this task, I used Docker Compose to start and manage a multi-container environment with a web container and a database container.

I practiced starting containers, checking their status, viewing logs, testing exposed ports, troubleshooting port conflicts, using Docker volumes, using Docker networks, scaling services, and stopping/removing the environment.
