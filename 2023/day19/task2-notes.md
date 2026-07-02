# Day 19 - Task 2: Docker Volumes and Named Volumes

In this task, I practiced Docker Volumes and Named Volumes.

Docker volumes are used to persist and share data between containers. A named volume is managed by Docker and can be mounted into one or more containers.

## 1. Create a named volume

```bash
docker volume create shared-data
```

List Docker volumes:

```bash
docker volume ls
```

## 2. Create the first container using the volume

```bash
docker run -dit --name container-one --mount source=shared-data,target=/shared alpine sh
```

## 3. Create the second container using the same volume

```bash
docker run -dit --name container-two --mount source=shared-data,target=/shared alpine sh
```

Both containers are now using the same Docker volume mounted at `/shared`.

## 4. Write data from the first container

```bash
docker exec container-one sh -c "echo 'Hello from container-one' > /shared/message.txt"
```

## 5. Read the same data from the second container

```bash
docker exec container-two cat /shared/message.txt
```

Expected output:

```text
Hello from container-one
```

## 6. Write more data from the second container

```bash
docker exec container-two sh -c "echo 'Hello from container-two' >> /shared/message.txt"
```

## 7. Read the file from the first container

```bash
docker exec container-one cat /shared/message.txt
```

Expected output:

```text
Hello from container-one
Hello from container-two
```

## 8. Verify files inside both containers

```bash
docker exec container-one ls -l /shared
docker exec container-two ls -l /shared
```

Both containers should show the same `message.txt` file because they are using the same volume.

## 9. Stop and remove the containers

```bash
docker stop container-one container-two
docker rm container-one container-two
```

## 10. Remove the volume

Before removing a volume, the containers using it must be removed.

```bash
docker stop 41feabd7f002 661ce133cca4
docker rm 41feabd7f002 661ce133cca4
docker volume rm shared-data
```

Confirm the volume was removed:

```bash
docker volume ls
```

## Summary

In this task, I created a Docker named volume called `shared-data`.

Then I created two Alpine containers and mounted the same volume inside both containers at `/shared`.

I wrote data from `container-one` and confirmed that `container-two` could read the same data. Then I wrote data from `container-two` and confirmed that `container-one` could also read it.

This shows that Docker volumes can be used to persist data and share files between multiple containers.
