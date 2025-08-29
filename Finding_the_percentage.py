n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sumMarks = 0

for value in range(0, 3):
    sumMarks += student_marks[query_name][value]

averageMark = sumMarks / 3

print(f"{averageMark:.2f}")