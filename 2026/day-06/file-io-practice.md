# File IO Practice

## Commands

```bash
touch notes.txt
echo "Line 1: DevOps needs clear notes." > notes.txt
echo "Line 2: Logs and configs are text files." >> notes.txt
echo "Line 3: Practice makes commands faster." | tee -a notes.txt
cat notes.txt
head -n 2 notes.txt
tail -n 2 notes.txt
```

## What I Learned

- Redirection creates or appends content.
- `cat` reads the full file.
- `head` and `tail` are useful for checking only part of a file.

