# Day 09: Sets in Python

# 1. Creating sets
fruits = {"apple", "banana", "cherry"}
print("Fruits:", fruits)

# 2. Unique elements
numbers = {1, 2, 2, 3, 4, 4}
print("Unique numbers:", numbers)

# 3. Adding elements
fruits.add("orange")
print("After add:", fruits)

# 4. Removing elements
fruits.discard("banana")
print("After discard:", fruits)

# 5. Union
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)

# 6. Intersection
print("Intersection:", a & b)

# 7. Difference
print("Difference:", a - b)

# 8. Symmetric difference
print("Symmetric difference:", a ^ b)

# 9. Membership
print("Is 3 in set A?", 3 in a)

# 10. Set length
print("Length:", len(a))
