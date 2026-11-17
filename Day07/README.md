# Day 07 — Python Sets

## Topics
- Creating sets
- Adding and removing elements
- Set operations
- Union and intersection
- Difference and symmetric difference
- Subsets and supersets

## What is a Set?

A set is an unordered collection of unique elements.

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}
fruits = {"apple", "banana", "orange"}
empty_set = set()
fruits.add("mango")
fruits.remove("banana")
fruits.discard("grape")
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric difference
python3 Day07/examples.py


cat > Day07/README.md <<'EOF'
# Day 07 — Python Sets

## Topics
- Creating sets
- Adding and removing elements
- Set operations
- Union and intersection
- Difference and symmetric difference
- Subsets and supersets

## What is a Set?
A set is an unordered collection of unique elements.

Example:
    numbers = {1, 2, 3, 3, 4}
    print(numbers)

## Creating Sets
    fruits = {"apple", "banana", "orange"}
    empty_set = set()

## Adding and Removing Elements
    fruits.add("mango")
    fruits.remove("banana")
    fruits.discard("grape")

## Set Operations
    a = {1, 2, 3}
    b = {3, 4, 5}

    print(a | b)  # Union
    print(a & b)  # Intersection
    print(a - b)  # Difference
    print(a ^ b)  # Symmetric difference

## Practice
Complete the exercises in tasks.py.

## Summary
- Sets contain unique elements.
- Sets are unordered.
- Sets do not support indexing.
- Sets support mathematical operations.
