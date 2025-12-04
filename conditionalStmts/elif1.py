#Calculating Grades

marks = float(input("Enter marks scored :"))
if(90 <= marks <= 100):
    print("You Scored A Grade")
elif(80 <= marks <=89):
    print("You Scored B Grade")
elif(70 <= marks <= 79):
    print("You Scored C Grade")
elif(60 <= marks <= 69):
    print("You Scored D Grade")
else:
    print("Fail")