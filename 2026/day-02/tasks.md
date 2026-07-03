# Tasks - Day 02

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `ps aux \| head` | Lists running processes with the requested format. |
| `top` | Opens a live view of CPU, memory and process activity. |
| `systemctl status ssh` | Shows status, recent logs and health information for a systemd service. |
| `systemctl list-units --type=service --state=running` | Lists systemd units filtered by type or state. |
| `journalctl -u ssh -n 50` | Reads logs from journald, optionally filtered by service and line count. |
| `cd 2026/day-02` | Changes into the target directory before running the exercise commands. |
| `touch linux-architecture-notes.md` | Creates one or more empty files if they do not already exist. |
