

print("Cheese and Crackers")

monthList = [
   ("January", "01"),
   ( "February", "01"),
    ("March", "01"),
    ("April", "01"),
    ("May","01"),
    ("June", "01"),
    ("July", "01"),
    ("August", "01"),
    ("September", "01"),
    ("October", "01"),
    ("November", "01"),
    ("December","01")
]

month1 = "January"
for month, code in monthList:
    if month == month1:
        print(code)