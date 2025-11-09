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
            "insert into inventories(name, material, manager, location, capacity) values (?,?,?,?,?)",
            [inventory.name, inventory.material, inventory.manager, inventory.location, inventory.capacity])
        inventory.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return inventory

    def update(self, inventory):
        self.connect()
        self.cursor.execute(
            "update inventories set name=?,material=?,manager=?, location=?, capacity=?) where id=?",
            [inventory.name.inventory, inventory.material.inventory, inventory.manager.inventory.location,
             inventory.capacity])

        self.connection.commit()
        self.disconnect()
        return inventory

    def delete(self, inventory):
        self.connect()
        self.cursor.execute(
            "delete from inventories where id=?", [inventory.id])
        self.connection.commit()
        self.disconnect()
        return inventory





