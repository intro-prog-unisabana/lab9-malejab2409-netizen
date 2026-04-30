class Car:
    def __init__(self, car_id, brand, year, color, mileage=0.0):
        self.car_id = car_id
        self.brand = brand
        self.year = year
        self.color = color
        self.mileage = mileage
    def change_color(self, new_color):
        self.color = new_color
    def drive(self, miles):
        self.mileage += miles
    def __str__(self):
        return f"{self.car_id} - {self.year} {self.color} {self.brand} with {self.mileage} miles"
my_car = Car("CAR001", "Toyota", "2007", "Azul", "0.0")
