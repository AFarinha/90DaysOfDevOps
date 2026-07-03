# Tasks - Day 13

Use these commands as a practical checklist for the day. Replace placeholders such as `<...>` before running them.

## Commands

| Command | What it does |
|---|---|
| `sudo -i` | Starts a root shell for administrative storage commands. |
| `lsblk` | Lists block devices and their mount relationships. |
| `pvs` | Shows LVM pvs information. |
| `vgs` | Shows LVM vgs information. |
| `lvs` | Shows LVM lvs information. |
| `df -h` | Shows filesystem disk usage. |
| `dd if=/dev/zero of=/tmp/disk1.img bs=1M count=1024` | Creates a virtual disk image for LVM practice. |
| `losetup -fP /tmp/disk1.img` | Creates or lists loop devices backed by disk image files. |
| `losetup -a` | Creates or lists loop devices backed by disk image files. |
| `pvcreate /dev/loop0` | Initializes a block device as an LVM physical volume. |
| `vgcreate devops-vg /dev/loop0` | Creates an LVM volume group from a physical volume. |
| `lvcreate -L 500M -n app-data devops-vg` | Creates an LVM logical volume. |
| `mkfs.ext4 /dev/devops-vg/app-data` | Formats the target device with a filesystem. |
| `mkdir -p /mnt/app-data` | Creates the requested directory path. |
| `mount /dev/devops-vg/app-data /mnt/app-data` | Mounts a filesystem at the target mount point. |
| `df -h /mnt/app-data` | Shows filesystem disk usage. |
| `lvextend -L +200M /dev/devops-vg/app-data` | Extends the size of an LVM logical volume. |
| `resize2fs /dev/devops-vg/app-data` | Expands an ext filesystem after the logical volume grows. |
