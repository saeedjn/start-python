persons = []

for i in range(5) :
    person = {} 
    person["name"] = input("enter your name: ")
    person["age"] = int(input("enter your age: "))
    persons.append(person)

print(persons)