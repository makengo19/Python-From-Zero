# Day 03 — Python Operators 🐍

> **Level:** Beginner · **Estimated reading time:** 20–30 minutes · **Requirement:** Python 3 and Days 01–02
>
> **Lesson focus:** Calculate values, update variables, and write clear conditions using Python operators.

Welcome to Day 03 of **Python From Zero with Makengo!**

Day 02 introduced a few operations alongside variables and data types. Today, we will look more closely at how operators work and how to choose the right one. The goal is to understand the expressions you have already used in practice.

An **operator** performs an operation on one or more values, called **operands**. In `12 + 3`, `+` is the operator and `12` and `3` are its operands. An **expression** is code that evaluates to a value: `12 + 3` evaluates to `15`.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Choose between arithmetic operators, including `/`, `//`, and `%`.
- Update numeric variables with augmented assignment.
- Compare values and combine conditions.
- Distinguish equality, identity, and membership.
- Read expressions using precedence and parentheses.

## 📚 Table of Contents

1. [Arithmetic Operators](#1-arithmetic-operators)
2. [Assignment Operators](#2-assignment-operators)
3. [Comparison Operators](#3-comparison-operators)
4. [Logical Operators](#4-logical-operators)
5. [Identity and Membership](#5-identity-and-membership)
6. [Operator Precedence](#6-operator-precedence)
7. [Cheat Sheet and Summary](#7-cheat-sheet-and-summary)

---

## 1. Arithmetic Operators

Arithmetic operators calculate numeric results.

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `17 + 5` | `22` |
| `-` | Subtraction | `17 - 5` | `12` |
| `*` | Multiplication | `17 * 5` | `85` |
| `/` | True division | `17 / 5` | `3.4` |
| `//` | Floor division | `17 // 5` | `3` |
| `%` | Remainder | `17 % 5` | `2` |
| `**` | Exponentiation | `2 ** 5` | `32` |

### Division, Whole Groups, and Leftovers

Imagine sharing 17 apples among 5 people:

```python
apples = 17
people = 5

print(apples / people)   # 3.4: an equal share if apples can be cut
print(apples // people)  # 3: whole apples per person
print(apples % people)   # 2: apples left over
```

For built-in integers and floats, `/` produces a float, even when the result is a whole number: `10 / 5` is `2.0`.

Floor division rounds the quotient **down**, toward negative infinity. It does not simply remove the decimal part:

```python
print(-17 / 5)   # -3.4
print(-17 // 5)  # -4
print(-17 % 5)   # 3
```

For integer operands and a nonzero divisor, floor division and remainder fit together like this:

```python
print((-17 // 5) * 5 + (-17 % 5))  # -17
```

A nonzero remainder has the same sign as the divisor. With positive integers, `%` is useful for checking divisibility:

```python
number = 18
print(number % 2 == 0)  # True: the number is even
print(number % 5 == 0)  # False: not divisible by 5
```

Dividing by zero with `/`, `//`, or `%` raises `ZeroDivisionError`.

### Powers and Text

Use `**` for powers: `4 ** 2` is `16`. The symbol `^` is a bitwise operator, not exponentiation; bitwise operations are outside this lesson.

The meaning of an operator also depends on the operand types:

```python
print(4 + 2)       # 6
print("4" + "2")   # 42: join two strings
print("ha" * 3)    # hahaha: repeat a string
print(int("4") + 2)  # 6: convert before adding
```

`"4" + 2` raises `TypeError`. Python does not automatically turn numeric text into a number for addition.

## 2. Assignment Operators

Assignment uses `=` to make a name refer to a value. Python evaluates the right-hand side first:

```python
score = 10
score = score + 5
print(score)  # 15
```

**Augmented assignment** combines an operation with assignment. For the numeric variables in this lesson, these forms give the same result:

| Short form | Expanded form |
| --- | --- |
| `score += 5` | `score = score + 5` |
| `score -= 5` | `score = score - 5` |
| `score *= 5` | `score = score * 5` |
| `score /= 5` | `score = score / 5` |
| `score //= 5` | `score = score // 5` |
| `score %= 5` | `score = score % 5` |
| `score **= 5` | `score = score ** 5` |

Each row describes a separate update. When you write updates one after another, each uses the latest value:

```python
score = 10
score += 5
score *= 2
print(score)  # 30

score /= 3
print(score)  # 10.0
```

Define a variable before updating it. Starting with `points += 1` when `points` does not exist raises `NameError`.

> **Remember:** `=` assigns a value; `==` checks equality. Python has no `++` increment operator. Use `score += 1`.

## 3. Comparison Operators

For the numbers and strings used here, comparisons produce a boolean: `True` or `False`.

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | Equal to | `8 == 8` | `True` |
| `!=` | Not equal to | `8 != 8` | `False` |
| `>` | Greater than | `8 > 3` | `True` |
| `<` | Less than | `8 < 3` | `False` |
| `>=` | Greater than or equal to | `8 >= 8` | `True` |
| `<=` | Less than or equal to | `8 <= 3` | `False` |

Store a comparison result when you want to reuse it:

```python
temperature = 22
is_comfortable = 18 <= temperature <= 25
print(is_comfortable)  # True
```

Python supports **chained comparisons**. Here, `18 <= temperature <= 25` checks both boundaries, including 18 and 25.

Types still matter:

```python
print(5 == 5.0)           # True: equal numeric values
print("5" == 5)           # False: text and a number
print("Python" == "python")  # False: text comparison is case-sensitive
```

Ordering a string and an integer, such as `"5" < 10`, raises `TypeError`. Convert numeric text before comparing it with numbers.

Floating-point calculations can contain small representation errors: `0.1 + 0.2 == 0.3` is `False`. When you need approximate numeric equality, tools such as `math.isclose()` are more suitable than a direct `==` check.

## 4. Logical Operators

Use `and`, `or`, and `not` to work with conditions.

For boolean operands:

| `a` | `b` | `a and b` | `a or b` |
| --- | --- | --- | --- |
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

`not` reverses the truth value: `not True` is `False`, and `not False` is `True`.

```python
age = 19
has_ticket = True
has_invitation = False

can_enter = age >= 18 and has_ticket
has_access_document = has_ticket or has_invitation

print(can_enter)            # True
print(has_access_document)  # True
print(not has_ticket)       # False
```

`or` includes the case where **both** conditions are true.

### Short-Circuit Evaluation

Python evaluates the left operand first. With `and`, it skips the right operand if the left is false. With `or`, it skips the right operand if the left is true.

```python
divisor = 0
is_large_share = divisor != 0 and 20 / divisor > 3
print(is_large_share)  # False
```

The division is skipped because `divisor != 0` is false, so this expression does not divide by zero.

### Truth Values Beyond Booleans

Zero, empty strings, empty collections, and `None` are false in a boolean context. Nonzero numbers and nonempty strings are true.

`and` and `or` return one of their operands, which is not necessarily a boolean. `not` always returns a boolean:

```python
print("" or "Guest")       # Guest
print("Makengo" and "Ready")  # Ready
print(not "")             # True
print(bool("False"))      # True: a nonempty string
```

For now, use explicit comparisons when they make a condition easier to read. Write `age == 18 or age == 19`, not `age == 18 or 19`: the second expression does not compare `age` with 19.

## 5. Identity and Membership

### Identity: `is` and `is not`

Equality asks, “Do these objects have equal values?” Identity asks, “Are these names referring to the very same object?”

```python
first = [1, 2]
second = [1, 2]
alias = first

print(first == second)  # True: equal contents
print(first is second)  # False: two separate lists
print(first is alias)   # True: the same list
```

The square brackets create lists. We will explore lists in a later lesson; here they make the difference between equality and identity visible.

A common use of identity is checking for `None`, which represents an absent value:

```python
result = None
print(result is None)      # True
print(result is not None)  # False
```

Use `==` to compare numbers and text by value. Do not rely on `is` for those checks: Python may reuse some objects internally.

### Membership: `in` and `not in`

Membership checks whether something is contained in another object.

```python
print("Py" in "Python")           # True: substring
print("py" in "Python")           # False: case-sensitive
print("Java" not in "Python")      # True
print(3 in [1, 2, 3])             # True: list element
print("red" in ["red", "green"])  # True
```

For strings, `in` searches for a substring. For lists, it checks elements for equality: `"re" in ["red", "green"]` is `False`, because neither element equals `"re"`.

For a dictionary, membership checks **keys**, not values:

```python
profile = {"name": "Makengo"}
print("name" in profile)     # True
print("Makengo" in profile)  # False
```

## 6. Operator Precedence

**Precedence** determines how operators are grouped when parentheses do not specify the grouping. This is a simplified guide for the operators in this lesson, from higher to lower precedence:

| Priority | Operators |
| --- | --- |
| Higher | `**` |
| | Unary `+` and `-`, as in `-number` |
| | `*`, `/`, `//`, `%` |
| | `+`, `-` |
| | Comparisons, `in`, `not in`, `is`, `is not` |
| | `not` |
| | `and` |
| Lower | `or` |

Parentheses explicitly group an expression:

```python
print(2 + 3 * 4)        # 14
print((2 + 3) * 4)      # 20
print(True or False and False)    # True
print((True or False) and False)  # False
```

Operators at the same arithmetic level generally group left to right. Powers are an exception: they group right to left.

```python
print(20 / 5 * 2)   # 8.0: (20 / 5) * 2
print(2 ** 3 ** 2)  # 512: 2 ** (3 ** 2)
```

Powers also need care with negative numbers:

```python
print(-3 ** 2)    # -9: -(3 ** 2)
print((-3) ** 2)  # 9
print(2 ** -2)    # 0.25: a negative exponent is allowed
```

Use parentheses when the intended grouping is not immediately clear. Assignment with `=` is a statement; its right-hand expression is evaluated before the name is updated.

## 7. Cheat Sheet and Summary

| Goal | Example |
| --- | --- |
| Calculate a total | `price * quantity` |
| Divide into whole groups | `17 // 5` → `3` |
| Find a remainder | `17 % 5` → `2` |
| Check whether a number is even | `number % 2 == 0` |
| Raise to a power | `3 ** 2` → `9` |
| Update a number | `score += 1` |
| Compare values | `answer == 42`, `answer != 0` |
| Check an inclusive range | `0 <= score <= 100` |
| Require both conditions | `age >= 18 and has_ticket` |
| Accept either condition | `has_ticket or has_invitation` |
| Reverse a truth value | `not is_ready` |
| Check for an absent value | `result is None` |
| Check membership | `"Py" in "Python"` |
| Make grouping explicit | `(price + delivery) * quantity` |

### Key Takeaways

- `/` calculates a quotient, `//` floors it, and `%` gives the remainder.
- `=` assigns, `==` compares values, and `is` checks object identity.
- Augmented assignment updates a variable using its current value.
- `and` and `or` short-circuit and can return nonboolean operands.
- `in` checks containment; its meaning depends on the container type.
- Parentheses help you express the calculation or condition you intend.

You can now read calculations and combine conditions with confidence. These expressions will be useful when you begin making decisions with `if` statements.

---

## 🔗 References and Acknowledgements

This lesson is independently written for **Python From Zero with Makengo**. The official documentation provides further detail:

- [Python Documentation — Expressions](https://docs.python.org/3/reference/expressions.html) — arithmetic, comparisons, identity, membership, and precedence
- [Python Documentation — Built-in Types](https://docs.python.org/3/library/stdtypes.html) — numeric operations and truth values

[← Day 02 — Variables and Data Types](../Day02/README.md) · [Course Home](../README.md)
