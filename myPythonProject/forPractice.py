# get 4 grades and then read throught htem
# pput them in an array?
x = []

numOfGrades = int(input('How many grades do you have? '))

for grade in range(0, numOfGrades, 1):
    y = float(input('Input Grade '))
    x.append(y)  # put each grade in x
for i in range(0, numOfGrades,1):
    print(x[i])

avgGrade = sum(x) / numOfGrades
print('Average is: ', avgGrade)

# ask user for how many grades, input and take avg - finished 7/17/24 1:42 am
# take avg grades -> what is the highest grade? lowest