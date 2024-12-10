class Transportation:

    def __init__(self, name):
        self.name = name


    def move(self):
        return 'This transportation moves.'
    

class Airplane(Transportation):
    
    def __init__(self, name, altitude):
        super().__init__(name)
        self.altitude = altitude

    def move(self):
        return f"The airplane moves very fast and has an altitude of about {self.altitude} meters."
    
class Train(Transportation):

    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed


    def move(self):
        return f"The train is a slow means of transportation. It travels {self.speed}mph"
    
class Boat(Transportation):

    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity 


    def move(self):
        return f"The boat has a large capacity It can carry up to {self.capacity} people for a trip."


boat1 = Boat('Kalango', 250)
print(boat1.name, boat1.move())

airplane1 = Airplane('KAR-34-F7', 250)
print(airplane1.name, airplane1.move())

train1 = Train('Jos', 250)
print(train1.name, train1.move())