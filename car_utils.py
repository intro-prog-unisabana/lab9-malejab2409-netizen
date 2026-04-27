# FREEZE CODE BEGIN
from car import *

def create_car_from_input():
    car_id = input("Enter car ID (e.g., CAR001):\n")
    brand = input("Enter car brand:\n")
    year = int(input("Enter car year:\n"))
    color = input("Enter car color:\n")
    mileage = float(input("Enter mileage:\n"))
    return Car(car_id, brand, year, color, mileage)

def display_cars(car_dict):
  for car in car_dict.values():
            print(car)
# FREEZE CODE END