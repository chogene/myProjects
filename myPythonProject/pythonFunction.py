# python requires function on the top of the screen

def tally(numnum, myArray):
#    z = x + y
#    a = 23
#    b = 24
#    print(a, b)     # lives inside the function
    tot = 0
    for i in range(0, numnum, 1):
        tot = tot + myArray[i]

    return tot


# a = float(input('Please input your first number: '))
# b = float(input('Please input your second number: '))
# c = tally(a, b)     # lives outside of function
# print(a, b)
# print(c)

x = [2, 4, 6, 8, 10]
nums = 3

mySum = tally(nums, x)
print('Array Total= ', mySum)