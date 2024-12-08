class Customer:

    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def add_to_cart(self, product, quantity):
        products = ['bread', 'sugar', 'garri']
        if product not in products:
            print(f'{product} is not in store')
        else:
            self.cart[product] = quantity

    def remove_from_cart(self, product):
        del self.cart[product]

    def checkout(self):
        prices = {'bread': 100, 'sugar': 50, 'garri': 200}
        total = []

        for item, price in prices.items():
            for g, q in self.cart.items():
                if item in g:
                    total.append(price * q)
        return f"Total: {sum(total)}"
        


customer1 = Customer('Dave', {})

print(customer1.cart)

customer1.add_to_cart('bread', 5)
customer1.add_to_cart('sugar', 5)
customer1.add_to_cart('garri', 10)
print(customer1.cart)

print(customer1.checkout())