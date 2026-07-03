# Shell Scripting Cheat Sheet

## Quick Reference

| Topic | Key Syntax | Example |
|-------|------------|---------|
| Variable | `VAR="value"` | `NAME="DevOps"` |
| Argument | `$1`, `$2` | `./script.sh arg1` |
| If | `if [ condition ]; then` | `if [ -f file ]; then` |
| For loop | `for i in list; do` | `for i in 1 2 3; do echo "$i"; done` |
| Function | `name() { ... }` | `greet() { echo "Hi"; }` |
| Grep | `grep pattern file` | `grep -i "error" app.log` |
| Awk | `awk '{print $1}' file` | `awk -F: '{print $1}' /etc/passwd` |
| Sed | `sed 's/old/new/g' file` | `sed 's/foo/bar/g' config.txt` |

## Basics

```bash
#!/bin/bash
chmod +x script.sh
./script.sh
bash script.sh
NAME="DevOps"
echo "$NAME"
read -p "Name: " NAME
echo "$0 $1 $# $@ $?"
```

## Operators and Conditionals

```bash
if [ -f "$1" ]; then
    echo "file exists"
elif [ -d "$1" ]; then
    echo "directory exists"
else
    echo "missing"
fi
```

- Strings: `=`, `!=`, `-z`, `-n`
- Integers: `-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`
- Files: `-f`, `-d`, `-e`, `-r`, `-w`, `-x`, `-s`

## Loops

```bash
for file in *.log; do
    echo "$file"
done

while read -r line; do
    echo "$line"
done < app.log
```

## Functions

```bash
greet() {
    local name="$1"
    echo "Hello $name"
}
greet "DevOps"
```

## Text Processing

```bash
grep -in "error" app.log
awk '{print $1}' app.log
sed 's/old/new/g' file.txt
cut -d: -f1 /etc/passwd
sort app.log | uniq -c | sort -rn
tail -f app.log | grep --line-buffered ERROR
```

## Useful One-Liners

```bash
find /var/log -name "*.gz" -mtime +30 -delete
find . -name "*.log" -exec wc -l {} \;
grep -R "old-value" . -n
systemctl is-active --quiet nginx && echo ok || echo failed
df -h | awk '$5+0 > 80 {print}'
```

## Error Handling and Debugging

```bash
set -euo pipefail
set -x
trap 'echo "cleanup"' EXIT
exit 1
```

