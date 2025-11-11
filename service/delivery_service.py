from repository.delivery_repository import Delivery_repository


class Delivery_Service:
    delivery_repository = Delivery_repository()

    @classmethod
    def save(cls, delivery):
        return cls.delivery_repository.save(delivery)

    @classmethod
    def update(cls, delivery):
        return cls.delivery_repository.update(delivery)

    @classmethod
    def delete(cls, delivery):
        return cls.delivery_repository.delete(delivery)

    @classmethod
    def find_by_rider(cls, rider):
        delivery = cls.delivery_repository.find_by_rider(rider)
        if delivery:
            return delivery
        else:
            raise ValueError("Delivery not found")

    @classmethod
    def find_by_status(cls,status):
        delivery = cls.delivery_repository.find_by_status(status)
        if delivery:
            return delivery
        else:
            raise ValueError("Delivery not found")



    @classmethod
    def find_by_order_id(cls, order_id):
        delivery = cls.delivery_repository.find_by_order_id(order_id)
        if delivery:
            return delivery
        else:
            raise ValueError("Delivery not found")

    @classmethod
    def find_by_id(cls, id):
        delivery = cls.delivery_repository.find_by_id(id)
        if delivery:
            return delivery
        else:
            raise ValueError("Delivery not found")


    @classmethod
    def get_all(cls):
        return cls.delivery_repository.get_all()
