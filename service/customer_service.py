from repository.customer_repository import Customer_repository


class Customer_Service:
    customer_repository = Customer_repository()

    @classmethod
    def save(cls, customer):
        return cls.customer_repository.save(customer)

    @classmethod
    def update(cls, customer):
        return cls.customer_repository.update(customer)

    @classmethod
    def delete(cls, customer):
        return cls.customer_repository.delete(customer)

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        customer = cls.customer_repository.find_by_firstname_and_lastname(firstname, lastname)
        if customer:
            return customer
        else:
            raise ValueError("Customer not found")

    @classmethod
    def find_by_phone_number(cls, phone_number):
        customer = cls.customer_repository.find_by_phone_number(phone_number)
        if customer:
            return customer
        else:
            raise ValueError("Customer not found")


    @classmethod
    def find_by_order_id(cls, order_id):
        customer = cls.customer_repository.find_by_order_id(order_id)
        if customer:
            return customer
        else:
            raise ValueError("Customer not found")

    @classmethod
    def find_by_id(cls, id):
        customer = cls.customer_repository.find_by_id(id)
        if customer:
            return customer
        else:
            raise ValueError("Customer not found")


    @classmethod
    def get_all(cls):
        return cls.customer_repository.get_all()
