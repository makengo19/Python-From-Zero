
# Day 06: Tuples

## Introduction
A tuple is an ordered and immutable collection of items in Python.

## 1. Creating Tuples

```python
empty_tuple = ()
fruits = ("apple", "banana", "orange")
numbers = (1, 2, 3, 4, 5)
```

## 2. Accessing Tuple Items

```python
fruits = ("apple", "banana", "orange")

print(fruits[0])
print(fruits[-1])
```

## 3. Tuple Slicing

```python
numbers = (1, 2, 3, 4, 5)

print(numbers[1:4])
print(numbers[::-1])
```

## 4. Tuple Methods

```python
numbers = (1, 2, 2, 3, 4)

print(numbers.count(2))
print(numbers.index(3))
```

## 5. Tuple Unpacking

```python
person = ("Makhsat", 18, "Kazakhstan")

name, age, country = person

print(name)
print(age)
print(country)
```

## 6. Tuples vs Lists

- Lists are mutable.
- Tuples are immutable.
- Lists use square brackets `[]`.
- Tuples usually use parentheses `()`.

## Exercises

1. Create an empty tuple.
2. Create a tuple containing five numbers.
3. Print the first and last elements.
4. Slice a tuple to get its middle elements.
5. Find the length of a tuple.
6. Count how many times a value appears.
7. Unpack a tuple into three variables.

## Summary

Today I learned how to create tuples, access elements, use slicing, work with tuple methods, and unpack tuple values.
