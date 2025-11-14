from repository.order_repository import Order_repository


class Order_Service:
    order_repository = Order_repository()

    @classmethod
    def save(cls, order):
        return cls.order_repository.save(order)

    @classmethod
    def update(cls, order):
        return cls.order_repository.update(order)

    @classmethod
    def delete(cls, order):
        return cls.order_repository.find_by_id(order)

    @classmethod
    def find_by_customer_name(cls, name):
        order = cls.order_repository.find_by_customer_name(name)
        if order:
            return order
        else:
            raise ValueError("Order not found")

    @classmethod
    def find_by_status(cls, status):
        order = cls.order_repository.find_by_status(status)
        if order:
            return order
        else:
            raise ValueError("Order not found")

    @classmethod
    def find_by_delivery_id(cls, id):
        order = cls.order_repository.find_by_delivery_id(id)
        if order:
            return order
        else:
            raise ValueError("Order not found")

    @classmethod
    def find_by_id(cls, id):
        order = cls.order_repository.find_by_id(id)
        if order:
            return order
        else:
            raise ValueError("Order not found")

    @classmethod
    def get_all(cls):
        return cls.order_repository.get_all()
