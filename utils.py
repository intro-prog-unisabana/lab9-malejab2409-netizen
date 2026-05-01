from bank_account import BankAccount
from person import Person
def person_data():
    name= input("Enter the person's name:")
    person = Person(name)
    while True:
        numero_cuenta = int(input("Enter a 4-digit account number:"))
        saldo_inicial = float(input("Enter the initial balance:"))
        cuenta = BankAccount(numero_cuenta, saldo_inicial)
        person.accounts.append(cuenta)
        añadir = input("Are you done adding accounts? (yes/no):")
        if añadir == "yes":
            break
    return person 
def balance_summary(person_list):
        for person in person_list:
            total = 0
            for account in person.accounts: 
                total += account.balance
            print(f"{person.name} : {total:.2f}")
