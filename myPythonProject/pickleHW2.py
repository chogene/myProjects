import pickle

nameCheck = input("Who's grade do you want to check? ")
i = 0

with open('Name_Grade.pkl', 'rb') as f:
    data1 = pickle.load(f)
    data2 = pickle.load(f)


while i < len(data1):
    if nameCheck == data1[i]:
        print(data1[i])
        print(data2[i])
    i = i + 1

print(data1, data2)

# len(list) to check length of list
# i can "deserialize" data in a different python program
# fin 7/18/2024 1:57 am