import os 
from os import system 
import operations as ops

system('cls')

operationList = ["Read", "Insert", "DeleteOrder", "UpdateCustomer", "UpdateOrder"]
counter = 1

print("These are the operations that you can perform in our database: ")
for operation in operationList:
    print(f'{counter}. {operation}')
    counter += 1
choice = int(input("Select one above [1-5] >> "))

if choice == 1:
    ops.readCustomerOperation()
elif choice == 2:
    ops.insertOperation()
elif choice == 3:
    ops.deleteOperation()
elif choice == 4:
    ops.updateCOperation()
elif choice == 5:
    ops.updateOOperation()

    

print()