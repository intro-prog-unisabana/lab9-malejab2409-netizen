class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance: 
            return -1
        else:
            self.balance -= amount
            return 0
    def _str_(self):
        account_str = str(self.account_number)
        ultimo = account_str[-2:]
        return f"Account Number: **{ultimo}\nCurrent Balance:{self.balance:.1f}"