# Day 10 — Dictionaries

## Goal

Learn how to store, read, update, and organize data with Python dictionaries.

A **dictionary** stores **key–value pairs**. Keys must be unique and hashable (for example, strings, integers, or tuples of immutable values).

```python
student = {
    "name": "Amina",
    "age": 19,
    "major": "IT"
}
print(student["name"])  # Amina
```

## 1. Create a dictionary

```python
person = {"name": "Ali", "city": "Almaty"}
empty = {}
```

## 2. Read values

```python
print(person["name"])            # Ali
print(person.get("country"))      # None (no KeyError)
print(person.get("country", "KZ")) # KZ
```

Use `dict[key]` when the key must exist. Use `dict.get(key, default)` when a key may be missing.

## 3. Add and update values

```python
person["age"] = 18       # Add
person["city"] = "Astana" # Update
```

## 4. Remove values

```python
age = person.pop("age")
del person["city"]
```

`pop()` returns the removed value. `del` removes a key without returning it.

## 5. Loop through a dictionary

```python
scores = {"math": 90, "python": 95}

for subject in scores:               # Keys
    print(subject)

for score in scores.values():        # Values
    print(score)

for subject, score in scores.items(): # Key–value pairs
    print(subject, score)
```

## 6. Useful operations

```python
print("math" in scores)  # True: checks keys
print(len(scores))       # 2
print(list(scores.keys()))
print(list(scores.values()))
```

## 7. Dictionary comprehension

```python
squares = {number: number ** 2 for number in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## 8. Nested dictionaries

```python
users = {
    "ali": {"age": 18, "active": True},
    "amina": {"age": 19, "active": False}
}
print(users["ali"]["age"])  # 18
```

## Common mistakes

- Looking up a missing key with `dict[key]` raises `KeyError`.
- Dictionary keys cannot be lists or other unhashable objects.
- Assigning the same key again **replaces** its previous value.
- `"value" in dictionary` checks **keys**, not values.

## Files

- [`examples.py`](examples.py) — working code examples.
- [`tasks.py`](tasks.py) — eight exercises to solve yourself.

## Run

From the repository root:

```bash
python3 Day10/examples.py
python3 Day10/tasks.py
```

## Checklist

- [ ] Create dictionaries and get values safely.
- [ ] Add, update, and delete pairs.
- [ ] Use `keys()`, `values()`, and `items()`.
- [ ] Write a dictionary comprehension.
- [ ] Solve the exercises in `tasks.py`.
