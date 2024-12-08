class Order():

    number_of_order = 0

    def __init__(self, order_id, customer_name, order_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_amount = order_amount

        Order.number_of_order += 1

    def cancel_order(self):
        self.order_amount = 0


order1 = Order(1, 'David', 100)
order2 = Order(2, 'Maki', 200)
order3 = Order(3, 'Jay', 300)

order1.cancel_order()

total_revenue = order1.order_amount + order2.order_amount + order3.order_amount
print(total_revenue)