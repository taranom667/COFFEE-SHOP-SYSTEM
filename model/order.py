from customer import Customer
from dish import Dish
from payment import  Payment

class Order:
    def __init__(self, order_id, customer_name, dish, status,total_price,delivery,date_time):
        self.order_id = order_id
        self.customer_name= customer_name
        self.dish = dish
        self.status = status
        self.total_price = total_price
        self.delivery = delivery
        self.date_time = date_time

    def order_registration(self):
        pass

    def add_item(self):
        pass

    def delete_item(self):
        pass

    def edit(self):
        pass

    def calculate_total_price(self):
        pass

    def set_status(self):
        pass


    def validate(self):
        pass

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.customer_id, self.first_name, self.last_name, self.phone_number, self.order_id))
