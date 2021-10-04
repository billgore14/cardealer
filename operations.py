import os
import sqlOps as sql
from os import system
from Customer import Customer

system('cls')

Customer = []

# read function
def readCustomerOperation():
    sql.readCustomerInfo()

# insert function
def insertOperation():
    numberOfEntries = int(input("Enter number of records >> "))
    for entry in range(numberOfEntries):
        print(f'--- Customer # {entry + 1} ---')
        Customer = Customer()
        fName = input("What is your first name? >> ")
        Customer.set_fName(fName)
        lName = input("What is your last name? >> ")
        Customer.set_lName(lName)
        email = input("What is your email? >> ")
        Customer.set_email(email)
        phone = input("What is your phone number? >> ")
        Customer.set_phone(phone)
        Customer.append(Customer)
    for Customer in Customer:
        sql.insertCustomerInfo(Customer.get_fName(), Customer.get_lName(), Customer.get_email(), Customer.get_phone())
    readCustomerOperation()


# delete function
def deleteOperation():
    sql.readOrderInfo()
    orderId = int(input("Which id do you want choose so that we can delete the order? >> "))
    sql.deleteOrder(orderId)


# update customer function
def updateCOperation():
    sql.readCustomerInfo()
    customerId = int(input("Which id do you want choose so that we can update the customer? >> "))
    sql.updateCustomer(customerId)

# update order function
def updateOOperation():
    sql.readcar_orderInfo()
    orderId = int(input("Which id do you want choose so that we can update the order? >> "))
    sql.updateOrder(orderId)
