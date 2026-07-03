# Tasks - Day 07

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `ls -l /` | Lists files, directories or metadata such as permissions and ownership. |
| `ls -l /etc` | Lists files, directories or metadata such as permissions and ownership. |
| `ls -l /var/log` | Lists files, directories or metadata such as permissions and ownership. |
| `ls -la ~` | Lists files, directories or metadata such as permissions and ownership. |
| `du -sh /var/log/* 2>/dev/null \| sort -h \| tail -5` | Shows disk usage for files or directories. |
| `cat /etc/hostname` | Prints file contents to the terminal. |
| `systemctl status myapp` | Shows status, recent logs and health information for a systemd service. |
| `journalctl -u myapp -n 50` | Reads logs from journald, optionally filtered by service and line count. |
| `systemctl is-enabled myapp` | Checks whether a service is enabled to start at boot. |
| `ps aux --sort=-%cpu \| head -10` | Lists running processes with the requested format. |
| `journalctl -u docker -n 50` | Reads logs from journald, optionally filtered by service and line count. |
| `ls -l /home/user/backup.sh` | Lists files, directories or metadata such as permissions and ownership. |
| `chmod +x /home/user/backup.sh` | Changes file or directory permissions. |
