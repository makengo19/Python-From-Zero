# Day 08 — Python Dictionaries

A dictionary stores **key–value pairs**. Use it when you want to look up a value by a name or ID. For example, a student dictionary can map the key `"name"` to `"Aruzhan"`.

## Create a dictionary

```python
student = {"name": "Aruzhan", "score": 85}
empty_dictionary = {}
```

Keys are unique. Strings, numbers, and tuples of hashable items can be keys. Lists, sets, and dictionaries cannot be keys. Values can be any type, and multiple keys can have the same value.

The empty literal `{}` creates a dictionary. Use `set()` to create an empty set.

## Read and check values

```python
print(student["name"])  # Aruzhan
print(student.get("city", "Unknown"))  # Unknown
print("score" in student)  # True
```

Square brackets raise `KeyError` if the key is missing. Use `get()` when a key may be absent. It returns `None` by default or the fallback you provide. The `in` operator checks keys.

## Add, update, and remove entries

```python
student["city"] = "Almaty"  # Adds a key
student["score"] = 90  # Updates an existing key
city = student.pop("city")  # Removes the key and returns its value
```

Assigning to an existing key replaces its value. Use `pop(key, fallback)` to handle a missing key, or `del student["score"]` to remove a key you know exists.

## Loop through a dictionary

```python
for key, value in student.items():
    print(key, value)
```

Iterating over a dictionary directly gives its keys. Use `keys()` for keys, `values()` for values, or `items()` for both. Dictionaries iterate in insertion order.

## Count repeated words

```python
words = "python java python".split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)  # {'python': 2, 'java': 1}
```

On the first occurrence, `get(word, 0)` starts the count at zero. Later occurrences use the count already stored in the dictionary.

## Run and practice

From the repository root, run the examples.

```bash
python3 Day08/examples.py
```

Complete the exercises in [tasks.py](tasks.py). Run `python3 Day08/tasks.py` and compare your output with the expected results in the comments.
