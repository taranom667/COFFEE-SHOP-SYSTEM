from customer import Customer
from dish import Dish
from payment import  Payment

class Order:
    def __init__(self, order_id, customer_id, dish, status,payment_status,total_price):
        self.order_id = order_id
        self.customer_id = customer_id
        self.dish = dish
        self.status = status
