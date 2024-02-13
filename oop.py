class Car:

     def __init__(self, make, model, year, colour) :
         self.make = make
         self.model = model
         self.year = year
         self.colour = colour
     def describe_car(self):
         #describe-car is an method
         print(f"The car is a {self.make} {self.model} manufactured in {self.year}. ")
         print(f"It is {self.colour} in colour.")
myobj = Car("Ford", "Mustang", 2022, "red")
myobj.describe_car()

myobj2 = Car("Subaru", "Impreza", 2013, "green")
myobj2.describe_car()

