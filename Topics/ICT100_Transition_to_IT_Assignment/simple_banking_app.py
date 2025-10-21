"""
# Purpose: ICT100 Transition to IT Assignment 2 - Simple Banking App
# Author/s: Andre Fabre
NOTE # Copyright: 10 October 2025

Problem Description:

Develop a simple banking application, the application will allow users to simulate opening a bank account and performing various basic banking operations, as well as the bank performing automated tasks

Constraints:
- A text-based (aka console) application
- No graphical user interface (GUI)
- No desktop application
- No web application
- No mobile application
- There is only one account existing at any time and when the application ends, the bank account will disappear, nothing is saved.

Functions:
    - menu(): Displays the menu and gets user menu choice
    - savings_account(): Prompts user to enter an initial deposit amount to open a savings account
    - view_bank_account(): Displays the current balance and account details
    - credit_account(): User can create a credit account and spend more money than they have.
    - make_deposit(): User can make a deposit to their account
    - make_withdrawal(): User can make a withdrawal from their account

"""

def main():
    """Main function to run the banking application.
    """
    
    # Constants
    SAVINGS_ACCT_INTEREST_RATE = 0.02  # 2% annual interest rate
    CREDIT_ACCT_INTEREST_RATE = 0.15   # 15% annual interest rate
    MONTHLY_FEE = 5.00                  # $5 monthly fee for savings accounts
    MONTHLY_OVERCHARGE_FEE = 10.00        # $10 monthly fee for credit accounts
    
    # Variables
    savings_account_balance = 0.0
    credit_account_balance = 10_000.0
    account_type = "" # "Savings" or "Credit"

    print("\nWelcome to the Simple Banking App")
    print("----------------------------------")
    
    # Print menu and get user choice
    menu_choice = menu()
    
    while menu_choice in [1, 2, 3, 4, 5, 6]:
    # If menu_choice == 6, print exit message; else print "Feature coming soon"
        if menu_choice == 1:
            
            print("\nFeature coming soon: Create Savings Account")
            if account_type == "":
                account_name = savings_account()
                account_type = "Savings"
                print(f"Savings account created for {account_name.title()}.")
            elif account_type == "Credit":
                print("You already have a Credit Account. Cannot create Savings Account.")
            else:
                print("You already have a Savings Account.")
                
        elif menu_choice == 2:
            
            print("\nFeature coming soon: View Bank Account")
            if account_name:
                if account_type == "Savings":
                    view_bank_account(account_name, account_type, savings_account_balance)
                else:
                    view_bank_account(account_name, account_type, credit_account_balance)
            else:
                print("No account exists. Please create an account first.")
                continue
                
        elif menu_choice == 3:
            
            print("\nFeature coming soon: Credit Account")
            if account_type == "":
                account_name = credit_account()
                account_type = "Credit"
                print(f"Credit account created for {account_name}.")
            elif account_type == "Savings":
                print("You already have a Savings Account. Cannot create Credit Account.")
            else:
                print("You already have a Credit Account.")
                
        elif menu_choice == 4:
            
            print("\nFeature coming soon: Make Deposit")
            if account_type:
                if account_type == "Savings":
                    savings_account_balance = make_deposit(account_name, account_type, savings_account_balance)
                    print(f"Deposit successful! New balance: ${savings_account_balance:.2f}")
                else:
                    credit_account_balance = make_deposit(account_name, account_type, credit_account_balance)
                    print(f"Deposit successful! New balance: ${credit_account_balance:.2f}")
            else:
                print("No account exists. Please create an account first.")
                continue
            
        elif menu_choice == 5:
            print("\nFeature coming soon: Make Withdrawal")
            if account_type:
                if account_type == "Savings":
                    make_withdrawal(account_name, account_type, savings_account_balance)
                else:
                    make_withdrawal(account_name, account_type, credit_account_balance)
            else:
                print("No account exists. Please create an account first.")
                continue
            
        elif menu_choice == 6:
            confirm_exit = input("\nAre you sure you want to exit? (Y/N): ").lower()
            if confirm_exit == "y":
                break
            else:
                print("Returning to main menu...")
        
        # Print menu and get user choice again
        menu_choice = menu()

    print("Thank you for using the Simple Banking App. Goodbye!")
    
def menu():
    """Prints menu to the console, prompts user for a menu choice, and returns the choice.
    
    Returns:
        menu_choice (int): The user's menu choice.
    """
    # Print menu
    print("""
----- Main Menu -----
1. Create Savings Account
2. View Bank Account
3. Credit Account
4. Make Deposit
5. Make Withdrawal 
6. Exit
""")
    
    # Get user menu choice
    menu_choice = int(input("Please enter your choice (1-6): "))
    return menu_choice



def savings_account():
    """_summary_
    
    Args:
    
    Returns:
        account_name (str): The name of the account holder.
    """
    account_name = input("Enter account holder's name: ")
    while True:
        if len(account_name) < 5:
            print("Account name must be at least 5 characters long. Please try again.")
            account_name = input("Enter account holder's name: ")
        else:
            break
    return account_name

def credit_account():
    """_summary_
    
    Args:

    Returns:
        account_name (str): The name of the account holder.
    """
    
    account_name = input("Enter account holder's name: ")
    while True:
        if len(account_name) < 5:
            print("Account name must be at least 5 characters long. Please try again.")
            account_name = input("Enter account holder's name: ")
        else:
            break

    return account_name

def view_bank_account(account_name, account_type, account_balance):
    """_summary_
    
    Args:
    
    Returns
    """
    # Constants
    SAVINGS_ACCT_INTEREST_RATE = 0.02  # 2% annual interest rate
    CREDIT_ACCT_INTEREST_RATE = 0.15   # 15% annual interest rate
    MONTHLY_FEE = 5.00                  # $5 monthly fee for savings accounts
    MONTHLY_OVERCHARGE_FEE = 10.00        # $10 monthly fee for credit accounts

    print(f"Account Name: {account_name}")
    print(f"Account Type: {account_type}")
    print(f"Account Balance: ${account_balance:.2f}")

    if account_type == "Savings":
        print(f"Interest Rate: {SAVINGS_ACCT_INTEREST_RATE * 100}%")
        print(f"Monthly Fee: ${MONTHLY_FEE}")
    elif account_type == "Credit":
        print(f"Interest Rate: {CREDIT_ACCT_INTEREST_RATE * 100}%")
        print(f"Monthly Overcharge Fee: ${MONTHLY_OVERCHARGE_FEE}")

def make_deposit(account_name, account_type, account_balance):
    """_summary_
    
    Args:
    
    Returns
    """
    
    print(f"\nMaking a deposit to {account_type} account for {account_name}.")
    
    # Get deposit amount from user and validate input
    while True:
        try:
            deposit_amount = float(input("Enter deposit amount: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
    
    # Update account balance and print to console
    account_balance += deposit_amount
    return account_balance


def make_withdrawal(account_name, account_type, account_balance):
    """_summary_

    Args:

    Returns
    """
    print(f"\nMaking a withdrawal from {account_type} account for {account_name}.")

    # Get withdrawal amount from user and validate input
    while True:
        try:
            withdrawal_amount = float(input("Enter withdrawal amount: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

    if account_type == "Savings":
        while True:
            if withdrawal_amount > account_balance:
                print("Insufficient funds. Please enter a lower amount.")
                print("You can only withdraw up to your current balance.")
                print(f"Your current balance is: ${account_balance:.2f}")
                continue
            else:
                account_balance -= withdrawal_amount
                print(f"Withdrawal successful! New balance: ${account_balance:.2f}")
                return account_balance
    elif account_type == "Credit":
        # Allow overdraft for credit account with a limit of $5000
        overdraft_limit = 5000.0
        while True:
            if withdrawal_amount > (account_balance + overdraft_limit):
                print("Withdrawal exceeds overdraft limit. Please enter a lower amount.")
                print(f"You can withdraw up to: ${account_balance + overdraft_limit:.2f}")
                continue
            else:
                break
        
        # Update account balance and print to console
        account_balance -= withdrawal_amount
        return account_balance


main()