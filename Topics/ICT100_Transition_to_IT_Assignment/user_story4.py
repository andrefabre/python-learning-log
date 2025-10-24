def main():
    """Main function to run the banking application.
    """
    
    # Initialise Variables
    account_balance = 0.0 # General account balance
    account_type = "" # "Savings" or "Credit"
    account_name = "" # Name of account holder
    
    # Print welcome message
    print("\nWelcome to the Simple Banking App")
    print("----------------------------------")
    
    # Print menu and get user choice
    menu_choice = menu()
    
    while menu_choice in [1, 2, 3, 4, 5, 6]:
    # If menu_choice == 6, print exit message; else print "Feature coming soon"
        if menu_choice == 1: # Create Savings Account
            
            if account_type == "":
                account_name = create_account()
                account_type = "Savings"
                print(f"\nCongratulations {account_name.title()}, your new {account_type} has been created.")
            else:
                print("You already have a Savings Account.")
                
            # Print account details
            print(f"\nAccount Name: {account_name}")
            print(f"Account Type: {account_type}")
            print(f"Account Balance: ${account_balance:.2f}")
            print(f"To make a deposit select option 4, to make a withdrawal, please select option 5 from the main menu.")
            
        elif menu_choice == 2: # View Bank Account
            
            print("\nFeature coming soon: View Bank Account")
            
        elif menu_choice == 3: # Create Credit Account
            
            print("\nFeature coming soon: Credit Account")
            
        elif menu_choice == 4: # Make Deposit
            
            print("\nFeature coming soon: Make Deposit")

        elif menu_choice == 5: # Make withdrawal
            print("\nFeature coming soon: Make Withdrawal")
            
        elif menu_choice == 6: # Exit
            confirm_exit = input("\nAre you sure you want to exit? (Y/N): ").lower()
            if confirm_exit == "y":
                break
            else:
                print("Returning to main menu...")
        
        # Print menu and get user choice again
        menu_choice = menu()

    # Print exit message
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
main()