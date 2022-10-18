import json

customer_file = "./json_data/customers.json"


# https://cloud.smartdraw.com/share.aspx/?pubDocShare=3E3F1AC07B1A20ACA149B26FBE674D1991D
def purchase():
    while True:
        print('')
        print("-" * 50)
        print("""
            ******* Purchase Menu Section *********

            1) Purchase products
            2) List purchases
            3) Back to Main Menu

        """)
        print("-" * 50)

        choice = input('Select a Menu option to continue: >> ')

        if choice == "1":

            process_order()

        elif choice == "2":

            completed_orders()

        elif choice == "3":
            from main import main

            main()
        else:
            print('\nINVALID MENU OPTION')


def process_order():
    final_order = {}
    with open("./json_data/cart.json", "r") as json_file:
        order_temp = json.load(json_file)
    # checks if cart is empty
    if not order_temp:
        from customers.customers import view_data
        view_data()
        with open(customer_file, "r") as json_file:
            customer_temp = json.load(json_file)
            data_length = len(customer_temp)
            while True:
                try:
                    customer_id = int(input(f"\nEnter Customer ID(1-{data_length}) of the buyer: >> "))
                except ValueError:
                    print(f"\nINVALID INPUT! Selection can't be an Alphabet")
                    continue
                if customer_id > data_length:
                    print("CUSTOMER DOES NOT EXIST! Enter VALID Customer ID!")
                    continue
                else:
                    break

            i = 1
            for entry in customer_temp:
                if i == int(customer_id):
                    final_order["Customer Name"] = entry["name"]
                    order_temp.append(final_order)
                    i = i + 1
                else:
                    pass
                    i = i + 1
        from products.products import view_data
        view_data()

        with open("./json_data/products.json", "r") as json_file:
            product_temp = json.load(json_file)
        data_length = len(product_temp)

        with open("./json_data/cart.json", "r") as json_file:
            cart_temp = json.load(json_file)
        option = int(input(f"Enter Product ID(1 - {data_length}) of item you wish to add to cart: >> "))
        i = 1
        for entry in product_temp:

            if i == int(option):
                prod_id = create_product_id()
                final_order[prod_id] = {}
                prod_qty = entry["stock"]
                final_order[prod_id]["id"] = option
                final_order[prod_id]["name"] = entry["name"]
                final_order[prod_id]["stock"] = int(input(f"\nEnter quantity (less than or equal "
                                                          f"to {prod_qty}) you wish to purchase: >> "))
                final_order[prod_id]["Product_Price"] = entry["price"]
                price = float(final_order[prod_id]["Product_Price"])
                subtotal = price * final_order[prod_id]["stock"]
                final_order[prod_id]["Sub-Total"] = float(subtotal)
                cart_temp.append(final_order)
                i = i + 1

            else:
                pass
                i = i + 1
        with open("./json_data/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\nProduct Added to cart!")

    else:
        from products.products import view_data
        view_data()
        with open("./json_data/products.json", "r") as json_file:
            prod_temp = json.load(json_file)
        data_length = len(prod_temp)

        with open("./json_data/cart.json", "r") as json_file:
            cart_temp = json.load(json_file)

        option = int(input(f"Enter Product ID(1 - {data_length}) of item you wish to add to cart: >> "))
        i = 1
        for entry in prod_temp:

            if i == int(option):
                prod_id = create_product_id()
                final_order[prod_id] = {}
                prod_qty = entry["stock"]
                final_order[prod_id]["Product_id"] = option
                final_order[prod_id]["Product_Name"] = entry["name"]
                final_order[prod_id]["Product_Quantity"] = int(input(f"\nEnter quantity (less than or equal "
                                                                     f"to {prod_qty}) you wish to purchase: >> "))
                final_order[prod_id]["Product_Price"] = entry["price"]
                price_tint = float(final_order[prod_id]["Product_Price"])
                subtotal = price_tint * final_order[prod_id]["Product_Quantity"]
                final_order[prod_id]["Sub-Total"] = float(subtotal)
                [open_cart_temp] = cart_temp
                open_cart_temp.update(final_order)

                i = i + 1

            else:
                pass
                i = i + 1
        with open("./json_data/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\nProduct Added to cart!")

    while True:
        cont_shopping = int(input("\nPress 1 to continue shopping and 2 to complete purchase: >> "))
        if cont_shopping == 1:
            process_order()
        elif cont_shopping == 2:
            # calculating total from subtotal
            with open("./json_data/cart.json", "r") as json_file:
                checkout_temp = json.load(json_file)
            emp_prd = {}
            [opened_checkout_temp] = checkout_temp
            new_id = "Total"
            total = 0
            for i in opened_checkout_temp:
                if i == "Customer Name":
                    continue
                else:
                    sub_total = float(opened_checkout_temp[i]["Sub-Total"])
                    total += sub_total
            emp_prd[new_id] = float(total)
            opened_checkout_temp.update(emp_prd)

            with open("./json_data/cart.json", "w") as json_file:
                json.dump(checkout_temp, json_file, indent=4)
        break

    # printing a receipt
    with open("./json_data/cart.json", "r") as json_file:
        fin_temp = json.load(json_file)
    [strip_fin_temp] = fin_temp

    print("\n----------------------------------------------")
    print("-------------------SHOP RECEIPT -----------------")
    print("----------------------------------------------")
    for i in strip_fin_temp:
        if i == "Customer Name":
            print(f"\nCustomer Name: {strip_fin_temp[i]}")
        elif i == "Total":
            print(f"\nTotal: Ksh. {strip_fin_temp[i]}")
        else:
            print(f"\nProduct Name: {strip_fin_temp[i]['name']}")
            print(f"Product Quantity: {strip_fin_temp[i]['stock']}")
            print(f"Product Price: Ksh. {strip_fin_temp[i]['Product_Price']}")
            print(f"Sub-Total: Ksh. {strip_fin_temp[i]['Sub-Total']}")

    print("\n----------------------------------------------")
    print("-------Thank you for Shopping with us---------")
    print("----------------------------------------------")

    # product quantity decrement
    with open("./json_data/cart.json", "r") as json_file:
        pid_temp = json.load(json_file)
    [open_pid] = pid_temp
    for i in open_pid:
        if i == "Customer Name":
            continue
        elif i == "Total":
            continue
        else:
            p_id_list = open_pid[i]["id"]
            p_qty_list = open_pid[i]["stock"]
            with open("./json_data/products.json", "r") as json_file:
                prod_temp = json.load(json_file)
            update_list = []
            j = 1
            for entry in prod_temp:
                if j == p_id_list:
                    product_id = entry["code"]
                    product_name = entry["name"]
                    product_qty = entry["stock"]
                    product_price = entry["price"]
                    product_qty = product_qty - p_qty_list
                    update_list.append({
                        "code": product_id,
                        "name": product_name,
                        "stock": product_qty,
                        "price": product_price})
                    j = j + 1
                else:
                    update_list.append(entry)
                    j = j + 1
            with open("./json_data/products.json", "w") as json_file:
                json.dump(update_list, json_file, indent=4)

    # generating a purchase list
    with open("./json_data/cart.json", "r") as json_file:
        c_temp = json.load(json_file)
    [strip_c_temp] = c_temp
    with open("./json_data/cart.json", "r") as json_file:
        o_temp = json.load(json_file)

    purchase_combination = {}
    order_id = create_purchase_id()
    purchase_combination[order_id] = strip_c_temp
    if not o_temp:
        o_temp.append(purchase_combination)
    else:
        [open_o_temp] = o_temp
        open_o_temp.update(purchase_combination)

    with open("./json_data/cart.json", "w") as json_file:
        json.dump(o_temp, json_file, indent=4)
        print("\nOrder record captured!")
    cart = []
    with open("./json_data/cart.json", "w") as json_file:
        json.dump(cart, json_file, indent=4)

    process_order()


def create_product_id():
    with open("./json_data/cart.json", "r") as json_file:
        gen_temp = json.load(json_file)
    if not gen_temp:
        new_id = 1
        return new_id
    else:
        [open_gen_temp] = gen_temp
        prev_id = list(open_gen_temp)[-1]
        length = len(prev_id)
        num = int(length) + 1
        new_id = num
        return new_id


def create_purchase_id():
    with open("./json_data/cart.json", "r") as json_file:
        od_temp = json.load(json_file)
    if not od_temp:
        new_id = 1
        return new_id
    else:
        [open_od_temp] = od_temp
        prev_id = list(open_od_temp)[-1]
        length = len(prev_id)
        num = int(length) + 1
        new_id = num
        return new_id


# Generating a purchase list
def completed_orders():
    with open("./json_data/cart.json", "r") as json_file:
        o_temp = json.load(json_file)
    [strip_o_temp] = o_temp

    print("\n------------------------------- Processed Customer Orders -----------------------------------\n")

    for i in strip_o_temp:
        print(f"Order: {i}")
        for j in strip_o_temp[i]:
            if j == "Customer Name":
                print(f"Customer Name: {strip_o_temp[i]['Customer Name']}")
            elif j == "Total":
                print(f"Total: Ksh. {strip_o_temp[i]['Total']}\n")
            else:
                # p_code = strip_o_temp[i][j]['code']
                p_name = strip_o_temp[i][j]['name']
                p_price = strip_o_temp[i][j]['price']
                p_qty = strip_o_temp[i][j]['stock']
                print(f"Product Name: {p_name}, Product Price: {p_price}, "
                      f"Product Quantity: {p_qty}, Sub-Total: Ksh. {strip_o_temp[i][j]['Sub-Total']}")
    print("-----------------------------------------------------------------------------------------")
    exit(0)

# purchase()
