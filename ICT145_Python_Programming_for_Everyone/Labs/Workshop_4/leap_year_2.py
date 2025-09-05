"""
A year is a leap year if:
    It is divisible by 4, and not divisible by 100, or
    It is divisible by 400
Write a program that allows the user to input a starting year and an ending year.
Determine how many leap years exist between them and display those leap years also.
If the end year entered by the user is smaller than the start year, print a message,
The start year should be less than the end year, and the program should end.
"""

while True:
    startYear = int(input("Enter the start year: "))
    endYear = int(input("Enter the end year: "))
    if startYear < endYear:break
    else:
        print("\nThe start year should be less than the end year\n")

print(f"The leap years between {startYear} and {endYear} are: ")

countYears = 0
for year in range(startYear, endYear+1):
    if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
        print(year)
        countYears += 1

print(f"Total number leap years: {countYears}")
