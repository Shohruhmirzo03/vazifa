import sqlite3


class DataBase:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    def execute(self, sql: str, parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
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
            brand_name VARCHAR(15) UNIQUE
        )'''
        self.execute(sql, commit=True)

    def insert_brand(self, brand_name):
        sql = '''INSERT INTO brands(brand_name) VALUES (?)'''
        self.execute(sql, parameters=(brand_name,), commit=True)

    def select_brands(self):
        sql = '''SELECT * FROM brands'''
        return self.execute(sql, fetchall=True)

    def delete_brand(self, brand_name):
        sql = '''DELETE FROM brands WHERE brand_name = ?'''
        self.execute(sql, parameters=(brand_name,), commit=True)

    def create_table_models(self):
        sql = '''CREATE TABLE IF NOT EXISTS models(
            model_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name VARCHAR(30) UNIQUE,
            color VARCHAR(10),
            price INTEGER,
            brand_id INTEGER REFERENCES brands(brand_id)
        )'''
        self.execute(sql, commit=True)

    def insert_model(self, model_name, color, price, brand_id):
        sql = '''INSERT INTO models(model_name, color, price, brand_id) VALUES (?, ?, ?, ?)'''
        self.execute(sql, parameters=(model_name, color, price, brand_id), commit=True)

    def select_models(self):
        sql = '''SELECT model_id, model_name, color, price, brand_name FROM models
        JOIN brands ON models.brand_id = brands.brand_id'''
        return self.execute(sql, fetchall=True)


db = DataBase()