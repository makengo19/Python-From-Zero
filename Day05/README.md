# Day 05 — Lists 🐍

In Day 04, `split()` turned one string into several pieces. Python stored
those pieces in a **list**. Today you'll use lists to keep related values
together and update them as your program runs.

## 🎯 Learning Objectives

- Create lists and count their items with `len()`.
- Read items by index, take slices, and check membership with `in`.
- Replace, add, and remove items.
- Tell when two names share a list and make a separate copy.

## 📚 Table of Contents

1. [Creating Lists](#1-creating-lists)
2. [Accessing Items](#2-accessing-items)
3. [Changing Lists](#3-changing-lists)
4. [Sorting and Copying](#4-sorting-and-copying)
5. [Practice](#5-practice)
6. [Cheat Sheet](#6-cheat-sheet)

Run the [examples](examples.py) from the repository root.

```bash
python3 Day05/examples.py
```

## 1. Creating Lists

Use square brackets around comma-separated values. A list keeps items in
order and can contain duplicates. Use `[]` for an empty list.

```python
groceries = ["bread", "milk", "milk"]
shopping_cart = []

print(len(groceries))      # 3
print("milk" in groceries)  # True
```

You can also create a list from text using the `split()` method from Day 04.

```python
topics = "print,strings,lists".split(",")
print(topics)  # ['print', 'strings', 'lists']
```

## 2. Accessing Items

As with strings, index `0` selects the first item and `-1` selects the last.
A slice returns a new list, with the stop index excluded.

```python
topics = ["print", "strings", "lists"]

print(topics[0])    # print
print(topics[-1])   # lists
print(topics[1:3])  # ['strings', 'lists']
```

For a list of three items, reading `topics[3]` raises `IndexError`. An
empty list has no first or last item.

## 3. Changing Lists

Lists are mutable. Assign to an index to replace an existing value, or
use a method to add or remove items.

```python
groceries = ["bread", "milk", "eggs"]
groceries[1] = "oat milk"
groceries.append("apples")
groceries.insert(1, "rice")
groceries.remove("eggs")
last_item = groceries.pop()

print(last_item)  # apples
print(groceries)  # ['bread', 'rice', 'oat milk']
```

`remove(value)` deletes the first matching item and raises `ValueError`
if the value is absent. `pop(index)` removes and returns the item at that
index. With no index, it takes the last item. Popping from an empty list
raises `IndexError`.

## 4. Sorting and Copying

Assignment gives the same list another name. Use `copy()` to create a
separate list before making changes. With a list of numbers, the copied
items can be replaced or reordered independently.

```python
scores = [18, 12, 20]
same_scores = scores
same_scores.append(15)

ranking = scores.copy()
ranking.sort(reverse=True)

print(scores)   # [18, 12, 20, 15]
print(ranking)  # [20, 18, 15, 12]
```

Both `append()` and `sort()` change the list in place and return `None`.
When you want a new sorted list in one expression, use
`ranking = sorted(scores, reverse=True)`.

## 5. Practice

Complete the starter values in [tasks.py](tasks.py) and run the self-check.

```bash
python3 -m unittest discover -s tests -v -k TestDay05
```

1. Make a list of three favorite meals. Print how many are in the list
   and check whether it contains `"pizza"`.
2. Given `["Mon", "Tue", "Wed", "Thu", "Fri"]`, print Tuesday through
   Thursday using a single slice.
3. Start with `["tea", "tea", "water"]`. Remove one `"tea"`, insert
   `"juice"` at the start, and print the result.
4. Split `"physics,math,history"` into a list. Sort a copy alphabetically
   and print both the original and the copy.
5. Challenge — Start with an empty to-do list. Add three tasks, change
   the first task, and mark the last one complete by popping it. Print
   the completed task and the tasks that are still on the list.

## 6. Cheat Sheet

| Operation | What it does |
|---|---|
| `len(items)` | Counts items |
| `value in items` | Checks whether the list contains a value |
| `items[0]`, `items[-1]` | Reads the first or last item |
| `items[1:3]` | Makes a list of items at indices 1 and 2 |
| `items[0] = value` | Replaces the first item |
| `items.append(value)` | Adds a value at the end |
| `items.insert(index, value)` | Inserts a value before an index |
| `items.remove(value)` | Removes the first matching value |
| `items.pop()` | Removes and returns the last item |
| `items.sort()` | Sorts the list in place |
| `items.copy()` | Makes a shallow copy |

## 🔗 References and Acknowledgements

- [Python Tutorial — Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
