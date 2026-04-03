"""
Create a base class Vehicle with a method move() and two subclasses Car and Bicycle. Override the move() method in both subclasses. The Car should print ""Driving on the road"", and the Bicycle should print ""Pedaling on the road"". Demonstrate polymorphism by calling the move() method on both objects.		
"""

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

def demonstrate_movement(vehicle):
    vehicle.move()

car = Car()
bicycle = Bicycle()
demonstrate_movement(car)
demonstrate_movement(bicycle)