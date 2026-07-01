# Install Java
sudo apt update
sudo apt install fontconfig openjdk-21-jre -y
java -version

# Add Jenkins repository
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key

echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update

# Install Jenkins
sudo apt install jenkins -y

sudo systemctl start jenkins
sudo systemctl status jenkins


# http://localhost:8080

sudo systemctl stop jenkins