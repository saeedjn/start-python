numbers = [1, 2, 3, 2, 4, 5, 3, 6, 4, 7]

unique_numbers = set(numbers)

print(unique_numbers)

print("Unique numbers sorted:", sorted(unique_numbers))


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union_set = A | B
intersection_set = A & B
difference_set = A - B

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
