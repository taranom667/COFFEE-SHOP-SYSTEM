from model.dish import Dish
from service.dish_service import Dish_Service
from tools.logging1 import Logger


class Dish_Controller:
    @classmethod
    def save(cls, name,quantity,price,category,available,ingredients):
        try:
            dish = Dish(None,name,quantity,price,category,available,ingredients)
            #dish.validate()
            dish =Dish_Service.save(dish)
            Logger.info(f"Dish {dish} saved")
            return True, f"Dish Saved Successfully"
        except Exception as e:
            Logger.error(f"Dish Save Error: {e}")
            return False, e

    @classmethod
    def update(cls,id,name,quantity,price,category,available,ingredients):
        try:
            dish = Dish(id,name,quantity,price,category,available,ingredients)
            #dish.validate()
            dish =Dish_Service.update(dish)
            Logger.info(f"Dish {dish} updated")
            return True, "Dish Updated Successfully"
        except Exception as e:
            Logger.error(f"Dish Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls,id):
        try:
            dish =Dish_Service.delete(id)
            Logger.info(f"Dish {dish} deleted")
            return True, f"Dish Deleted Successfully"
        except Exception as e:
            Logger.error(f"Dish Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            dish_list =Dish_Service.get_all()
            Logger.info("Dish FindAll")
            return True, dish_list
        except Exception as e:
            Logger.error(f"Dish FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_name(cls,name):
        try:
            dish = Dish_Service.find_by_name(name)
            if dish:
                Logger.info(f"Dish FindByname {name}")
                return True, dish
            else:
                raise Exception("dish Not Found !!!")
        except Exception as e:
            Logger.error(f"Dish FindByname Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls,id):
        try:
            dish =Dish_Service.find_by_id(id)
            Logger.info(f"Dish FindById {id}")
            return True, dish
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e

    @classmethod
    def find_by_category(cls, category):
        try:
            dish_list =Dish_Service.find_by_category(category)
            Logger.info(f"Dish FindByCategory {category}")
            return True, dish_list
        except Exception as e:
            Logger.error(f"Dish FindByCategory Error: {e}")
            return False, e

    @classmethod
    def find_by_available(cls,available):
        try:
            dish_list =Dish_Service.find_by_available(available)
            Logger.info(f"Dish FindByPhoneNumber {available}")
            return True, dish_list
        except Exception as e:
            Logger.error(f"Dish FindByAvailability Error: {e}")
            return False, e

