numGrades = int(input('How many grades? '))
grades = []
j = 1
i = 0

while j <= numGrades:
    j = j + 1
    x = float(input('Enter a grade: '))
    grades.append(x)

while i < numGrades:
    print(grades[i])
    i = i + 1
print(grades)

# while loops -> keep in mind when there are x amount in list, it is 0~x-1
# finished 7/18/2024 1:25am
