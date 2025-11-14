
from tools.order_validator import  *
class Order:
    def __init__(self, id, customer_name, dish, status, total_price, delivery_id, date_time):
        self.id = id
        self.customer_name = customer_name
        self.dish = dish
        self.status = status
        self.total_price = total_price
        self.delivery_id = delivery_id
        self.date_time = date_time

    def order_registration(self):
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
        return tuple((self.id, self.customer_name, self.dish, self.status, self.total_price, self.delivery_id, self.date_time))
''' customer_name_validator(self.customer_name)
        status_validator(self.status)
        total_price_validator(self.total_price)'''
