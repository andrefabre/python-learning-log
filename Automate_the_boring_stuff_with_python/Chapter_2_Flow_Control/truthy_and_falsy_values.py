name = ""
while not name:
    print("Enter your name: ")
    name = input()
print("How many guests will you have: ?")
numOfGuests = int(input())
if numOfGuests:
    print("Be sure to have enough room for all your guests")
print("Done")

print("My name is: ")
for i in range(5):
    print("Jimmy 5 times (" + str(i) + ")")