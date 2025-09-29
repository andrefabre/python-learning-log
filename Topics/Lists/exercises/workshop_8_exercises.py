# Write a program that converts a sentence into snake_case

my_sentence = input("Enter your sentence: ").replace(" ", "_").lower()
print(my_sentence)


# Write a function that takes a full name as input and returns the initials of the person in uppercase
def get_initials(full_name):
    """ Takes a full name as input and returns the initials of the person in uppercase """
    fullname = full_name.upper().split()
    initials = ""
    for i in range(len(fullname)):
        initials += fullname[i][0] + "."
    return initials

full_name = input("Enter the full name: ")
print("Initials: ", get_initials(full_name))

# Wrtite a python program that takes a string as input and returns a new string made up of the first two and last two characters of the original string. If the string length is less than 2, return an empty string.

new_string = "Hi" #input("Enter a string: ")
if len(new_string) < 2:
    print("")
else:
    new_string = new_string[:2] + new_string[-2:]
    print(new_string)
    
# Write a program to validate a password based on the following criteria:
# At least 8 characters long
# Contains at least one uppercase letter
# Contains at least one one digit
# Contains at least one special character

password = "Password@123"

count_upper = 0
count_digit = 0
count_special = 0

for char in password:
    if char.isupper():
        count_upper += 1
    elif char.isdigit():
        count_digit += 1
    elif not char.isalnum():
        count_special += 1

if len(password) >= 8 and count_upper > 0 and count_digit > 0 and count_special > 0:
    print("Valid password")
else:
    print("Invalid password")
    
