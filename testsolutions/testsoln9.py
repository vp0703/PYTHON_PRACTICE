# 9. OOP - BankAccount
# --------------------------------------------------
# Create a BankAccount class with deposit and withdraw methods.

# account_holder = "John"
# balance = 1000
# deposit = 500
# withdraw = 300
# Expected Output:
# Final Balance: 1200
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"{amt} rupees deposited")

    def withdraw(self, amt):
        self.balance -= amt
        print(f"{amt} rupees withdrawn")

    def show_balance(self):
        print(f"Final Balance: {self.balance}")
    
account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(300)
account.show_balance()
