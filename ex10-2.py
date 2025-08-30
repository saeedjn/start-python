import json

try:
    students = []
    lenStudents = int(input("How many Student? "))
    for i in range(lenStudents):
        student = {}
        student["name"] = input(f"enter name Student {i+1}: ")
        student["score"] = int(input(f"enter score student {i+1}: "))
        students.append(student)

    with open("student.json", 'w') as studentFile:
        json.dump(students, studentFile)
        print("write Done")

    with open("student.json", 'r') as studentFile:
        content = json.load(studentFile)
        print("\nStudent List:")
        for student in content:
            print(f"- {student['name']} : {student['score']}")
        totalScore = sum(student['score'] for student in content)
        avgScore = totalScore / len(content)
        maxScore = max(content, key= lambda x: x['score'])
        print(f"Avg Score: {round(avgScore,2)}")
        print(f"Max Score: {maxScore['score']} by {maxScore['name']}")

except ValueError:
    print("Error: Please enter a valid number")

except FileNotFoundError:
    print("Error: file not found")

finally:
    print("Have Good time")

