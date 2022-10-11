from datetime import datetime
import random
import sys
import json

with open('products.json', 'r') as f:
  data = json.load(f)


#pprint.pprint(data)

all_products = data.get('products', [])


class purchaseSystem:

    def purchase(self):
        print("*************************************")
        print("\tThe Purchase Menu Options")
        print("*************************************")
        print("\t1.Show All Products")
        print("\t2.Buy Product")
        print("\t3.Exit")
        print("**************************************")

        def display_all():
            print('ID\tName\t\tPrice')
            print('-'*50)
            for product in all_products:
              print(f'{product.get("id")}\t{product.get("name")}\t{product.get("price")}')
            print('-'*50)

        # def order_summary(product, name):
            

        # def generate_bill(product, name):
        #     print("***********************************************")
        #     print("\t\tEk Electronic Shop")
        #     print("***********************************************")
        #     print("Bill:{} \tDate:{}".format(int(random.random() * 100000), str(datetime.now())))
        #     print("Customer Name: {}".format(name))
        #     print("Product Name: {}".format(item[1]))
        #     print("Price: {}".format(item[-1]))
        #     print("***********************************************")
        #     print("\t\tTotal Amount: {}".format(item[-1]))

        while True:
            choice = int(input())
            if choice == 1:
                display_all()
            elif choice == 2:
                print("***********************************************")
                print("\t\tTodays Available Products")
                print("***********************************************")
                print("Order Summary\tDate:{}".format(str(datetime.now())))
                ordered_items = {}
                order_items = list(map(int, input('What do you want to buy today? ').split(',')))
                print('-'*50)
                print('ID\tName\tPrice\tquantity\tAmount')
                print('-'*50)

                total_bill = 0
                for order_item in order_items:
                  for item in all_products:
                    if item['id'] == order_item:
                      if order_item in ordered_items:
                        ordered_items[order_item]['quantity'] += 1
                      else:
                        ordered_items[order_item] = item
                        ordered_items[order_item]['quantity'] = 1
                        break
                for item in ordered_items:
                  name = ordered_items[item]['name']
                  price = ordered_items[item]['price']
                  quantity = ordered_items[item]['quantity']
                  amount = price * quantity
                  print(f'{item}\t{name}\t{price}\t{quantity}\t\t{amount}')
                  total_bill += amount
                print('-'*50)
                print(f'\t Total Amount: {total_bill}')
                print('-'*50)
                
          
            elif choice == 3:
                print("Quitting Program")
            print("Continue Shopping!")
