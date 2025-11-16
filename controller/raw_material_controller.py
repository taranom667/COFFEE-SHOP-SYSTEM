from model.raw_material import Raw_material
from service.raw_material_service import Raw_material_Service
from tools.logging1 import Logger


class Raw_material_Controller:
    @classmethod
    def save(cls, name, category, unit, quantity, price, purchase_date, expiry_date, location):
        try:
            raw_material = Raw_material(None, name, category, unit, quantity, price, purchase_date, expiry_date, location)
            #raw_material.validate()
            raw_material = Raw_material_Service.save(raw_material)
            Logger.info(f"Raw_material {raw_material} saved")
            return True, f"Raw_material Saved Successfully"
        except Exception as e:
            Logger.error(f"Raw_material Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, name, category, unit, quantity, price, purchase_date, expiry_date, location):
        try:
            raw_material = Raw_material( id, name, category, unit, quantity, price, purchase_date, expiry_date, location)
            #raw_material.validate()
            raw_material = Raw_material_Service.update(raw_material)
            Logger.info(f"Raw_material {raw_material} updated")
            return True, "Raw_material Updated Successfully"
        except Exception as e:
            Logger.error(f"Raw_material Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, id):
        try:
            raw_material = Raw_material_Service.delete(id)
            Logger.info(f"Raw_material {raw_material} deleted")
            return True, f"Raw_material Deleted Successfully"
        except Exception as e:
            Logger.error(f"Raw_material Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            raw_material_list = Raw_material_Service.get_all()
            Logger.info("Raw_material FindAll")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_name(cls, name):
        try:
            raw_material = Raw_material_Service.find_by_name(name)
            if raw_material:
                Logger.info(f"Raw_material FindByname {name}")
                return True, raw_material
            else:
                raise Exception("User Not Found !!!")
        except Exception as e:
            Logger.error(f"Raw_material FindByname Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, id):
        try:
            raw_material = Raw_material_Service.find_by_id(id)
            Logger.info(f"Raw_material FindById {id}")
            return True, raw_material
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e

    @classmethod
    def find_by_category(cls, category):
        try:
            raw_material_list = Raw_material_Service.find_by_category(category)
            Logger.info(f"Raw_material FindBycategory{category} {category}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindBycategoryError: {e}")
            return False, e

    @classmethod
    def find_by_quantity(cls, quantity):
        try:
            raw_material_list = Raw_material_Service.find_by_quantity(quantity)
            Logger.info(f"Raw_material FindByquantity {quantity}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindByquantity Error: {e}")
            return False, e

    @classmethod
    def find_by_purchase_date(cls, purchase_date):
        try:
            raw_material_list = Raw_material_Service.find_by_purchase_date(purchase_date)
            Logger.info(f"Raw_material FindBypurchase_date {purchase_date}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindBypurchase_date Error: {e}")
            return False, e

    @classmethod
    def find_by_expiry_date(cls, expiry_date):
        try:
            raw_material_list = Raw_material_Service.find_by_purchase_date(expiry_date)
            Logger.info(f"Raw_material FindByExpiry_date {expiry_date}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindByExpiry_date Error: {e}")
            return False, e


