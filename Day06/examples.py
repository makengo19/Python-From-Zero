
# Day 06: Tuples
# Python From Zero With Makengo

# 1. Creating Tuples

empty_tuple = ()
fruits = ("apple", "banana", "orange")
numbers = (1, 2, 3, 4, 5)

print("Fruits:", fruits)
print("Numbers:", numbers)

# 2. Accessing Tuple Items

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Tuple Slicing

print("Slice:", numbers[1:4])
print("Reversed:", numbers[::-1])

# 4. Tuple Methods

values = (1, 2, 2, 3, 4)

print("Count:", values.count(2))
print("Index:", values.index(3))

# 5. Tuple Length

print("Length:", len(fruits))

# 6. Tuple Unpacking

person = ("Makhsat", 18, "Kazakhstan")

name, age, country = person

print("Name:", name)
print("Age:", age)
print("Country:", country)

# 7. Single Item Tuple

single = ("Python",)

print("Single tuple:", single)
print("Type:", type(single))

# 8. Joining Tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print("Combined:", combined)

# 9. Tuple Membership

print("Apple exists:", "apple" in fruits)

# 10. Tuple Immutability

# Tuples cannot be modified after creation.
# fruits[0] = "mango"  # TypeError
