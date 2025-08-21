import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # phoneNumRegex variable contains a Regex object
mo = phoneNumRegex.search("My number is 415-555-4242.")
print(f"Phone number found: {mo.group()}")