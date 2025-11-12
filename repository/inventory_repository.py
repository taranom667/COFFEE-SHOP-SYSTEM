import sqlite3
from model.inventory import Inventory


class Inventory_repository:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("../database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, inventory):
        self.connect()
        self.cursor.execute(
            "insert into inventories(id=None,name,material,manager,location,capacity) values (?,?,?,?,?)",
            [inventory.name,inventory.material,inventory.manager,inventory.location,inventory.capacity])
        inventory.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return inventory

    def update(self, inventory):
        self.connect()
        self.cursor.execute(
            "update inventories set name=?,material=?,manager=?,location=?,capacity=?) where id=?",
            [inventory.name,inventory.material,inventory.manager,inventory.location,inventory.capacity,inventory.id])

        self.connection.commit()
        self.disconnect()
        return inventory

    def delete(self, inventory):
        self.connect()
        self.cursor.execute(
            "delete from inventories where id=?", [inventory.id])
        self.connection.commit()
        self.disconnect()

    def find_by_name(self,name):
        self.connect()
        self.cursor.execute("select * from inventories where name=?", [name])
        inventory_list = [Inventory(*inventory) for inventory in self.cursor.fetchall()]
        self.disconnect()
        return inventory_list

    def find_by_location(self,location):
        self.connect()
        self.cursor.execute("select * from inventories where location=?", [location])
        inventory_list = [Inventory(*inventory) for inventory in self.cursor.fetchall()]
        self.disconnect()
        return inventory_list


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from inventories where  id=?", [id])
        inventory_list = [Inventory(*inventory) for inventory in self.cursor.fetchall()]
        self.disconnect()
        return inventory_list

    def get_all(self):
        self.connect()
        self.cursor.execute("select * from inventories")
        inventory_list = [Inventory(*inventory) for inventory in self.cursor.fetchall()]
        self.disconnect()
        return inventory_list


'''
inventory1 = Inventory("0", "taranom", "bagheri", "manager", "tari", "tari123", 98765,9125214321)
inventory_r = Inventory_repository()
inventory_r.save(inventory1)
#inventory_r.delete(inventory1)
'''