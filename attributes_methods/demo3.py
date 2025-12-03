#Example 3:using Dictionary

class Dict:
    dict1 = {"name" : "Mira", "cls" : "XI", "mrks" : 98.40, "Grade" : "A++"}
    dict2 = {"name" : "Radha", "cls" : "XI", "mrks" : 90.40, "Grade" : "A+"}
    dict3 = {"name" : "Sham", "cls" : "XI", "mrks" : 82.00, "Grade" : "A"}
    def display(self):
        print(self.dict1)
        print(self.dict2)
        print(self.dict3)
d = Dict()
d.display()