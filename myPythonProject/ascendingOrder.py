grades = []
grades2 = []
numGrades = int(input('How many grades do you have? '))
lowGrade = float(input('What is the maximum grade? '))
highGrade = 0
n = 0

for i in range(0, numGrades, 1):
    x = float(input('Enter Grade: '))
    grades.append(x)
for j in range(0, numGrades, 1):
    if grades[j] < lowGrade:
        lowGrade = grades[j]
for k in range(0, numGrades, 1):
    if grades[k] > highGrade:
        highGrade = grades[k]

for l in range(n, numGrades, 1):
    for m in range(n+1, numGrades, n+1):
        if grades[l] > grades[m]:
            grades2.append(grades[m])
        if grades[l] < grades[m]:
            grades2.append(grades[l])

avgGrade = sum(grades) / numGrades
print('Your grades: ', grades2)
print('Your lowest grade: ', lowGrade)
print('Your highest grade: ', highGrade)
print('Your average ', avgGrade)

