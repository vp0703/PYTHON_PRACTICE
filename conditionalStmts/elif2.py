#Ticket

age = float(input("Enter age :"))
if(age < 5):
    print("Free")
elif(5 <= age <= 12):
    print("child Ticket")
elif(13 <= age <= 60):
    print("Adult Ticket")
else:
    print("Senior citizen discount")


   