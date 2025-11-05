class Customer:
    def __init__(self, customer_id, first_name, last_name, phone_number, order_id):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.order_id = order_id

    def validate(self):
        pass



    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.customer_id, self.first_name, self.last_name, self.phone_number, self.order_id))

    def full_name(self):
        return f"{self.first_name} {self.last_name}"