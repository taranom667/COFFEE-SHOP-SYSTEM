import sqlite3
from logging import exception

from fontTools.misc.cython import returns

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

    def save(self, employee):
        self.connect()
        self.cursor.execute(
            "insert into employees(first_name, last_name,role,username,password,salary,phone_number) values (?,?,?,?,?,?,?)",
            [employee.first_name, employee.last_name, employee.role, employee.username, employee.password,
             employee.salary, employee.phone_number])
        employee.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return employee

    def update(self, employee):
        self.connect()
        self.cursor.execute(
            "update employees set first_name=?,last_name=?,role=?,username=?,password=?,salary=?,phone_number=? where id=?",
            [employee.first_name, employee.last_name, employee.role, employee.username, employee.password,employee.salary,employee.phone_number, employee.id])


        self.connection.commit()
        self.disconnect()
        return employee

    def delete(self,id):
        self.connect()
        self.cursor.execute(
            "delete from employees where id=?", [id])
        self.connection.commit()
        self.disconnect()


    def find_by_firstname_and_lastname(self, firstname, lastname):
        self.connect()
        self.cursor.execute("select * from employees where first_name=? and last_name=?", [firstname, lastname])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_phone_number(self, number):
        self.connect()
        self.cursor.execute("select * from employees where  phone_number=?", [number])
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

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from employees where username=? and password=?", [username, password])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_salary_min(self, salary):
        self.connect()
        self.cursor.execute("select * from employees where salary=?", [salary])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def get_all(self):
        self.connect()
        self.cursor.execute("select * from employees")
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

'''

employee_r.save(employee1)
#

employee1 = Employee("11", "taranom", "bagheri", "manager", "tari", "tari123", 98765,9125214321)
employee_r = Employee_repository()
employee_r.delete(employee1)'''
