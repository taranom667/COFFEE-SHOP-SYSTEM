import sqlite3

class Customer_repository:
        def __init__(self):
            self.cursor = None
            self.connection = None

        def connect(self):
            self.connection = sqlite3.connect("./database/COFFESHOP_db")
            self.cursor = self.connection.cursor()