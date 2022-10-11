import json

with open('products.json', 'r') as f:
  data = json.load(f)


#pprint.pprint(data)

products = data.get('products', [])


def product():
    try:
        # initialize product list
        productsList = []
        infile = open("products.json", "r")
        line = infile.readline()
        while line:
            productsList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("the <productList.json> file is not found ")
        print("Starting a new product list!")
        productsList = []

    choice = 0
    while choice != 6:
        print('')
        print("-"*50)
        print("******* Products Menu Section *********")
        print("-"*50)
        print('')
        print("1) Create | Add a product")
        print("2) Lookup a product")
        print("3) Read | Display products")
        print("4) Update a product")
        print("5) Delete a product")
        print("6) Quit")

        choice = int(input())

        if choice == 1:
            print("Adding a product........")
            productName = input("Enter the name of the product >>> ")
            productPrice = input("Enter the price of the product >>> ")
            # Adding the products to an array
            productsList.append([productName, productPrice])

            # Saving to external JSON file
            products.append({
              'id': len(products) + 1,
              'name': productName,
              'price': productPrice,
            })

            data['products'] = products
            with open('products.json', 'w') as f:
              json.dump(data, f)
            print('*****Added Successfully......*****')
            print("-"*50)

        elif choice == 2:
            print("Looking up for a product...")
            keyword = input("Enter Search Term: ")
            for product in productsList:
                if keyword in product:
                    print(product)
            # keyword = input("Enter Search Term: ")
            # for product in products:
            #     if keyword in product:
            #         print('Name\t\tPrice')
            #         print('-'*50)
            #         print(f'{product.get("name")}\t{product.get("price")}')
            #         print('-'*50)

        elif choice == 3:
            print("Displaying all products...")
            print('ID\tName\t\tPrice')
            print('-'*50)
            for product in products:
              print(f'{product.get("id")}\t{product.get("name")}\t{product.get("price")}')
            print('-'*50)

        elif choice == 4:
            print("Updating a product...")
            

        elif choice == 5:
            print("Deleting products...")
            

        elif choice == 6:
            print("Quitting Program")
    print("Program Terminated!")
