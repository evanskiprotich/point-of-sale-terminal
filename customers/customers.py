"""
This program keeps track of all of our customers
version : 1.0.0
Date :06.10.2022
"""
import json
import re


def view_data():
    print('Id\tName\t\tPhone\t\t\tEmail')
    print('-' * 50)
    f = open('./json_data/customers.json', 'r')
    customers = json.load(f)
    for customer in customers:
        print(f'{customer.get("id")}\t{customer.get("name")}\t\t\t{customer.get("phone")}\t\t\t{customer.get("email")}')
    print('-' * 50)


def solve(email):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, email):
        return True
    return False


def validate_phone(phone):
    pattern = r"^[07]|[01][0-9]{10}$"
    if re.match(pattern, phone):
        return True
    return False


def add_data():
    f = open('./json_data/customers.json', 'r')
    customers_add = json.load(f)
    data_length = len(customers_add)

    # item_data = {
    #     "id": data_length + 1,
    #     "name": input("Name of the Customer: >> "),
    #     "phone": input("Phone Number of the Customer: >> "),
    #     "email": input("Email of the Customer: >> ")
    # }
    customer = {}
    customer["id"] = data_length + 1
    customer["name"] = input("Enter Name: ")
    while True:
        email = input("Customer Email: ")
        if solve(email):
            customer["email"] = email
            break
        else:
            print("Enter the correct email format!")
            continue
    while True:
        phone = input("Enter Phone Number: ")
        if validate_phone(phone):
            customer["phone"] = phone
            break
        else:
            print("Phone number should start with 0 !")
            continue
    customers_add.append(customer)

    # customers_add.append(item_data)

    with open("./json_data/customers.json", 'w') as json_file:
        json.dump(customers_add, json_file, indent=4)


def edit_data():
    print("Want to update a customer?")
    print("Press 1 to view index of Customer you want to update: >> ")
    user_input = input("Enter value to proceed: ")
    if user_input == "1":
        view_data()
        new_data = []
        f = open('./json_data/customers.json', 'r')
        customers = json.load(f)
        data_length = len(customers) - 1
        print("Which index would you like to update?")
        edit_option = input(f"Select a number between 0 and {data_length}: ")
        i = 0
        for customer in customers:
            if i == int(edit_option):
                id = customer["id"]
                name = customer["name"]
                phone = customer["phone"]
                email = customer["email"]
                print(f"ID of customer is: {id}")
                print(f"Name of customer is:  {name}")
                name = input("What would you like the new name of customer be?:  ")
                print(f"Phone No of customer is: {phone}")
                phone = input("What would you like the new Phone No of customer be?:  ")
                print(f"Email of customer is: {email}")
                email = input("What would you like the new email of customer be?:  ")
                new_data.append({"id": id, "name": name, "phone": phone, "email": email})
                print("\n")

                i = i + 1
            else:
                new_data.append(customer)
                i = i + 1
        with open('./json_data/customers.json', 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print("Customer updated successfully")

    else:
        print("Invalid input try again")
        edit_data()


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
