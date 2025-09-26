"""
1. Gets a street address from the command line arguments or clipboard
2. Opens the webbrowser to the Google Maps page for the address
2a. Read the command line arguments from sys.argv
2b. Read the clipboard contents
2c. Call the webbrowser.open() function to open the web browser
"""

#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)


