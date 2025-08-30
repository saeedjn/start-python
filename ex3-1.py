numbers = []

for i in range(1,6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

for n in numbers:
    print(n)

print("numbers: ", ",".join(map(str,numbers)))