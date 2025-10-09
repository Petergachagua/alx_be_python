class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default is 0)."""
        self.account_balance = initial_balance
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance}")
