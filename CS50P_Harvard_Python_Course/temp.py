"""
In plates.py, implement a program that prompts the user for a vanity plate.
- output:
    Valid if meets all of the requirements
    Invalid if it does not.

- Assumptions
    Assume that any letters in the user’s input will be uppercase.
    Assume that s will be a str

- Specifications
    is_valid() returns True if input string meets all requirements and False if it does not.
    Assume that s will be a str.
    You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

- Requirements:
    - All vanity plates must start with at least two letters.
    - Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters. DONE
    - Numbers cannot be used in the middle of a plate; they must come at the end.
      For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    - The first number used cannot be a ‘0’. DONE
    - No periods, spaces, or punctuation marks are allowed.” DONE
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    a = onlyNumAndChar(s) # if only letters and numbers return true
    b = stringLength(s) # if 2 <= len(s) <== 6 return true
    c = firstCharNotZero(s) # if first char is not 0 return true
    #d = firstTwoCharNotNum(s) # if first two char are not numbers returns true
    e = middleCharNotChar(s) # if middle chars are not numbers returns true
    return a and b and c and e

def onlyNumAndChar(s):
    return s.isalnum()

def stringLength(s):
    """
    Takes a string 's', returns True if len(s) is between 2 and 6 char.
    Input: String
    Output: Bool
    """
    if 2 <= len(s) <= 6:
        countchar = 0
        for char in s:
            if char.isalpha():
                countchar += 1
        if countchar < 2:
            return False
        if s[2] == "0":
            return False
    else:
        return False
    return True #2 <= len(s) <= 6 and s[2] != "0"

def firstCharNotZero(s):
    """
    Takes a string 's', returns True if char[0] != 0.
    Input: String
    Output: Bool
    """
    return s[0] != "0"

# def firstTwoCharNotNum(s):
#     """
#     Takes a string 's', returns True if char[0] and char[1] != int.
#     Input: String
#     Output: Bool
#     """
#     if len(s) <= 2:
#         return False

#     for char in s[0:2]:
#         if char.isdecimal():
#             return False
#     return True

def middleCharNotChar(s):
    """
    Takes a string 's', and returns false if middle char/s are returns false if type int
    Input: String
    Output: Bool
    """
    if len(s) % 2 == 0: #checks if string is even num of chars
        newString = s[len(s) // 2 - 1:len(s) // 2 + 1] #s[len(s) // 2 - 1 : len(s) // 2 + 1] # get middle
        if newString[0].isdecimal() and newString[1].isdecimal():
            return False
    else: # string is odd num of chars
        newString = s[len(s) // 2 : len(s) // 2 + 1] # get middle chars in string
        if newString[0].isdecimal(): # checks if char is a decimal
                return False
    return True


main()
