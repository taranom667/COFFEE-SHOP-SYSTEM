from model.payment import Payment
from service.payment_service import Payment_Service
from tools.logging1 import Logger


class Payment_Controller:
    @classmethod
    def save(cls, order_id, total_price, payment_type, date_time, customer_id, status, factor_id):
        try:
            payment = Payment(None, order_id, total_price, payment_type, date_time, customer_id, status, factor_id)
            payment.validate()
            payment = Payment_Service.save(payment)
            Logger.info(f"Payment {payment} saved")
            return True, f"Payment Saved Successfully"
        except Exception as e:
            Logger.error(f"Payment Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, order_id, total_price, payment_type, date_time, customer_id, status, factor_id):
        try:
            payment = Payment(id, order_id, total_price, payment_type, date_time, customer_id, status, factor_id)
            payment.validate()
            payment = Payment_Service.update(payment)
            Logger.info(f"Payment {payment} updated")
            return True, "Payment Updated Successfully"
        except Exception as e:
            Logger.error(f"Payment Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, id):
        try:
            payment = Payment_Service.delete(id)
            Logger.info(f"Payment {payment} deleted")
            return True, f"Payment Deleted Successfully"
        except Exception as e:
            Logger.error(f"Payment Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            payment_list = Payment_Service.get_all()
            Logger.info("Payment FindAll")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_customer_id(cls, customerid):
        try:
            payment = Payment_Service.find_by_customer_id(customerid)
            if payment:
                Logger.info(f"Payment FindByCustomer_id {customerid}")
                return True, payment
            else:
                raise Exception("Payment Not Found !!!")
        except Exception as e:
            Logger.error(f"Payment FindByCustomer_id Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, id):
        try:
            payment = Payment_Service.find_by_id(id)
            Logger.info(f"Payment FindById {id}")
            return True, payment
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e



    @classmethod
    def find_by_status(cls, status):
        try:
            payment_list = Payment_Service.find_by_status(status)
            Logger.info(f"Payment FindByRole {status}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByRole Error: {e}")
            return False, e

    @classmethod
    def find_by_order_id(cls, order_id):
        try:
            payment_list = Payment_Service.find_by_status(order_id)
            Logger.info(f"Payment FindByRole {order_id}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByRole Error: {e}")
            return False, e
'''
    @classmethod
    def find_by_datetime(cls, salary_min):
        try:
            payment_list = Payment_Service.find_by_salary_min(salary_min)
            Logger.info(f"Payment FindBySalaryMin {salary_min}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindBySalaryMin Error: {e}")
          return False, e
'''