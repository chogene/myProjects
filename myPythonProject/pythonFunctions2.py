def tally(nums):
    x = []
    for i in range(0, nums, 1):
        myNum = float(input('Enter your number '))
        x.append(myNum)
    return x


numbers = int(input('Enter how many Number '))
y = tally(numbers)
print(y)

# write functions
# input grades
# print grades
# avg grades
# high/low grades
