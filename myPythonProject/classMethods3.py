from classMethods2 import Car

# do not need to use 'self'

car_1 = Car('Chevy', 'Corvette', 2021, 'blue')
car_2 = Car('Ford', 'Mustang', 2022, 'red')

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_2.stop()


#  object = a "bundle" of attributes (variables) methods (functions)
#  class = "blueprint" used to design structure and layout of an object
