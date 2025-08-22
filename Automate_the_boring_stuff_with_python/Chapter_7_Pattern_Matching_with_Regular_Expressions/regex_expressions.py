import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # phoneNumRegex variable contains a Regex object
# mo = phoneNumRegex.search("My number is 415-555-4242.")
# print(f"Phone number found: {mo.group()}")

# Grouping with Parentheses
# Say you want to separate the area code from the rest of the phone number.
# Adding parentheses will create groups in the regex 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242.")
mo.group(1) # 415
mo.group(2) # 555
mo.group(3) # 4242 
mo.group() # 415-555-4242

# if you want to retrieve all the groups at once, user the groups() method
# note the plural form of the name

mo.groups() # ('415', '555', '4242')
num1, num2, num3 = mo.groups()
print(num1, num2, num3) 

phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search("My number is (415)-555-4242.")
mo.group(1) #'(415)'
mo.group(2) # '555'

# Matching multiple groups with the Pipe
# The | character is called a pipe. You can use it anywhere you want to match
# one of many expressions

heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
mo1.group() # Batman #NOTE: if both terms are in the search string it will return the first one. You can find all matching occurrences with the findall() method
count = 0
while count != 1:
    try:
        playerChoice = input("Choose rock, paper, scissors").lower()
        throwRegex = re.compile(f"rock|paper|scissors")
        moT = throwRegex.search(playerChoice)
        throw = moT.group()
        print(throw)
        count += 1
    except: 
        print("Invalid Input")
        
# You can also use the pipe method to match one of several patterns as part of your
# regex

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
mo.group() #"Batmobile"
mo.group(1) # "mobile"

count = 0
while count != 1:
    try:
        playerChoice = "rock1"
        throwRegex = re.compile(f"rock(1|2|3)")
        moT = throwRegex.search(playerChoice)
        throw = moT.group(1)
        print(throw)
        count += 1
    except: 
        print("Invalid Input")
        
# Optional matching with a Question Mark
# Somtimes there is a pattern that you only want to match only optionally.
# That is the, the regex shoould find a mtch regardless of whether that bit of
# text is there.
# The ? character flags the group that precedes it as an optional part of the
# pattern

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search("The Adventures of Batman")
mo1.group() # "Batman"

mo2 = batRegex.search("The Adventures of Batwoman")
mo2.group() # Batwoman

# Match Zero or More with the Star
# The * (called the star or asterix) means "match zero or more"
# the group before the star can occur any number of times in the text. It can
# be completely absent or repeated over and over again.

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman")
mo1.group() # "Batman"

mo2 = batRegex.search("The Adventures of Batwoman")
mo2.group() # "Batwoman"

mo3 = batRegex.search("The Adventures of Batwowowowowoman")
mo3.group() # 'Batwowowowowoman'

# Matching 1 or more with the Plus
# The '+' means match zero or more
# The group preceding a plus must appear at least once

batRegex = re.compile(r"Bat(wo)+man")
mo1 = batRegex.search("The Adventures of Batwoman")
mo1.group() # "Batwoman"

mo2 = batRegex.search("The Adventures of Batwowowowoman")
mo2.group() # 'Batwowowowoman'

mo3 = batRegex.search("The Adventures of Batman")
mo3 == None # True

# Matching specific Repetitions with Braces
# If you have a group that you want to repeat a specific number of times, follow
# the group in your regex with a number in braces.
# For example, the regex (Ha){3} will match the string "HaHaHa" but it will not
# match "HaHa"
# Instead of one number, you can specify a range by writing a minimum, a comma,
# and a maximum in between braces
# Ha{3, 5} will match "Hahaha", "HaHaHaHa" and "HaHaHaHaHa"

# Greedy and Non-greedy Matching
# Python's regular expressions are greedy by default, which means that in
# ambiguous situations they will match the longest string possible

greedyHaRegex = re.compile(r"Ha){3, 5}")
mo1 = greedyHaRegex.search("HaHaHaHaHa")
mo1.group() # "HaHaHaHaHa"

nongreedyHaRegex = re.compile(r"Ha){3, 5}?")
mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
mo2.group() # "HaHaHa"

# NOTE: The ? can have two meanings in regular expressions: declaring a non-greedy
# match or flagging an optional group. These meanings are entirely unrelated

# The Findall() method
# The findall() method will return thea list of strings of every match in the searched
# string - as long as there are no groups in the regular expression

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # has no groups
phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000") # ['415-555-9999', '212-555-0000']

# if there ARE groups in the regular expression, then findall() will return a list
# of tuples. Each tuple represents a found match, and its items are matched strings
# for each group in the regex

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)") # has groups
phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000") # [('415', '555', '9999'), ('212', '555', '0000')]