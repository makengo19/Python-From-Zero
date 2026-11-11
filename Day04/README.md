# Day 04 — Strings 🐍

> **Level:** Beginner · **Estimated reading time:** 25–35 minutes · **Requirement:** Python 3.6+ and Days 01–03
>
> **Lesson focus:** Create, read, clean, and format text using Python strings.

Welcome to Day 04 of **Python From Zero with Makengo!**

Day 02 introduced strings and `len()`, and Day 03 used `in` to check whether text contains a smaller piece of text. Today, you will work with individual characters, clean up input, and build readable messages.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Create strings with quotes, line breaks, and escape sequences.
- Combine text and format values in messages.
- Read individual characters and extract slices.
- Use string methods to clean, search, split, and join text.
- Save the result of a string operation when you need it later.

## 📚 Table of Contents

1. [Creating Strings](#1-creating-strings)
2. [Combining and Formatting Strings](#2-combining-and-formatting-strings)
3. [Indexing and Slicing](#3-indexing-and-slicing)
4. [String Methods](#4-string-methods)
5. [Practice — 14 Exercises](#5-practice--14-exercises)
6. [Cheat Sheet and Summary](#6-cheat-sheet-and-summary)

---

## 1. Creating Strings

A **string**, or `str`, is an ordered sequence of text characters. Use single or double quotes for a string on one line. Choose double quotes when the text contains an apostrophe, or single quotes when the text contains double quotation marks.

```python
notice = "The library opens at nine."
reply = "I'll be there."
label = 'Press "Enter" to continue.'

print(reply)             # I'll be there.
print(label)             # Press "Enter" to continue.
print(len("Room 7"))     # 6
print(len(""))           # 0
```

Spaces count toward the length. An empty string has length zero.

### Multiline Strings and Escape Sequences

Triple quotes let you put line breaks directly in a string. Inside an ordinary quoted string, `\n` inserts a newline, `\t` inserts a tab, and `\\` produces one backslash. Use `\'` or `\"` when you need to include the same quote character that surrounds the string.

```python
schedule = """Monday: reading
Tuesday: practice"""

print(schedule)
print("Wednesday: review\nThursday: quiz")
print("Day\tTopic")
print("notes\\day04.txt")
print('It\'s time to practice.')
```

The first two calls each print two lines. The tab in `Day\tTopic` moves the text to the next tab stop in a typical terminal.

## 2. Combining and Formatting Strings

Use `+` to join strings, an operation called **concatenation**. Add spaces where you need them. Use `*` with an integer to repeat text.

```python
first_name = "Dana"
last_name = "Park"
seat = 12

full_name = first_name + " " + last_name
print(full_name)                 # Dana Park
print("Seat " + str(seat))       # Seat 12
print("-" * 8)                   # --------
```

Both sides of `+` must be strings when you concatenate text. `str(seat)` turns the number into text for the label.

### f-Strings, `str.format()`, and `%`

Put `f` before the opening quote and place variables or expressions inside braces. The format specifier `:.2f` displays a number with two digits after the decimal point.

```python
item = "Notebook"
price = 3.5
quantity = 3
total = price * quantity

print(f"{item} x {quantity} = {total:.2f}")
print("{} x {} = {:.2f}".format(item, quantity, total))
print("%s x %d = %.2f" % (item, quantity, total))
print(f"Next order: {quantity + 1} notebooks")
```

**Output**

```text
Notebook x 3 = 10.50
Notebook x 3 = 10.50
Notebook x 3 = 10.50
Next order: 4 notebooks
```

In `str.format()`, the arguments fill the braces from left to right. In older code, you may see `%` formatting, where `%s` displays text, `%d` displays an integer, and `%.2f` displays a number with two decimal places. Formatting controls the displayed text and leaves the stored number available for calculations.

## 3. Indexing and Slicing

An **index** is a position in the string. Count from zero on the left or from `-1` on the right.

| Character | B | r | i | d | g | e |
| --- | --- | --- | --- | --- | --- | --- |
| Index from the left | `0` | `1` | `2` | `3` | `4` | `5` |
| Index from the right | `-6` | `-5` | `-4` | `-3` | `-2` | `-1` |

```python
word = "Bridge"

print(word[0])     # B
print(word[-1])    # e
print(word[-2])    # g

first, second, third = "MAP"
print(first, second, third)  # M A P
```

Accessing an index outside the string raises `IndexError`. In the last example, Python **unpacks** three characters into three variables. With this form of unpacking, the number of variables must match the number of characters.

### Taking a Slice

A **slice** uses `text[start:stop:step]` to select part of a string. The start is included and the stop is excluded. With the default step of `1`, omitting the start begins at the first character and omitting the stop goes through the last character. A negative step moves backward.

```python
word = "Bridge"

print(word[1:4])     # rid
print(word[:3])      # Bri
print(word[-3:])     # dge
print(word[::2])     # Big
print(word[::-1])    # egdirB
```

### Strings Are Immutable

Once a string exists, its characters cannot be changed in place. To replace the first letter, build a new string and assign it back to the variable.

```python
word = "map"
word = "c" + word[1:]
print(word)  # cap
```

## 4. String Methods

A **method** is an operation you call on a value using dot notation, as in `text.upper()`. Methods such as `strip()` and `replace()` return a new string. Assign the result to a variable if you want to keep it.

### Cleaning and Changing Case

```python
raw_name = "  dAnA PARK  "
name = raw_name.strip()

print(name)                 # dAnA PARK
print(name.lower())         # dana park
print(name.upper())         # DANA PARK
print(name.capitalize())    # Dana park
print(name.title())         # Dana Park
print(len(raw_name))        # 13
```

`strip()` removes whitespace from both ends and preserves spaces inside the string. `capitalize()` uppercases the first character in this example and lowercases the rest. `title()` is useful for simple labels such as `"weekly reading club"`.

### Searching and Checking Text

```python
filename = "draft_notes_notes.txt"

print("notes" in filename)          # True
print(filename.find("notes"))       # 6
print(filename.rfind("notes"))      # 12
print(filename.find("report"))      # -1
print(filename.count("notes"))      # 2
print(filename.startswith("draft")) # True
print(filename.endswith(".txt"))    # True
```

Use `in` when you only need a yes-or-no answer. `find()` returns the first matching position and `rfind()` returns the last. Both return `-1` for a missing match. `index()` and `rindex()` find positions in the same directions and raise `ValueError` when the text is missing. `count()` counts nonoverlapping matches.

```python
print("Desk".isalpha())     # True
print("204".isdecimal())   # True
print("204".isdigit())     # True
print("B204".isalnum())     # True
print("B 204".isalnum())    # False
print("".isalpha())        # False
```

These methods check the whole string and require at least one character. `isalpha()` checks for letters, `isdecimal()` checks for decimal digits, and `isalnum()` accepts letters and numeric characters. `isdigit()` also accepts some characters such as `"²"`.

### Replacing, Splitting, and Joining

```python
topics = "reading,writing,drawing"
updated_topics = topics.replace("writing", "coding")
parts = updated_topics.split(",")

print(updated_topics)      # reading,coding,drawing
print(parts)               # ['reading', 'coding', 'drawing']
print(" / ".join(parts))   # reading / coding / drawing
```

`replace(old, new)` replaces every occurrence by default. `split(",")` returns a list of strings by cutting at each comma. With no argument, `split()` separates words at runs of whitespace and ignores whitespace at the ends. Put the separator before `.join()` and pass the pieces to join inside the parentheses.

## 5. Practice — 14 Exercises

Create `practice.py` inside `Day04`. Run it from the repository root with `python3 Day04/practice.py`. Predict the output before running each example you write.

1. **Write a notice.** Store a sentence containing an apostrophe and a separate sentence containing double quotation marks. Print both.
2. **Build a schedule.** Print `Start` and `Finish` on separate lines using one string with `\n`. Create the same text with triple quotes and compare the strings with `==`.
3. **Make a book label.** Combine `"Shelf"`, `"B"`, and the integer `7` to produce `Shelf B7` using concatenation. Print the label and its length.
4. **Print a receipt line.** Use an f-string to print `Pencil x 4 = 5.00` from the item name, a quantity of `4`, and a unit price of `1.25`. Build the same line with `.format()`.
5. **Read characters.** Given `"Compass"`, print the first and last characters using indexes. Use a negative index for the last one.
6. **Read sections.** From `"ALM-204"`, extract `"ALM"` and `"204"` using two slices.
7. **Read backward and skip.** Use slices to reverse `"abcdef"` and to take every second character starting at index zero.
8. **Unpack a code.** Assign the three characters of `"R2D"` to three variables in one statement. Print them using `sep="-"`.
9. **Clean a name.** Starting from `"  sARA lee  "`, remove surrounding spaces and display `Sara Lee`. Print the original length and the cleaned length.
10. **Search a label.** For `"red-blue-red"`, print the first and last positions of `"red"`, its count, and the result of looking for `"green"` with `find()`.
11. **Check a filename.** Store `"lesson_04.txt"` and print whether it starts with `"lesson_"` and ends with `".txt"`. Repeat with `"lesson_04.csv"`.
12. **Check codes.** Run `isalpha()`, `isdecimal()`, and `isalnum()` on each of `"Q7"`, `"204"`, and `"blue"`. Compare the results.
13. **Reformat a list of tags.** Replace `"draft"` with `"review"` in `"python,strings,draft"`. Split on commas and join the tags with `" / "`.
14. **Build a badge from input.** Ask for a name and a room code. Try `"  dana park  "` and `" b204 "`. Remove surrounding spaces, title-case the name, uppercase the code, and print `Dana Park | Room B204` using an f-string.

**Self-check:** Exercise 3 gives a label length of `8`. Exercise 7 produces `fedcba` and `ace`. Exercise 10 gives `0`, `9`, `2`, and `-1`.

## 6. Cheat Sheet and Summary

| Goal | Example |
| --- | --- |
| Measure text | `len("Room 7")` → `6` |
| Combine text and a number | `"Room " + str(7)` |
| Display two decimal places | `f"{3.5:.2f}"` → `"3.50"` |
| Read the first or last character | `text[0]`, `text[-1]` |
| Take the first three characters | `text[:3]` |
| Reverse the order | `text[::-1]` |
| Remove surrounding whitespace | `text.strip()` |
| Change case | `text.lower()`, `text.upper()` |
| Check containment | `"notes" in filename` |
| Find a position | `filename.find("notes")` |
| Check a suffix | `filename.endswith(".txt")` |
| Replace matching text | `text.replace("draft", "review")` |
| Split and join | `text.split(",")`, `", ".join(parts)` |

### Key Takeaways

- Use quotes to create strings and escape sequences to represent characters such as newlines and tabs.
- An index selects one character. A slice selects a range and excludes its stop position.
- Strings are immutable. Save the result when you want to keep an edited version.
- Use an f-string to combine labels, values, and calculations in readable output.

---

## 🔗 References and Acknowledgements

This lesson is independently written for **Python From Zero with Makengo**. Asabeneh Yetayeh's strings lesson informed the topic selection.

- [30 Days of Python — Day 04: Strings](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md)
- [Python Documentation — Text Sequence Type and String Methods](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Tutorial — Formatted String Literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

[← Day 03 — Python Operators](../Day03/README.md) · [Course Home](../README.md)
