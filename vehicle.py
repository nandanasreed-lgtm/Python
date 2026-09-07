
class Vehicle:
    def __init__(self, speed, height):
        self.speed = speed
        self.height = height
    def show_traits(self):
        print("speed in miles per hour : ",self.speed)
        print("height in meters : ",self.height)
class Bus(Vehicle):
    def __init__(self, speed, weight, height, colour):
        self.speed = speed
        self.weight = weight
        self.height = height
        self.colour = colour
        super().__init__(speed, height)
    def show_traits(self):
        print("speed in miles per hour : ",self.speed)
        print("weight in pounds : ",self.weight)
        print("colour : ",self.colour)
        super().show_traits()
child = Bus(12, 20000, 3, "yellow")
child.show_traits()
print(issubclass(Bus, Vehicle))

