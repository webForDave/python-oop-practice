class Customer:

    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def add_to_cart(self, product, quantity):
        self.cart[product] = quantity

    def remove_from_cart(self, product):
        del self.cart[product]


customer1 = Customer('Dave', {'Bread': 4, 'Sugar': 3})
print(customer1.cart)

try:
    customer1.remove_from_cart('Sugar')
except KeyError:
    print('No key')
print(customer1.cart)