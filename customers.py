"""
This program keeps track of all of our customers
version : 1.0.0
Date :06.10.2022
"""
import json

with open('customers.json', 'r') as f:
  data = json.load(f)


#pprint.pprint(data)

customers = data.get('customers', [])

def customer():
    try:
        # initialize customers list
        customersList = []
        infile = open("customers.json", "r")
        line = infile.readline()
        while line:
            customersList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("the <customersList.json> file is not found ")
        print("Starting a new customers list!")
        customersList = []

    choice = 0
    while choice != 6:
        print('')
        print("-"*50)
        print("****** Customers Menu Section ********")
        print("-"*50)
        print('')
        print("1) Create | Add a customer")
        print("2) Lookup a customer")
        print("3) Read | Display customers")
        print("4) Update a customer")
        print("5) Delete a customer")
        print("6) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a customer......")
            name = input("Enter the name of the customer >>>")
            phone = input("Enter the phone of the customer >>>")
            customersList.append([name, phone])

            customers.append({
              'id': len(customers) + 1,
              'name': name,
              'phone': phone,
            })

            data['customers'] = customers
            with open('customers.json', 'w') as f:
              json.dump(data, f)
            print('*****Added Successfully......*****')
            print("-"*50)

        elif choice == 2:
            print("Looking up for a customer...")
            keyword = input("Enter Search Term: ")
            for customer in customers:
                if keyword in customer:
                    print(customer)
                    print("-"*50)

        elif choice == 3:
          print('ID\tName\t\tPhone')
          print('-'*50)
          for custom in customers:
            print(f'{custom.get("id")}\t{custom.get("name")}\t{custom.get("phone")}')
          print('-'*50)

        elif choice == 4:
            print("Updating customer details...")
            item_id = int(input('Enter item Id: '))
            #name = input('Give new name: ')
            new_phone = input('Give new phone: ')
            for i, customer in enumerate(customers):
                if customer['id'] == item_id:
                    #customer[i]['name'].append(name)
                    customer[i]['phone'].append(new_phone)
                    break
                print('Changes made to customer....')

        elif choice == 5:
            print("Deleting a customer...")
            

        elif choice == 6:
            data['items'] = customers
            with open('customers.json', 'w') as f:
                json.dump(data, f)
            print("Quitting Program.....")
    print("Program Terminated!")





