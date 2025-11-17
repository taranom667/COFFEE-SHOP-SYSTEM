import sqlite3
from model.dish import Dish


class Dish_repository:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, dish):
        self.connect()
        self.cursor.execute(
            "insert into dishes(name,quantity,price,category,available,ingredients) values (?,?,?,?,?,?)",
            [dish.name, dish.quantity, dish.price,dish.category, dish.available, dish.ingredients])
        dish.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return dish

    def update(self, dish):
        self.connect()
        self.cursor.execute(
            "update dishes set name=?,quantity=?,price=?,category=?,available=?,ingredients=? where id=?",
            [dish.name,dish.quantity,dish.price,dish.category,dish.available,dish.ingredients,dish.id])

        self.connection.commit()
        self.disconnect()
        return dish

    def delete(self, id):
        self.connect()
        self.cursor.execute(
            "delete from dishes where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_by_name(self,name):
        self.connect()
        self.cursor.execute("select * from dishes where name=?", [name])
        dish_list = [Dish(*dish) for dish in self.cursor.fetchall()]
        self.disconnect()
        return dish_list

    def find_by_category(self,category):
        self.connect()
        self.cursor.execute("select * from dishes where  category=?", [category])
        dish_list = [Dish(*dish) for dish in self.cursor.fetchall()]
        self.disconnect()
        return dish_list

    def find_by_available(self,available):
        self.connect()
        self.cursor.execute("select * from dishes where  available=True", [available])
        dish_list = [Dish(*dish) for dish in self.cursor.fetchall()]
        self.disconnect()
        return dish_list



    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from dishes where  id=?", [id])
        dish_list = [Dish(*dish) for dish in self.cursor.fetchall()]
        self.disconnect()
        return dish_list


    def get_all(self):
        self.connect()
        self.cursor.execute("select * from dishes")
        dish_list = [Dish(*dish) for dish in self.cursor.fetchall()]
        self.disconnect()
        return dish_list


