from model.order import Order
from service.order_service import Order_Service
from tools.logging1 import Logger


class Order_Controller:
    @classmethod
    def save(cls, customer_name, dish, status, total_price, delivery_id, date_time):
        try:
            order = Order(None,customer_name, dish, status, total_price, delivery_id, date_time)
            order.validate()
            order = Order_Service.save(order)
            Logger.info(f"Order {order} saved")
            return True, f"Order Saved Successfully"
        except Exception as e:
            Logger.error(f"Order Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, customer_name, dish, status, total_price, delivery_id, date_time):
        try:
            order = Order(id, customer_name, dish, status, total_price, delivery_id, date_time)
            order.validate()
            order = Order_Service.update(order)
            Logger.info(f"Order {order} updated")
            return True, "Order Updated Successfully"
        except Exception as e:
            Logger.error(f"Order Update Error: {e}")
            return False, e
 
    @classmethod
    def delete(cls, id):
        try:
            order = Order_Service.delete(id)
            Logger.info(f"Order {order} deleted")
            return True, f"Order Deleted Successfully"
        except Exception as e:
            Logger.error(f"Order Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            order_list = Order_Service.get_all()
            Logger.info("Order FindAll")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_customer_name(cls, customername):
        try:
            order = Order_Service.find_by_customer_name(customername)
            if order:
                Logger.info(f"Order FindBycustomername {customername}")
                return True, order
            else:
                raise Exception("Customer Not Found !!!")
        except Exception as e:
            Logger.error(f"Order FindBycustomername Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, id):
        try:
            order = Order_Service.find_by_id(id)
            Logger.info(f"Order FindById {id}")
            return True, order
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e

    @classmethod
    def find_by_status(cls,status):
        try:
            order_list = Order_Service.find_by_status(status)
            Logger.info(f"Order FindBystatus {status}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindBystatus Error: {e}")
            return False, e

    @classmethod
    def find_by_delivery_id(cls, delivery_id):
        try:
            order_list = Order_Service.find_by_delivery_id(delivery_id)
            Logger.info(f"Order FindBydelivery_id {delivery_id}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindBydelivery_id Error: {e}")
            return False, e

