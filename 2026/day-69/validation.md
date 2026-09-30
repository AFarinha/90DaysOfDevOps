# Day 69 Local Validation

All three local inventory names refer to the SAME Ubuntu WSL host. These checks do not prove remote SSH connectivity, three-server isolation, or remote package/service idempotency.

| Command | Exit code |
| --- | --- |
| `ansible-playbook -i inventory-local.ini --syntax-check essential-modules.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check install-nginx.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check multi-play.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check nginx-config.yml` | 0 |
| `ansible-inventory -i inventory.ini --graph` | 0 |
| `ansible-playbook -i inventory-local.ini essential-modules.yml --tags diagnostics` | 2 |
| `ansible-playbook -i inventory-local.ini install-nginx.yml --list-hosts --list-tasks` | 0 |
| `ansible-playbook -i inventory-local.ini nginx-config.yml --list-hosts --list-tasks` | 0 |
| `ansible-playbook -i inventory-local.ini multi-play.yml --list-hosts --list-tasks` | 0 |


## Corrected local inspections

The initial tagged runs attempted sudo during automatic fact gathering because the play uses become=true. No tasks modified the system. The read-only local reruns explicitly set ansible_become=false; the remote playbook privilege settings remain intact.

```text
$ ansible-playbook -i inventory-local.ini essential-modules.yml -e ansible_become=false --tags diagnostics

PLAY [Practice essential modules on Ubuntu servers] ****************************

TASK [Gathering Facts] *********************************************************
ok: [web-server]
ok: [db-server]
ok: [app-server]

TASK [Read disk space] *********************************************************
ok: [app-server]
ok: [web-server]
ok: [db-server]

TASK [Print disk space] ********************************************************
ok: [db-server] => {
    "disk_output.stdout_lines": [
        "Filesystem      Size  Used Avail Use% Mounted on",
        "none            7.8G     0  7.8G   0% /usr/lib/modules/6.6.87.2-microsoft-standard-WSL2",
        "none            7.8G  4.0K  7.8G   1% /mnt/wsl",
        "drivers         475G  423G   52G  90% /usr/lib/wsl/drivers",
        "/dev/sdd       1007G   18G  939G   2% /",
        "none            7.8G   88K  7.8G   1% /mnt/wslg",
        "none            7.8G     0  7.8G   0% /usr/lib/wsl/lib",
        "rootfs          7.8G  2.7M  7.8G   1% /init",
        "none            7.8G  648K  7.8G   1% /run",
        "none            7.8G     0  7.8G   0% /run/lock",
        "none            7.8G   68K  7.8G   1% /run/shm",
        "none            7.8G   76K  7.8G   1% /mnt/wslg/versions.txt",
        "none            7.8G   76K  7.8G   1% /mnt/wslg/doc",
        "C:\\             475G  423G   52G  90% /mnt/c",
        "tmpfs           7.8G   16K  7.8G   1% /run/user/1000"
    ]
}
ok: [web-server] => {
    "disk_output.stdout_lines": [
        "Filesystem      Size  Used Avail Use% Mounted on",
        "none            7.8G     0  7.8G   0% /usr/lib/modules/6.6.87.2-microsoft-standard-WSL2",
        "none            7.8G  4.0K  7.8G   1% /mnt/wsl",
        "drivers         475G  423G   52G  90% /usr/lib/wsl/drivers",
        "/dev/sdd       1007G   18G  939G   2% /",
        "none            7.8G   88K  7.8G   1% /mnt/wslg",
        "none            7.8G     0  7.8G   0% /usr/lib/wsl/lib",
        "rootfs          7.8G  2.7M  7.8G   1% /init",
        "none            7.8G  648K  7.8G   1% /run",
        "none            7.8G     0  7.8G   0% /run/lock",
        "none            7.8G   68K  7.8G   1% /run/shm",
        "none            7.8G   76K  7.8G   1% /mnt/wslg/versions.txt",
        "none            7.8G   76K  7.8G   1% /mnt/wslg/doc",
        "C:\\             475G  423G   52G  90% /mnt/c",
        "tmpfs           7.8G   16K  7.8G   1% /run/user/1000"
    ]
}
ok: [app-server] => {
    "disk_output.stdout_lines": [
        "Filesystem      Size  Used Avail Use% Mounted on",
        "none            7.8G     0  7.8G   0% /usr/lib/modules/6.6.87.2-microsoft-standard-WSL2",
        "none            7.8G  4.0K  7.8G   1% /mnt/wsl",
        "drivers         475G  423G   52G  90% /usr/lib/wsl/drivers",
        "/dev/sdd       1007G   18G  939G   2% /",
        "none            7.8G   88K  7.8G   1% /mnt/wslg",
        "none            7.8G     0  7.8G   0% /usr/lib/wsl/lib",
        "rootfs          7.8G  2.7M  7.8G   1% /init",
        "none            7.8G  648K  7.8G   1% /run",
        "none            7.8G     0  7.8G   0% /run/lock",
        "none            7.8G   68K  7.8G   1% /run/shm",
        "none            7.8G   76K  7.8G   1% /mnt/wslg/versions.txt",
        "none            7.8G   76K  7.8G   1% /mnt/wslg/doc",
        "C:\\             475G  423G   52G  90% /mnt/c",
        "tmpfs           7.8G   16K  7.8G   1% /run/user/1000"
    ]
}

TASK [Count processes using a pipeline] ****************************************
ok: [app-server]
ok: [web-server]
ok: [db-server]

TASK [Print process count] *****************************************************
ok: [db-server] => {
    "msg": "Total processes: 92"
}
ok: [web-server] => {
    "msg": "Total processes: 92"
}
ok: [app-server] => {
    "msg": "Total processes: 95"
}

PLAY RECAP *********************************************************************
app-server                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db-server                  : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web-server                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Exit code: 0
```
