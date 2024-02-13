class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =  0
    def describe_car(self):
        return f"{self.make} {self.model} {self.year}"
    def read_odometer(self):
        return f"This car has {self.odometer_reading} mileage."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print ("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

car1 = Car("Ford", "Mustang", 2022)
print(car1.describe_car())
print(car1.read_odometer())
car1.update_odometer(100)
print(car1.read_odometer())
