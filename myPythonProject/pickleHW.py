import pickle

numStudent = int(input('How many students do you have? '))
studentName = []
studentGrade = []
i = 1

while i <= numStudent:
    x = input('Name of Student ')
    y = float(input('Grade '))
    studentName.append(x)
    studentGrade.append(y)
    i = i + 1

with open('Name_Grade.pkl', 'wb') as f:
    pickle.dump(studentName, f)
    pickle.dump(studentGrade, f)

with open('Name_Grade.pkl', 'rb') as f:
    data1 = pickle.load(f)
    data2 = pickle.load(f)

print(data1)
print(data2)

# pickled or "serialized" data into a file
