"""Day 04 — Strings."""

# Clean the input before using it in a label.
raw_name = "  dAnA PARK  "
name = raw_name.strip().title()
room_code = "b204".upper()
print(f"{name} | Room {room_code}")

# Read parts of the code by position.
print("First character:", room_code[0])
print("Room number:", room_code[1:])
print("Reversed code:", room_code[::-1])

# Check, replace, split, and join.
filename = "draft_notes.txt"
print(filename.endswith(".txt"))
print(filename.replace("draft", "final"))
tags = "reading,writing,drawing".split(",")
print(" / ".join(tags))
