xCheck = "❌"

def collatz(number):
    if number == 1:
        return number
    elif number % 2 == 0:
        return number // 2
    return 3 * number + 1

# myNum = 0
    
# while True:
#     while not myNum:
#         try:
#             myNum = int(input("Enter a number: "))
#             if myNum <= 0:
#                 print("You must enter an integer value greater than 0")
#         except ValueError:
#             print("Value Error: You must enter an integer value greater than 0")
#     if myNum == 1:
#         print(myNum)
#         break
#     else:
#         print(myNum)
#         myNum = collatz(myNum)

## NOTE: Reminder Andre: The code below works because when you loop the collatz function, whatever
# positive integer value is passed into it, it will always end up with a base case value of 1.
# Also the value 0 in a boolean expression will return False. As myNum is initialised as 0, myNum = False.
# Therefore, 'while not myNum' on the first iteration == True, 
# Once a valid integer input is received, the next iteration returns 'not True' == False and exits the loop.
myNum = 0
while myNum != 1:
    while not myNum:
        try:
            myNum = int(input("Enter a number: "))
            if myNum <= 0:
                print("You must enter an integer value greater than 0")
            else:
                print(myNum)
        except ValueError:
            print(f"\033[91mValue Error:\033[0m You must enter an integer value greater than 0")
    
    myNum = collatz(myNum)
    print(myNum)