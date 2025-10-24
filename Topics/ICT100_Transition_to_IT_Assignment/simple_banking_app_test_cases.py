def main():
    """Main function to run the banking application.
    """
    # Print welcome message
    print("\nWelcome to the Simple Banking App")
    print("----------------------------------")
    
    # Print menu and get user choice
    menu_choice = menu()
    
    # If menu_choice == 6, print exit message; else print "Feature coming soon"
    if menu_choice == 1: # Create Savings Account
        print("\nFeature coming soon: Create Savings Account")

    elif menu_choice == 2: # View Bank Account
        print("\nFeature coming soon: View Bank Account")
        
    elif menu_choice == 3: # Create Credit Account
        print("\nFeature coming soon: Credit Account")
        
    elif menu_choice == 4: # Make Deposit
        print("\nFeature coming soon: Make Deposit")

    elif menu_choice == 5: # Make withdrawal
        print("\nFeature coming soon: Make Withdrawal")

    elif menu_choice == 6: # Exit
        print("Are you sure you want to exit? (Y/N): ")

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

main()