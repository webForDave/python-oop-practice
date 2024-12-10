class Vehicle:

    def __init__(self, max_speed):
        self.max_speed = max_speed


    def describe(self):
        return f"This is a vehicle with a max speed of {self.max_speed}"


class Car(Vehicle):
    
    def __init__(self, max_speed, brand):
        super().__init__(max_speed)
        self.brand = brand

    def describe(self):
        return f"This is a {self.brand} vehicle"


class Bicycle(Vehicle):

    def __init__(self, max_speed, gear_count):
        super().__init__(max_speed)
        self.gear_count = gear_count
    
    def describe(self):
        return f"This bicycle has {self.gear_count} gears"


class Boat(Vehicle):

    def __init__(self, max_speed, capacity):
        super().__init__(max_speed)
        self.capacity = capacity


    def describe(self):
        return f"This is a {self.capacity} people capacity boat"
    

vehicle1 = Car(4, 'Toyota')
bicycle1 = Bicycle(3, 6)
boat1 = Boat(2, 100)
print(vehicle1.max_speed, vehicle1.brand, vehicle1.describe())
print(bicycle1.max_speed, bicycle1.gear_count, bicycle1.describe())
print(boat1.max_speed, boat1.capacity, boat1.describe())