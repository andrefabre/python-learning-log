"""
 implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""
# Create empty dict to store grocery list; key: item, value: total number of items
groceries = {}

while True:

    # Validate Input
    try:
        item = input()
        if item == "":
            raise ValueError
        # if "," in item:
        #     item = item.split(",", 1)
    except EOFError:
        break
    except ValueError:
        continue
    
    item = item.strip().upper() # strip whitespace and convert to uppercase
    # Add item to groceries dict
    groceries.setdefault(item, 0) # check if item in dict, if false add it with value of 0,
    groceries[item] = groceries[item] + 1 # get item and add one 
    # print(groceries)

# Sort Grocery List
myGroceryList = [[k, v] for k, v in groceries.items()] # list comprehesion, create list of tuples(key, value) 
myGroceryList.sort() # sort list

# Display Grocery List
for grocery in range(len(myGroceryList)):
    print(f"{myGroceryList[grocery][1]} {myGroceryList[grocery][0]}")


# #print(myGroceryList)
# for k, v in groceries.items():
#     print(f"{v} {k}")

 
# myDict = {'bananaa': 1, 'applie': 1, 'cheese': 3}


