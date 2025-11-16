from model.delivery import Delivery
from service.delivery_service import Delivery_Service
from tools.logging1 import Logger


class Delivery_Controller:
    @classmethod
    def save(cls, order_id, rider, status, address):
        try:
            delivery = Delivery(None, order_id, rider, status, address)
            #delivery.validate()
            delivery = Delivery_Service.save(delivery)
            Logger.info(f"Delivery {delivery} saved")
            return True, f"Delivery Saved Successfully"
        except Exception as e:
            Logger.error(f"Delivery Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id,order_id, rider, status, address):
        try:
            delivery = Delivery(id,order_id, rider, status, address)
            #delivery.validate()
            delivery = Delivery_Service.update(delivery)
            Logger.info(f"Delivery {delivery} updated")
            return True, "Delivery Updated Successfully"
        except Exception as e:
            Logger.error(f"Delivery Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, id):
        try:
            delivery = Delivery_Service.delete(id)
            Logger.info(f"Delivery {delivery} deleted")
            return True, f"Delivery Deleted Successfully"
        except Exception as e:
            Logger.error(f"Delivery Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            delivery_list = Delivery_Service.get_all()
            Logger.info("Delivery FindAll")
            return True, delivery_list
        except Exception as e:
            Logger.error(f"Delivery FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_rider(cls,rider):
        try:
            delivery = Delivery_Service.find_by_rider(rider)
            if delivery:
                Logger.info(f"Delivery FindByUsernameAndPassword {rider}")
                return True, delivery
            else:
                raise Exception("User Not Found !!!")
        except Exception as e:
            Logger.error(f"Delivery FindByrider Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, id):
        try:
            delivery = Delivery_Service.find_by_id(id)
            Logger.info(f"Delivery FindById {id}")
            return True, delivery
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e

    @classmethod
    def find_by_status(cls,status):
        try:
            delivery_list = Delivery_Service.find_by_status(status)
            Logger.info(f"Delivery FindBystatus {status}")
            return True, delivery_list
        except Exception as e:
            Logger.error(f"Delivery FindBystatus Error: {e}")
            return False, e

    @classmethod
    def find_by_address(cls, address):
        try:
            delivery_list = Delivery_Service.find_by_address(address)
            Logger.info(f"Delivery FindByaddress {address}")
            return True, delivery_list
        except Exception as e:
            Logger.error(f"Delivery FindByaddress Error: {e}")
            return False, e


    @classmethod
    def find_by_order_id(cls, order_id):
        try:
            delivery_list = Delivery_Service.find_by_role(order_id)
            Logger.info(f"Delivery FindByRole {order_id}")
            return True, delivery_list
        except Exception as e:
            Logger.error(f"Delivery FindByRole Error: {e}")
            return False, e

