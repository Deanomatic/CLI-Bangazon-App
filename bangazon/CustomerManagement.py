 # import sys
import sqlite3
 
global active_customer 
active_customer = None


def save_customer_to_database(first_name, last_name, address, phone_number):
        ''' Allows user to add a new Customer Account and information to the database
        '''
        with sqlite3.connect('bangazon2.db') as conn:
            c = conn.cursor()


        c.execute("insert into Customer values (?, ?, ?, ?, ?)",
                        (None, first_name, last_name, address, phone_number))

        conn.commit()

def get_customer(first_name, last_name, address, phone_number):
    return 1


def get_all_customers():
    with sqlite3.connect("bangazon2.db") as conn:
        c = conn.cursor()
        customer_list = c.execute("select * from Customer")
        customer_list = c.fetchall()
    return customer_list
        

def get_active_customer():

    return active_customer
 

def set_active_customer(customer_id):

    active_customer = customer_id


def save_payment_option_to_database(payment_type, account_number, active_customer):

    with sqlite3.connect('bangazon2.db') as conn:
        c = conn.cursor()

        c.execute("insert into Payment values(?, ?, ?, ?)",
                (None, payment_type, account_number, active_customer))

        conn.commit()


def get_payment_option(payment_type, account_number, active_customer):
    return 2