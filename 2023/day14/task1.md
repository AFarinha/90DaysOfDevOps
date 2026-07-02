# Difference between List, Tuple and Set in Python

Python has different data structures to store multiple values. Three common data structures are List, Tuple and Set.

## List

A List is an ordered and mutable collection of items.

This means that the values keep their order, and we can add, remove or change items after the list is created.

A List also allows duplicate values.

Example:

```python id="okcrx1"
my_list = ["Docker", "Kubernetes", "Jenkins", "Docker"]
my_list.append("Terraform")

print(my_list)
```

Output:

```text id="wxvupc"
['Docker', 'Kubernetes', 'Jenkins', 'Docker', 'Terraform']
```

## Tuple

A Tuple is an ordered and immutable collection of items.

This means that the values keep their order, but we cannot add, remove or change items after the tuple is created.

A Tuple also allows duplicate values.

Example:

```python id="rz7hao"
my_tuple = ("Docker", "Kubernetes", "Jenkins", "Docker")

print(my_tuple)
```

Output:

```text id="puxrje"
('Docker', 'Kubernetes', 'Jenkins', 'Docker')
```

## Set

A Set is an unordered collection of unique items.

This means that the values do not keep a fixed order, and duplicate values are automatically removed.

A Set is mutable, so we can add or remove items.

Example:

```python id="0jh6ue"
my_set = {"Docker", "Kubernetes", "Jenkins", "Docker"}
my_set.add("Terraform")

print(my_set)
```

Output example:

```text id="62n972"
{'Docker', 'Kubernetes', 'Jenkins', 'Terraform'}
```

## Summary

| Data Structure | Ordered | Mutable | Allows Duplicates |
| -------------- | ------- | ------- | ----------------- |
| List           | Yes     | Yes     | Yes               |
| Tuple          | Yes     | No      | Yes               |
| Set            | No      | Yes     | No                |

In DevOps, these data structures can be useful when working with scripts, configuration values, server lists, package names, environments, logs or automation tasks.
