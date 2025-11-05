import sqlite3
from model.employee import Employee


class Employee_repository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def add_employee(self, employee):
        self.cursor.execute(
            "insert into employees(id,first_name, last_name,role,username,password,salary) values (?,?,?,?,?,?)",
            [employee.id, employee.first_name, employee.last_name, employee.role, employee.username, employee.password,
             employee.salary])

        employee.id = self.cursor.lastrowid
        self.connection.commit()
        return employee

    def update_employee(self, employee):
        self.cursor.execute(
            "update employees set first_name=?,last_name=?,role=?,username=?,password=?,salary=?) where id=?",
            [employee.first_name, employee.last_name, employee.role, employee.username, employee.password,
             employee.salary])

        self.connection.commit()
        self.disconnect()
        return employee

    def delete_employee(self, employee):
        self.cursor.execute(
            "delete from customers where id=?", [id])

        self.connection.commit()
        self.disconnect()
        return employee

    def find_by_firstname_and_lastname(self, firstname, lastname):
        self.connect()
        self.cursor.execute("select * from customers where first_name=? and last_name=?", [firstname, lastname])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_phone_number(self, number):
        self.connect()
        self.cursor.execute("select * from customers where  phone_number=?", [number])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_order_id(self, id):
        self.connect()
        self.cursor.execute("select * from employees where  order_id=?", [id])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_role(self, role):
        self.connect()
        self.cursor.execute("select * from employees where  role=?", [role])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from employees where  id=?", [id])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def get_all_employees(self):
        self.connect()
        self.cursor.execute("select * from employees")
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from customers where username=? and password=?", [username, password])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def reset_username_password(self, employee):
        self.cursor.execute(
            "update employee set username=?,password=?) where id=?",
            [employee.username, employee.password])

        self.connection.commit()
        self.disconnect()
        return employee
