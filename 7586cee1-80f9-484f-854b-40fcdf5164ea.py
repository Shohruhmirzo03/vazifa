# int, float, decimal

# print(0.1 + 0.1 + 0.1 == 0.3)
# print(0.1 + 0.1 + 0.1)

# from decimal import Decimal
#
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3'))
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))
#
# print(Decimal(0.1))

# -----------------------------------------------------------------------------------
# Funksiyalar

# def multiplay(x, y=4):
#     return x * y
#
# print(multiplay(5))


# -----------------------------------------------------------------------------------
# users = []
# def add_user(id, name, lastname):
#     users.extend([id, name, lastname])
#     return users
#
# while True:
#     id = int(input("ID: "))
#     name = input("Name: ")
#     last_name = input("Lastname: ")
#     print(add_user(id, name, last_name))


# users_list = []
# def users(id, name, lastname, age, address):
#     users_list.extend([id, name, lastname, age, address])
#     return users_list
#
# print(users(1, 'Toxir', 'Toxirov', 22, 'Fergana'))


# ----------------------------------------------------------


# def users(id: int, name: str, lastname: str, age: int, address: str):
#     user_info = {
#         "id": id,
#         "name": name,
#         "lastname": lastname,
#         "age": age,
#         "address": address
#     }
#     return user_info
#
# print(users(1, 'Toxir', 'Toxirov', 22, 'Fergana'))


# ---------------------------------------------------------------------------------------------

# def user(name, lastname='Sobirov', *args, **kwargs):
#     print(name, lastname, args, kwargs)
#
# user("Toxir", "Toxirov", 'Futbol', 'Coding', 'Reading', age=27, address="Fergana")

# ----------------------------------------------------------------------------------------------

# Closure (Замыкание)

# def hello():
#     print("Nimadir bo'ladi")
#     def inner(name):
#         print(f"Assalomu alaykum {name}")
#     return inner
#
# hello1 = hello()
#
# hello1("Toxir")
#
# hello1('Sobir')


# ----------------------------------------------------------------------------------------------

# def multiplay(num1):
#     def inner(num2):
#         return num1 * num2
#     return inner
#
# number1 = multiplay(5)
#
# print(number1(3))
# print(number1(6))
# print(number1(7))
#
# number2 = multiplay(3)
# print(number2(9))


# ----------------------------------------------------------------------------------------------

# users = [
#     {"id": 1, "name": "Toxir", "password": "123"},
#     {"id": 2, "name": "Sobir", "password": "sobir1225"}
# ]
#
# def get_user(users_list: list):
#     def inner(id):
#         return list(filter(lambda user: user['id'] == id, users_list))
#     return inner
#
# us = get_user(users)
#
# id_1 = us(1)
# print(id_1)
#
# id_2 = us(2)
# print(id_2)
#
# '''
# admins
# id, name, lastname, password, address, phone
# '''

# ----------------------------------------------------------------------------------------------
















