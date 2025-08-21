"""
    Write a function that takes a list value as an argument and returns a string
    with all the items separated by a comma and a space, with 'and' inserted
    before the last item
"""

def commaCode(param1):
    
    if len(param1) == 0:
        return "List is empty"
    elif len(param1) == 1:
        return param1[0]
    elif len(param1) == 2:
        return f"{param1[0]} and {param1[1]}"
    else:
        myString = ""
        for index, item in enumerate(param1):
            if index in range(len(param1)-2):
                myString = myString + item + ", "
        return f"{myString}{param1[-2]} and {param1[-1]}"
            
    
myList = ["apples", "bananas", "tofu", "cats", "cheese", "dogs"]
runList = commaCode(myList)
print(runList)
print(type(runList))
print(commaCode([]))
print(commaCode(["boot", "strap", "boxing"]))
# if index in range(len(param1)-1):
#             print(f"{item},")
#         ela00