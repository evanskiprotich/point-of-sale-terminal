from datetime import datetime
from customers import customer
from products import product
from purchase import purchaseSystem
import sys

def main():
    print('')
    print('-'*50)
    msg = '**** WELCOME TO EK POINT OF SALE SYSTEM ****'
    print(msg)
    print('-'*50)

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)

    menu = 0
    while menu != 5:
        print('')
        print('-'*50)
        print('Please Select a Menu Option...')
        print("1) Customers")
        print("2) Products")
        print("3) Purchase")
        print("0) Quit")
        print('-'*50)
        menu = int(input())

        if menu == 1:
            print("Opening customers menu......")
            customer()

        elif menu == 2:
            print('Opening products menu.....')
            product()

        elif menu == 3:
            print('Opening purchase menu.....')
            a = purchaseSystem()
            while 1:
                a.purchase()

        elif menu == 0:
            print("Quitting Program.....")
        
    print("Program Terminated!")


if __name__ == "__main__":
    main()
