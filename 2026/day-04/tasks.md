# Tasks - Day 04

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-04` | Changes into the target directory before running the exercise commands. |
| `ps aux \| head` | Lists running processes with the requested format. |
| `top` | Opens a live view of CPU, memory and process activity. |
| `pgrep ssh` | Finds process IDs matching the provided process name. |
| `systemctl status ssh` | Shows status, recent logs and health information for a systemd service. |
| `systemctl list-units --type=service --state=running \| head` | Lists systemd units filtered by type or state. |
| `journalctl -u ssh -n 50` | Reads logs from journald, optionally filtered by service and line count. |
| `tail -n 50 /var/log/syslog` | Shows the last lines of a file, commonly used for logs. |
| `touch linux-practice.md` | Creates one or more empty files if they do not already exist. |
