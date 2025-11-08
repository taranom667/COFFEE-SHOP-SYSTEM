import sqlite3
connection=sqlite3.connect('coffeshop_db')
cursor=connection.cursor()
cursor.connection.close()
connection.close()