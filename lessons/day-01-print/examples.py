
# ============================================================
# Python From Zero with Makengo
# Day 01 — Python print() Function
# ============================================================

# 1. BASIC PRINT
# The print() function displays information in the console.

print("Hello, World!")
print("Welcome to Python!")

# Both single and double quotes can be used.

print('Hello, Python!')
print("Python's print() function")


# 2. THE SEP PARAMETER
# sep controls the separator between multiple values.
# The default separator is a space.

print("Python", "Java", "C++", sep=", ")
print("Python", "Java", "C++", sep=" | ")
print("2026", "11", "02", sep="-")
print("Python", "From", "Zero", sep="")


# 3. THE END PARAMETER
# By default, print() ends with a newline.
# The end parameter lets us change this behavior.

print("Hello", end=" ")
print("World!")

print("Loading", end="...")
print("Done!")

print("Python", end=" -> ")
print("From Zero")


# 4. ESCAPE SEQUENCES
# Escape sequences control how text appears.

# \n — Newline
print("Hello\nWorld")

# \t — Horizontal tab
print("Python\tCourse")

# \\ — Backslash
print("C:\\Python\\Lessons")

# \" — Double quotation mark
print("She said: \"Hello!\"")

# \' — Single quotation mark
print('It\'s time to learn Python!')


# 5. COMMENTS
# Comments explain code and are ignored by Python.

# This is a single-line comment.
print("Comments make code easier to understand.")

print("Hello, Makengo!")  # Inline comment

# ============================================================
# End of Day 01
# ============================================================
