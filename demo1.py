class Car:

    # Constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        return f"{self.brand} {self.model} is starting..."