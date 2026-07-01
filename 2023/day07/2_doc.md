# Installing Docker and Jenkins using Package Managers

A package manager is a tool used to install, update, remove and manage software packages in Linux.

On Ubuntu, the most common package manager is `apt`. On CentOS and other Red Hat based distributions, package managers like `yum` and `dnf` are commonly used.

## Installing Docker on Ubuntu

Docker can be installed on Ubuntu using the official Docker `apt` repository.

First, the old or conflicting Docker packages should be removed. Then the official Docker GPG key and repository are added to the system. After that, Docker can be installed using `apt`.

Example commands:

```bash
sudo apt update
sudo apt install ca-certificates curl -y
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

After installation, Docker can be started and checked with:

```bash
sudo systemctl start docker
systemctl status docker
sudo docker run hello-world
```

## Installing Jenkins on Ubuntu

Jenkins requires Java. On Ubuntu, Java can be installed first, and then Jenkins can be installed using the Jenkins `apt` repository.

Example commands:

```bash
sudo apt update
sudo apt install fontconfig openjdk-21-jre -y

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key

echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install jenkins -y
```

Jenkins can be started and checked with:

```bash
sudo systemctl start jenkins
systemctl status jenkins
```

## Installing Docker on CentOS

On CentOS, Docker can be installed using the Docker RPM repository with `dnf`.

Example commands:

```bash
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
sudo systemctl enable --now docker
sudo docker run hello-world
```

## Installing Jenkins on CentOS

On CentOS or other Red Hat based distributions, Jenkins can be installed through `yum`.

Example commands:

```bash
sudo wget -O /etc/yum.repos.d/jenkins.repo \
  https://pkg.jenkins.io/rpm-stable/jenkins.repo

sudo yum upgrade -y
sudo yum install fontconfig java-21-openjdk -y
sudo yum install jenkins -y
sudo systemctl daemon-reload
sudo systemctl enable jenkins
sudo systemctl start jenkins
systemctl status jenkins
```

## systemctl vs service

`systemctl` is used to manage services controlled by `systemd`. It is the modern way to start, stop, restart, enable and check services on most Linux distributions.

Example:

```bash
systemctl status docker
```

`service` is an older command. It can still be used on many systems, but on modern Linux systems, `systemctl` is usually preferred.

Example:

```bash
service docker status
```

Both commands can check service status, but `systemctl` provides more control and more detailed information when the system uses `systemd`.
