"""Day 02 — Variables and Data Types."""

from math import pi

# Assignment, types, and string length
first_name = "Dana"
age = 18
is_student = True
print(first_name, type(first_name), len(first_name))
print(age, type(age))
print(is_student, type(is_student))

# input() also returns a string. Use fixed text here for a quick example.
age_text = "18"
age = int(age_text)
print("Age next year:", age + 1)

# Arithmetic and formatted output
radius = 3
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")
