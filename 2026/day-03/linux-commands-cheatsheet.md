# Linux Commands Cheat Sheet

## Processes

- `ps aux`: list all processes.
- `top`: live process and resource view.
- `pgrep <name>`: find process IDs by name.
- `kill <pid>`: send a signal to a process.
- `systemctl status <service>`: inspect a service.

## Filesystem

- `pwd`: print current directory.
- `ls -lah`: list files with details.
- `cd <dir>`: change directory.
- `touch <file>`: create an empty file.
- `mkdir -p <dir>`: create directories.
- `cp <src> <dst>`: copy files.
- `mv <src> <dst>`: move or rename.
- `rm <file>`: remove a file.
- `find <path> -name <pattern>`: search files.
- `du -sh <path>`: show directory size.
- `df -h`: show mounted filesystem usage.

## Logs

- `journalctl -u <service> -n 50`: last service logs.
- `tail -f <file>`: follow a log file.
- `grep -i error <file>`: search errors.

## Networking

- `ping -c 4 <host>`: check reachability.
- `ip addr show`: show network interfaces and IPs.
- `ss -tulpn`: list listening ports.
- `dig <domain>`: query DNS records.
- `curl -I <url>`: check HTTP response headers.

