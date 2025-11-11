from repository.employee_repository import Employee_repository


class Employee_Service:
    employee_repository = Employee_repository()

    @classmethod
    def save(cls, employee):
        return cls.employee_repository.save(employee)

    @classmethod
    def update(cls, employee):
        return cls.employee_repository.update(employee)

    @classmethod
    def delete(cls, employee):
        return cls.employee_repository.delete(employee)

    @classmethod
    def find_by_firstname_and_lastname(cls, firstname, lastname):
        employee = cls.employee_repository.find_by_firstname_and_lastname(firstname, lastname)
        if employee:
            return employee
        else:
            raise ValueError("Employee not found")

    @classmethod
    def find_by_phone_number(cls, phone_number):
        employee = cls.employee_repository.find_by_phone_number(phone_number)
        if employee:
            return employee
        else:
            raise ValueError("Employee not found")

    @classmethod
    def find_by_role(cls, role):
        employee = cls.employee_repository.find_by_role(role)
        if employee:
            return employee
        else:
            raise ValueError("Employee not found")

    @classmethod
    def find_by_order_id(cls, order_id):
        employee = cls.employee_repository.find_by_order_id(order_id)
        if employee:
            return employee
        else:
            raise ValueError("Employee not found")

    @classmethod
    def find_by_id(cls, id):
        employee = cls.employee_repository.find_by_id(id)
        if employee:
            return employee
        else:
            raise ValueError("Employee not found")

    @classmethod
    def find_by_username_and_password(cls, username, password):
        employee = cls.employee_repository.find_by_username_and_password(username, password)
        if employee:
            return employee
        else:
            raise ValueError("Employee not found")

    @classmethod
    def find_by_salary_min(cls, salary_min):
        employee = cls.employee_repository.find_by_salary_min(salary_min)
        if employee:
            return employee
        else:
            raise ValueError("Employee not found")

    @classmethod
    def get_all(cls):
        return cls.employee_repository.get_all()
