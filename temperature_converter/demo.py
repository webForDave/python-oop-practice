class Temperature:

    def init(self):
        ...


    @classmethod
    def to_celcuis(cls, temperature):
        cls.temperature = temperature
        return f"{int((cls.temperature - 32) * (5/9))}C"
    
    @classmethod
    def to_fahrenheit(cls, temperature):
        cls.temperature = temperature
        return f"{int(cls.temperature * (9/5)) + 32}F"
    
    
    

print(Temperature.to_celcuis(32))
print(Temperature.to_fahrenheit(30))