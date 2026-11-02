# Day 01 — Your First Python Program: `print()` 🐍

> **Level:** Beginner · **Estimated reading time:** 15–20 minutes · **Requirement:** Python 3
>
> **Lesson focus:** Learn how to display information and control its appearance using Python's built-in `print()` function.

Welcome to Day 01 of our Python course!

Today, we will focus on **one function: `print()`**. You will learn its basic syntax and several useful features without introducing variables, data types, arithmetic, loops, or custom functions.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Explain what the built-in `print()` function does.
- Display text in the console using `print()`.
- Customize the separator between pieces of output with `sep`.
- Control what appears at the end of a print call with `end`.
- Use common escape sequences such as `\n`, `\t`, `\\`, and `\"`.
- Add simple comments to your Python code.

## 📚 Table of Contents

1. [Introduction to `print()`](#1-introduction-to-print)
2. [Understanding the Syntax](#2-understanding-the-syntax)
3. [The `sep` Parameter](#3-the-sep-parameter)
4. [The `end` Parameter](#4-the-end-parameter)
5. [Escape Sequences](#5-escape-sequences)
6. [Comments](#6-comments)
7. [Cheat Sheet and Summary](#7-cheat-sheet-and-summary)

---

## 1. Introduction to `print()`

`print()` is a **built-in function** in Python. It is used to display information, usually in the console. More precisely, by default it writes to the **standard output** (`stdout`).

Here is a simple example:

```python
print('Welcome to Day 01!')
```

**Output:**

```text
Welcome to Day 01!
```

Notice that the quotation marks are part of the Python code, but **they do not appear in the output**.

You can also use double quotation marks. They are especially convenient when the text contains an apostrophe:

```python
print("I'm learning Python!")
```

**Output:**

```text
I'm learning Python!
```

> **For now:** Think of quotation marks as a way to write the text you want to display. We will explore strings in a separate lesson.

## 2. Understanding the Syntax

Let's look at a `print()` call:

```python
print("Hello, Python!")
```

| Part | Meaning |
| --- | --- |
| `print` | The name of Python's built-in function |
| `(` and `)` | Parentheses used to call the function |
| `"Hello, Python!"` | The text to display |

When Python executes this statement, it calls `print()` and displays the provided text.

By default, `print()` also adds a **newline** at the end, so the next output starts on a new line. We will see how to change that behavior shortly.

**Important:** `print()` is a function, **not a method**. You can call it directly without importing a module or creating an object yourself.

## 3. The `sep` Parameter

`sep` stands for **separator**. It specifies what Python places **between** items passed to the same `print()` call.

```python
print("Python", "Java", "C++", sep=" | ")
```

**Output:**

```text
Python | Java | C++
```

If you do not specify `sep`, Python uses a single space as the separator.

Here are two more examples:

```python
print("2026", "11", "02", sep="-")
print("P", "Y", "T", "H", "O", "N", sep="")
```

**Output:**

```text
2026-11-02
PYTHON
```

| Code | Output |
| --- | --- |
| `print("A", "B")` | `A B` |
| `print("A", "B", sep="-")` | `A-B` |
| `print("A", "B", sep="")` | `AB` |

**Remember:** `sep` controls what appears *between* items. If only one item is printed, there is nothing to separate.

## 4. The `end` Parameter

By default, each `print()` call ends with a newline. That is why these two statements appear on separate lines:

```python
print("Hello")
print("World")
```

**Output:**

```text
Hello
World
```

The `end` parameter changes what is added **after** the printed content.

```python
print("Hello", end=" ")
print("World")
```

**Output:**

```text
Hello World
```

The first call ends with a space instead of a newline, so the second call continues on the same line.

You can also combine `sep` and `end`:

```python
print("Day", "01", sep="-", end=" -> ")
print("Completed!")
```

**Output:**

```text
Day-01 -> Completed!
```

**The key difference:**

- `sep` controls what appears **between** items in a single `print()` call.
- `end` controls what appears **after** all the items in that call.

## 5. Escape Sequences

An **escape sequence** is a special combination of characters that begins with a backslash (`\`). It lets you include special characters or formatting inside the text you print.

| Escape sequence | Meaning |
| --- | --- |
| `\n` | Newline |
| `\t` | Tab |
| `\\` | A literal backslash |
| `\"` | A double quotation mark |
| `\'` | A single quotation mark |

### Newline — `\n`

```python
print("First line\nSecond line")
```

**Output:**

```text
First line
Second line
```

### Tab — `\t`

```python
print("Name:\tPython")
```

**Output:** `Python` appears after a tab character. Its visual width depends on the terminal or editor.

### Backslash — `\\`

```python
print("Use \\ to show a backslash")
```

**Output:**

```text
Use \ to show a backslash
```

### Quotation Marks — `\"`

```python
print("She said: \"Hello!\"")
```

**Output:**

```text
She said: "Hello!"
```

> **A useful detail:** Escape sequences such as `\n` and `\t` are interpreted as part of the text before `print()` displays it. We will explore this more deeply in the lesson on strings.

## 6. Comments

A **comment** is a note for people reading the code. A single-line comment starts with `#`. Python ignores comments when executing instructions.

```python
# My first Python program
print("Hello!")  # Display a greeting
```

**Output:**

```text
Hello!
```

Good comments explain **why** something is done, rather than repeating what the code already makes obvious.

## 7. Cheat Sheet and Summary

### Quick Reference

| Goal | Example |
| --- | --- |
| Display text | `print("Hello")` |
| Use single quotation marks | `print('Hello')` |
| Change the separator | `print("A", "B", sep="-")` |
| Continue output on the same line | `print("A", end="")` |
| Add a newline within text | `print("A\nB")` |
| Add a tab within text | `print("A\tB")` |
| Display a backslash | `print("A\\B")` |
| Include a double quote | `print("She said: \"Hi!\"")` |
| Add a comment | `# Explain the next line` |

### Key Takeaways

- `print()` displays information, usually in the console.
- The default separator between items is a space, and the default ending is a newline.
- Use `sep` to change what appears between items and `end` to change what appears after them.
- Escape sequences help format displayed text.
- Comments make code easier to understand without changing its output.

**What's next?** In the following lessons, we will gradually explore other Python fundamentals. For now, the goal is simply to feel comfortable reading and using `print()`.

---

## 🔗 References and Acknowledgements

This is an **independently written educational lesson**. The following resources are useful for further reading and for checking technical details:

- [Python Documentation — `print()`](https://docs.python.org/3/library/functions.html#print)
- [Python Documentation — Escape Sequences](https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences)
- [30 Days of Python — Asabeneh Yetayeh](https://github.com/Asabeneh/30-Days-Of-Python) — inspiration for the structured learning journey
- [Metanit — Python Tutorial](https://metanit.com/python/tutorial/)
- [W3Schools — Python Tutorial](https://www.w3schools.com/python/)

> We explain concepts in our own words and do not republish other authors' lessons or exercise collections without permission.
