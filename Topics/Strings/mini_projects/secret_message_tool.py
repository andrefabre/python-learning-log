"""
Create a Python-based Secret Message Tool that allows users to encode, decode, reverse
and mask the messages.

Requirements:

You must build a console-based menu-driven program as shown in sample output offering
the following features. The menu should be displayed repeatedly until the user exits
the menu. Create functions for each feature and menu.
"""

def main():
    
    secret_key = ""
    message = ""
    shift_value = ""
    encoded_message = ""
    
    while True:
        
        menu_choice = int(user_interface())
        if menu_choice == 5:
            print("Thanks for using Secret Message Tool")
            break
            # sys.exit()
        else:
            match (menu_choice):
                case 1: # Encode a message
                    secret_key = get_keyword()
                    message = get_message()
                    shift_value = int(get_shift_value())
                    encoded_message = encode_message(message, shift_value)
                    print(f"\nEncoded message: {encoded_message}")
                    continue
                case 2: # Decode a message
                    if len(secret_key) == 0:
                        print("\nYou need to encode a message first\nSelect option 1 from the menu")
                    else:
                        print("\nDecoded message:", decode_message(encoded_message, shift_value, secret_key))
                    continue
                case 3: # Reverse a message
                    msg_option = int(input("\nTo reverse an Encoded Message enter 1.\nTo reverse a New Message enter 2\n\nEnter your choice (1-2): "))
                    while 1 <= msg_option <= 2 is False:
                        print("Invalid entry")
                        msg_option = int(input("\nEnter your choice (1-2): "))
                        
                    if msg_option == 1:
                        if len(encoded_message) != 0:
                            print("\nReversed message:", reverse_message(encoded_message))
                        else:
                            print("\nNo encoded message found")
                            message = input("\nEnter your new message: ")
                            print("Reversed message:", reverse_message(message))  
                    else:
                        message = input("\nEnter your message: ")
                        print("Reversed message:", reverse_message(message))  
                    continue
                case 4: # Mask a message
                    message = get_message()
                    print("Masked message:", mask_message(message))

    
    
def user_interface():
    print("""
--- Secret Message Tool ---
1. Encode a message
2. Decode a message
3. Reverse a message
4. Mask a message
5. Exit
---------------------------
""")
    
    # Enter choice
    while True:
        choice = input("Enter your choice (1-5): ")
        # Validate input, isdigit and in range 1-5
        if choice.isdigit() and 1 <= int(choice) <= 5:
            break
        else:
            print("Invalid entry")
    return choice
    
def get_keyword():
    keyword = input("Set a secret keyword: ")
    while len(keyword) == 0:
        print("Keyword cannot be empty")
        keyword = input("Set a secret keyword: ")
    return keyword

def get_message():
    message = input("Enter the message to encode: ")
    while len(message) == 0:
        print("Message cannot be empty")
        message = input("Enter the message to encode: ")
    return message

def get_shift_value():
    shift_value = input("Enter a shift value: ")
    while not shift_value.isdigit():
        print("Invalid entry, please enter a positive integer")
        shift_value = input("Enter a shift value: ")
    return shift_value

def encode_message(message, shift_value):
    """
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
    3. User is prompted to enter the correct secret unlock keyword
    
    Args:
        message (str): The encoded message to decode
        shift_value (int): The shift value used during encoding
        secret_key (str): The secret keyword set by the user
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