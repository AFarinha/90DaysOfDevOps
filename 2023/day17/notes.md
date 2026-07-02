### Tests

afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17$ mkdir day17-docker-app
cd day17-docker-app


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ cat > app.py << EOF
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Day 17 Docker Project!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ cat app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Day 17 Docker Project!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


farinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ cat > requirements.txt << EOF
flask
EOF


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ cat > Dockerfile << EOF
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
EOF


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ cat > .dockerignore << EOF
__pycache__
*.pyc
.git
EOF


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ docker build -t day17-python-app .
[+] Building 9.2s (10/10) FINISHED                                                      docker:default
 => [internal] load build definition from Dockerfile                                              0.1s
 => => transferring dockerfile: 206B                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                               1.5s
 => [internal] load .dockerignore                                                                 0.1s
 => => transferring context: 63B                                                                  0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:423ed6ab25b1921a477529254bfeeabf5855151  2.4s
 => => resolve docker.io/library/python:3.12-slim@sha256:423ed6ab25b1921a477529254bfeeabf5855151  0.1s
 => => sha256:b32430367bf08f32c23778909985ac645d1794f0aeef670aa796a50c8751527d 248B / 248B        0.1s
 => => sha256:df79d931cd67092e2b8e48d8f6369922571efe4ee0f9af71636ce36600481492 12.11MB / 12.11MB  0.5s
 => => sha256:aff2d9f8dc87f4c10bbb7f438f3a325169379776bdfad5c49e4be5acc3c2f192 1.29MB / 1.29MB    0.7s
 => => sha256:e95a6c7ea7d49b37920899b023ecd0e32796c976c1748491f76cae53ba86d13a 29.79MB / 29.79MB  0.9s
 => => extracting sha256:e95a6c7ea7d49b37920899b023ecd0e32796c976c1748491f76cae53ba86d13a         0.7s
 => => extracting sha256:aff2d9f8dc87f4c10bbb7f438f3a325169379776bdfad5c49e4be5acc3c2f192         0.1s
 => => extracting sha256:df79d931cd67092e2b8e48d8f6369922571efe4ee0f9af71636ce36600481492         0.4s
 => => extracting sha256:b32430367bf08f32c23778909985ac645d1794f0aeef670aa796a50c8751527d         0.0s
 => [internal] load build context                                                                 0.1s
 => => transferring context: 276B                                                                 0.0s
 => [2/5] WORKDIR /app                                                                            0.6s
 => [3/5] COPY requirements.txt .                                                                 0.1s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                      2.9s
 => [5/5] COPY app.py .                                                                           0.1s
 => exporting to image                                                                            1.2s
 => => exporting layers                                                                           0.7s
 => => exporting manifest sha256:5b307ae5b1647434b0cc7ef3d688affbc9f1719adedee5239d82362508447c8  0.0s
 => => exporting config sha256:bfc533b11b3fed6c7518df2710340d20105987886e4194f5527232e3b6af6ef8   0.0s
 => => exporting attestation manifest sha256:b92349f44402f29385726d2db6d8404c03c25a0c55557626ca8  0.0s
 => => exporting manifest list sha256:6bb22f52265f70bb2589ca1aa0d29d9bcdbc8b176341dc6ff8361b286b  0.0s
 => => naming to docker.io/library/day17-python-app:latest                                        0.0s
 => => unpacking to docker.io/library/day17-python-app:latest                                     0.3s



afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ docker images
                                                                                   i Info →   U  In Use
IMAGE                     ID             DISK USAGE   CONTENT SIZE   EXTRA
day17-python-app:latest   6bb22f52265f        197MB         48.2MB


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ docker run -d --name day17-app -p 5000:5000 day17-python-app
6b3e3a6e00c229d1a20d248dfc2f1a9510bd5ea1e9b520b1e65730d74780af41


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ docker ps
CONTAINER ID   IMAGE              COMMAND           CREATED         STATUS         PORTS                                         NAMES
6b3e3a6e00c2   day17-python-app   "python app.py"   7 seconds ago   Up 6 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp   day17-app


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ curl http://localhost:5000
Hello from Day 17 Docker Project!


afarinha@polarising-p416:~/git/90DaysOfDevOps/2023/day17/day17-docker-app$ docker logs day17-app
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [02/Jul/2026 13:59:42] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [02/Jul/2026 13:59:42] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [02/Jul/2026 13:59:51] "GET / HTTP/1.1" 200 -

### Push the image to a public or private repository (e.g. Docker Hub )
    docker login
    docker tag day17-python-app <username>/day17-python-app:latest
    docker push <username>/day17-python-app:latest