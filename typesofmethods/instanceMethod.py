class Cars:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

     #Instance Method
    def show(self):
        print(f'Brand : {self.brand}')
        print(f'Color : {self.color}') 
        print(f'Model : {self.model}')   
c = Cars("BMW", "Purple", "M3 Series")
c.show()   #Calls instance Method using Object