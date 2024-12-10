class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        return f"This is a {self.species} named {self.name}"
    

class Lion(Animal):
    def __init__(self, name, species, pride_name):
        super().__init__(name, species)
        self.pride_name = pride_name


    def describe(self):
        return f"This is a lion named {self.name} from the {self.pride_name}"
    

class Elephant(Animal):
    def __init__(self, name, species, trunk_length):
        super().__init__(name, species)
        self.trunk_length = trunk_length


    def describe(self):
        return f"This is an elephant named {self.name} with a trunk {self.trunk_length} meters long"
    

class Penguin(Animal):
    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly


    def describe(self):
        can_fly = 'cannot' if not self.can_fly else 'can'
        return f"This is a penguin named {self.name} It {can_fly} fly"
    

lion1 = Lion('Leo', 'Panther', 'Zulum')
elephant1 = Elephant('Ron', 'Mammal', 100)
penguin1 = Penguin('Rick', 'Manguu', True) 


print(lion1.describe())
print(elephant1.describe())
print(penguin1.describe())