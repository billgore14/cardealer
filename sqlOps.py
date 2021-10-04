import connection as c
import mysql.connector


def readCustomerInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Customer')
        for column in cursor:
            print(f'''
            id .............. {column[0]}
            First Name ...... {column[1]}
            Last Name ....... {column[2]}
            Email............ {column[3]}
            Phone ........... {column[4]}
            ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)

def readOrderInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM car_order')
        for column in cursor:
            print(f'''
            Order id......... {column[0]}
            Customer id...... {column[1]}
            Product id....... {column[2]}
            Total............ {column[3]}
            ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)
    

def insertCustomerInfo(fName, lName, email, phone):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO customer (customer_fName, customer_lName, customer_email, customer_phone) VALUES ('{fName}', '{lName}', '{email}' , '{phone}')")
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)

def deleteOrder(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM car_order WHERE orderID = {id}')
        conn.commit()
        readOrderInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)

def updateCustomer(id, fname, lname, age, phone):
    conn = c.returnConnection()
    
