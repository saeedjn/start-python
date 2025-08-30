evenNumbers1 = []
evenNumbers2 = []

for n in range(1,51) :
    if n % 2 == 0 :
        evenNumbers1.append(n)

print(evenNumbers1)


n = 1 

while n < 51 :
    if n % 2 == 0 :
        evenNumbers2.append(n)
    n = n + 1 

print(evenNumbers2)


