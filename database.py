import sqlite3



class DataBase:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = sqlite3.connect(self.path_to_db)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_brands(self):
        sql = '''CREATE TABLE IF NOT EXISTS brands(
            brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand_name VARCHAR(15)
        )'''
        self.execute(sql, commit=True)

    def insert_brand(self, brand_name):
        sql = '''INSERT INTO brands(brand_name) VALUES (?)'''
        self.execute(sql, parameters=(brand_name,), commit=True)

db = DataBase()