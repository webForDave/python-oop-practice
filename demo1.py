class Car:

    # Constructor
    def __init__(self, brand, model, year, engine_status):
        self.brand = brand
        self.model = model
        self.year = year
        self.__engine_status = engine_status

    def start(self):
        return f"{self.brand} {self.model} is starting..."
    
    def check_engine(self):
        if self.__engine_status == 'not checked':
            self.__engine_status = 'faulty'
            return f"This engine is {self.__engine_status}"
        return f"This engine is good to go"
    