import sqlite3
from model.payment import Payment


class Payment_repository:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("../database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, payment):
        self.connect()
        self.cursor.execute(
            "insert into payments(order_id, total_price, payment_type, date_time, customer_id, status, factor_id) values (?,?,?,?,?,?,?)",
            [payment.order_id, payment.total_price.payment_type, payment.date_time, payment.customer_id, payment.status,
             payment.factor_id])
        payment.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return payment

    def update(self, payment):
        self.connect()
        self.cursor.execute(
            "update payments set order_id=?, total_price=?, payment_type=?, date_time=?, customer_id=?, status=?, factor_id=? where id=?",
            [payment.order_id, payment.total_price, payment.customer_id, payment.status, payment.factor_id,payment.id])

        self.connection.commit()
        self.disconnect()
        return payment

    def delete(self, payment):
        self.connect()
        self.cursor.execute(
            "delete from payments where id=?", [payment.id])
        self.connection.commit()
        self.disconnect()
        return payment

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from payments where customer_id=?", [customer_id])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list


'''
    def find_by_date_time(self, number):
        self.connect()
        self.cursor.execute("select * from payments where  phone_number=?", [number])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list'''


def find_by_order_id(self, id):
    self.connect()
    self.cursor.execute("select * from payments where  order_id=?", [id])
    payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
    self.disconnect()
    return payment_list


def find_by_status(self, status):
    self.connect()
    self.cursor.execute("select * from payments where  status=?", [status])
    payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
    self.disconnect()
    return payment_list


def find_by_id(self, id):
    self.connect()
    self.cursor.execute("select * from payments where  id=?", [id])
    payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
    self.disconnect()
    return payment_list


def get_all(self):
    self.connect()
    self.cursor.execute("select * from payments")
    payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
    self.disconnect()
    return payment_list
