import json
from email.message import EmailMessage
import ssl
import smtplib

customer_file = "./json_data/customers.json"


def purchase():
    while True:
        print('')
        print("-" * 50)
        print("""
            ******* Purchase Menu Section *********

            1) Purchase products
            0) Back to Main Menu

        """)
        print("-" * 50)

        choice = input('Select a Menu option to continue: >> ')

        if choice == "1":

            process_order()

        # elif choice == "2":
        #
        #     completed_orders()

        elif choice == "0":
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
                    print(f"\nINVALID INPUT!")
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
                product_id = create_product_id()
                final_order[product_id] = {}
                prod_qty = entry["stock"]
                final_order[product_id]["id"] = option
                final_order[product_id]["name"] = entry["name"]
                final_order[product_id]["stock"] = int(input(f"\nEnter quantity (less than or equal "
                                                             f"to {prod_qty}) you wish to purchase: >> "))
                final_order[product_id]["Product_Price"] = entry["price"]
                price = float(final_order[product_id]["Product_Price"])
                subtotal = price * final_order[product_id]["stock"]
                final_order[product_id]["Sub-Total"] = float(subtotal)
                cart_temp.append(final_order)
                i = i + 1

            else:
                pass
                i = i + 1
        with open("./json_data/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\n\n*****Product Added to cart!*****")

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
                product_id = create_product_id()
                final_order[product_id] = {}
                prod_qty = entry["stock"]
                final_order[product_id]["id"] = option
                final_order[product_id]["name"] = entry["name"]
                final_order[product_id]["stock"] = int(input(f"\nEnter quantity (less than or equal "
                                                             f"to {prod_qty}) you wish to purchase: >> "))
                final_order[product_id]["Product_Price"] = entry["price"]
                price_tint = float(final_order[product_id]["Product_Price"])
                subtotal = price_tint * final_order[product_id]["stock"]
                final_order[product_id]["Sub-Total"] = float(subtotal)
                [open_cart_temp] = cart_temp
                open_cart_temp.update(final_order)

                i = i + 1

            else:
                pass
                i = i + 1
        with open("./json_data/cart.json", "w") as json_file:
            json.dump(cart_temp, json_file, indent=4)
            print("\n\n***Product Added to cart!****")

    while True:
        cont_shopping = int(input("\nPress 1 to continue shopping and 2 to complete purchase: >> "))
        if cont_shopping == 1:
            process_order()
        elif cont_shopping == 2:
            # calculating total from subtotal
            with open("./json_data/cart.json", "r") as json_file:
                checkout = json.load(json_file)
            product = {}
            [open_checkout] = checkout
            new_id = "Total"
            total = 0
            for i in open_checkout:
                if i == "Customer Name":
                    continue
                else:
                    sub_total = float(open_checkout[i]["Sub-Total"])
                    total += sub_total
            product[new_id] = float(total)
            open_checkout.update(product)

            with open("./json_data/cart.json", "w") as json_file:
                json.dump(checkout, json_file, indent=4)
        break

    # printing a receipt
    with open("./json_data/cart.json", "r") as json_file:
        final_temp = json.load(json_file)
    [receipt] = final_temp

    print("\n----------------------------------------------")
    print("-------------------SHOP RECEIPT -----------------")
    print("----------------------------------------------")
    for i in receipt:
        if i == "Customer Name":
            print(f"\nCustomer Name: {receipt[i]}")
        elif i == "Email":
            pass
        elif i == "Total":
            print(f"\nTotal: Ksh. {receipt[i]}")
        else:
            print(f"\nProduct Name: {receipt[i]['name']}")
            print(f"Product Quantity: {receipt[i]['stock']}")
            print(f"Product Price: Ksh. {receipt[i]['Product_Price']}")
            print(f"Sub-Total: Ksh. {receipt[i]['Sub-Total']}")

    print("\n----------------------------------------------")
    print("-------Thank you for Shopping with us---------")
    print("----------------------------------------------")

    send_mail()
    # product quantity decrement
    with open("./json_data/cart.json", "r") as json_file:
        prod_temp = json.load(json_file)
    [ordered] = prod_temp
    for i in ordered:
        if i == "Customer Name":
            continue
        elif i == "Total":
            continue
        else:
            p_id_list = ordered[i]["id"]
            p_qty_list = ordered[i]["stock"]
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
    [purchases] = c_temp
    with open("./json_data/cart.json", "r") as json_file:
        order_temp = json.load(json_file)

    purchase_combination = {}
    order_id = create_purchase_id()
    purchase_combination[order_id] = purchases
    if not order_temp:
        order_temp.append(purchase_combination)
    else:
        [open_o_temp] = order_temp
        open_o_temp.update(purchase_combination)

    with open("./json_data/cart.json", "w") as json_file:
        json.dump(order_temp, json_file, indent=4)
        print("\n\n****Order has been successfully recorded****")
    cart = []
    with open("./json_data/cart.json", "w") as json_file:
        json.dump(cart, json_file, indent=4)

    process_order()


def create_product_id():
    with open("./json_data/cart.json", "r") as json_file:
        create_temp = json.load(json_file)
    if not create_temp:
        new_id = 1
        return new_id
    else:
        [create_id] = create_temp
        prev_id = list(create_id)[-1]
        length = len(prev_id)
        num = int(length) + 1
        new_id = num
        return new_id


def create_purchase_id():
    with open("./json_data/cart.json", "r") as json_file:
        purchase_id = json.load(json_file)
    if not purchase_id:
        new_id = 1
        return new_id
    else:
        [id_purchase] = purchase_id
        prev_id = list(id_purchase)[-1]
        length = len(prev_id)
        num = int(length) + 1
        new_id = num
        return new_id


# Generating a purchase list
def completed_orders():
    with open("./json_data/cart.json", "r") as json_file:
        completed = json.load(json_file)
    [complete_order] = completed

    print("\n******* Processed Customer Orders **********\n")

    for i in complete_order:
        print(f"Order: {i}")
        for j in complete_order:
            if j == "Customer Name":
                print(f"Customer Name: {complete_order['Customer Name']}")
            elif j == "Total":
                print(f"Total: Ksh. {complete_order['Total']}\n")
            else:
                # p_code = complete_order[i][j]['code']
                p_name = complete_order[i][j]['name']
                p_price = complete_order[i][j]['price']
                p_qty = complete_order[i][j]['stock']
                print(f"Product Name: {p_name}, Product Price: {p_price}, "
                      f"Product Quantity: {p_qty}, Sub-Total: Ksh. {complete_order[i][j]['Sub-Total']}")
    print("-" * 50)
    exit(0)


def send_mail():
    f = open('./json_data/customers.json', 'r')
    customers = json.load(f)
    for customer in customers:
        email_receive = customer.get("email")

    with open("./json_data/cart.json", "r") as json_file:
        email_temp = json.load(json_file)
    [email] = email_temp

    email_sender = 'evanskiprotich14@gmail.com'
    email_password = 'kvhblstbslluoftn'
    email_receiver = email_receive

    subject = "YOUR RECEIPT"

    body = "\n--------------------------------------------------"
    body += "-------------------SHOP RECEIPT--------------------"
    body += "\n"

    for i in email:
        if i == "Customer Name":
            body += f"\nCustomer Name: {email[i]}"
        elif i == "Total":
            body += f"\nTotal: Ksh. {email[i]}"
        elif i == "Email":
            email_receiver = {email[i]}
        else:
            body += f"\nProduct Name: {email[i]['name']}"
            body += f"\nProduct Quantity: {email[i]['stock']}"
            body += f"\nProduct Price: Ksh. {email[i]['Product_Price']}"
            body += f"\nSub-Total: Ksh. {email[i]['Sub-Total']}"
            body += "\n"
    body += "\n*" * 50
    body += "******** Thank you for Shopping with us *******"
    body += "*" * 50

    mail = EmailMessage()
    mail['From'] = email_sender
    mail['To'] = email_receiver
    mail['subject'] = subject
    mail.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, mail.as_string())

# purchase()
