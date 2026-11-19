# Day 08 — Python Dictionaries
# Complete each exercise and compare your output with the expected result.

# Exercise 1 — Create and read a dictionary
# Create a dictionary named book with title "Python Basics" and 120 pages.
# Print the title. Expected: Python Basics

# Exercise 2 — Use a fallback
product = {"name": "Notebook", "price": 800}
# Use get() to read the missing "color" key. Expected: Unknown

# Exercise 3 — Add and update entries
scores = {"Ali": 80, "Dana": 95}
# Update Ali's score to 85 and add Maksat with a score of 90.
# Print scores. Expected: {'Ali': 85, 'Dana': 95, 'Maksat': 90}

# Exercise 4 — Remove an entry
inventory = {"pens": 12, "pencils": 8}
# Use pop() to remove "pencils". Print the quantity returned. Expected: 8

# Exercise 5 — Loop through key–value pairs
prices = {"apple": 300, "banana": 450}
# Use items() to print each fruit and its price.
# Expected lines: apple 300, then banana 450

# Exercise 6 — Count repeated words
words = "red blue red green blue red".split()
# Use a dictionary and get() to count each word.
# Print the counts. Expected: {'red': 3, 'blue': 2, 'green': 1}
