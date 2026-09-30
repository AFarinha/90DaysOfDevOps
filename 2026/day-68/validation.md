# Day 68 Local Validation

| Command | Exit code |
| --- | --- |
| `terraform fmt -recursive` | 0 |
| `terraform init -backend=false -input=false -no-color` | 0 |
| `terraform validate -no-color` | 0 |

Installed provider selections: hashicorp/aws 5.100.0.... Provider selections/checksums are recorded in the dependency lock file.

terraform validate returned: `Success! The configuration is valid.`.


AWS execution is pending: STS could not locate credentials. No AWS resources were created.

## Executed local Ansible checks

All aliases use the same WSL host. Twelve checks passed; this is not remote EC2 or SSH evidence. Temporary copied files were removed.

| Command | Exit code |
| --- | --- |
| `ansible-inventory -i inventory.ini --graph` | 0 |
| `ansible all -i inventory-local.ini -m ping` | 0 |
| `ansible application -i inventory-local.ini -m ping` | 0 |
| `ansible db -i inventory-local.ini -m ping` | 0 |
| `ansible all_servers -i inventory-local.ini -m ping` | 0 |
| `ansible web:app -i inventory-local.ini -m ping` | 0 |
| `ansible all:!db -i inventory-local.ini -m ping` | 0 |
| `ansible all -i inventory-local.ini -m command -a uptime` | 0 |
| `ansible web -i inventory-local.ini -m command -a free -h` | 0 |
| `ansible all -i inventory-local.ini -m command -a df -h /` | 0 |
| `ansible all -i inventory-local.ini -m copy -a src=hello.txt dest=/home/afarinha/git/90DaysOfDevOps/2026/day-68/ansible-practice/day68-final-5cidoet6/hello.txt` | 0 |
| `ansible all -i inventory-local.ini -m command -a cat /home/afarinha/git/90DaysOfDevOps/2026/day-68/ansible-practice/day68-final-5cidoet6/hello.txt` | 0 |

```text
$ ansible all -i inventory-local.ini -m ping
web-server | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
app-server | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
db-server | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

```text
$ ansible all -i inventory-local.ini -m command -a uptime
web-server | CHANGED | rc=0 >>
 15:17:04 up  5:03,  1 user,  load average: 0.98, 0.87, 0.97
app-server | CHANGED | rc=0 >>
 15:17:04 up  5:03,  1 user,  load average: 0.98, 0.87, 0.97
db-server | CHANGED | rc=0 >>
 15:17:04 up  5:03,  1 user,  load average: 0.98, 0.87, 0.97
```

```text
$ ansible web -i inventory-local.ini -m command -a free -h
web-server | CHANGED | rc=0 >>
               total        used        free      shared  buff/cache   available
Mem:            15Gi       1.9Gi       5.9Gi        13Mi       7.9Gi        13Gi
Swap:          4.0Gi       268Ki       4.0Gi
```

```text
$ ansible all -i inventory-local.ini -m command -a df -h /
web-server | CHANGED | rc=0 >>
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G   18G  939G   2% /
db-server | CHANGED | rc=0 >>
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G   18G  939G   2% /
app-server | CHANGED | rc=0 >>
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G   18G  939G   2% /
```

```text
$ ansible all -i inventory-local.ini -m command -a cat /home/afarinha/git/90DaysOfDevOps/2026/day-68/ansible-practice/day68-final-5cidoet6/hello.txt
app-server | CHANGED | rc=0 >>
Hello from Ansible
db-server | CHANGED | rc=0 >>
Hello from Ansible
web-server | CHANGED | rc=0 >>
Hello from Ansible
```


Generated .terraform provider/module cache was removed after validation. The dependency lock file is retained. Run init again before repeating validation. User-local installed tools and the shared provider cache are retained.
