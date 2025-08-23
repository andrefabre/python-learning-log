# String Methods

# # join()
# print(', '.join(["cats", "rats", "bats"]))
# # cats, rats, bats
# print(" ".join(["My", "name", "is", "Simon"]))
# # My name is Simon
# print("ABC".join(["My", "name", "is", "Simon"]))
# # MyABCnameABCisABCSimon

# # partition() method

# myString = "Hello world"
# print(myString.partition("w"))
# # ('Hello ', 'w', 'orld')

# # multiple assignment to variables
# myString2 = "Hello world! each my dust"
# before, sep, after = myString2.partition(" ")
# print(before)
# print(sep)
# print(after)
# """
# ('Hello ', 'w', 'orld')
# Hello

# world! each my dust
# """

# ljust() and rjust() methods

def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))
        
picnicItems = {"Sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

"""
---PICNIC ITEMS--
Sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
Sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
"""