docker run hello-world
docker run -d --name day16-nginx -p 8080:80 nginx:alpine
docker ps
docker inspect day16-nginx
docker port day16-nginx
docker stats day16-nginx
docker top day16-nginx
docker save nginx:alpine -o nginx-alpine.tar
ls -lh nginx-alpine.tar
docker stop day16-nginx
docker rm day16-nginx
docker rmi nginx:alpine
docker load -i nginx-alpine.tar
docker images
docker stop day16-nginx
docker rm nginx:alpine
docker rmi nginx:alpine
docker ps -a --filter ancestor=hello-world:latest
docker rm a2ef0cdb7d3d
docker rm 9f74bb42e7b7
docker images
docker rmi hello-world:latest
history