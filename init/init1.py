class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def show(self):
        print(f"Brand : {self.brand}")
        print(f"Color : {self.color}")
c = Car("BMW", "Green")
c.show()