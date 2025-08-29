"""
Purpose: Workshop 5: Mini Project
Group Name: External Group 14
Author/s: Andre Fabre and Joshua Williams
Copyright: 9 August 2025

Vending: This project simulates a vending machine where users can purchase drinks
by inserting coins.
    Inputs:
        selection; int - selection option from menu 1-3

    Calculations:
        compute change owed and return change amount
        - amount_due = drink_price - amount_inserted
        
    Outputs:
        change_amount; int
"""

# Constants - Drinks
COCA_COLA = 3.35
SOLO = 2.50
FANTA = 2.65

# Error Message - invalid coin entered
message = """
------- Invalid coin inserted.--------
Coin Denominations accepted are:

5 cents, 10 cents, 20 cents, 50 cents,
1 dollar and 2 dollars
Please enter as a whole number.
For example, enter '5 cents' as 5.
--------------------------------------
"""

def vending_machine():
    """
    Main function that controls the full vending machine process
    """
    # Display menu.
    menu()
    
    # Select drink.
    while True:
       try:
            selection = int(input("Enter 1, 2, or 3 to select a drink: "))
            if 1 <= selection <= 3:
                break
            else:
                print("\nOops...Invalid option entered, please try again.")
                continue
       except ValueError:
            print("\nOops...Invalid option entered, please try again")
            continue
       
    # Get name and price of drink
    drink_name, drink_price = drink_input(selection)
    print(f"\nDrink Selected: {drink_name}\nAmount Due: AUD {drink_price:.2f}")

    # Convert price of drink to cents.
    drink_price = int(drink_price * 100)
    
    # Validate coin inserted and display change amount.
    while True:
        # Input and validate coin inserted
        try:
            amount_inserted = int(input("\nInsert Coin: "))
            
            if amount_inserted in [1, 2, 5, 10, 20, 50]: # Validate coin denomination
                if 1 <= amount_inserted <= 2: # convert 1 and 2 dollar denominations to cents
                    amount_inserted = int(amount_inserted * 100) 
                else:
                    pass
            else:
                print(message)
                print(f"Amount Due: AUD {drink_price/100:.2f}")
                continue
        except ValueError: 
            print(message)
            print(f"Amount Due: AUD {drink_price/100:.2f}")
            continue
            
        # Get and display amount due or change owed
        change_amount = calculate_change(amount_inserted, drink_price)
        
        if change_amount > 0:
            print(f"Amount Due: AUD {change_amount / 100:.2f}")
            drink_price = change_amount
            continue
        elif change_amount < 0:
            if -95 <= change_amount <= -5: 
                print(f"Change owed: AUD {abs(change_amount / 100):.2f} ({abs(change_amount)} cents)")
            else:
                print(f"Change owed: AUD {abs(change_amount / 100):.2f}")
            break
        else:
            print(f"Change owed: AUD 0.00")
            break

def menu():
    """Display drink menu with three drink options in dollars and cents
    """
    print(f"""
Select your Drink:

Option  Drink        Price
  1     Coca-Cola    AUD {COCA_COLA:.2f}
  2     Solo         AUD {SOLO:.2f}
  3     Fanta        AUD {FANTA:.2f}
""")

def drink_input(drink_choice):
    """
    Takes the input of choice of drink and returns its name and price
    
    Args:
        int: drink_choice, 1="Coca-Cola", 2="Solo", 3="Fanta"
        
    Returns:
        tuple: (drink_name, drink_price)
    """
    if drink_choice == 1: return ("Coca-Cola", COCA_COLA)
    elif drink_choice == 2: return ("Solo", SOLO)
    else: return ("Fanta", FANTA)

def calculate_change(amount_inserted, drink_price):
    """
    Computes the change owed and returns the change amount
    
    Args:
        int: amount_inserted - coin value in cents
        int: drink_price - price of drink in cents
    
    Returns:
        int: change_amount - change owed
    """
    change_amount = drink_price - amount_inserted
    return change_amount

## Call vending_machine function
vending_machine()
