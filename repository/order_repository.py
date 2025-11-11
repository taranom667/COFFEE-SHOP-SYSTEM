import sqlite3
from model.order import Order


class Order_repository:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, order):
        self.connect()
        self.cursor.execute(
            "insert into orders(id=none,customer_name,dish,status,total_price,delivery_id,date_time) values (?,?,?,?,?,?)",
            [order.customer_name, order.dish, order.status, order.total_price, order.delivery_id, order.date_time])
        order.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return order

    def update(self, order):
        self.connect()
        self.cursor.execute(
            "update orders set customer_name=?,dish=?,status=?,total_price=?,delivery_id=?,date_time=?) where id=?",
            [order.customer_name, order.dish, order.status, order.total_price, order.delivery_id, order.date_time])

        self.connection.commit()
        self.disconnect()
        return order

    def delete(self, order):
        self.connect()
        self.cursor.execute(
            "delete from orders where id=?", [order.id])
        self.connection.commit()
        self.disconnect()

    def find_by_customer_name(self, customername):
        self.connect()
        self.cursor.execute("select * from orders where customer_name=?", [customername])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_status(self, status):
        self.connect()
        self.cursor.execute("select * from orders where  status=?", [status])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_delivery_id(self, id):
        self.connect()
        self.cursor.execute("select * from orders where  delivery_id=?", [id])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from orders where  id=?", [id])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def get_all(self):
        self.connect()
        self.cursor.execute("select * from orders")
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list


'''
    def find_by_date_time(self, role):
        self.connect()
        self.cursor.execute("select * from orders where  role=?", [role])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list
'''
'''
order1 = Order("0", "taranom", "bagheri", "manager", "tari", "tari123", 98765,9125214321)
order_r = Order_repository()
order_r.save(order1)
#order_r.delete(order1)

'''
