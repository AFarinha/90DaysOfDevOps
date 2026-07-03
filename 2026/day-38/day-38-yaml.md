# Day 38 YAML

## Files Created

- `person.yaml`
- `server.yaml`

## Lists in YAML

YAML supports two common list styles.

Block style:

```yaml
tools:
  - docker
  - kubernetes
```

Inline style:

```yaml
hobbies: [reading, running, homelab]
```

Block style is easier to read for longer lists. Inline style is compact for short lists.

## Nested Objects

Nested objects are represented through indentation. Two spaces per level is a common convention:

```yaml
database:
  credentials:
    user: appuser
    password: change-me
```

## Multi-line Strings

Use `|` when line breaks must be preserved, such as scripts:

```yaml
startup_script: |
  echo "start"
  echo "done"
```

Use `>` when the content should be folded into a paragraph:

```yaml
description: >
  This text is written across multiple lines
  but is read as one paragraph.
```

## Broken YAML Example

This block is broken:

```yaml
name: devops
tools:
- docker
  - kubernetes
```

The list indentation is inconsistent. Both list items should be aligned under `tools`:

```yaml
name: devops
tools:
  - docker
  - kubernetes
```

## What I Learned

- YAML structure depends on indentation.
- Tabs should not be used in YAML.
- Validation is a fast way to catch syntax mistakes before YAML reaches production tools.

