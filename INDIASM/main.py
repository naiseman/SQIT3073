import csv
import pandas as pd
from functions import verify_user, calculate_tax, save_to_csv, read_from_csv

# Initialize user data dictionary
user_data = {}

# Main menu from the start
def main():
    print("Welcome to the Malaysian Tax Input Program!")
    while True:
        print("Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ") # Prompt message ffor user to enter their choice
        if choice == "1":
            register_user() # go to registration part
        elif choice == "2":
            if is_registered(): # check whether got data in users.csv
                login_user() # go to login part
            else:
                print("You don't have an account yet. Please register first.") # prompt invalid message if the users.csv is empty
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.") # prompt invalid message if the choice is other than 1-3

def is_registered(): 
    try:
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row:  # Check if row is not empty
                    if row[0] in user_data:
                        return True
        return False
    except FileNotFoundError: # file does not exist
        return False

def register_user(): # registration part
    print("Register a new user")
    id = input("Enter your ID: ")
    ic_number = input("Enter your IC number: ")
    password = input("Enter the last 4 digits of your IC number: ")
    if verify_user(ic_number, password): # verify user ic number
        if is_id_used(id) and is_ic_number_used(ic_number): # verify id and ic is it been used
            print("ID or IC number already in use. Please try again.")
        else:
            user_data[id] = {'ic_number': ic_number, 'password': password} # save user data to users.csv
            save_to_csv(user_data, 'users.csv', [], 'tax_data.csv')
            print("Registration successful!") 
    else:
        print("Invalid IC number or password. Please try again.") # back to enter id message

def is_id_used(id): # check id is it been used
    try:
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row and len(row) > 0:  # Check if row is not empty and has at least one element
                    if row[0] == id:
                        return True
        return False
    except FileNotFoundError:
        return False

def is_ic_number_used(ic_number): # check ic number is it been used
    try:
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row and len(row) > 1:  # Check if row is not empty and has at least two elements
                    if row[1] == ic_number:
                        return True
        return False
    except FileNotFoundError: # if file does not exist
        return False

def login_user(): # login part 
    print("Login to the system")
    while True: # while loop for login validation
        id = input("Enter your ID: ")
        password = input("Enter the last 4 digits of your IC number: ")
        if id in user_data and verify_user(user_data[id]['ic_number'], password):
            print("Login successful!")
            break
        else:
            print("Invalid ID or password. Please try again.") 
    income = float(input("Enter your annual income: ")) # tax calculation part
    tax_relief = float(input("Enter your tax relief amount: "))
    tax_payable = calculate_tax(income, tax_relief)
    print(f"Your tax payable is: RM {tax_payable:.2f}") # prompt user tax payable after the calculation 
    save_tax_data(user_data[id]['ic_number'], income, tax_relief, tax_payable) # save data to tax_data.csv

def save_tax_data(ic_number, income, tax_relief, tax_payable): # save tax data function
    data = [[ic_number, income, tax_relief, tax_payable]]
    save_to_csv({}, 'users.csv', data, 'tax_data.csv')

# Run main() when script is executed directly
if __name__ == "__main__": 
    main()