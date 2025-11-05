class Payment:
    def __init__(self, id, order_id, total_price, payment_type, date_time, customer_id, status, factor_id):
        self.id = id
        self.order_id = order_id
        self.total_price = total_price
        self.payment_type = payment_type
        self.date_time = date_time
        self.customer_id = customer_id
        self.status = status
        self.factor_id = factor_id

    def validate(self):
        pass

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((
                     self.id, self.order_id, self.total_price, self.payment_type, self.date_time, self.customer_id,
                     self.status, self.factor_id))
