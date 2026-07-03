# Tasks - Day 08

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `ssh -i your-key.pem ubuntu@<your-instance-ip>` | Connects to the remote server over SSH. |
| `sudo apt update` | Updates package metadata or installs packages on Debian/Ubuntu systems. |
| `sudo apt install -y nginx` | Updates package metadata or installs packages on Debian/Ubuntu systems. |
| `sudo systemctl status nginx` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `curl -I http://localhost` | Makes an HTTP request or checks HTTP headers for the target URL. |
| `sudo tail -n 100 /var/log/nginx/access.log` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `sudo tail -n 100 /var/log/nginx/error.log` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `sudo sh -c 'tail -n 100 /var/log/nginx/access.log > /home/ubuntu/nginx-logs.txt'` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `scp -i your-key.pem ubuntu@<your-instance-ip>:~/nginx-logs.txt .` | Copies a file between local and remote machines over SSH. |
