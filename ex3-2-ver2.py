numbers = []
avg = 0
total = 0
maxNumber = 0

for i in range(1,6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

maxNumber = max(numbers)
avg = sum(numbers) / len(numbers)

print(f"Largest number: {maxNumber}")
print(f"average is: {avg}")

