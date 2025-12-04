#Basic Banking System 

balance = 1000
print("Enter the following numbers to perform an operation :")
print("1: Check Balance")
print("2: Deposit")
print("3: Withdraw")
print("4: Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Balance:", balance)

    case 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Updated Balance:", balance)

    case 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Updated Balance:", balance)
        else:
            print("Insufficient Balance")

    case 4:
        print("Thank you!")

    case _:
        print("Invalid choice")