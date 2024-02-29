from database import db

db.create_table_brands()
db.create_table_models()


def add_brand():
    brand = input("Brand nomini kiriting: ")
    db.insert_brand(brand)
    yes_no = input("Yana brand qo'shasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_brand()


def del_brand():
    view_brands()
    brand = input("O'chirmoqchi bo'lgan brand nomini kiriting: ")
    db.delete_brand(brand)
    yes_no = input("Yana brand o'chirasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        del_brand()


def view_brands():
    brands = db.select_brands()
    for brand in brands:
        print(brand[0], brand[1])


def add_model():
    model = input("Model nomini kiriting: ")
    color = input("Model rangini kiriting: ")
    price = int(input("Model narxini kiriting: "))
    view_brands()
    brand_id = int(input("Brand id sini kiriting: "))
    db.insert_model(model, color, price, brand_id)
    yes_no = input("Yana model qo'shasizmi? yes/no: ").lower()
    if yes_no == 'yes':
        add_model()

def view_models():
    models = db.select_models()
    for model in models:
        model_id, model, color, price, brand = model
        print(model_id, model, color, price, brand)


def run():
    while True:
        command = input("Nima qilmoqchisiz? : ").lower()
        if command == 'add brand':
            add_brand()

        if command == 'del brand':
            del_brand()

        if command == 'view brands':
            view_brands()

        if command == 'add model':
            add_model()

        if command == 'view models':
            view_models()

        if command == 'stop':
            break



if __name__ == '__main__':
    run()