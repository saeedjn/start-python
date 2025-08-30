try:
    a = int(input("enter a number x= "))
    b = int(input("enter a number x= "))
    result = a / b
    print(result)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("Error: Division by zreo")
finally:
    print("Good Bye")

filename = input("Enter filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program ended")
