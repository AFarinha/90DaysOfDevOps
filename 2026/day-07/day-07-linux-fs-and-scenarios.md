# Day 07 Linux FS and Scenarios

## File System Hierarchy

- `/`: root of the filesystem.
- `/home`: user home directories.
- `/root`: root user's home directory.
- `/etc`: system and service configuration.
- `/var/log`: log files used during troubleshooting.
- `/tmp`: temporary files.
- `/bin` and `/usr/bin`: command binaries.
- `/opt`: optional or third-party software.

## Scenario Practice

### Service Not Starting

```bash
systemctl status myapp
journalctl -u myapp -n 50
systemctl is-enabled myapp
systemctl list-units --type=service | grep myapp
```

### High CPU Usage

```bash
top
ps aux --sort=-%cpu | head -10
```

### Finding Service Logs

```bash
systemctl status docker
journalctl -u docker -n 50
journalctl -u docker -f
```

### File Permissions Issue

```bash
ls -l /home/user/backup.sh
chmod +x /home/user/backup.sh
ls -l /home/user/backup.sh
./backup.sh
```

