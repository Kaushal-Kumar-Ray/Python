# Base class (Parent)
class Vehicle:
    def show(self):
        return "This is a vehicle"

# First child class (inherits from Vehicle)
class Car(Vehicle):
    def car_details(self):
        return "This is a Car"

# Second child class (inherits from Vehicle)
class Bike(Vehicle):
    def bike_details(self):
        return "This is a Bike"

# Third child class (inherits from both Car and Bike → Multiple Inheritance)
class HybridCar(Car, Bike):
    def hybrid_details(self):
        return "This is a Hybrid Car"

# Creating an object of HybridCar
obj = HybridCar()

# Accessing methods
print(obj.show())          # From Vehicle
print(obj.car_details())   # From Car
print(obj.bike_details())  # From Bike
print(obj.hybrid_details()) # From HybridCar
