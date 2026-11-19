# Day 08 — Python Dictionaries

# Create a dictionary and look up values.
student = {"name": "Aruzhan", "score": 85}
print("Student:", student["name"])
print("City:", student.get("city", "Unknown"))
print("Has a score?", "score" in student)

# Add an entry, update a value, and remove an entry.
student["city"] = "Almaty"
student["score"] = 90
removed_city = student.pop("city")
print("Removed city:", removed_city)

# Read keys, values, and key–value pairs.
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
for key, value in student.items():
    print(key, value)

# Count repeated words.
words = "python java python javascript java python".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print("Word counts:", counts)
