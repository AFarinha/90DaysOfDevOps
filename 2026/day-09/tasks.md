# Tasks - Day 09

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `sudo useradd -m tokyo` | Creates a Linux user, usually with a home directory when -m is used. |
| `sudo useradd -m berlin` | Creates a Linux user, usually with a home directory when -m is used. |
| `sudo useradd -m professor` | Creates a Linux user, usually with a home directory when -m is used. |
| `sudo passwd tokyo` | Sets or changes the password for the specified user. |
| `sudo passwd berlin` | Sets or changes the password for the specified user. |
| `sudo passwd professor` | Sets or changes the password for the specified user. |
| `grep -E 'tokyo\|berlin\|professor' /etc/passwd` | Searches text using the provided pattern. |
| `ls -ld /home/tokyo /home/berlin /home/professor` | Lists files, directories or metadata such as permissions and ownership. |
| `sudo groupadd developers` | Creates a Linux group. |
| `sudo groupadd admins` | Creates a Linux group. |
| `sudo usermod -aG developers tokyo` | Modifies user account settings, here adding users to groups. |
| `sudo usermod -aG developers,admins berlin` | Modifies user account settings, here adding users to groups. |
| `sudo usermod -aG admins professor` | Modifies user account settings, here adding users to groups. |
| `groups tokyo` | Shows group membership for the specified user. |
| `groups berlin` | Shows group membership for the specified user. |
| `groups professor` | Shows group membership for the specified user. |
| `sudo mkdir -p /opt/dev-project` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `sudo chgrp developers /opt/dev-project` | Changes group ownership for the target path. |
| `sudo chmod 775 /opt/dev-project` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `ls -ld /opt/dev-project` | Lists files, directories or metadata such as permissions and ownership. |
| `sudo useradd -m nairobi` | Creates a Linux user, usually with a home directory when -m is used. |
| `sudo groupadd project-team` | Creates a Linux group. |
| `sudo usermod -aG project-team nairobi` | Modifies user account settings, here adding users to groups. |
| `sudo usermod -aG project-team tokyo` | Modifies user account settings, here adding users to groups. |
| `sudo mkdir -p /opt/team-workspace` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `sudo chgrp project-team /opt/team-workspace` | Changes group ownership for the target path. |
| `sudo chmod 775 /opt/team-workspace` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
| `sudo -u nairobi touch /opt/team-workspace/nairobi-test.txt` | Runs this step as part of the day exercise; review the surrounding task before executing it. |
