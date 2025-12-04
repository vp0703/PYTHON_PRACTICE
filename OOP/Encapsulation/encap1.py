class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

# Example usage
account = BankAccount(100)
account.deposit(50)
print("Balance is :", account.get_balance())  # Accessing balance through a public method