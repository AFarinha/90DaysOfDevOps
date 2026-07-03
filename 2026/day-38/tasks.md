# Tasks - Day 38

Use these commands as a practical checklist for the day. Replace placeholders only if you customize the files.

## Commands

| Command | What it does |
|---|---|
| `cd 2026/day-38` | Changes into the Day 38 directory before working with the YAML files. |
| `cat person.yaml` | Prints the person YAML file so you can visually inspect key-value pairs and lists. |
| `cat server.yaml` | Prints the server YAML file so you can inspect nested objects and multi-line strings. |
| `python -c "import yaml, pathlib; [yaml.safe_load(pathlib.Path(p).read_text()) for p in ['person.yaml','server.yaml']]; print('YAML files are valid')"` | Validates both YAML files using Python and PyYAML when that package is installed. |
| `yamllint person.yaml server.yaml` | Validates both YAML files with yamllint if it is installed locally. |
| `python -c "from pathlib import Path; [print(p) for p in ['person.yaml','server.yaml'] if '\\t' in Path(p).read_text()]"` | Checks whether either YAML file contains tab characters. |

