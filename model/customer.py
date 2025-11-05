class Customer:
    def __init__(self, id, first_name, last_name, phone_number, order_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.order_id = order_id

    def validate(self):
        pass

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.first_name, self.last_name, self.phone_number, self.order_id))

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
