"""
# Purpose: Workhop 11 - Mini Project - ATM Simulator
# Group Name: External Group - 14
# Author/s: Andre Fabre
# Copyright: 25 October 2025

Program Description:

The program will simulate and Automated Teller Machine (ATM) system with secure card login and basic banking functionalities. It will use Python's csv module to handle account storage and employ exception handling to manage valid inputs and data errors. Account information (card number, pin number and balance) will be stored in a flat file (accounts.csv), simulating a lightweight database.

Requirements:

- You must build a console-based menu-driven program offering the following features. 

Functions:
    - main_menu(): Displays the menu program and gets user menu choice
    - atm_menu(): Displays the ATM menu and gets user menu choice
    - load_records(): Loads account records from the CSV file
    - save_records(): Saves updated account records to the CSV file
    - authenticate_user(): Authenticates user credentials against loaded account records
    - check_balance(): Checks and displays the account balance
    - deposit_funds(): Deposits funds into the account
    - withdraw_funds(): Withdraws funds from the account
"""

from pathlib import Path
import os

def main():
    
    # Load accoount records from file
    accounts_records = load_records()
    
   # Display main menu and get user choice
    menu_choice = main_menu()
    
    # if user choice == 2, exit program
    
    while True:
        if menu_choice == 2:
            print("Thank you for using the ATM. Goodbye!")
            # Close the accounts_records file
            accounts_records.close()
            return
    # If user choice == 1, proceed to login and verify user credentials
        if authenticate_user(accounts_records) != None:
            card_number, pin = authenticate_user(accounts_records)
            break
        else:
            menu_choice = main_menu()
    
    # If login successful, display ATM menu repeatedly until user chooses to exit
    # Get atm_menu_choice from atm_menu function
    atm_menu_choice = atm_menu()

    while atm_menu_choice != 4:

        if atm_menu_choice == 1:
            check_balance(card_number, pin, accounts_records)
        elif atm_menu_choice == 2:
            new_deposit = deposit_funds(card_number, pin, accounts_records)
            update_accounts_records = save_records(card_number, pin, new_deposit, accounts_records)
        elif atm_menu_choice == 3:
            new_withdrawal = withdraw_funds(card_number, pin, accounts_records)
            update_accounts_records = save_records(card_number, pin, new_withdrawal, accounts_records)

        atm_menu_choice = atm_menu()

    print("Thank you for using the ATM. Goodbye!")
    
    #Close the accounts_records file
    accounts_records.close()
    
def main_menu():
    """ Displays the main program menu and gets user menu choice.
    Valid choice: int [1, 2]
    
    Returns:
        menu_choice (int): user menu choice
    """
    
    print("""
=== ATM Simulation ===

Main Menu
1. Login with Card
2. Exit""")
    
    # Get user choice for main menu
    while True:
        try:
            menu_choice = int(input("Please enter your choice (1-2): "))
            if menu_choice not in [1, 2]:
                print("Invalid option. Please choose 1 or 2.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    return int(menu_choice)
        
def atm_menu():
    """ Displays atm menu and gets user menu choice.
    Valid choice: int [1, 2, 3, 4]

    Returns:
        menu_choice (int): user menu choice
    """
    # Display a 4-option interactive menu
    print("""
Welcome, Card Ending in ****3456
1. Check Balance
2. Deposit
3. Withdraw
4. Exit""")
    
    while True:
        try:
            menu_choice = int(input("Please enter your choice (1-4): "))
            if menu_choice < 1 or menu_choice > 4:
                print("Invalid choice. Please enter 1 to 4.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    return menu_choice

def load_records():
    """ Loads account records from a file into a dictionary.
    Validates data integrity and handles file access errors.
    
    Returns:
        accounts_data (dict): Dictionary of account records
    """
    # Load account records from a file
    path = Path("accounts.csv")
    
    # if file is missing: raise IOError with message "Error accessing database. Please contact the administrator."
    if not os.path.exists():
        raise IOError("Error accessing database. Please contact the administrator.")
    
    
    contents = path.read_text().rstrip()
    lines = contents.splitlines()
    account_data = {}

    for line in lines:
        
        # Split each line by comma and strip whitespace, convert to list using list comprehension
        values = [item.strip() for item in line.split(",")]
        
        # Validate list thas exactly 3 items
        if len(values) != 3:
            print("Corrupted entry. Skipping....")
            continue
        
        # assign values to variables by unpacking the list
        card_number, pin, balance = values
        
        # check if balance can be converted to float, handle ValueError in except block with message: "Corrupted entry. Skipping...."
        
        try:
            balance = float(balance)
        except ValueError:
            print("Corrupted entry. Skipping....")
            continue

        
        account_data[card_number] = {
            "pin": pin,
            "balance": float(balance)
        }
        
    # Return the account data dictionary
    return account_data

def save_records(accounts_records):
    """ Write all the account data back to the accounts.csv file after a successful deposit or withdrawal
    
    Returns:
        None
    """
    # Write all the account data back to the accounts.csv file after a successful deposit or withdrawal
    for k, v in accounts_records.items():
        record_line = f"{k},{v['pin']},{v['balance']}\n"
        with open("accounts.csv", "w") as file:
            file.write(record_line)
    
    return None

def authenticate_user(accounts_records):
    """ Authentivate user by verfiying Card Number (16 digit) and PIN (4 digit)
    
    Returns:
        None
    """
    # Authentivate user by verfiying Card Number (16 digit) and PIN (4 digit)
    card_number = input("Please enter your 16-digit card number: ")
    pin = input("Please enter your 4-digit PIN: ")
    
    # Use assert statement to raise AssertionError is the card number is not all digits and 16 characters long with a message: "Invalid card number format."
    assert card_number.isdigit() and len(card_number) == 16, "Invalid card number format."
    
    # Use assert statement to raise AssertionError if the PIN is not all digits and 4 chracters long with a message: "Invalid card number or PIN"
    assert pin.isdigit() and len(pin) == 4, "Invalid card number or PIN."
    
    # Check whether the card exists and the PIN matches from the loaded data
    if card_number in accounts_records and accounts_records[card_number]['pin'] == pin:
        print("Login successful.")
        return (card_number, pin)
    else:
        print("Login failed. Exiting...")
    
    return None
    

def check_balance(card_number, accounts_records):
    """ Check the account balance for a given card number and PIN.
    
    Returns:
        None
    """
    # Check card_number and pin values in accounts_records dictionary
    if not (card_number in accounts_records and accounts_records[card_number]['pin'] == pin):
        raise ValueError("Account not found. Invalid card number or PIN.")
    
    # Display current account balance
    account_balance = accounts_records[card_number]['balance']
    print(f"Current balance: ${account_balance:.2f}")

def deposit_funds(card_number, pin, accounts_records):
    """ Deposit funds into the account.
    
    Returns:
        new_balance (float): updated account balance after deposit
    """
    # Prompt the user for a deposit amount
    while True:
        try:
            deposit_amount = float(input("Enter amount to deposit: $"))
            if deposit_amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            else: 
                break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Check card_number and pin values in accounts_records dictionary
    if not (card_number in accounts_records and accounts_records[card_number]['pin'] == pin):
        raise ValueError("Account not found. Invalid card number or PIN.")
    
    # Get existing balance and add deposit amount
    account_balance = accounts_records[card_number]['balance']
    new_balance = account_balance + deposit_amount
    accounts_records[card_number]['balance'] = new_balance

    # Print confirmation message with new balance to console
    print(f"Deposit successful. New balance: ${new_balance:.2f}")
    return new_balance


def withdraw_funds(card_number, pin, accounts_records):
    """ Withdraw funds from the account.
    
    Returns:
        new_balance (float): updated account balance after withdrawal
    """
    
    # Check card_number and pin values in accounts_records dictionary
    if not (card_number in accounts_records and accounts_records[card_number]['pin'] == pin):
        raise ValueError("Account not found. Invalid card number or PIN.")
    
    # Get existing balance
    account_balance = accounts_records[card_number]['balance']
    
    # Prompt the user for a withdrawal amount
    
    while True:
        try:
            withdrawal_amount = float(input("Enter amount to withdraw: $"))
            if withdrawal_amount > account_balance:
                raise ValueError("Insufficient balance.")
            elif withdrawal_amount <=0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    
    # Subtract withdrawal amount from existing balance
    accounts_records[card_number]['balance'] = account_balance - withdrawal_amount
    new_balance = accounts_records[card_number]['balance']
    
    return new_balance

main()