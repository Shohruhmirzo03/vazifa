import psycopg2 as sql

db = sql.connect(
    database='autasalon',
    host='localhost',
    user='postgres',
    password='1',
    port='5432'
)

cursor = db.cursor()



cursor = db.cursor()

cursor.execute('''SELECT * FROM customers''')
cursor.execute('''SELECT * FROM models''')
cursor.execute('''SELECT * FROM brands''')
cursor.execute('''SELECT * FROM colors''')
cursor.execute('''SELECT * FROM models''')


customers = cursor.fetchall()
print(customers)





db.commit()
db.close()
