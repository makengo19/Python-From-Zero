# Day 02 — Variables and Data Types 🐍

> **Level:** Beginner · **Estimated reading time:** 25–35 minutes · **Requirement:** Python 3 and Day 01
>
> **Lesson focus:** Store values, inspect their types, work with numbers and text, and collect user input.

Welcome to Day 02 of **Python From Zero with Makengo!**

In Day 01, you displayed information with `print()`. Today, you will give values meaningful names and use them to build small calculations and interactive programs.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Create and update variables using readable names.
- Recognize common Python data types and inspect them with `type()`.
- Measure strings with `len()` and compare their lengths.
- Convert values between strings, integers, and floating-point numbers.
- Use arithmetic, comparison, and logical operators.
- Read user input and calculate the area and circumference of a circle.

## 📚 Table of Contents

1. [Variables and Assignment](#1-variables-and-assignment)
2. [Naming Variables](#2-naming-variables)
3. [Data Types and `type()`](#3-data-types-and-type)
4. [String Length and `len()`](#4-string-length-and-len)
5. [Type Conversion](#5-type-conversion)
6. [Operations](#6-operations)
7. [User Input](#7-user-input)
8. [Circle Formulas](#8-circle-formulas)
9. [Practice — 14 Exercises](#9-practice--14-exercises)
10. [Challenge — Personal Calculator and Profile](#10-challenge--personal-calculator-and-profile)
11. [Cheat Sheet and Summary](#11-cheat-sheet-and-summary)

---

## 1. Variables and Assignment

A variable is a name that refers to a value. Use `=` to assign a value; you do not need a declaration keyword or an explicit type.

```python
first_name = "Ali"
age = 18
print(first_name)
print(age)
```

**Output:**

```text
Ali
18
```

Read `age = 18` as “assign 18 to age.” Assignment is different from checking equality, which uses `==`.

You can update a variable:

```python
age = 18
age = age + 1
print(age)  # 19
```

The right-hand side is evaluated before the assignment. `age += 1` is a shorter way to update this numeric variable.

Python is dynamically typed: values have types, and a name can later refer to a value of another type. Prefer keeping each variable's meaning consistent so the program stays easy to follow.

Multiple assignment is also possible:

```python
first_name, last_name = "Ali", "Smith"
x = y = 0
print(first_name, last_name, x, y)
```

**Output:** `Ali Smith 0 0`

## 2. Naming Variables

Choose names that explain what a value represents.

| Guideline | Example |
| --- | --- |
| Use lowercase words separated by underscores (`snake_case`) | `first_name`, `circle_area` |
| Start with a letter or underscore | `age`, `_count` |
| Digits are allowed after the first character | `player_2` |
| Names are case-sensitive | `age` and `Age` are different names |
| Avoid Python keywords | Use `class_name`, not `class` |
| Avoid replacing built-in names | Use `text_length`, not `len` |

For this course, use English letters, digits, and underscores. Python also accepts many Unicode letters in identifiers.

Names such as `2name`, `first-name`, and `first name` are not valid variable names. `first-name` is interpreted as subtraction rather than one name.

Use spaces around assignment and arithmetic operators:

```python
unit_price = 12
quantity = 3
total_price = unit_price * quantity
print(total_price)
```

## 3. Data Types and `type()`

A data type describes the kind of value you are working with.

| Type | Meaning | Example |
| --- | --- | --- |
| `str` | Text | `"Python"` |
| `int` | Whole number | `18` |
| `float` | Floating-point number | `3.5` |
| `bool` | Logical value | `True`, `False` |
| `NoneType` | Absence of a value | `None` |
| `list` | Mutable sequence | `[1, 2, 3]` |
| `tuple` | Immutable sequence | `(1, 2, 3)` |
| `dict` | Key-value mapping | `{"name": "Ali"}` |
| `set` | Collection of unique elements | `{1, 2, 3}` |

We will study collections in later lessons. Today, focus on text, numbers, and booleans.

Call the built-in `type()` function to inspect a value:

```python
first_name = "Ali"
age = 18
height = 1.75
is_student = True

print(type(first_name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(None))
```

**Output:**

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
```

`"18"` is a string; `18` is an integer. Quotes change the meaning. Boolean literals are spelled `True` and `False`, with capital letters.

## 4. String Length and `len()`

`len()` returns the number of items in a supported object. For a string, it counts Unicode code points, including spaces and punctuation. Some visible characters, such as combined emoji, contain more than one code point.

```python
first_name = "Ali"
last_name = "Smith"

print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len("Hi there!"))
```

**Output:**

```text
3
5
False
9
```

Numbers do not have a length. To count the digits of a positive integer, first convert it to text:

```python
number = 2026
print(len(str(number)))  # 4
```

Calling `len(2026)` directly raises `TypeError`.

## 5. Type Conversion

Use built-in conversion functions when you need a different representation.

| Function | Example | Result |
| --- | --- | --- |
| `int()` | `int("18")` | `18` |
| `float()` | `float("3.5")` | `3.5` |
| `str()` | `str(18)` | `"18"` |
| `bool()` | `bool(0)` | `False` |

```python
age_text = "18"
age = int(age_text)
print(age + 1)  # 19

price = float("12.50")
print(price)  # 12.5

print("Age: " + str(age))  # Age: 18
```

**Important details:**

- `int(3.9)` produces `3`: conversion truncates toward zero; it does not round.
- `int("3.9")` and `int("hello")` raise `ValueError`.
- `float("3.9")` accepts decimal text; use a dot as the decimal separator.
- Zero, empty strings, empty collections, and `None` are false in a boolean context.
- Nonempty strings are true, so `bool("False")` is `True`.

Python can mix integers and floats in arithmetic, but it does not automatically convert numeric text for addition: `"18" + 1` raises `TypeError`.

## 6. Operations

### Arithmetic Operators

```python
num_one = 5
num_two = 4

print(num_one + num_two)
print(num_one - num_two)
print(num_one * num_two)
print(num_one / num_two)
print(num_one % num_two)
print(num_one ** num_two)
print(num_one // num_two)
```

**Output:**

```text
9
1
20
1.25
1
625
1
```

| Operator | Purpose | Example |
| --- | --- | --- |
| `+` | Addition | `5 + 4` → `9` |
| `-` | Subtraction | `5 - 4` → `1` |
| `*` | Multiplication | `5 * 4` → `20` |
| `/` | True division | `5 / 4` → `1.25` |
| `%` | Remainder | `5 % 4` → `1` |
| `**` | Exponentiation | `5 ** 4` → `625` |
| `//` | Floor division | `5 // 4` → `1` |

`/` returns a float for these integer operands, even when division is exact. Floor division rounds the quotient down: `-5 // 4` is `-2`. Dividing by zero with `/`, `//`, or `%` raises `ZeroDivisionError`.

Parentheses control evaluation order:

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

Powers are evaluated before multiplication and division, which are evaluated before addition and subtraction. Use parentheses to make your intention clear.

### Comparison and Logical Operators

Comparisons return booleans:

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` / `<` | Greater than / less than |
| `>=` / `<=` | Greater than or equal to / less than or equal to |

```python
age = 18
has_ticket = True

print(age >= 18)                 # True
print(age >= 18 and has_ticket)  # True
print(age < 18 or has_ticket)    # True
print(not has_ticket)            # False
```

For boolean operands, `and` requires both to be true, `or` requires at least one, and `not` reverses the truth value. More generally, `and` and `or` return one of their operands.

### String Operations

```python
first_name = "Ali"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Ali Smith
print("Py" * 3)   # PyPyPy
```

`+` joins strings, while `*` repeats a string an integer number of times. For numeric strings, `"5" + "4"` is `"54"`; convert them before doing arithmetic.

## 7. User Input

`input()` displays an optional prompt, waits for a line of text, and returns a string without the final newline.

```python
first_name = input("First name: ")
age = int(input("Age in whole years: "))

print("Hello,", first_name)
print("Next year you will be", age + 1)
```

**Example session:**

```text
First name: Ali
Age in whole years: 18
Hello, Ali
Next year you will be 19
```

Use `int()` for whole numbers and `float()` for decimal numbers. These conversions assume valid input; invalid numeric text raises `ValueError`. Error handling appears in the optional challenge below.

## 8. Circle Formulas

For a circle with radius `r`:

- **Area:** `π × r²`
- **Circumference:** `2 × π × r`

Python uses `**` for powers, not `^` (which is a bitwise operator). Import `pi` from the standard library's `math` module for a convenient approximation of π.

```python
from math import pi

radius = 3
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Area:", area_of_circle)
print("Circumference:", circum_of_circle)
```

**Approximate output:**

```text
Area: 28.274333882308138
Circumference: 18.84955592153876
```

If the radius is measured in centimeters, area is in square centimeters and circumference is in centimeters. A radius must be nonnegative; zero describes a degenerate circle.

For an interactive version, replace the radius assignment with:

```python
radius = float(input("Radius (nonnegative number): "))
```

This reads a number but does not yet reject negative input. Add validation in the challenge.

## 9. Practice — 14 Exercises

Create a file named `practice.py` inside `Day02`. Run it from the repository root with `python3 Day02/practice.py`. Save calculated results in variables before printing them.

1. **Build a profile.** Create `first_name`, `last_name`, `country`, `city`, `age`, `is_student`, and `year` with sensible values. Print each value and its type using `type()`.
2. **Measure a name.** Store `len(first_name)` in `first_name_length` and print it.
3. **Compare name lengths.** Print the lengths of your first and last names. Store whether the first name is longer in `is_first_name_longer`. What happens when the lengths are equal?
4. **Prepare two numbers.** Assign `5` to `num_one` and `4` to `num_two`. Use these values throughout exercises 5–11.
5. **Addition.** Add the two numbers, assign the result to `total`, and print it.
6. **Subtraction.** Subtract `num_two` from `num_one`, assign the result to `diff`, and print it.
7. **Multiplication.** Multiply the numbers, assign the result to `product`, and print it.
8. **Division.** Divide `num_one` by `num_two`, assign the result to `division`, and print its value and type.
9. **Remainder.** Find the remainder when `num_one` is divided by `num_two`. Store it in `remainder` and print it.
10. **Exponentiation.** Raise `num_one` to the power of `num_two`. Store it in `exp` and print it.
11. **Floor division.** Calculate `num_one // num_two`, store it in `floor_division`, and print it. Compare it with exercise 8.
12. **Fixed-radius circle.** Set `radius = 30`. Use `math.pi` or `from math import pi` to calculate `area_of_circle` and `circum_of_circle`. Print labels and units for both results.
13. **Interactive circle.** Ask for a radius with `input()`, convert it to a float, and calculate its area and circumference. Try a whole number, a decimal, and zero. For now, assume valid nonnegative numeric input.
14. **Interactive profile and conversion.** Ask for first name, last name, country, and age. Convert age to an integer, calculate next year's age, and print a readable profile. Print the type of the raw age text and the converted age to explain the difference.

**Self-check for exercises 5–11:** `9`, `1`, `20`, `1.25`, `1`, `625`, `1`.

For exercise 12, the area is approximately `2827.4334` square units and the circumference is approximately `188.4956` units. Small display differences from floating-point arithmetic are normal.

## 10. Challenge — Personal Calculator and Profile

Already comfortable with the basics? Combine the lesson into one program without copying a complete solution.

Your program should:

- Ask for first name, last name, age, and country.
- Report whether the first name, last name, or neither is longer.
- Calculate and label all seven arithmetic results for `5` and `4`.
- Ask for a radius and display its area and circumference.
- Present a readable final report, with circle results rounded to two decimal places.

**Optional extension:** Use `try` / `except ValueError` to handle nonnumeric age or radius input. Use `if` to reject negative ages and radii. For an extra challenge, reject nonfinite radius values such as `nan` and `inf` with `math.isfinite()`, and allow another attempt with a loop.

These control-flow tools are a preview of later lessons. Try valid input first, then `hello`, `-2`, and `0`. Zero is a valid radius; invalid input should produce a useful message instead of an unexplained crash.

## 11. Cheat Sheet and Summary

| Goal | Example |
| --- | --- |
| Assign a value | `age = 18` |
| Update a number | `age += 1` |
| Inspect a type | `type(age)` |
| Measure text | `len("Python")` → `6` |
| Convert numeric text | `int("18")`, `float("3.5")` |
| Convert to text | `str(18)` |
| Read text | `input("Name: ")` |
| Compare values | `age >= 18` |
| Calculate a power | `radius ** 2` |
| Calculate circle area | `pi * radius ** 2` |
| Calculate circumference | `2 * pi * radius` |

### Key Takeaways

- Variables give meaningful names to values; assignment uses `=`.
- Values have types, and `type()` helps you inspect them.
- `len()` measures strings and collections, not numbers directly.
- `input()` returns text, so convert it before numeric calculations.
- `/`, `//`, and `%` perform different operations.
- Store results when you need to reuse them; `print()` alone does not save them.

---

## 🔗 References and Acknowledgements

This lesson is independently written. Its practice sequence follows the Day 02 study plan used in this course; the explanations and exercise wording are original.

- [Python Documentation — Built-in Functions](https://docs.python.org/3/library/functions.html) — `type()`, `len()`, conversions, and `input()`
- [Python Documentation — Built-in Types](https://docs.python.org/3/library/stdtypes.html) — numbers, strings, comparisons, and truth values
- [Python Documentation — Names](https://docs.python.org/3/reference/lexical_analysis.html#names) — identifier rules and keywords
- [Python Documentation — `math.pi`](https://docs.python.org/3/library/math.html#math.pi)
- [30 Days of Python — Asabeneh Yetayeh](https://github.com/Asabeneh/30-Days-Of-Python) — inspiration for the structured learning journey

[← Day 01 — The `print()` Function](../lessons/day-01-print/README.md) · [Course Home](../README.md)
