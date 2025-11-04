class Payment:
    def __init__(self,payment_id,order,total_price,payment_type,date_time,customer_id,payment_status,factor_id):
       self.payment_id = payment_id
       self.order = order
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
        return tuple((self.payment_id,self.order,self.total_price,self.payment_type,self.date_time,self.customer_id,self.status,self.factor_id))
