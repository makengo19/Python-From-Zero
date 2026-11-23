"""Day 10: Dictionaries — runnable beginner-friendly examples."""


def main():
    # 1. Create a dictionary.
    student = {"name": "Amina", "age": 19, "major": "IT"}
    print("Student:", student)

    # 2. Read values. get() is safe for missing keys.
    print("Name:", student["name"])
    print("City:", student.get("city", "Unknown"))

    # 3. Add and update values.
    student["city"] = "Almaty"
    student["age"] = 20
    print("Updated student:", student)

    # 4. Remove a key.
    removed_city = student.pop("city")
    print("Removed city:", removed_city)

    # 5. Loop through key–value pairs.
    scores = {"python": 95, "math": 90, "english": 88}
    for subject, score in scores.items():
        print(f"{subject}: {score}")

    print("Subjects:", list(scores.keys()))
    print("Scores:", list(scores.values()))
    print("Has python score?", "python" in scores)

    # 6. Dictionary comprehension.
    squares = {number: number ** 2 for number in range(1, 6)}
    print("Squares:", squares)

    # 7. Nested dictionaries.
    users = {
        "ali": {"age": 18, "active": True},
        "amina": {"age": 19, "active": False},
    }
    print("Ali's age:", users["ali"]["age"])

    # 8. Count how many times each word appears.
    words = ["python", "java", "python", "git", "java", "python"]
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print("Word counts:", counts)


if __name__ == "__main__":
    main()
