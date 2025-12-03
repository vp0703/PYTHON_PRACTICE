class Car:
    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2
    def show(self):
        print(f'lst1 : {self.lst1}')
        print(f'lst2 : {self.lst2}')
c = Car([10, 20, "Mira", 33.67], [33, 56, "Radha", 66.89])
c.show()