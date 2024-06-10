import csv 
import pandas as pd
def verify_user(ic_number, password):
    # Verification for user ic number
    if len(ic_number) != 12 or not ic_number.isdigit():
        return False
    if password != ic_number[-4:]:
        return False
    return True

def calculate_tax(income, tax_relief):
    # Simplified tax calculation based on Malaysian tax rates
    taxable_income = max(0, income - tax_relief)
    tax_payable = 0
    if taxable_income <= 5000:
        tax_payable = taxable_income * 0
    elif taxable_income <= 20000:
        tax_payable = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax_payable = 150 + (taxable_income - 20000) * 0.03
    elif taxable_income <= 50000:
        tax_payable = 450 + (taxable_income - 35000) * 0.06
    elif taxable_income <= 70000:
        tax_payable = 1350 + (taxable_income - 50000) * 0.11
    elif taxable_income <= 100000:
        tax_payable = 3350 + (taxable_income - 70000) * 0.19
    elif taxable_income <= 250000:
        tax_payable = 9350 + (taxable_income - 100000) * 0.25
    elif taxable_income <= 400000:
        tax_payable = 53500 + (taxable_income - 250000) * 0.26
    else:
        tax_payable = 115500 + (taxable_income - 400000) * 0.28
    return tax_payable

def save_to_csv(user_data, filename_users, tax_data, filename_tax):
    # Save user data to two file 
    try:
        with open(filename_users, 'r') as file:
            if file.readline() == '':  # If the file is empty, write the header row
                with open(filename_users, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['id', 'ic_number', 'password'])
        with open(filename_users, 'a', newline='') as file:
            writer = csv.writer(file)
            for id, user_info in user_data.items():
                writer.writerow([id, user_info['ic_number'], user_info['password']])
    except FileNotFoundError: # If the file does not exist, a new file will be created with header row
        with open(filename_users, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'ic_number', 'password'])
            for id, user_info in user_data.items():
                writer.writerow([id, user_info['ic_number'], user_info['password']])

    try:
        with open(filename_tax, 'r') as file:
            if file.readline() == '':  # If the file is empty, write the header row
                with open(filename_tax, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['ic_number', 'income', 'tax_relief', 'tax_payable'])
        with open(filename_tax, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tax_data)
    except FileNotFoundError: # If the file does not exist, a new file will be created with header row
        with open(filename_tax, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ic_number', 'income', 'tax_relief', 'tax_payable'])
            writer.writerows(tax_data)

def read_from_csv(filename): # read data from csv file
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return None