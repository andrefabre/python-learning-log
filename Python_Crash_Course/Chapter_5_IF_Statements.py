#-------------------------------------------------------------------------------
#   Chapter 5: IF Statements
#-------------------------------------------------------------------------------

# Conditional Tests: every if statement is an expression that can be evaluated
# as True or False and is called a conditional test.
# If a conditional test evaluates to True, python executes the code following
# the if statement.
# If the test evaluates to False, python ignores the code following the if
# statement

# Checking for Equality
# The simplest conditional est checks whether the value of a variable is equal
# to the value of interest. x == y
# Testing for equality is case sensitive in python.

# Checking for Inequality
# When you want to determine whether two values are not equal, you can use the
# inequality operator '!='

# Using and to check Multiple Conditions
# To check whether two conditions are both True simultaneously, use the 
# keyword 'and' to combine the two conditional tests. If each test passes, the
# overall expression evaluates to True. If either test fails or both tests fail
# the expression evaluates to False.

# Using or to check Multiple Conditions
# Using the keyword 'or' allows you to check multiple conditions as well, but
# it passes when either or both of the individual tests pass. An or expression
# fails on when both individual tests fail

# Checking Whether a Value Is in a List
# To find out whether a particular value is already on a list, use the 
# keyword 'in'.

# Checking Whether a Value Is Not in a List
# To find out whether a particular value is not in a list, use the keyword
# 'not'

# Boolean Expressions
# A Boolean value is either True or False. Boolean values are often used to 
# keep track of certain conditions e.g. game_active = True

# if Statements
# Simple if statements have one test and one action

# if-else Statements:
# Take action when a condition passes and a different action in all other cases

# if-elif-else
# Tests more than two possible situations.
# Each conditional test is run in order until one passes

# Using multiple elif Blocks
# You can use as many elif blocks as you like

# Tesing Multiple Conditions
# The if-elif-else chain is powerful. But it is only appropriate to use when
# you just need one test to pass.

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
#   Create a variable called alien_color and assign it a value of 'green",
#   "yellow" or "red".
#-------------------------------------------------------------------------------

# alien_color = "green"

# If statement to tesst whether the aliens color is greem. If it is, print a 
# message that the player just earned 5 points

# if alien_color == 'green':
#     print("Congratulations, you have earned 5 points")
    
# Write one version that passes the if test and another that fails

# if alien_color == 'blue':
#     print("Congratulations, you have earned 5 points")

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   5-4. Choose a color for an alien as you did in 5.3, and write an if-else
#   chain.
#-------------------------------------------------------------------------------

# if the aliens color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# if the alien's color isn't green, print a statement that the player just
# earned 10 points. Write one version of the program that runs the if block
# and another that runs the else block

# alien_color = "green"
# alien_color = "blue"
# points = 0

# if alien_color == "green":
#     points = 5
# else:
#     points = 10
# print(f"Congratulations, you have earned {points} points")

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   5-5. Turn you if-else chain from Ex 5.4 into an if/elif/else chain.
#   If the alien is green, print a message that the player earned 5 points
#   If the alien is yellow, print a message that the player earned 10 points.
#   If the alien is red, print a message that the player earned 15 points.
#   Write three versions of this program, making sure each message is printed
#   for the appropriate color alien.
#-------------------------------------------------------------------------------

# alien_color = "green"
# alien_color = "yellow"
# alien_color = "red"
# alien_color = "blue"
# points = 0

# if alien_color == "green":
#     points = 5
# elif alien_color == "yellow":
#     points = 10
# elif alien_color == "red":
#     points = 15
    
# if points > 0:
#     print(f"Congratulations, you have earned {points} points")
    
#-------------------------------------------------------------------------------
#   Try it Yourself:
#   5-6. Stages of Life: Write an if-elif-else chain that determines a person's
#   stage of life. Set a value for the variable age, and then:
#-------------------------------------------------------------------------------

# age = 65
# value = "elder" #returned if age is >= 65

# If the person is less than 2 years old, print a message that the person is a
# a baby.
# If the person is at least 2 years old but less than 4, print a message
# that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that
# person is a kid.
# If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

# if age < 2:
#     value = "baby"
# elif age < 4:
#     value = "toddler"
# elif age < 13:
#     value = "kid"
# elif age < 20:
#     value = "teenager"
# elif age < 65:
#     value = "adult"

# message = f"You are a {value}"
# print(message)

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   5-8. Hello Admin: Make a list of five or more usernames, including the name
#   'admin'. Imagine you are writing code that will print a greeting to each
#   user after they log in to a website. Loop through the list, and print a
#   greeting to each user
#-------------------------------------------------------------------------------

#if the username is 'admin', print a special greeting, such as Hello admin,
# would you like a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

#usernames = ["admin", "John", "Steve", "Peter", "Juicy"]
#usernames = []

# Add an if to check the list is not empty. Below are two different versions
# that do the check is the list is not empty

# if usernames == []:
#     print("We need some users")
# else:
#     for name in usernames:
#         if name != "admin":
#             print(f"Hello {name}, thankyou for logging in again")
#         else:
#             print("Hello admin, would you like to see a status report?")
        
# if usernames:
#     for name in usernames:
#         if name != "admin":
#             print(f"Hello {name}, thankyou for logging in again")
#         else:
#             print("Hello admin, would you like to see a status report?")
# else:
#     print("We need some users")

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   5-10. Checking Usernames: Do the following to create a program that
#   simulates how websites ensure that everyone has a unique username
#------------------------------------------------------------------------------

# Make a list of 5 or more usernames called current_users:
current_users = ["PixelDrift92",
    "EchoFalconX",
    "QuantumMango",
    "FrostByteCraze",
    "SilentNova7",
    "ShadowPineX",
    "CrimsonYak",
    "GlitchHunter88",
    "NebulaNomad",
    "HexaSparkle",
    "TurboKoala",
    "WiredWaffle9"]

# Make another list of 5 usernames called new_users. Make sure one or two of
# the new usernames are also in the current_users list
new_users = ["CyberTofu42",
    "BlizzardBeetle",
    "ShadowPineX",
    "VortexLlama",
    "HexaSparkle",
    "hexasparkle"]

# Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying that
# the username is available.

# make sure comparision is case insensitive i.e. if John has been used, JOHN
# should not be accepted

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
    
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username {user} is unavailable")
    else:
        print(f"Congratulations {user}, the username you have chosen is available")

