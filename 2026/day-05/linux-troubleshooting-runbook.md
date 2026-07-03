# Linux Troubleshooting Runbook

## Target Service / Process

Target: `ssh` or another service available on the host.

## Snapshot: CPU and Memory

- `top`: inspect live CPU usage.
- `free -h`: check available memory and swap.

## Snapshot: Disk and IO

- `df -h`: check filesystem usage.
- `du -sh /var/log`: estimate log directory size.

## Snapshot: Network

- `ss -tulpn`: list listening ports.
- `ping -c 4 google.com`: test outbound reachability.

## Logs Reviewed

- `journalctl -u ssh -n 50`
- `tail -n 50 /var/log/syslog`

## Quick Findings

Record actual command output and 1-2 lines of interpretation for each check.

## If This Worsens

1. Increase log detail or collect more service-specific logs.
2. Check recent deployments or configuration changes.
3. Restart only after capturing enough evidence.

