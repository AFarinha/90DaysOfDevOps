# Day 18 - Task 2 Summary

In this task, I practiced how to pull and run a Docker image from a public repository, inspect the container, check logs, stop/start the container and remove it.

First, I added my Linux user to the Docker group so I could run Docker commands without using `sudo`.

```bash
sudo usermod -aG docker $USER
```

After that, I restarted the WSL instance and confirmed Docker was working with:

```bash
docker ps
```

Then I pulled the `nginx:alpine` image from Docker Hub:

```bash
docker pull nginx:alpine
```

To run the container, I used:

```bash
docker run -d --name task2-nginx -p 8080:80 nginx:alpine
```

This command starts an Nginx container in detached mode, names it `task2-nginx`, and maps port `8080` on my machine to port `80` inside the container.

To check if the container was running, I used:

```bash
docker ps
```

To inspect detailed information about the container, I used:

```bash
docker inspect task2-nginx
```

To check the exposed ports, I used:

```bash
docker inspect --format='{{json .NetworkSettings.Ports}}' task2-nginx
```

To view the running processes inside the container, I used:

```bash
docker top task2-nginx
```

To view the container logs, I used:

```bash
docker logs task2-nginx
```

To stop the container, I used:

```bash
docker stop task2-nginx
```

To start it again, I used:

```bash
docker start task2-nginx
```

Finally, when I finished the task, I stopped and removed the container:

```bash
docker stop task2-nginx
docker rm task2-nginx
```

This task helped me understand how to manage a Docker container lifecycle using basic Docker commands.
