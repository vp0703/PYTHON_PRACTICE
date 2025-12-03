class Cars:
    color = "purple"
    Model = "M3 Series"
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
    
    @classmethod      #decorator
    def new(cls, newColor, newModel):
        cls.newColor = newColor    #Modifies class variable
        cls.newModel = newModel    #Modifies class variable
    
print(Cars.color)
print(Cars.Model)
Cars.new("Black", "M4")
print(Cars.newColor)
print(Cars.newModel)
