students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted({s[1] for s in students})
secondLowest = scores[1]

samePointStudents = []

for student in students:
    if student[1] == secondLowest:
        samePointStudents.append(student[0])

sortedSamePointStudents = sorted(samePointStudents)

for student in sortedSamePointStudents:
    print(student)