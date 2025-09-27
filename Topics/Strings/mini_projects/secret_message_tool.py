"""
Create a Python-based Secret Message Tool that allows users to encode, decode, reverse
and mask the messages.

Requirements:

You must build a console-based menu-driven program as shown in sample output offering
the following features. The menu should be displayed repeatedly until the user exits
the menu. Create functions for each feature and menu.
"""

# Constants
BLUE_TEXT_START, RED_TEXT_START, GREEN_TEXT_START, END_TEXT_COLOR, = "\033[34m", "\033[31m", "\033[32m", "\033[0m" # ANSI Codes for text Formatting

def main():

    # Variables
    secret_key, message, shift_value, encoded_message = "", "", "", ""

    while True:

        # Display Menu
        menu_choice = int(user_interface())
        if menu_choice == 5: # If menu choice option == 5 Exit the program
            print("\nThanks for using Secret Message Tool")
            break
        else:
            match (menu_choice):
                case 1: # Encode a message - Get secretkey, message, shift value; return encoded message
                    secret_key = get_secret_key()
                    message = get_message()
                    shift_value = int(get_shift_value())
                    encoded_message = encode_message(message, shift_value)
                    print(f"\n{GREEN_TEXT_START}Encoded message:{END_TEXT_COLOR} {encoded_message}")
                    continue
                case 2: # Decode a message - if no coded message return to menu, else run decode_message function
                    if len(secret_key) == 0: # Check encoded message exists
                        print("\nYou need to encode a message first\nSelect option 1 from the menu")
                    else:
                        decoded_message = decode_message(encoded_message, shift_value, secret_key)
                        if decoded_message == "Access Denied":
                            print(f"\n{RED_TEXT_START}{decoded_message}{END_TEXT_COLOR}")
                        else:
                            print(f"\n{GREEN_TEXT_START}Decoded message:{END_TEXT_COLOR} {decoded_message}")
                    continue
                case 3: # Reverse a message - Get new message to be reversed or reverse existing encoded message
                    # Choose message option: 1. New Message, 2. Encoded Message
                    msg_option = int(input("\nTo reverse an Encoded Message enter 1.\nTo reverse a New Message enter 2.\n\nEnter your choice (1-2): "))
                    while not 1 <= msg_option <= 2: # Validate user input
                        print(f"{RED_TEXT_START}Invalid entry{END_TEXT_COLOR}")
                        msg_option = int(input("\nEnter your choice (1-2): "))

                    # Reverse Message
                    if msg_option == 1: # Check if Encoded Message exists; if False, prompt user to create New Message to reverse
                        if len(encoded_message) != 0:
                            print(f"\n{GREEN_TEXT_START}Reversed message:{END_TEXT_COLOR} {reverse_message(encoded_message)}")
                        else:
                            print(f"\n{RED_TEXT_START}No encoded message found{END_TEXT_COLOR}")
                            message = get_message()
                            print(f"\n{GREEN_TEXT_START}Reversed message:{END_TEXT_COLOR} {reverse_message(message)}")  
                    else:
                        message = get_message()
                        print(f"\n{GREEN_TEXT_START}Reversed message:{END_TEXT_COLOR} {reverse_message(message)}")  
                    continue
                case 4: # Mask a message - Get New Message, replace all chars except " " with "*"
                    message = get_message()
                    print(f"\n{GREEN_TEXT_START}Masked message:{END_TEXT_COLOR} {mask_message(message)}")

def user_interface():
    """ Display Secret Tool Menu """
    
    print(f"""
{BLUE_TEXT_START}--- Secret Message Tool{END_TEXT_COLOR} ---

1. Encode a message
2. Decode a message
3. Reverse a message
4. Mask a message
5. Exit

{BLUE_TEXT_START}---------------------------{END_TEXT_COLOR} """)
    
    # Enter choice
    while True:
        choice = input("\nEnter your choice (1-5): ")
        # Validate input, isdigit() and in range 1-5
        if choice.isdigit() and 1 <= int(choice) <= 5:
            break
        else:
            print(f"{RED_TEXT_START}Invalid entry{END_TEXT_COLOR}")
    return choice
    
def get_secret_key():
    """ Get secret key from input(); returns str: 
    
    Returns:
        secret_key(str): user created secret_key """
    
    secret_key = input("Set a secret key: ")
    while len(secret_key) == 0:
        print(f"{RED_TEXT_START}Secret Key cannot be empty{END_TEXT_COLOR}")
        secret_key = input("Set a secret key: ")
    return secret_key

def get_message():
    """ Get message from input(); returns str: message """
    
    message = input("Enter the message to encode: ")
    while len(message) == 0:
        print(f"{RED_TEXT_START}Message cannot be empty{END_TEXT_COLOR}")
        message = input("Enter the message to encode: ")
    return message

def get_shift_value():
    """ Get shift_value from input(): returns str: shift_value """
    
    shift_value = input("Enter a shift value: ")
    while not shift_value.isdigit() and int(shift_value) <= 0:
        print(f"{RED_TEXT_START}Invalid entry, please enter a positive integer greater than 0{END_TEXT_COLOR}")
        shift_value = input("Enter a shift value: ")
    return shift_value

def encode_message(message, shift_value):
    """ Encode Message using the message and shift_value

    Args:
        message(str): The message to encode
        shift_value(int): The shift value used to encode message
    
    Returns:
        coded_message(str): The encoded message
    """
    coded_message = ""
    for _ in message:
        if 97 <= ord(_) <= 120:# ord "x" == 120 ord "a" == 97
            coded_message += chr((ord(_) - ord('a') + shift_value) % 26 + ord('a'))
        elif 65 <= ord(_) <= 88: # ord "X" == 88 ord "A" == 65
            coded_message += chr((ord(_) - ord("A") + shift_value) % 26 + ord("A"))
        elif 48 <= ord(_) <= 57: # ord "0" == 48 ord ("9") == 57 
            coded_message += chr((ord(_) - ord('0') + shift_value) % 10 + ord('0'))
        else:
            coded_message += _
    return coded_message

def decode_message(message, shift_value, secret_key):
    """
    Decode the encoded message using the shift value and secret key
    1. Reverse the encoding process using the shift value from get_shift_value()
    2. Ensure the message returns to its original form
    3. User is prompted to enter the correct secret key to decode the message
    
    Args:
        message (str): The encoded message to decode
        shift_value (int): The shift value used during encoding
        secret_key (str): The secret key set by the user
    """
    # Validate the secret key
    access_key = input("Enter your secret key: ")
    if len(secret_key) != len(access_key):
        return "Access Denied"
    else:
        for i in range(len(secret_key)):
            if access_key[i] != secret_key[i]:
                return "Access Denied"
    
    # Decode the message
    decoded_message = ""
    for _ in message:
        if 97 <= ord(_) <= 120:# ord "x" == 120 ord "a" == 97
            decoded_message += chr((ord(_) - ord('a') - shift_value) % 26 + ord('a'))
        elif 65 <= ord(_) <= 88: # ord "X" == 88 ord "A" == 65
            decoded_message += chr((ord(_) - ord("A") - shift_value) % 26 + ord("A"))
        elif 48 <= ord(_) <= 57: # ord "0" == 48 ord ("9") == 57 
            decoded_message += chr((ord(_) - ord('0') - shift_value) % 10 + ord('0'))
        else:
            decoded_message += _

    return decoded_message


def reverse_message(message=""):
 # reverse the entire string
 # can be used on raw or encoded messages
    if len(message) == 0:
        message = input("Enter your message: ")
    return message[::-1]



def mask_message(message):
# Replace all characters in the message with asterisks * except spaces
    masked_message = ""
    for _ in message:
        if _ == " ":
            masked_message += _
        else:
            masked_message += "*"
    return masked_message
    
    
main()