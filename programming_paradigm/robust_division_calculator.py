class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional starting balance"""
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient"""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance"""
        print(f"Current Balance: ${self.__account_balance:.2f}")
