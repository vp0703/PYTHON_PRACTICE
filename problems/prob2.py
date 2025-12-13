# Q1 - Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
# Q2 - Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Q3 - Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Q4 - Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Q5 - Create a Bus child class that inherits from the Vehicle class. The default fare charge for any vehicle is its seating capacity multiplied by 100 (seating capacity * 100).
#      If the vehicle is a Bus instance, we need to add an extra 10% to the full fare as a maintenance charge. 
#      Therefore, the total fare for a Bus instance will be the final amount, calculated as total fare plus 10% of the total fare. 
#      (final amount = total fare + 10% of the total fare.)

class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def fullfair(self):
        return self.capacity*100
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self. capacity = capacity
    def fullfair(self):
        amt = super().fullfair()
        amt +=amt*10/100
        return amt
    def seating_capacity(self):
        return f"The seating capacity of a {self.name} bus is {self.capacity} passengers"
    
b = Bus("School", 260, 19, 50)
print(f"color : {b.color}")
print(f"Vehicle Name: {b.name}")
print(f"Speed: {b.max_speed}")
print(f"Mileage: {b.mileage}")
print(b.seating_capacity())
print("the full fair is :", b.fullfair())