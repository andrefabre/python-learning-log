"""
# Purpose: Workshop 2: Mini Project
# Group Name: External Group 14
# Author/s: Andre Fabre and Joshua Williams
# Copyright: 9 August 2025


Currency Converter: Takes currency amount as input and converts currency
for a defined set of currencies and exchange rates.
Displays converted currencies in table.
    Inputs:
        string; personName, name of user
        float; amount = amount of currency in AUD to be converted

    Calculations:
        amount in convertedCurrency = amountAUD * currency exchange rate
        
    Outputs:
        display list of currencies in table form.
"""

# 1.    Declare list of currencies as dict.
#       key: "exchange rate id", values: ("country name", exchange rate)
currencies = {"BDT": ("Bangladeshi Taka", 75.1),
              "CAD": ("Canadian Dollar", 0.89),
              "CNY": ("Chinese Yaun", 4.46),
              "EUR": ("Euro", 0.60),
              "HKD": ("Hong Kong Dollar", 4.84),
              "INR": ("Indian Rupee", 54.44),
              "JPY": ("Japanese Yen", 95.83),
              "NZD": ("New Zealand Dollar", 1.10),
              "SGD": ("Singapore Dollar", 0.85),
              "USD": ("United States Dollar", 0.62)
             }

# 2.    Display welcome message
print("Welcome to Currency Converter!")

# 3.    Get persons name and print to screen
personName = input("Please enter your name: ").title()
print(f"\nHi {personName}!,\n")

# 4.    Get amount to be converted
amountAUD = 0
while (amountAUD <= 0):

    try:
        amountAUD = float(input("Please enter the amount (in AUD) you want to convert: "))
        if amountAUD <= 0:
            print(f"\nYou entered ${amountAUD:,.2f} AUD, amount must be greater than 0.\n")
            continue
    except ValueError:
        print(f"\nPlease enter a valid number.\n")
        continue

# 5.     Display table headings
    print(f"\nHey {personName}!,\n\nPlease see below the ${amountAUD:,.2f} AUD converted in different currencies!")
    print("\nCurrency\t\tExchange Rate\t\tAustralian Dollars\tAmount")
    print("\t\t\t\t\t\tto be converted\t\t(in given currency)\n")

# 6.    Calculate and display converted currencies.
    for key, values in currencies.items():
        convertedCurrency = amountAUD * values[1]
        # format number of tabs
        if key in ["CAD", "CNY", "INR", "JPY"]:
            tabs = "\t\t"
        elif key == "EUR":
            tabs = "\t\t\t"
        else:
            tabs = "\t"
        print(f"{values[0]}{tabs}1 AUD = {values[1]:.2f} {key}\t${amountAUD:,.2f} AUD\t\t{convertedCurrency:,.2f} {key}")    

print("\n")