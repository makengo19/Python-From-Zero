# Day 07 — Python Sets

# 1. Creating sets
fruits = {"apple", "banana", "orange"}
print("Fruits:", fruits)

# 2. Sets contain unique elements
numbers = {1, 2, 2, 3, 4, 4, 5}
print("Unique numbers:", numbers)

# 3. Empty set
empty_set = set()
print("Empty set:", empty_set)

# 4. Adding elements
fruits.add("mango")
print("After add:", fruits)

# 5. Updating sets
fruits.update(["grape", "cherry"])
print("After update:", fruits)

# 6. Removing elements
fruits.remove("banana")
fruits.discard("pineapple")
print("After remove:", fruits)

# 7. Membership
print("Is apple present?", "apple" in fruits)

# 8. Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric difference:", a ^ b)

# 9. Subsets and supersets
small = {1, 2}
large = {1, 2, 3, 4}

print("Subset:", small.issubset(large))
print("Superset:", large.issuperset(small))

# 10. Removing duplicates from a list
values = [1, 2, 2, 3, 3, 4, 5]
unique_values = set(values)
print("Unique values:", unique_values)
