import sqlite3
from model.customer import Customer


class Customer_repository:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "insert into customers(first_name, last_name,phone_number,order_id) values (?,?,?,?)",
            [customer.first_name, customer.last_name, customer.phone_number, customer.order_id])
        customer.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return customer

    def update(self, customer):
        self.connect()
        self.cursor.execute(
            "update customers set first_name=?,last_name=?,phone_number=?,order_id=? where id=?",
            [customer.first_name, customer.last_name, customer.phone_number, customer.order_id, customer.id])

        self.connection.commit()
        self.disconnect()
        return customer

    def delete(self, customer):
        self.connect()
        self.cursor.execute(
            "delete from customers where id=?", [customer.id])
        self.connection.commit()
        self.disconnect()

    def find_by_firstname_and_lastname(self, firstname, lastname):
        self.connect()
        self.cursor.execute("select * from customers where first_name=? and last_name=?", [firstname, lastname])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_phone_number(self, number):
        self.connect()
        self.cursor.execute("select * from customers where  phone_number=?", [number])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_order_id(self, id):
        self.connect()
        self.cursor.execute("select * from customers where  order_id=?", [id])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from customers where  id=?", [id])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list


    def get_all(self):
        self.connect()
        self.cursor.execute("select * from customers")
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list


'''
customer1 = Customer("0", "taranom", "bagheri", "manager", "tari", "tari123", 98765,9125214321)
customer_r = Customer_repository()
customer_r.save(customer1)
#customer_r.delete(customer1)
'''
