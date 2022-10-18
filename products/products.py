import json

filename = "./json_data/products.json"


def view_data():
    print('Code\tName\t\tPrice\tStock')
    print('-' * 50)
    f = open(filename, 'r')
    products = json.load(f)
    for product in products:
        print(f'{product.get("code")}\t{product.get("name")}\t\t{product.get("price")}\t{product.get("stock")}')
    print('-' * 50)


def add_data():
    f = open(filename, 'r')
    products_add = json.load(f)
    item_data = {
        "code": input("Code of Product: >> "),
        "name": input("Name of Product: >> "),
        "price": int(input("Price of Product: >> ")),
        "stock": int(input("Stock Available: >> "))
    }

    products_add.append(item_data)

    with open(filename, 'w') as json_file:
        json.dump(products_add, json_file, indent=4)


def delete_data():
    view_data()
    new_data = []
    f = open(filename, 'r')
    products_delete = json.load(f)
    data_length = len(products_delete) - 1
    print("Which Index Number to Delete")
    delete_option = input(f"select a number 0-{data_length}: >> ")
    i = 0
    for entry in products_delete:
        if i == int(delete_option):
            pass
            i += 1
        else:
            new_data.append(entry)
            i = i + 1
    with open(filename, 'w') as f:
        json.dump(new_data, f, indent=4)


def edit_data():
    view_data()
    new_data = []
    f = open(filename, 'r')
    products_edit = json.load(f)
    data_length = len(products_edit) - 1
    print("Which Index Number to edit")
    edit_option = input(f"select a number 0-{data_length}: >> ")
    i = 0
    for entry in products_edit:
        if i == int(edit_option):
            code = entry['code']
            name = entry['name']
            price = entry['price']
            stock = entry['stock']
            print(f"Current Code: {code}")
            name = input("What would you like the new code to be: >> ")
            print(f"Current Name: {name}")
            name = input("What would you like the new name to be: >> ")
            print(f"Current Price : {price}")
            price = input("What would you like the new price to be: >> ")
            print(f"Current Stock : {stock}")
            stock = input("What would you like the new stock to be: >> ")
            new_data.append({"code": code, "name": name, "price": price, "stock": stock})
            i += 1
        else:
            new_data.append(entry)
            i = i + 1
    with open(filename, 'w') as f:
        json.dump(new_data, f, indent=4)


# search for product by name
def search_name():
    while True:
        product_name = input("\nEnter name of product to search: >> ")
        check = confirm_name(product_name)
        if check == 'y':
            break
        else:
            print("\nProduct not found!!!")


def confirm_name(product_name):
    with open("./json_data/products.json", "r") as json_file:
        product_temp = json.load(json_file)
    for entry in product_temp:
        if product_name in entry['name']:
            print(f"Product Name: {entry['name']}")
            return 'y'
        else:
            continue
    return


def product():
    def choices():
        print('')
        print("-" * 50)
        print("******* Products Menu Section *********")
        print("-" * 50)
        print('')
        print("1) View | Read Products")
        print("2) Add | Create a Product")
        print("3) Delete a Product")
        print("4) Update a product")
        print("5) Search a product")
        print("6) Quit")

    while True:
        choices()
        choice = int(input("\nChoose an option: "))
        if choice == 1:
            print("Opening all Products...")
            view_data()
        elif choice == 2:
            print("Adding a product........")
            add_data()
            print("**** Successfully Added the product ****")
        elif choice == 3:
            delete_data()
            print("**** Successfully Deleted the product ****")
        elif choice == 4:
            print("Editing a product....")
            edit_data()
            print("**** Successfully Deleted the product ****")

        elif choice == 5:
            print("Searching For a Product.....")
            search_name()
        elif choice == 6:
            break
        else:
            print("Invalid choice, please choose a different option")
