#Single Inheritance

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year  = year

class Car(Vehicle):
    def __init__(self, brand, year, model):
        self.model = model
        super().__init__(brand, year)
        

    def show(self):
        print(f'{self.brand}, \n{self.year}, \n{self.model}')

c = Car("BMW", "2020", "M3")
c.show()   
        