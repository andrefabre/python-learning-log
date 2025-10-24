def main():
    """Main function to run the banking application.
    """
    # Print welcome message
    print("\nWelcome to the Simple Banking App")
    print("----------------------------------")
    
    # Print menu
    print("""
----- Main Menu -----
1. Peform a task
2. Exit
---------------------
""")
    
    # Validate user choice
    while True:
        try:
            choice = int(input("Please enter your choice (1-2): "))
            if choice < 1 or choice > 2:
                print("Invalid choice. Please enter a number between 1 and 2.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please try again.")
    
    
    # If choice == 6, print exit message; else print "Feature coming soon"
    if choice == 1: 
        print("\nFeature coming soon: Create Savings Account")

    else : # Exit
        print("\nExiting application ")

    # Print exit message
    print("Thank you for using the Simple Banking App. Goodbye!")

main()