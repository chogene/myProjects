class Car:
# replace 'self' w/ car_1 car_2 etc
    def __init__(self, make, model, year, color):  # constructor. assign 'Car' object unique variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('This ' + self.model + ' is driving')

    def stop(self):
        print('This ', self.model, ' is stopped')
