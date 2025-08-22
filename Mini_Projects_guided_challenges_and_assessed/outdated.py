"""
In a file called outdated.py, implement a program that prompts the user for a date,
anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below:

Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


"""

monthList = [
   ("January", "01"),
   ( "February", "02"),
    ("March", "03"),
    ("April", "04"),
    ("May","05"),
    ("June", "06"),
    ("July", "07"),
    ("August", "08"),
    ("September", "09"),
    ("October", "10"),
    ("November", "11"),
    ("December","12")
]

def main():
    # Get and validate user input
    formatDate = userInput()
 
def userInput():
    #formatted like 9/8/1636
    while True:
        try:
            dateEntered = input("Date: ")
        except EOFError:
            break
            # "9/10/0"  #"September 8, 1636"
        # check for "/"
        if "/" in dateEntered:
            dateEntered = dateEntered.strip() # strip input()
            monthShort, dayShort, yearShort = dateEntered.split("/") # unpack into variables and cast to int
            if yearShort.isdigit() and monthShort.isdigit() and dayShort.isdigit(): # variable of type(str) only contains digits
                pass
            else:
                continue
            
            monthShort, dayShort, yearShort = (map(int, [monthShort, dayShort, yearShort])) # cast variables to type int
            if yearShort <= 0 or not 1 <= monthShort <= 12 or not 1 <= dayShort <= 31:
                continue
            else:
                pass

            if monthShort < 10 and dayShort < 10:
                finalDate = f"{yearShort}-0{monthShort}-0{dayShort}"
            elif monthShort < 10:
                finalDate = f"{yearShort}-0{monthShort}-{dayShort}"
            elif dayShort < 10:
                finalDate = f"{yearShort}-{monthShort}-0{dayShort}"
            print(finalDate)
            break
        elif "," in dateEntered:
            
            dateEntered = dateEntered.replace(","," ")
            monthLong, dayLong, yearLong = dateEntered.split()
            monthLong = monthLong.rstrip() # remove all trailing white space
            dayLong = dayLong.strip()
            yearLong = yearLong.lstrip()
            
            if yearLong.isdigit() and monthLong.isalpha() and dayLong.isdigit():
                pass
            else:
                continue
            
            yearLong, dayLong = map(int, [yearLong, dayLong])
            #dayLong = int(dayLong)
            monthLong = monthLong.title()
            if yearLong <= 0:
                continue
            
            month_map = dict(monthList)
            if monthLong in month_map and 1 <= dayLong <= 31: # check if month is in month list;
                monthNum = month_map[monthLong]
            else:
                continue

            if dayLong < 10:
                print(f"{yearLong}-{monthNum}-0{dayLong}")
                break
            else:
                print(f"{yearLong}-{monthNum}-{dayLong}") 
                break          

        else:
            continue
    
main()