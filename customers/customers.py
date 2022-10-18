"""
This program keeps track of all of our customers
version : 1.0.0
Date :06.10.2022
"""
import json


def view_data():
    print('Id\tName\t\tPhone')
    print('-' * 50)
    f = open('./json_data/customers.json', 'r')
    customers = json.load(f)
    for customer in customers:
        print(f'{customer.get("id")}\t{customer.get("name")}\t\t{customer.get("phone")}')
    print('-' * 50)


def add_data():
    f = open('./json_data/customers.json', 'r')
    customers_add = json.load(f)
    data_length = len(customers_add)
    item_data = {
        "id": data_length + 1,
        "name": input("Name of the Customer: >> "),
        "phone": input("Phone Number of the Customer: >> ")
    }

    customers_add.append(item_data)

    with open("./json_data/customers.json", 'w') as json_file:
        json.dump(customers_add, json_file, indent=4)


def edit_data():
    view_data()
    new_data = []
    f = open('./json_data/customers.json', 'r')
    customers_edit = json.load(f)
    data_length = len(customers_edit) - 1
    id_length = len(customers_edit)
    print("Which Index Number to edit")
    edit_option = input(f"select a number 0-{data_length}: >> ")
    i = 0
    for entry in customers_edit:
        if i == int(edit_option):
            customers_name = entry['name']
            customers_phone = entry['phone']
            customers_id = id_length
            print(f"Current Name: {customers_name}")
            customers_name = input("What would you like the new name to be: ")
            print(f"Current Phone : {customers_phone}")
            customers_phone = input("What would you like the new phone to be: ")
            new_data.append({"id": customers_id, "name": customers_name, "phone": customers_phone})
            i += 1
        else:
            new_data.append(entry)
            i = i + 1
    with open("./json_data/customers.json", 'w') as f:
        json.dump(new_data, f, indent=4)


def delete_data():
    view_data()
    new_data = []
    f = open('./json_data/customers.json', 'r')
    customers_delete = json.load(f)
    data_length = len(customers_delete) - 1
    print("Which Index Number to Delete")
    delete_option = input(f"select a number 0-{data_length}: >> ")
    i = 0
    for entry in customers_delete:
        if i == int(delete_option):
            pass
            i += 1
        else:
            new_data.append(entry)
            i = i + 1
    with open("./json_data/customers.json", 'w') as f:
        json.dump(new_data, f, indent=4)


def customer_search():
    while True:
        print("""
             ----------------------------------------------
             Customer Search Sub-Menu:-
             1) Search by Name
             2) Back to Customer Sub-Menu
             ----------------------------------------------
                 """)
        c_choice = input('Enter a Menu option to continue:')
        if c_choice == "1":
            search_name()
        else:
            print('INVALID MENU OPTION')


# search for customer by name
def search_name():
    while True:
        cus_name = input("\nEnter name of customer to search:")
        check = confirm_name(cus_name)
        if check == 'y':
            break
        else:
            print("\nCustomer not found! Please input an existing Customer name")


def confirm_name(customer_name):
    with open("./json_data/customers.json", "r") as json_file:
        c_cus_temp = json.load(json_file)
    for entry in c_cus_temp:
        if customer_name in entry['name']:
            print(f"Customer Name: {entry['name']}")
            print(f"Customer Phone: {entry['phone']}")
            return 'y'
        else:
            continue
    return


def customer():
    try:
        # initialize customers list
        customersList = []
        infile = open("./json_data/customers.json", "r")
        line = infile.readline()
        while line:
            customersList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("the <customersList.json> file is not found ")
        print("Starting a new customers list!")

    choice = 0
    while True:
        print('')
        print("-" * 50)
        print("******* Customers Menu Section *********")
        print("-" * 50)
        print('')
        print("1) View | Read Customers")
        print("2) Add | Create a Customer")
        print("3) Delete a Customer")
        print("4) Update a Customer")
        print("5) Search a Customer")
        print("6) Quit")
        choice = int(input())

        if choice == 1:
            view_data()
            print("-" * 50)

        elif choice == 2:
            print("Adding a customer......")
            add_data()
            print('*****Added Successfully......*****')
            print("-" * 50)

        elif choice == 3:
            print("Deleting a customer...")
            delete_data()
            print('*****Deleted Successfully......*****')
            print("-" * 50)

        elif choice == 4:
            print("Updating customer details...")
            edit_data()
            print('*****Updated Successfully......*****')
            print("-" * 50)

        elif choice == 5:
            print("Search customer details...")
            search_name()
            print('*****Customer Found......*****')
            print("-" * 50)

        elif choice == 6:
            print("Quitting Program.....")
            break
