---
title: "Boolean Values"
description: ""
summary: ""
showAuthor: true
date: 2026-05-09
featureimage: "featured.jpg"
tags: ["Python"]
---

Booleans are the simplest data type in Python: every expression either evaluates to `True` or `False`.

What you'll learn

- **What** Boolean values are
- **How** comparisons and `bool()` evaluate values
- **Common falsy values** and practical examples

> Tip: Booleans power program flow — `if`, `while`, list filtering, and more.

## Quick comparison examples

These comparisons return a Boolean value:

```python
a = 3
b = 5
print(a > b)   # False
print(a < b)   # True
print(a == 3)  # True
print(a != b)  # True
```

## Truthiness and `bool()`

Not every value is explicitly `True` or `False`; Python uses the concept of "truthiness":

- Values that are "empty" or zero are considered Falsey
- Non-empty values and non-zero numbers are Truthy

Examples:

```python
print(bool(""))          # False (empty string)
print(bool("Rahhhhhhh")) # True  (non-empty string)
print(bool(0))            # False
print(bool(22))           # True
print(bool([]))           # False (empty list)
print(bool([1, 2]))       # True
```

## Common falsy values

- `None`
- `False`
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]`, `()`, `{}` (empty containers)

## Using Booleans in `if` statements

```python
liam = 20
russell = 30

if russell > liam:
	print("Russell is greater than Liam")
else:
	print("Liam is greater or equal to Russell")
```

## Functions that return Booleans

You can write functions that return Boolean expressions directly:

```python
def is_even(n):
	return n % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False
```

## Useful built-ins

- `isinstance(obj, type)` — checks the object type
- `any(iterable)` — True if any element is truthy
- `all(iterable)` — True only if every element is truthy

```python
print(isinstance(3, int))       # True
print(any([0, "", 5]))         # True (5 is truthy)
print(all([1, 2, 3]))           # True
print(all([1, 0, 3]))           # False (0 is falsy)
```

## A short practical example: filtering a list

```python
items = [0, 1, "", "hello", None, [], [1]]
truthy = [x for x in items if x]
print(truthy)  # [1, 'hello', [1]]
```

## Final notes

Booleans are tiny but powerful — mastering truthiness helps you write clearer conditions and cleaner code. Try changing the example values above and re-running them to see how small changes affect outcomes.