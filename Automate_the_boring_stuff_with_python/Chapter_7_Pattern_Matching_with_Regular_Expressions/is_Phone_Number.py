"""
    American phone number is three numbers a hyphen, three numbers a hyphen and three numbers
    Create a function isPhoneNumber to check whether a string matches this pattern
"""

def isPhoneNumber(text):
    
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print("Is 415-555-4242 a phone number?")
# print(isPhoneNumber("415-555-4242"))
# print("Is moshi moshi a phone number?")
# print(isPhoneNumber("moshi moshi"))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f"Phone number found: {chunk}")
print("Done")