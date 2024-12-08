class Customer:

    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def add_to_cart(self, product, quantity):
        self.cart[product] = quantity
