import json

students = []

for i in range(1,5):
    person = {}
    person["name"] = input(f"please enter name {i}: ")
    person["score"] = int(input(f"please enter score of {person['name']}:"))
    students.append(person)

with open("score.txt",'w') as scoreFile:
    json.dump(students, scoreFile)


with open("score.txt", 'r') as scoreFile:
    studentsFile = json.load(scoreFile)

for student in studentsFile:
    print(f"{student['name']} : {student['score']}")

totalScore = sum(student['score'] for student in studentsFile)
avgScore = totalScore / len(studentsFile)
maxScore = max(studentsFile, key= lambda x: x['score'])

print(f"Avg Score: {avgScore}")
print(f"Max Score: {maxScore['score']} by {maxScore['name']}")

