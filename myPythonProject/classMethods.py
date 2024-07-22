class Rectangle:
    def __init__(self, c, l, w):
        self.color = c
        self.length = l
        self.width = w

    def area(self):
        self.area = self.length * self.width
        return self.area

    def per(self):
        self.perimeter = 2*self.length + 2*self.width
        return self.perimeter

    def diag(self):
        self.diagonal = (self.width**2 + self.length**2)**(1/2)
        return self.diagonal

    def vol(self, h):  # i can add another variable? ONLY for vol because a regular rectangle doesnt have height
        self.height = h
        self.volume = self.width * self.length * self.height
        return self.volume


myRect1 = Rectangle('red', 3, 4)  # create the myRect1 object
print(myRect1.color)
myRect2 = Rectangle('blue', 3, 2)
print(myRect2.color)
area = myRect1.area()
print('myRect1 area = ', area)
print('myRect1 length = ', myRect1.length)
print(myRect1.per())
print(myRect1.diag())
x = float(input('Enter the height of the box: '))
volume = myRect1.vol(x)
print(volume)

#  class students
#  object (st1,2,3) first/last name. student age
#  method inputs grades
