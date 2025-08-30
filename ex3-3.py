
numbers = []


while True :
    num = int(input("enter your number: "))
    if num > 0 :
        numbers.append(num)
    else : 
        total = sum(numbers)
        print("Numbers: ",numbers)
        print(total)
        break
