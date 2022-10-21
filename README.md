# `Point of Sale Terminal`
A python point of sale CLI terminal System
## `SEPA Sprint 1` ##

# Sprint Deliverables
- Develop a POS system using python
- Validate input data(phone number and email)
- Print a receipt and send either via Email 

## The POS Description
POS Console App is a Command - Line based Point Of Sale System. 
This program is developed  using Python programming language. 
It is a single user application meant to operate in a sales store or shops. 
This system allows for CRUD operations for customers and products. When the operations are done, a customer should be able to make purchases based on the products they added to their program. This is a menu-driven program based on a user's input.
This program implemented a JSON file to store its file and SMTP for email authentication.



## Table of contents
* [Sprint Deliverables] (#Sprint Deliverables)
* [The POS Description](#The POS Description)
* [Flow Chart](#FLow Chart)
* [Features](#Features)
* [Goals](#Goals)
* [Setup](#Setup)
* [Author](#Author)

## Flow Chart
https://cloud.smartdraw.com/share.aspx/?pubDocShare=3E3F1AC07B1A20ACA149B26FBE674D1991D


## Features
## Main Menu
A menu when the app is launched. It contains Customer Menu, Product Menu and Shopping Menu.
### Customer Operations
A user is able to feed into the system customer data, view available customers, update existing customer data and delete a particular customer. All customer records can further be accessed.
Sample Customer details Format
    ```
        [
    {
        "id": 1,
        "name": "Evan",
        "phone": "0723287190",
        "email": "evanskiprotich14@gmail.com"
    }
]
    ```

### Product Operations
A user can key in the product's data for inventory purposes, view the available products, update product data and delete a product.
Sample Product details Format
    ```
        [
            {
        "code": 1,
        "name": "Chicken",
        "stock": 22,
        "price": 89
    },
        ]
    ```

### Purchase function
Customer details were first retrieved then added to the ongoing purchase, the user then adds the products and the quantities that the customer has ordered into a cart. In the process the subtotal of all products are calculated. During checkout, the total cost is calculated, product quantity decremented for the remaining products in the store and a receipt issued to the customer. The data captured in the cart is used to generate a purchase log that can later be viewed. The cart is then emptied to make room for future purchases. The purchase log generated contains the orders that were made from different purchases, the customers in-charge, purchased products and total amounts.

## Goals

Implement a python program that starts with a menu, gets user menu choice and proceeds to execute the subprogram associated with the menu.
The data will be stored in a json file.

## Setup
### Requirements
Python 3 is required to be installed in your system. Depending on your operating system, you can download one that is compatible from the [Official Python website](https://www.python.org/downloads/) 
### Installation
To install this application, one is required to clone this repo by running the following command on your terminal:
```bash 
git clone https://github.com/evanskiprotich/point-of-sale-terminal.git
```
Then enter the folder of the application by running:
```bash 
cd point-of-sale-terminal
```
Start the program by running the following command:
```bash 
python main.py
```

Author
---
This project was developed by : [Evans Kiprotich]
