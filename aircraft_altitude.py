from aircraft import Aircraft
def main():
    model = input ("Enter aircraft model: ")
    my_aircraft = Aircraft(model)
    while True:
        user_input = input("Enter command (A for ascent, D for descent, X to exit): ").split()
        command = user_input[0].upper()
        if command == "X":
            break 
        feet = int(user_input[1])
        if command == "A":
            my_aircraft.climb(feet)
        elif command == "D":
            my_aircraft.descend(feet)
    print(f"Final altitude: {my_aircraft.altitude} feet")
if __name__ == "__main__":
    main()