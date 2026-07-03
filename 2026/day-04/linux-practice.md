# Linux Practice

## Process Checks

- `ps aux | head`: lists processes and shows the first results.
- `top`: shows CPU and memory usage in real time.
- `pgrep ssh`: finds processes related to SSH.

## Service Checks

- `systemctl status ssh`: checks whether the SSH service is active.
- `systemctl list-units --type=service --state=running`: lists running services.

## Log Checks

- `journalctl -u ssh -n 50`: reads the last SSH service log lines.
- `tail -n 50 /var/log/syslog`: reads recent system events when the file exists.

## Mini Troubleshooting Flow

1. Confirm whether the process exists.
2. Validate the service state.
3. Read recent logs.
4. Only then decide whether to restart, change configuration or escalate.