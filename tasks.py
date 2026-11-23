"""Day 10: Dictionaries — practice tasks. Complete each TODO yourself.

Run: python3 Day10/tasks.py
"""


def main():
    # Task 1 — Student profile
    # Create a dictionary with keys: name, age, university.
    # Print the name and the number of key–value pairs.
    # TODO: Write your code here.

    # Task 2 — Update a dictionary
    student = {"name": "Ali", "age": 18}
    # Add "city": "Almaty"; change age to 19; print student.
    # TODO: Write your code here.

    # Task 3 — Safe lookup
    phone_book = {"Amina": "12345", "Dias": "67890"}
    # Ask for a name or set name = "Nura".
    # Use .get() to print the number or "Not found".
    # TODO: Write your code here.

    # Task 4 — Calculate average score
    grades = {"math": 85, "python": 95, "english": 90}
    # Compute and print the average of all values.
    # TODO: Write your code here.

    # Task 5 — Word frequency
    words = ["cat", "dog", "cat", "bird", "dog", "cat"]
    # Create a frequency dictionary, e.g. {"cat": 3, ...}.
    # TODO: Write your code here.

    # Task 6 — Dictionary comprehension
    # Create {1: 1, 2: 4, 3: 9, ..., 10: 100} using comprehension.
    # TODO: Write your code here.

    # Task 7 — Nested dictionaries
    users = {
        "user1": {"name": "Ali", "active": True},
        "user2": {"name": "Amina", "active": False},
        "user3": {"name": "Dias", "active": True},
    }
    # Print only the names of active users.
    # TODO: Write your code here.

    # Task 8 — Inventory
    inventory = {"apple": 5, "banana": 3, "orange": 0}
    # Add 2 bananas, remove items with stock 0, and print inventory.
    # Hint: Do not change the dictionary size while iterating over it directly.
    # TODO: Write your code here.

    print("Day 10 tasks are ready. Replace the TODO comments with your solutions!")


if __name__ == "__main__":
    main()
