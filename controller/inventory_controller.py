from model.inventory import Inventory
from service.inventory_service import Inventory_Service
from tools.logging1 import Logger


class Inventory_Controller:
    @classmethod
    def save(cls, name, material, manager, location, capacity):
        try:
            inventory = Inventory(None, name, material, manager, location, capacity)
            inventory.validate()
            inventory = Inventory_Service.save(inventory)
            Logger.info(f"Inventory {inventory} saved")
            return True, f"Inventory Saved Successfully"
        except Exception as e:
            Logger.error(f"Inventory Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, name, material, manager, location, capacity):
        try:
            inventory = Inventory(id, name, material, manager, location, capacity)
            inventory.validate()
            inventory = Inventory_Service.update(inventory)
            Logger.info(f"Inventory {inventory} updated")
            return True, "Inventory Updated Successfully"
        except Exception as e:
            Logger.error(f"Inventory Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, id):
        try:
            inventory = Inventory_Service.delete(id)
            Logger.info(f"Inventory {inventory} deleted")
            return True, f"Inventory Deleted Successfully"
        except Exception as e:
            Logger.error(f"Inventory Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            inventory_list = Inventory_Service.get_all()
            Logger.info("Inventory FindAll")
            return True, inventory_list
        except Exception as e:
            Logger.error(f"Inventory FindAll Error: {e}")
            return False, e

    

    @classmethod
    def find_by_id(cls, id):
        try:
            inventory = Inventory_Service.find_by_id(id)
            Logger.info(f"Inventory FindById {id}")
            return True, inventory
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e

    

    @classmethod
    def find_by_location(cls, location):
        try:
            inventory_list = Inventory_Service.find_by_location(location)
            Logger.info(f"Inventory FindByPhoneNumber {location}")
            return True, inventory_list
        except Exception as e:
            Logger.error(f"Inventory FindByPhoneNumber Error: {e}")
            return False, e

    @classmethod
    def find_by_name(cls, name):
        try:
            inventory_list = Inventory_Service.find_by_name(name)
            Logger.info(f"Inventory FindByRole {name}")
            return True, inventory_list
        except Exception as e:
            Logger.error(f"Inventory FindByRole Error: {e}")
            return False, e

