import sqlite3
from model.rawmaterial import Raw_material


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
            "insert into Raw_materials(name, category, unit, quantity, price, purchase_date, expiry_date, location) values (?,?,?,?,?,?,?,?)",
            [raw_material.name,raw_material.category,raw_material.unit,raw_material.quantity,raw_material.purchase_date,raw_material.expiry_date,raw_material.location])
        raw_material.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return raw_material

    def update(self, raw_material):
        self.connect()
        self.cursor.execute(
            "update Raw_materials set first_name=?,last_name=?,role=?,username=?,password=?,salary=?) where id=?",
            [raw_material.first_name, raw_material.last_name, raw_material.role, raw_material.username, raw_material.password,
             raw_material.salary, raw_material.id])

        self.connection.commit()
        self.disconnect()
        return raw_material

    def delete(self, raw_material):
        self.connect()
        self.cursor.execute(
            "delete from Raw_materials where id=?", [raw_material.id])
        self.connection.commit()
        self.disconnect()
        return raw_material

    def find_by_name(self,name):
        self.connect()
        self.cursor.execute("select * from Raw_materials where name=?", [name])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_category(self,category):
        self.connect()
        self.cursor.execute("select * from Raw_materials where  category=?", [category])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_quantity(self, quantity):
        self.connect()
        self.cursor.execute("select * from Raw_materials where  quantity=?", [quantity])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_role(self, role):
        self.connect()
        self.cursor.execute("select * from Raw_materials where  role=?", [role])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from Raw_materials where  id=?", [id])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from Raw_materials where username=? and password=?", [username, password])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def find_by_salary_min(self, salary):
        self.connect()
        self.cursor.execute("select * from Raw_materials where salary=?", [salary])
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list

    def reset_username_password(self, raw_material):
        self.connect()
        self.cursor.execute(
            "update Raw_materials set username=?,password=?) where id=?",
            [raw_material.username, raw_material.password, raw_material.id])

        self.connection.commit()
        self.disconnect()
        return raw_material

    def get_all(self):
        self.connect()
        self.cursor.execute("select * from Raw_materials")
        raw_material_list = [Raw_material(*raw_material) for raw_material in self.cursor.fetchall()]
        self.disconnect()
        return raw_material_list
