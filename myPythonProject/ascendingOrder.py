grades = []
grades2 = []
numGrades = int(input('How many grades do you have? '))
lowGrade = float(input('What is the maximum grade? '))
highGrade = 0
n = 0
swp = 0

for i in range(0, numGrades, 1):
    x = float(input('Enter Grade: '))
    grades.append(x)
for j in range(0, numGrades, 1):
    if grades[j] < lowGrade:
        lowGrade = grades[j]
for k in range(0, numGrades, 1):
    if grades[k] > highGrade:
        highGrade = grades[k]

for l in range(0, numGrades-1, 1):
    for m in range(0, numGrades-1, 1):
        if grades[m] > grades[m+1]:
            swp = grades[m]
            grades[m] = grades[m+1]
            grades[m+1] = swp



avgGrade = sum(grades) / numGrades
print('Your grades: ', grades)
print('Your lowest grade: ', lowGrade)
print('Your highest grade: ', highGrade)
print('Your average ', avgGrade)


# 89 68 99 95 60
#
# FIRST LOOP
# it 1
# 68 89 99 95 60
# it 2
# 68 89 99 95 60
# it 3
# 68 89 95 99 60
# it 4
# 68 89 95 60 99
#
# think about how the numbers swap and how many times you need to swap them

