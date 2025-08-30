

score = int(input("please enter your score : "))

if score >= 90 :
    message = "Great"
elif score >= 70 :
    message = "Good"
elif score >= 50 :
    message = "Not bad"
else:
    message = "Bad"

print(message)

