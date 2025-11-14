from model.customer import Customer
from service.customer_service import Customer_Service
from tools.logging1 import Logger


class Customer_Controller:
    @classmethod
    def save(cls,  first_name, last_name, phone_number, order_id):
        try:
            customer = Customer(None, first_name, last_name, phone_number, order_id)
            customer.validate()
            customer =Customer_Service.save(customer)
            Logger.info(f"Customer {customer} saved")
            return True, f"Customer Saved Successfully"
        except Exception as e:
            Logger.error(f"Customer Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, first_name, last_name, phone_number, order_id):
        try:
            customer = Customer(id,first_name, last_name,phone_number, order_id)
            customer.validate()
            customer =Customer_Service.update(customer)
            Logger.info(f"Customer {customer} updated")
            return True, "Customer Updated Successfully"
        except Exception as e:
            Logger.error(f"Customer Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls,id):
        try:
            customer =Customer_Service.delete(id)
            Logger.info(f"Customer {customer} deleted")
            return True, f"Customer Deleted Successfully"
        except Exception as e:
            Logger.error(f"Customer Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            customer_list =Customer_Service.get_all()
            Logger.info("Customer FindAll")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindAll Error: {e}")
            return False, e



    @classmethod
    def find_by_id(cls,id):
        try:
            customer =Customer_Service.find_by_id(id)
            Logger.info(f"Customer FindById {id}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        try:
            customer_list =Customer_Service.find_by_firstname_and_lastname(firstname, lastname)
            Logger.info(f"Customer FindByFirstnameAndLastname {firstname} {lastname}")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindByFirstnameAndLastname Error: {e}")
            return False, e

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            customer_list =Customer_Service.find_by_phone_number(phone_number)
            Logger.info(f"Customer FindByPhoneNumber {phone_number}")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindByPhoneNumber Error: {e}")
            return False, e



    @classmethod
    def find_by_order_id(cls,order_id):
        try:
            customer_list = Customer_Service.find_by_role(order_id)
            Logger.info(f"Customer FindByRole {order_id}")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindByRole Error: {e}")
            return False, e

    