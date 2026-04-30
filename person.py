class Person:
    def _init_(self, name):
        self.name = name 
        self.cuenta = []
    def add_account(self, account):
        self.cuenta.append(account)
    def _str_(self): 
        return f"Name = {self.name}, Number of accounts = {len(self.cuenta)} "
