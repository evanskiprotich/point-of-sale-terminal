import json


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
        print("5) Quit")

    def view_data():
        print('Code\tName\t\tPrice')
        print('-' * 50)
        f = open('products.json', 'r')
        products = json.load(f)
        for product in products:
            print(f'{product.get("code")}\t{product.get("name")}\t\t{product.get("price")}')
        print('-' * 50)

    def add_data():

        f = open('products.json', 'r')
        products_add = json.load(f)
        item_data = {
            "code": input("Code of Product: >> "),
            "name": input("Name of Product: >> "),
            "price": int(input("Price of Product: >> "))
        }

        products_add.append(item_data)

        with open("products.json", 'w') as json_file:
            json.dump(products_add, json_file, indent=4)

    def delete_data():
        view_data()
        new_data = []
        f = open('products.json', 'r')
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
        with open("products.json", 'w') as f:
            json.dump(new_data, f, indent=4)

    def edit_data():
        view_data()
        new_data = []
        f = open('products.json', 'r')
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
                print(f"Current Code: {code}")
                name = input("What would you like the new code to be: >> ")
                print(f"Current Name: {name}")
                name = input("What would you like the new name to be: >> ")
                print(f"Current Price : {price}")
                price = input("What would you like the new price to be: >> ")
                new_data.append({"code": code, "name": name, "price": price})
                i += 1
            else:
                new_data.append(entry)
                i = i + 1
        with open("products.json", 'w') as f:
            json.dump(new_data, f, indent=4)

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
            break
        else:
            print("Invalid choice, please choose a different option")


