class Table:
    def __init__(self, number,order_id,quantity,location):
        self.number = number
        self.order_id = order_id
        self.quantity = quantity
        self.location = location

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.number, self.order_id, self.quantity, self.location))
