class School:
    Sname = "R.M.E.S"
    city = "solapur"

class Stu1(School):
    # def __init__(self, stunm, stuclass):
    #     self.stunm = stunm
    #     self.stuclass = stuclass
    def stu1(self):
        print("Student name : Mira")
        print("class : 5th")
        print("Marks scored : 89")
        print("Promoted for 6th class\n")
    
class Stu2(School):
     def stu2(self):
       print("Student name : Radha")
       print("class : 6th")
       print("Marks scored : 78")
       print("Promoted for 7th class\n")

class Stu3(School):
     def stu3(self):
       print("Student name : Ram")
       print("class : 4th")
       print("Marks scored : 90")
       print("Promoted for 5th class\n")

s = Stu1()
print("School name is :", s.Sname)
print("School is in :", s.city, "\n")
s.stu1()
ss = Stu2()
ss.stu2()
sss = Stu3()
sss.stu3()