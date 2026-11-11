# 🐍 Python From Zero with Makengo

Welcome to **Python From Zero with Makengo!**

A free, beginner-friendly Python course designed to help you learn Python step by step, from the fundamentals to more advanced concepts.

## 📚 About This Course

This course focuses on:

- Clear and beginner-friendly explanations
- Practical Python code examples
- Understanding how and why Python works
- Building strong programming fundamentals
- Learning through real-world examples

## 🗺️ Course Roadmap

| Day | Lesson | What you'll learn | Examples | Tasks |
|---|---|---|---|---|
| 01 | [The print() Function](Day01/README.md) | Output, separators, line endings, and escape sequences | [examples.py](Day01/examples.py) | — |
| 02 | [Variables and Data Types](Day02/README.md) | Assignment, types, conversions, and user input | [examples.py](Day02/examples.py) | [tasks.py](Day02/tasks.py) |
| 03 | [Python Operators](Day03/README.md) | Arithmetic, comparisons, logic, and membership | [examples.py](Day03/examples.py) | [tasks.py](Day03/tasks.py) |
| 04 | [Strings](Day04/README.md) | Formatting, indexing, slicing, and string methods | [examples.py](Day04/examples.py) | [tasks.py](Day04/tasks.py) |

## Getting Started

You need Python 3.10 or newer and Git. The examples and self-checks use only the Python standard library.

Clone the repository and run a lesson example from the project directory.

```bash
git clone https://github.com/makengo19/Python-From-Zero.git
cd Python-From-Zero
python3 --version
python3 Day01/examples.py
python3 Day04/examples.py
```

On Windows, use `py -3` in place of `python3` if Python is installed through the Python launcher.

## Practice and Check Your Work

Open the day's `tasks.py` file and replace each `None` with your answer. Keep the starting values and variable names so the checks can read your results. The lesson pages also contain longer practice exercises.

From the repository root, run the checks for all three days.

```bash
python3 -m unittest discover -s tests -v
```

To check one day, add its test class name as a filter.

```bash
python3 -m unittest discover -s tests -v -k TestDay04
```

Unfinished answers fail their checks. Each test name identifies the result to review. The checks compare results for the starter inputs, so use the operations requested in the task even if another expression gives the same result.

## Code Style

GitHub Actions checks the lesson and test files with Ruff on pull requests. To run the same check locally, install Ruff and run it from the repository root.

```bash
python3 -m pip install ruff==0.17.4
python3 -m ruff check --select E,F,W Day01 Day02 Day03 Day04 tests
```

## 📖 Learning Resources

This independent course is informed by:

- [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python)
- [Metanit Python Tutorial](https://metanit.com/python/tutorial/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Official Python Documentation](https://docs.python.org/3/)

The explanations and learning materials in this repository are developed independently.

## 👨‍💻 Author

Created by **Makengo**.

Learn Python. Practice consistently. Build real skills.
