import os
import sqlite3
import sys
sys.path.append('bangazon')
from CustomerManagement import *
from ProductManagement import *

active_customer = 1


class Bangazon():

    def build_menu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print('*********************************************************')
        print('**  Welcome to Bangazon! Command Line Ordering System  **')
        print('*********************************************************\n')     
        print("1. Create Customer Account")
        print("2. Choose Active Customer")
        print("3. Create a Payment Option")
        print("4. Add Product to Shopping Cart")
        print("5. Complete an Order")
        print("6. See Product Popularity")

    
    def main_menu(self):

        self.build_menu()
        choice = input(">> ")

        if choice == "1":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            phone_number = input("Phone Number: ")

            save_customer_to_database(first_name, last_name, address, phone_number)
        



        # if choice == "2":





        if choice == "3":
            payment_type = input("What is your payment type? ")
            account_number = input("What is your account number? ")

            save_payment_option_to_database(payment_type, account_number, active_customer)    



        if choice == "4":
            """
            Arguments: None
            Author: Dean Smith
            """
            product_list = get_all_products()
            for i, product in enumerate(product_list):
                print(i, product[0])
            input("")



        if choice == "5":




            selected_payment = input("Choose your payment type")

            select_payment_option(selected_payment)    





if __name__ == "__main__":
  bangazon = Bangazon()
  bangazon.main_menu()