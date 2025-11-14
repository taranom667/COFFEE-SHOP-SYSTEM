from model.employee import Employee
from service.employee_service import Employee_Service
from tools.logging1 import Logger


class Employee_Controller:
    @classmethod
    def save(cls, first_name, last_name, role, username, password, salary, phone_number):
        try:
            employee = Employee(None, first_name, last_name, role, username, password, salary, phone_number)
            employee.validate()
            employee = Employee_Service.save(employee)
            Logger.info(f"Employee {employee} saved")
            return True, f"Employee Saved Successfully"
        except Exception as e:
            Logger.error(f"Employee Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, first_name, last_name, role, username, password, salary, phone_number):
        try:
            employee = Employee(id, first_name, last_name, role, username, password, salary, phone_number)
            employee.validate()
            employee = Employee_Service.update(employee)
            Logger.info(f"Employee {employee} updated")
            return True, "Employee Updated Successfully"
        except Exception as e:
            Logger.error(f"Employee Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, id):
        try:
            employee = Employee_Service.delete(id)
            Logger.info(f"Employee {employee} deleted")
            return True, f"Employee Deleted Successfully"
        except Exception as e:
            Logger.error(f"Employee Delete Error: {e}")
            return False, e

    @classmethod
    def get_all(cls):
        try:
            employee_list = Employee_Service.get_all()
            Logger.info("Employee FindAll")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            employee = Employee_Service.find_by_username_and_password(username, password)
            if employee:
                Logger.info(f"Employee FindByUsernameAndPassword {username}")
                return True, employee
            else:
                raise Exception("User Not Found !!!")
        except Exception as e:
            Logger.error(f"Employee FindByUsernameAndPassword Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, id):
        try:
            employee = Employee_Service.find_by_id(id)
            Logger.info(f"Employee FindById {id}")
            return True, employee
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        try:
            employee_list = Employee_Service.find_by_firstname_and_lastname(firstname, lastname)
            Logger.info(f"Employee FindByFirstnameAndLastname {firstname} {lastname}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByFirstnameAndLastname Error: {e}")
            return False, e

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            employee_list = Employee_Service.find_by_phone_number(phone_number)
            Logger.info(f"Employee FindByPhoneNumber {phone_number}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByPhoneNumber Error: {e}")
            return False, e

    @classmethod
    def find_by_role(cls, role):
        try:
            employee_list = Employee_Service.find_by_role(role)
            Logger.info(f"Employee FindByRole {role}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByRole Error: {e}")
            return False, e

    @classmethod
    def find_by_order_id(cls, order_id):
        try:
            employee_list = Employee_Service.find_by_role(order_id)
            Logger.info(f"Employee FindByRole {order_id}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindByRole Error: {e}")
            return False, e

    @classmethod
    def find_by_salary_min(cls, salary_min):
        try:
            employee_list = Employee_Service.find_by_salary_min(salary_min)
            Logger.info(f"Employee FindBySalaryMin {salary_min}")
            return True, employee_list
        except Exception as e:
            Logger.error(f"Employee FindBySalaryMin Error: {e}")
            return False, e
