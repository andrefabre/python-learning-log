
#1. Complete the following code snippets

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even")
    
# age = int(input("Enter your age: "))
# day = input("Enter  day of the week: ")

# def get_ticket_price(age, day):
    
#     if age < 0 and day == "":
#         return "Invalid input"
    
#     if age >= 18:
#         if day == "saturday" or day == "sunday":
#             price = 12
#         else:
#             price = 10
#     else:
#         if day == "saturday" or day == "sunday":
#             price = 8
#         else:
#             price = 6
    
#     return f"Ticket price: ${price}"

# test_data = {
#     "unitTest1": (-1, ""),
#     "unitTest2": (0, "saturday"),
#     "unitTest3": (0, "sunday"),
#     "unitTest4": (5, ""),
#     "unitTest5": (5, "saturday"),
#     "unitTest6": (5, "sunday"),
#     "unitTest7": (18, ""),
#     "unitTest8": (18, "saturday"),
#     "unitTest9": (18, "sunday"),
#     "unitTest10": (20, ""),
#     "unitTest11": (20, "saturday"),
#     "unitTest12": (20, "sunday")
# }

# for k, v in test_data.items():
#     print(get_ticket_price(v[0], v[1]))

#2. Find and fix the errors in this code snippet (Complete)

# x = 5
# if x == 0:
#     print("x is zero")
# else:
#     print("x is a non-zero number")
    
#3 A year is a leap year if: 
#   It is divisible by 4, and not divisible by 100, or 
#   It is divisible by 400. 
# Write a program that allows the user to input a year.  
# Determine whether the year entered by the use is leap year or not.

# def is_leap_year(year):
#     """
#     Determine whether the year entered by the use is a leap year or not
    
#     input: int; year
#     """
#     print(f"Enter the year: {year}")
#     if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
#         return f"{year}, is a leap year"
    
#     return f"{year}, is not a leap year"

# years = [
#     1996, 1981, 2008, 1985, 1980, 1993, 2012, 1987, 1988, 1991,
#     2000, 1983, 2004, 1989, 2016, 1995, 1984, 1999, 1992, 1997
# ]

# for i in years:
#     print(f"{is_leap_year(i)}\n")
    
