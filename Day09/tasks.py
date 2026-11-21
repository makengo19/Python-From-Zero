# Day 09: Sets - Practice Tasks

# Task 1: Create a set
# Create a set with your favorite programming languages.
languages = {"Python", "Java", "C++"}
print("Languages:", languages)

# Task 2: Add elements
# Add two new programming languages.
languages.add("JavaScript")
languages.add("Go")
print("Updated languages:", languages)

# Task 3: Remove an element
# Remove C++ from the set.
languages.discard("C++")
print("After removal:", languages)

# Task 4: Union
# Combine two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a.union(b))

# Task 5: Intersection
# Find common elements.
print("Intersection:", a.intersection(b))

# Task 6: Difference
# Find elements only in set A.
print("Difference:", a.difference(b))

# Task 7: Symmetric difference
# Find elements that are not shared.
print("Symmetric difference:", a.symmetric_difference(b))

# Task 8: Unique values
# Remove duplicate numbers using a set.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)
