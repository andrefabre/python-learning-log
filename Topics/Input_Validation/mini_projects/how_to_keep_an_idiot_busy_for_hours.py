"""
1.  Ask the user if they'd like to know how to keep an idiot busy for hours
2.  If the user answers no, quit
3.  If the user answers yes, go to step 1
"""

import pyinputplus as pyip

while True:
    prompt =  "Want to know how to keep an idiot busy for hours?\n"
    response = pyip.inputYesNo(prompt) # won't return until user enters valid answer; yes, no
    if response == "no":
        break

print("Thank you. Have a nice day")