class Discount:

    def __init__(self):
        ...


    @classmethod
    def calculate(cls, price, discount_percentage):
        cls.price = price
        cls.discount_percentage = discount_percentage
        return cls.price - cls.discount_percentage
    

print(Discount.calculate(100, 20))