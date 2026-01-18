class Vehicle:
    def __init__(self, name , max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class BMW(Vehicle):
    pass

car1=BMW("BMW",200,100)
print("Car name:",car1.name)
print("Car max speed:",car1.max_speed)
print("Car mileage:",car1.mileage)