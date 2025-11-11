from repository.payment_repository import Payment_repository


class Payment_Service:
    payment_repository = Payment_repository()

    @classmethod
    def save(cls, payment):
        return cls.payment_repository.save(payment)

    @classmethod
    def update(cls, payment):
        return cls.payment_repository.update(payment)

    @classmethod
    def delete(cls, payment):
        return cls.payment_repository.delete(payment)

    @classmethod
    def find_by_customer_id(cls, id):
        payment = cls.payment_repository.find_by_customer_id(id)
        if payment:
            return payment
        else:
            raise ValueError("Payment not found")

    @classmethod
    def find_by_status(cls, status):
        payment = cls.payment_repository.find_by_status(status)
        if payment:
            return payment
        else:
            raise ValueError("Payment not found")

    @classmethod
    def find_by_order_id(cls, order_id):
        payment = cls.payment_repository.find_by_order_id(order_id)
        if payment:
            return payment
        else:
            raise ValueError("Payment not found")

    @classmethod
    def find_by_id(cls, id):
        payment = cls.payment_repository.find_by_id(id)
        if payment:
            return payment
        else:
            raise ValueError("Payment not found")


    @classmethod
    def find_by_salary_min(cls, salary_min):
        payment = cls.payment_repository.find_by_salary_min(salary_min)
        if payment:
            return payment
        else:
            raise ValueError("Payment not found")

    @classmethod
    def get_all(cls):
        return cls.payment_repository.get_all()


'''  @classmethod
    def find_by_date_time(cls, datetime):
        payment = cls.payment_repository.find_by_date_time(datetime)
        if payment:
            return payment
        else:
            raise ValueError("Payment not found")
'''
