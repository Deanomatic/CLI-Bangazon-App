import sys
import sqlite3

def get_product(product_name, price):
	return 3

def add_product_to_order(active_customer, product_id):
	return 1

def get_all_products():
    with sqlite3.connect('bangazon2.db') as conn:
    	c = conn.cursor()
    	product_list = c.execute("select title from Product")
    return product_list

def complete_order(payment_id, active_order):
	return 7

def save_product_to_database(product_name, price):
    pass
  
def get_active_order(active_customer):
	return 1

def select_payment_option(selected_payment):

    # return 1

	with sqlite3.connect('bangazon.db') as connection:
		c = connection.cursor()

		c.execute("insert into Order values(?, ?, ?, ?)",
				(None, payment_type, account_number, active_customer))

		connection.commit()
