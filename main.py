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
            pass

        # Option 2: Add an account to an existing person
        elif choice == "2":
            pass

        # Option 3: Show all balances
        elif choice == "3":
            pass

        # Option 4: Quit
        elif choice == "4":
            print("Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

