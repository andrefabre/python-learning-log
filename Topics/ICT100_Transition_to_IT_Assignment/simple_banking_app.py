"""
# Purpose: ICT100 Transition to IT Assignment 2 - Simple Banking App
# Author/s: Andre Fabre
# Copyright: 25 October 2025

Problem Description:

Develop a simple banking application, the application will allow users to simulate opening a bank account and performing various basic banking operations, as well as the bank performing automated tasks

Constraints:
- A text-based (aka console) application
- No graphical user interface (GUI)
- No desktop application
- No web application
- No mobile application

Banking Domain Rules
- A customer can only have one account, and it can be a Savings Account or a Credit Account, 
and the account has a name (set by the customer) and interest rates (set by the bank).
- Savings Account: Monthly Interest Added, Monthly Bank Fee, and Balance must be greater than zero
- Credit Account: Balance can be negative up to a Credit Limit, Monthly Charge on Overdue Payment, and No Interest.

Functions:
    - menu(): Displays the menu and gets user menu choice
    - create_account(): Prompts user to create an account
    - view_bank_account(): Displays the current balance and account details
    - make_deposit(): User can make a deposit to their account
    - make_withdrawal(): User can make a withdrawal from their account

"""

def main():
    """Main function to run the banking application.
    """
    
    # Initialise Variables
    account_balance = 0.0 # General account balance
    account_type = "" # "Savings" or "Credit"
    account_name = "" # Name of account holder

    print("\nWelcome to the Simple Banking App")
    print("----------------------------------")
    
    # Print menu and get user choice
    menu_choice = menu()
    
    while menu_choice in [1, 2, 3, 4, 5, 6]:
    # If menu_choice == 6, print exit message; else print "Feature coming soon"
        if menu_choice == 1: # Create Savings Account
            
            print("\nFeature coming soon: Create Savings Account")
            if account_type == "":
                account_name = create_account()
                account_type = "Savings"
                print(f"\nCongratulations {account_name.title()}, your new {account_type} has been created.")
            else:
                if account_type == "Savings":
                    print("You already have a Savings Account.")
                else:
                    print("You already have a Credit Account. Cannot create Savings Account")

            # Print account details
            print(f"\nAccount Name: {account_name}")
            print(f"Account Type: {account_type}")
            print(f"Account Balance: ${account_balance:.2f}")
            print(f"To make a deposit select option 4, to make a withdrawal, please select option 5 from the main menu.")
                
        elif menu_choice == 2: # View Bank Account
            
            print("\nFeature coming soon: View Bank Account")
            if account_type == "Savings" or account_type == "Credit":
                account_balance = view_bank_account(account_name, account_type, account_balance)
            else:
                print("No account exists. Please create an account first.")
                continue
            
        elif menu_choice == 3: # Create Credit Account
            
            print("\nFeature coming soon: Credit Account")
            if account_type == "":
                account_name = create_account()
                account_type = "Credit"
                print(f"Credit account created for {account_name}.")
                print(f"Initial Credit Limit: $5000.00")
            else:
                if account_type == "Savings":
                    print("You already have a Savings Account. Cannot create Credit Account.")
                else:
                    print("You already have a Credit Account.")

            # Print Account Details
            print(f"\nAccount Name: {account_name}")
            print(f"Account Type: {account_type}")
            print(f"Account Balance: ${account_balance:.2f}")
            print(f"To make a deposit select option 4, to make a withdrawal, please select option 5 from the main menu.")
            
        elif menu_choice == 4: # Make Deposit
            
            print("\nFeature coming soon: Make Deposit")
            if account_type == "Savings" or account_type == "Credit":
                account_balance = make_deposit(account_name, account_type, account_balance)
                print(f"Deposit successful! New balance: ${account_balance:.2f}")
            else:
                print("No account exists. Please create an account first.")
                continue
            
        elif menu_choice == 5: # Make withdrawal
            print("\nFeature coming soon: Make Withdrawal")
            if account_type == "Savings" or account_type == "Credit":
                account_balance = make_withdrawal(account_name, account_type, account_balance)
                print(f"Withdrawal successful! New balance: ${account_balance:.2f}")
            else:
                print("No account exists. Please create an account first.")
                continue
            
        elif menu_choice == 6: # Exit
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
3. Create Credit Account
4. Make Deposit
5. Make Withdrawal 
6. Exit
""")
    
    # Get user menu choice
    
    
    # Validate user menu choice
    while True:
        try:
            menu_choice = int(input("Please enter your choice (1-6): "))
            if menu_choice < 1 or menu_choice > 6:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please try again.")
    
    return menu_choice

def create_account():
    """Creates a bank account by prompting the user for an account name.
    
    Returns:
        account_name (str): The name of the account holder.
    """
    
    # Get account name from user and validate input, account name must be at least 5 characters long
    account_name = input("Enter account holder's name: ")
    
    while True:
        if len(account_name) < 5:
            print("Account name must be at least 5 characters long. Please try again.")
            account_name = input("Enter account holder's name: ")
        else:
            break
        
    return account_name

def view_bank_account(account_name, account_type, account_balance):
    """Takes account details as parameters, applies banking fees, and prints them to the console.
    
    Args:
        account_name (str): The name of the account holder.
        account_type (str): The type of the account ("Savings" or "Credit").
        account_balance (float): The current balance of the account.

    Returns:
        end_of_month (float): The updated account balance after applying fees and interest.
    """
    # Constants
    SAVINGS_ACCT_INTEREST_RATE = 0.02  # 2% annual interest rate
    CREDIT_ACCT_INTEREST_RATE = 0.0   # 0% annual interest rate
    MONTHLY_FEE = 5.00                  # $5 monthly fee for savings accounts
    MONTHLY_OVERCHARGE_FEE = 10.00        # $10 monthly fee for credit accounts

    is_overdue = False  # Placeholder for overdue status
    
    # Calculate charges and fees for Savings account and print details
    if account_type == "Savings":
        monthly_interest = account_balance * (SAVINGS_ACCT_INTEREST_RATE / 12)
        end_of_month_balance = account_balance + monthly_interest - MONTHLY_FEE
    
        print(f"""
------------- Bank Details -------------

Account Name: {account_name}
Account Type: {account_type}

Starting Balance:       ${account_balance:.2f}
Interest Rate:          {SAVINGS_ACCT_INTEREST_RATE * 100}%
Monthly Interest:       ${monthly_interest:.2f}
Monthly Fee:            ${MONTHLY_FEE:.2f}
----------------------------------------
Balance after fees and interest: ${end_of_month_balance:.2f}

Account Balance: ${end_of_month_balance:.2f}
----------------------------------------""")

   
    # Calculate charges and fees for Credit account and print details
    if account_type == "Credit":
        monthly_interest = account_balance * (CREDIT_ACCT_INTEREST_RATE / 12)
        if is_overdue:
            over_charge_fee = MONTHLY_OVERCHARGE_FEE
            end_of_month_balance = account_balance - over_charge_fee
        else:
            over_charge_fee = 0.0
            end_of_month_balance = account_balance
        
        
        print(f"""
------------- Bank Details -------------

Account Name: {account_name}
Account Type: {account_type}

Starting Balance:       ${account_balance:.2f}
Interest Rate:          {CREDIT_ACCT_INTEREST_RATE * 100}%
Monthly Interest:       ${monthly_interest:.2f}
Monthly Overcharge Fee: ${over_charge_fee:.2f}
----------------------------------------
Balance after fees and interest: ${end_of_month_balance:.2f}

Account Balance: ${end_of_month_balance:.2f}
----------------------------------------""")
        
    return end_of_month_balance

def make_deposit(account_name, account_type, account_balance):
    """Creates a deposit to the specified account.
    
    Args:
        account_name (str): The name of the account holder.
        account_type (str): The type of the account ("Savings" or "Credit").
        account_balance (float): The current balance of the account.

    Returns:
        account_balance (float): The updated account balance after the deposit.
    """
    
    # Print deposit message
    print(f"\nMaking a deposit to {account_type} account for {account_name}.")
    
    # Get deposit amount from user and validate input
    while True:
        try:
            deposit_amount = float(input("Enter deposit amount: $"))
            if deposit_amount <= 0:
                print("Deposit amount must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
    
    # Update account balance
    account_balance += deposit_amount
    return account_balance


def make_withdrawal(account_name, account_type, account_balance):
    """Creates a withdrawal from the specified account.

    Args:
        account_name (str): The name of the account holder.
        account_type (str): The type of the account ("Savings" or "Credit").
        account_balance (float): The current balance of the account.

    Returns:
        float: The updated account balance after the withdrawal.
    """
    
    # Print withdrawal message
    print(f"\nMaking a withdrawal from {account_type} account for {account_name}.")

    # Get withdrawal amount from user and validate input
    while True:
        try:
            withdrawal_amount = float(input("Enter withdrawal amount: $"))
            
            if account_type == "Savings":
                if withdrawal_amount > account_balance:
                    print("Insufficient funds. Please enter a lower amount.")
                    print("You can only withdraw up to your current balance.")
                    print(f"Your current balance is: ${account_balance:.2f}")
                    continue
                else:
                    break
            elif account_type == "Credit":
                # Allow overdraft for credit account with a limit of $5000
                overdraft_limit = 5000.0
                if withdrawal_amount > (account_balance + overdraft_limit):
                    print("Withdrawal exceeds overdraft limit. Please enter a lower amount.")
                    print(f"You can withdraw up to: ${account_balance + overdraft_limit:.2f}")
                    continue
                else:
                    break
                
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

    # Calculate new account balance
    account_balance -= withdrawal_amount
    return account_balance

main()