"""Day 05 — Lists."""

topics = "print,strings,lists".split(",")
print("Topics:", topics)
print("Count:", len(topics))
print("First and last:", topics[0], topics[-1])
print("After the first topic:", topics[1:])
print("Contains strings:", "strings" in topics)

groceries = ["bread", "milk", "eggs"]
groceries[1] = "oat milk"
groceries.append("apples")
groceries.insert(1, "rice")
groceries.remove("eggs")
last_item = groceries.pop()
print("Removed from the end:", last_item)
print("Groceries:", groceries)

scores = [18, 12, 20]
same_scores = scores
same_scores.append(15)
ranking = scores.copy()
ranking.sort(reverse=True)
print("Original scores:", scores)
print("Ranked scores:", ranking)
