grades = []
# subjects = []
numGrades = int(input('Enter number of grades: '))


def inputGrades(y):
    for i in range(0, y, 1):
        text = 'Enter grade #', y
        grade = float(input('Enter grade: '))
        # sub = input('Enter subject: ')
        grades.append(grade)
        # subjects.append(sub)
    return grades


def avgGrades(x):
    avg = sum(x) / numGrades
    return avg


def highLow(x):
    lowest = float(input('Enter the max grade: '))
    highest = 0
    for i in range(0, numGrades, 1):
        if x[i] < lowest:
            lowest = x[i]
    for j in range(0, numGrades, 1):
        if x[j] > highest:
            highest = x[i]

    return highest, lowest


def ascending(x):
    for q in range(0, numGrades, 1):
        for i in range(0, numGrades, 1):
            swp = 0
            if x[i] > x[q]:
                swp = x[q]
                x[q] = x[i]
                x[i] = swp
    return x


z = inputGrades(numGrades)
order = ascending(grades)
j = round(avgGrades(grades), 2)
high, low = highLow(grades)

print('Top grade is :', high, 'Bottom grade is:', low)
print('Average grade is', j)
print('Grades:', order)
