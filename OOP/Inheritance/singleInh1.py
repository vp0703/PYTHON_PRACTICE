#Single Inheritance

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year  = year

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def show(self):
        print(f'{self.brand}, \n{self.year}, \n{self.model}')

c = Car("BMW", "2020", "M3")
c.show()   
        