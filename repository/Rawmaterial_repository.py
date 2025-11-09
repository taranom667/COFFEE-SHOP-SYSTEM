import sqlite3
from model.raw_material import Raw_material


class Raw_material_repository:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("../database/COFFEESHOP_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, raw_material):
        self.connect()
        self.cursor.execute(
            "insert into raw_materials(name, category, unit, quantity, price, purchase_date, expiry_date, location) values (?,?,?,?,?,?)",
            [raw_material.first_name, raw_material.last_name, raw_material.role, raw_material.username, raw_material.password,
             raw_material.salary])
        raw_material.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return raw_material

    def update(self, raw_material):
        self.connect()
        self.cursor.execute(
            "update raw_materials set first_name=?,last_name=?,role=?,username=?,password=?,salary=?) where id=?",
            [raw_material.first_name, raw_material.last_name, raw_material.role, raw_material.username, raw_material.password,
             raw_material.salary, raw_material.id])

        self.connection.commit()
        self.disconnect()
        return raw_material

    def delete(self, raw_material):
        self.connect()
        self.cursor.execute(
            "delete from raw_materials where id=?", [id])
        self.connection.commit()
        self.disconnect()
        return raw_material

    def find_by_firstname_and_lastname(self, firstname, lastname):
        self.connect()
        self.cursor.execute("select * from raw_materials where first_name=? and last_name=?", [firstname, lastname])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_phone_number(self, number):
        self.connect()
        self.cursor.execute("select * from raw_materials where  phone_number=?", [number])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_order_id(self, id):
        self.connect()
        self.cursor.execute("select * from raw_materials where  order_id=?", [id])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_role(self, role):
        self.connect()
        self.cursor.execute("select * from raw_materials where  role=?", [role])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from raw_materials where  id=?", [id])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from raw_materials where username=? and password=?", [username, password])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_salary_min(self, salary):
        self.connect()
        self.cursor.execute("select * from raw_materials where salary=?", [salary])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def reset_username_password(self, raw_material):
        self.connect()
        self.cursor.execute(
            "update raw_materials set username=?,password=?) where id=?",
            [raw_material.username, raw_material.password, raw_material.id])

        self.connection.commit()
        self.disconnect()
        return raw_material

    def get_all(self):
        self.connect()
        self.cursor.execute("select * from raw_materials")
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list
