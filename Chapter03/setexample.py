S1 = set([3, 5, 6, 10, 11, 100])
S2 = set([1, 3, 5, 6, 11, 15])

print("Length of set S1 is:", len(S1))
print("Maximum value in set S1 is:", max(S1))
print("Minimum value in set S2 is:", min(S2))
print("Sum of items in set S1 is:", sum(S1))
print("Applying any() to set S1 results into:", any(S1))
print("Union of the two sets is:", S1 | S2)
print("Intersection of the two sets is:", S1 & S2)
print("Difference of S1 - S2 is:", S1 - S2)
print("Difference of S2 - S1 is:", S2 - S1)

S1.add(0)
print("The items in set S1 after adding an item are:", sorted(S1))
print("As set S1 now has a value 0, so all() will result into", all(S1))

S1.update(S2)
print("The items in set S1 after merging set S2 are:", sorted(S1))
