import sqlite3
from model.delivery import Delivery


class Delivery_repository:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("../database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, delivery):
        self.connect()
        self.cursor.execute(
            "insert into deliveries(id=None,order_id,rider,status,address) values (?,?,?,?)",
            [delivery.order_id, delivery.rider, delivery.status, delivery.address])
        delivery.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return delivery

    def update(self, delivery):
        self.connect()
        self.cursor.execute(
            "update deliveries set order_id=?,rider=?,status=?,address=?) where id=?",
            [delivery.order_id, delivery.rider, delivery.status, delivery.address,delivery.id])

        self.connection.commit()
        self.disconnect()
        return delivery

    def delete(self, delivery):
        self.connect()
        self.cursor.execute(
            "delete from deliveries where id=?", [delivery.id])
        self.connection.commit()
        self.disconnect()

    def find_by_rider(self,rider):
        self.connect()
        self.cursor.execute("select * from deliveries where rider=?", [rider])
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list

    def find_by_status(self, status):
        self.connect()
        self.cursor.execute("select * from deliveries where  status=?", [status])
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list

    def find_by_address(self, address):
        self.connect()
        self.cursor.execute("select * from deliveries where  address=?", [address])
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from deliveries where  id=?", [id])
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list


    def get_all(self):
        self.connect()
        self.cursor.execute("select * from deliveries")
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list


'''
delivery1 = Delivery("0", "taranom", "bagheri", "manager", "tari", "tari123", 98765,9125214321)
delivery_r = Delivery_repository()
delivery_r.save(delivery1)
#delivery_r.delete(delivery1)

def r'''
