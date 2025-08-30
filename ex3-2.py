numbers = []
avg = 0
total = 0
maxNumber = 0

for i in range(1,6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

for num in numbers:
    total += num
    if num > maxNumber:
        maxNumber = num

avg = total / len(numbers)

print(f"Largest number: {maxNumber}")
print(f"average is: {avg}")

