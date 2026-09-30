# Day 70 Local Validation

All three local inventory names refer to the SAME Ubuntu WSL host. These checks do not prove remote SSH connectivity, three-server isolation, or remote package/service idempotency.

| Command | Exit code |
| --- | --- |
| `ansible-playbook -i inventory-local.ini --syntax-check conditional-demo.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check facts-demo.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check loops-demo.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check server-report.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check variables-demo.yml` | 0 |
| `ansible-playbook -i inventory-local.ini --syntax-check playbooks/site.yml` | 0 |
| `ansible-inventory -i inventory.ini --graph` | 0 |
| `ansible-playbook -i inventory-local.ini variables-demo.yml --tags inspect` | 2 |
| `ansible-playbook -i inventory-local.ini variables-demo.yml --tags inspect -e app_name=my-custom-app app_port=9090` | 2 |
| `ansible-playbook -i inventory-local.ini playbooks/site.yml --tags inspect` | 2 |
| `ansible-playbook -i inventory-local.ini playbooks/site.yml --tags inspect -e max_connections=3000` | 2 |
| `ansible-playbook -i inventory-local.ini conditional-demo.yml --tags inspect` | 2 |
| `ansible-playbook -i inventory-local.ini loops-demo.yml --tags inspect` | 2 |
| `ansible-playbook -i inventory-local.ini facts-demo.yml` | 0 |
| `ansible-playbook -i inventory-local.ini server-report.yml -e report_dir=/home/afarinha/git/90DaysOfDevOps/2026/day-70/ansible-practice/day70-report-jk61lmvq` | 0 |


## Corrected local inspections

The initial tagged runs attempted sudo during automatic fact gathering because the play uses become=true. No tasks modified the system. The read-only local reruns explicitly set ansible_become=false; the remote playbook privilege settings remain intact.

```text
$ ansible-playbook -i inventory-local.ini variables-demo.yml -e ansible_become=false --tags inspect

PLAY [Variable demo] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [db-server]
ok: [app-server]
ok: [web-server]

TASK [Print app details] *******************************************************
ok: [db-server] => {
    "msg": "Deploying terraweek-app on port 8080 to /opt/terraweek-app"
}
ok: [web-server] => {
    "msg": "Deploying terraweek-app on port 8080 to /opt/terraweek-app"
}
ok: [app-server] => {
    "msg": "Deploying terraweek-app on port 8080 to /opt/terraweek-app"
}

PLAY RECAP *********************************************************************
app-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db-server                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Exit code: 0
```

```text
$ ansible-playbook -i inventory-local.ini variables-demo.yml -e ansible_become=false --tags inspect -e app_name=my-custom-app app_port=9090

PLAY [Variable demo] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [app-server]
ok: [db-server]
ok: [web-server]

TASK [Print app details] *******************************************************
ok: [db-server] => {
    "msg": "Deploying my-custom-app on port 9090 to /opt/my-custom-app"
}
ok: [web-server] => {
    "msg": "Deploying my-custom-app on port 9090 to /opt/my-custom-app"
}
ok: [app-server] => {
    "msg": "Deploying my-custom-app on port 9090 to /opt/my-custom-app"
}

PLAY RECAP *********************************************************************
app-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db-server                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Exit code: 0
```

```text
$ ansible-playbook -i inventory-local.ini playbooks/site.yml -e ansible_become=false --tags inspect

PLAY [Apply common configuration] **********************************************

TASK [Gathering Facts] *********************************************************
ok: [app-server]
ok: [web-server]
ok: [db-server]

TASK [Show environment] ********************************************************
ok: [db-server] => {
    "msg": "Environment: development"
}
ok: [web-server] => {
    "msg": "Environment: development"
}
ok: [app-server] => {
    "msg": "Environment: development"
}

PLAY [Configure web servers] ***************************************************

TASK [Gathering Facts] *********************************************************
ok: [web-server]

TASK [Show web configuration] **************************************************
ok: [web-server] => {
    "msg": "HTTP port: 80, Max connections: 2000"
}

TASK [Show host message] *******************************************************
ok: [web-server] => {
    "msg": "This is the primary web server"
}

PLAY RECAP *********************************************************************
app-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db-server                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web-server                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Exit code: 0
```

```text
$ ansible-playbook -i inventory-local.ini playbooks/site.yml -e ansible_become=false --tags inspect -e max_connections=3000

PLAY [Apply common configuration] **********************************************

TASK [Gathering Facts] *********************************************************
ok: [web-server]
ok: [app-server]
ok: [db-server]

TASK [Show environment] ********************************************************
ok: [db-server] => {
    "msg": "Environment: development"
}
ok: [web-server] => {
    "msg": "Environment: development"
}
ok: [app-server] => {
    "msg": "Environment: development"
}

PLAY [Configure web servers] ***************************************************

TASK [Gathering Facts] *********************************************************
ok: [web-server]

TASK [Show web configuration] **************************************************
ok: [web-server] => {
    "msg": "HTTP port: 80, Max connections: 3000"
}

TASK [Show host message] *******************************************************
ok: [web-server] => {
    "msg": "This is the primary web server"
}

PLAY RECAP *********************************************************************
app-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db-server                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web-server                 : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Exit code: 0
```

```text
$ ansible-playbook -i inventory-local.ini conditional-demo.yml -e ansible_become=false --tags inspect

PLAY [Conditional tasks demo] **************************************************

TASK [Gathering Facts] *********************************************************
ok: [app-server]
ok: [db-server]
ok: [web-server]

TASK [Warn on low memory hosts] ************************************************
skipping: [db-server]
skipping: [web-server]
skipping: [app-server]

TASK [Run on Amazon Linux] *****************************************************
skipping: [db-server]
skipping: [web-server]
skipping: [app-server]

TASK [Run on Ubuntu] ***********************************************************
ok: [db-server] => {
    "msg": "Ubuntu host"
}
ok: [web-server] => {
    "msg": "Ubuntu host"
}
ok: [app-server] => {
    "msg": "Ubuntu host"
}

TASK [Run in production] *******************************************************
skipping: [db-server]
skipping: [web-server]
skipping: [app-server]

TASK [Multiple conditions] *****************************************************
skipping: [db-server]
ok: [web-server] => {
    "msg": "Web server with enough memory"
}
skipping: [app-server]

TASK [Either group] ************************************************************
skipping: [db-server]
ok: [web-server] => {
    "msg": "Web or app server"
}
ok: [app-server] => {
    "msg": "Web or app server"
}

PLAY RECAP *********************************************************************
app-server                 : ok=3    changed=0    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0
db-server                  : ok=2    changed=0    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
web-server                 : ok=4    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

Exit code: 0
```

```text
$ ansible-playbook -i inventory-local.ini loops-demo.yml -e ansible_become=false --tags inspect

PLAY [Loop demo] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [db-server]
ok: [app-server]
ok: [web-server]

TASK [Print user specification] ************************************************
ok: [db-server] => (item={'name': 'deploy', 'groups': 'sudo'}) => {
    "msg": "Requested user deploy in group sudo"
}
ok: [db-server] => (item={'name': 'monitor', 'groups': 'sudo'}) => {
    "msg": "Requested user monitor in group sudo"
}
ok: [web-server] => (item={'name': 'deploy', 'groups': 'sudo'}) => {
    "msg": "Requested user deploy in group sudo"
}
ok: [db-server] => (item={'name': 'appuser', 'groups': 'users'}) => {
    "msg": "Requested user appuser in group users"
}
ok: [web-server] => (item={'name': 'monitor', 'groups': 'sudo'}) => {
    "msg": "Requested user monitor in group sudo"
}
ok: [app-server] => (item={'name': 'deploy', 'groups': 'sudo'}) => {
    "msg": "Requested user deploy in group sudo"
}
ok: [web-server] => (item={'name': 'appuser', 'groups': 'users'}) => {
    "msg": "Requested user appuser in group users"
}
ok: [app-server] => (item={'name': 'monitor', 'groups': 'sudo'}) => {
    "msg": "Requested user monitor in group sudo"
}
ok: [app-server] => (item={'name': 'appuser', 'groups': 'users'}) => {
    "msg": "Requested user appuser in group users"
}

PLAY RECAP *********************************************************************
app-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db-server                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web-server                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Exit code: 0
```

## Executed local server report

The three aliases reported the same WSL machine. Temporary report files were removed after capture.

```text
Server: web-server
OS: Ubuntu 24.04
IP: 172.30.39.191
RAM: 15856MB
Disk: Filesystem     1024-blocks     Used Available Capacity Mounted on
/dev/sdd        1055762868 17894456 984164940       2% /
Memory:                total        used        free      shared  buff/cache   available
Mem:           15856        2018        6113          13        7979       13837
Swap:           4096           0        4095
Checked at: 2026-09-30T13:57:27Z
```
