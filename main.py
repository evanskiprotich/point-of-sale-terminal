from datetime import datetime
from customers.customers import customer
from products.products import product
from purchase import purchase


def main():
    print('')
    print('-' * 50)
    msg = '**** WELCOME TO OUR POINT OF SALE SYSTEM ****'
    print(msg)
    print('-' * 50)

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)

    menu = 0
    while menu != 5:
        print('')
        print('-' * 50)
        print('Please Select a Menu Option You Want to Access...')
        print("1) Customers Details")
        print("2) Products Details")
        print("3) Go To Shopping")
        print("0) Quit")
        print('-' * 50)
        menu = int(input())

        if menu == 1:
            print('-' * 50)
            print("Opening customers menu......")
            customer()

        elif menu == 2:
            print('-' * 50)
            print('Opening products menu.....')
            product()

        elif menu == 3:
            print('-' * 50)
            print('Opening shopping menu.....')
            purchase()
        elif menu == 0:
            print("Quitting Program.....")
            break
    print("Program Terminated!")


if __name__ == "__main__":
    main()
