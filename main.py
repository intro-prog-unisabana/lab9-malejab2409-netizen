from person import Person, person_data, balance_summary
from bank_account import BankAccount
def main():
    people = []  # List to store all Person objects

    while True:
        # Display menu
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        # Option 1: Add a new person
        if choice == "1":
            new_person = person_data()
            people.append(new_person)

        # Option 2: Add an account to an existing person
        elif choice == "2":
            target_name = input("Enter the person's name:").strip 
            found_person = None
            for p in people:
                if p.name == target_name:
                    found_person = p
                    break 
            if found_person:
                acc_num = int(input("Enter a 4-digit account number "))
                initial_balance = float(input("Enter the initial balance"))
                new_acc = BankAccount(acc_num, initial_balance)
                found_person.add_account(new_acc)
            else:
                print("Person not found.")

        # Option 3: Show all balances
        elif choice == "3":
            if not people:
                print("No data to show.")
            else:
                balance_summary(people)

        # Option 4: Quit
        elif choice == "4":
            print("Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

