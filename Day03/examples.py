"""Day 03 — Python Operators."""

# Whole groups and leftovers
books = 17
books_per_box = 5
print("Full boxes:", books // books_per_box)
print("Books left:", books % books_per_box)

# Augmented assignment and comparisons
score = 70
score += 10
has_ticket = True
print("May enter:", score >= 75 and has_ticket)

# Membership, identity, and grouping
print("Py" in "Python")
delivery_note = None
print(delivery_note is None)
print("Total:", (12 + 3) * 2)
