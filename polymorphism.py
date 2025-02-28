# It is the third pillar 

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
    def move(self):
        print("Move")


class Car(Vehicle):
    pass

class Bike(Vehicle):
    def move(self):
        print("Ride")

class Plane(Vehicle):
    def move(self):
        print("Fly")


# Create an object

car1 = Car("Tesla", "Model 3")

bike1 = Bike("Veloce", "inferno")

plane1 = Plane("Boeing", "777")

for x in (car1, bike1, plane1):
    x.move()
    print(x.brand)
    print(x.model)