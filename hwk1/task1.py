"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):

        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, item_and_price):
        self.total_items.update(item_and_price)

    def remove_item(self, item):
        self.total_items.pop(item)

    def apply_discount(self, monetary_amount):
        self.discount += monetary_amount

    def get_total(self):
        total_before_discount = sum(self.total_items.values())
        self.total_price = total_before_discount - self.discount
        return self.total_price

    def show_items(self):
        for item, price in self.total_items.items():
            print(f"{item} ... £{price:.2f}")

    def reset_register(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0


# Example code run
register = CashRegister()

# customer buying/adding items at the register
register.add_item({'chocolate': 5.40})
register.add_item({'milk': 2.50})
register.add_item({'oranges': 3.00})
register.add_item({'butter': 3.70})

# customer choosing not to buy the butter
register.remove_item('butter')

# 2 pound discount for chocolate
register.apply_discount(2.00)

# total price
print(register.get_total())

# the number of items and prices
register.show_items()

# reset the register
register.reset_register()