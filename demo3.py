from abc import ABC, abstractmethod

class Appliance(ABC):
    def operate(self):
        pass


class WashingMachine(Appliance):
    def operate(self):
        return f'Washing machine from {self}'
    
    def __str__(self):
        return 'Washing machine'
    

class Microwave(Appliance):
    def operate(self):
        return f"Microwave from {self}"
    