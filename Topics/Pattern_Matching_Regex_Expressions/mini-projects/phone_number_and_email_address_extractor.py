"""
1. Get the text off the clipboard
2. Find all the phone numbers and email addresses in the text.
3. Paste them onto the clipboard

The code will need to do the following
1.  User the pyperclip module to copy and paste strings
2.  Create two regexes, one for matching phone numbers and the other for
    matching email addresses
3.  Find all the matches, not just the first match of both regexes
4.  Neatly format the matching strings into a single string to paste
5.  Display some kind of message if no matches were found in the text.
"""

# Step 1. Create a Regex for Phone Numbers

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # a separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)""", re.VERBOSE)

# TODO: Create email regex
emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+       #username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)""", re.VERBOSE)

# TODO: Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[6] != "":
        phoneNum += " x" + groups[6]
        matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")