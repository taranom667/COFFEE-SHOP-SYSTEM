class Delivery():
    def __init__(self, id,order_id,rider,status,address):
        self.id = id
        self.order_id = order_id
        self.rider = rider
        self.status = status
        self.address = address





    def assign_rider(rider):
       pass

    def update_status(delivery,new_status):
       delivery.status = new_status




    def validate(self):
        pass

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id,self.order_id,self.rider,self.status,self.address))



