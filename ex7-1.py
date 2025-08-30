numbers = [1, 2, 3, 2, 4, 5, 3, 6, 4, 7]
maxNumber = max(numbers)
print(maxNumber)


def total_number(*n):
    total = sum(n)
    return total

result = total_number(*numbers)
print(result)