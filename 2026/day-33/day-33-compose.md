# Day 33 Compose

## Compose Basics

`compose-basics/docker-compose.yml` runs one Nginx container with port mapping.

## WordPress and MySQL

`wordpress-mysql/docker-compose.yml` runs WordPress and MySQL on the same Compose network. MySQL uses a named volume for persistence.

## Useful Commands

- `docker compose up -d`
- `docker compose ps`
- `docker compose logs -f`
- `docker compose logs <service>`
- `docker compose stop`
- `docker compose down`
- `docker compose up --build`

