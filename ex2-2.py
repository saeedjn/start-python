
for student_number in range(1,6):
    score = int(input(f"please enter student {student_number} score : "))
    if score >= 90 :
        message = "Great"
    elif score >= 70 :
        message = "Good"
    elif score >= 50 :
        message = "Not bad"
    else:
        message = "Bad"
    print(message)
    print("------------------")


