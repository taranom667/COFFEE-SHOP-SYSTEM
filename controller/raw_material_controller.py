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
    def find_by_username_and_password(cls, username, password):
        try:
            raw_material = Raw_material_Service.find_by_username_and_password(username, password)
            if raw_material:
                Logger.info(f"Raw_material FindByUsernameAndPassword {username}")
                return True, raw_material
            else:
                raise Exception("User Not Found !!!")
        except Exception as e:
            Logger.error(f"Raw_material FindByUsernameAndPassword Error: {e}")
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
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        try:
            raw_material_list = Raw_material_Service.find_by_firstname_and_lastname(firstname, lastname)
            Logger.info(f"Raw_material FindByFirstnameAndLastname {firstname} {lastname}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindByFirstnameAndLastname Error: {e}")
            return False, e

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            raw_material_list = Raw_material_Service.find_by_phone_number(phone_number)
            Logger.info(f"Raw_material FindByPhoneNumber {phone_number}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindByPhoneNumber Error: {e}")
            return False, e

    @classmethod
    def find_by_role(cls, role):
        try:
            raw_material_list = Raw_material_Service.find_by_role(role)
            Logger.info(f"Raw_material FindByRole {role}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindByRole Error: {e}")
            return False, e

    @classmethod
    def find_by_order_id(cls, order_id):
        try:
            raw_material_list = Raw_material_Service.find_by_role(order_id)
            Logger.info(f"Raw_material FindByRole {order_id}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindByRole Error: {e}")
            return False, e

    @classmethod
    def find_by_salary_min(cls, salary_min):
        try:
            raw_material_list = Raw_material_Service.find_by_salary_min(salary_min)
            Logger.info(f"Raw_material FindBySalaryMin {salary_min}")
            return True, raw_material_list
        except Exception as e:
            Logger.error(f"Raw_material FindBySalaryMin Error: {e}")
            return False, e
