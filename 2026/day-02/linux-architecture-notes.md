# Linux Architecture Notes

## Core Components

- Kernel: the central layer that manages CPU, memory, disk, networking and processes.
- User space: where shells, commands, libraries, services and applications run.
- systemd: the first user-space process on many distributions; it manages units and services.

## Process States

- Running: the process is executing or ready to use CPU time.
- Sleeping: the process is waiting for I/O, a timer or another event.
- Stopped: the process was paused by a signal.
- Zombie: the process has exited, but its parent has not collected its status yet.

## Daily Commands

- `ps aux`: lists running processes.
- `top`: shows CPU and memory usage in real time.
- `systemctl status <service>`: checks the state of a service.
- `journalctl -u <service>`: reads logs for a systemd service.
- `free -h`: shows available memory.