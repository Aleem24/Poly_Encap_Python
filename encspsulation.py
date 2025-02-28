class Vehicle:
    def __init__(self, speed):
        self._maxSpeed = speed

    def display(self):
        return f"It can run upto {self.maxspeed} kph speed"
    
class Protected:
    def __init__(self):
        self._maxspeed = 200

class Car(Protected):
    def display2(self):
        return f"It can run upto {self._maxspeed} kph speed"
    
obj = Car()

print(obj._maxspeed)
print(obj.display2())