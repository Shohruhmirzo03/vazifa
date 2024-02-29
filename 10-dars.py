import psycopg2 as sql

db = sql.connect(
    database='10-dars',
    host='localhost',
    user='postgres',
    password='123456',
    port='5432'
)

cursor = db.cursor()

cursor.execute('''SELECT * FROM customers''')

customers = cursor.fetchall()
print(customers)


cursor.execute('INSERT INTO brands(brand_name) VALUES (%s)', ('Nissan',))

brands = [
    ('Chevrolet',),
    ('Daewoo',),
    ('Mers',)
]

cursor.executemany('INSERT INTO brands(brand_name) VALUES (%s)', brands)


cursor.execute("SELECT * FROM brands")
brands = cursor.fetchmany(4)
print(brands)


db.commit()
db.close()