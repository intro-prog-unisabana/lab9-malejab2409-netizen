import car_utils, car
def main():
    cars = {}  # Dictionary to store cars with car_id as key and car objects as values

    while True:
        print("\nMenu:")
        print("1. Add a new car")
        print("2. View all cars")
        print("3. Drive a car")
        print("4. Paint a car")
        print("5. Exit")

        choice = input("Choose an option:\n")

        if choice == '1':
           


        elif choice == '2':
          """TODO: Call the appropriate function from utils.py to display
          all the cars in the cars dictionary."""

        elif choice == '3':
          car_id = input("Enter the car ID to drive:\n")
          miles = float(input("How many miles to drive?\n"))
          """TODO: Look up the car in the dictionary, call the appropriate
          class method to increase the mileage of the car, and print the car."""
          
        elif choice == '4':
          car_id = input("Enter the car ID to paint:\n")
          new_color = input("Enter the new color:\n")
          """TODO: Look up the car in the dictionary, call the appropriate
          class method to change the color of the car, and print the car."""

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
