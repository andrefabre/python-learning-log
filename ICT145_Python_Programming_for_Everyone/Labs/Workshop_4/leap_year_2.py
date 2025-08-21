"""
A year is a leap year if:
    It is divisible by 4, and not divisible by 100, or
    It is divisible by 400
Write a program that allows the user to input a starting year and an ending year.
Determine how many leap years exist between them and display those leap years also.
If the end year entered by the user is smaller than the start year, print a message,
The start year should be less than the end year, and the program should end.
"""

year = 1600
startDate = 2010
endDate = 2020
i = endDate - startDate
countYears = 0

# range (1, i)
# startDate = startDate + 1

if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
    print(f"{year}, is a leap year")
else:
    print(f"{year}, is not a leap year")
    
# if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
#     print(f"{year}, is a leap year")
# else:
#     print(f"{year}, is not a leap year")