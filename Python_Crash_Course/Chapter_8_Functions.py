#-------------------------------------------------------------------------------
#   Chapter 8: Functions
#-------------------------------------------------------------------------------

# Functions are named blocks of code designed to do one specific job.

# Defining a function

# def greet_user():
#     """ Display a simple greeting."""
#     print("Hello")

# greet_user()

# # Passing information into a function

# def greet_user(username): # username is the parameter
#     """Display a simple greeting

#     Args:
#         username (string): string to be displayed.
#     """
#     print(f"Hello, {username}")

# greet_user("Jelly Roll") # "Jelly Roll is the argument"

# # Arguments and parameters
# # Variable is an example of a parmeter - piece of information the
# # function needs to do its job
# # Argument - a piece of information that passed from a from a function 
# # call a function
# # In the above example the argument "Jelly Roll" was passed to the
# # function greet_user() and the the value was assigned to the
# # parameter 'username'.

# #-------------------------------------------------------------------------------
# #   Try it yourself:
# #   8.2: Favourite book: Write a function called favorite_book() that
# #   accepts one parameter, title. The function whouls print a message
# #   such as "One of my favourite books is Alice in Wonderland"
# #-------------------------------------------------------------------------------

# def favourite_book(title):
#     """Takes a title of a book as a string and prints to screen

#     Args:
#         title (string): title of the book
#     """
#     print(f"One of my favourite books is {title}")

# favourite_book("The cat sat on the mat")

# # Passing Arguments
# # You can pass arguments to functions in a number of ways:
# #   positional arguments - which need to be in the same order the 
# #                           parameters were written
# #   keyword arguments - where each argument consists of a variable name
# #                       and value; lists and dict's of values.

# # Positional Arguments

# def describe_pet(animal_type, pet_name):
#     """ Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet("dog", "Jesus")

# # Keyword arguments - a keyword argument is a name-value pair that you
# # pass to a function. The order of the keyword arguments does not matter

# def describe_pet(animal_type, pet_name):
#     """ Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet(animal_type="dog", pet_name="Jesus")
# describe_pet(pet_name="Junior", animal_type="bird")

# # Default Values - you can define a default value for each parameter.
# # When you use default values, any parameter with a default value needs
# # to be listed AFTER all the parameters that don't have default values.

# def describe_pet(pet_name, animal_type="dog"):
#     """ Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet("geordie")

# #-------------------------------------------------------------------------------
# #   Try it yourself:
# #   8.3: T Shirt: Write a function called make_shirt() that accepts a
# #   size and the text of a message that should be printed on the shirt.
# #   The function should print a sentence summarising the size of the
# #   shirt and the message printed on it.
# #-------------------------------------------------------------------------------

# def make_shirt(size, message):
#     """Takes the size of a t-shirt and prints a sentence summarising
#     the size of the shirt and the message printed on it.

#     Args:
#         size (string): Small, Medium, Large
#         message (string): The message to be printed
#     """
#     print(f"The size of your shirt is: {size}")
#     print(f"The message to be printed is: ")
#     print(f"{message}")

# make_shirt("Medium", "Once upon a time in a nursery rhyme")

# # Modify the make_shirt() function so that shirts are large by default
# # with a message that reads "I Love Python". Make a large shirt and a
# # medium shirt with a default message, and a shirt of any size with a
# # different message.

# def make_shirt(size, message="I Love Python"):
#     """Takes the size of a t-shirt and prints a sentence summarising
#     the size of the shirt and the message printed on it.

#     Args:
#         size (string): Small, Medium, Large
#         message (string): The message to be printed
#     """
#     print(f"The size of your shirt is: {size}")
#     print(f"The message to be printed is: ")
#     print(f"{message}")

# make_shirt("Medium")
# make_shirt("Large")
# make_shirt("Large", "This shirt is badass")

# #-------------------------------------------------------------------------------

# # Return Values - the value the function returns is called a return value
# # When you call a function that returns a value, you need to provide a
# # variable that the return value can be assigned to

# def get_formatted_name(first_name, last_name):
#     """ Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name("jimi", "hendrix")
# print(musician)

# # Making an argument optional - you can use default values to make an
# # argument optional

# def get_formatted_name(first_name, last_name, middle_name=""):
#     """ Return a full name, neatly formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician1 = get_formatted_name("jimi", "marshall", "hendrix")
# musician2 = get_formatted_name("pat", "benitar")
# print(musician1)
# print(musician2)

# # Returning a dictionary

# def build_person(first_name, last_name):
#     """ Return a dictionary of information about a person"""
#     person = {"first": first_name, "last": last_name}
#     return person

# print(build_person("John", "Smith"))
# new_person = build_person("Jessica", "Smith")
# print(new_person)

# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person"""
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person["age"] = age
#     return person

# print(build_person("Steve", "Prince"))
# print(build_person("Steve", "Prince", 43))

# Using Functions with a While Loop

# def get_formatted_name(first_name, last_name):
#     """Return a full name neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name

# while True:
#         print("\nPlease enter your name:")
#         print("Type 'q' at any time to quit")
    
#         first_name = input("First Name: ")
#         if first_name == "q":
#             break
    
#         last_name = input("Last Name: ")
#         if last_name == "q":
#             break
    
#         formatted_name = get_formatted_name(first_name, last_name)
#         print(f"Hello {formatted_name}")

#-------------------------------------------------------------------------------
#   Try it yourself:
#   8.6: City Names: Write a function called city_country() that takes
# in the name of a city and its country. The function should return a
# string formatted like this - "Santiago, Chile". Call your function with
# at least three city-country pairs, and print the values returned
#-------------------------------------------------------------------------------

# def city_country(city, country):
#     """Takes a city and country and returns a formatted string"""
    
#     formatted_name = f"{city}, {country}"
#     return formatted_name

# print(city_country("Perth", "Australia"))
# print(city_country("Sydney", "Australia"))
# print(city_country("Melbourne", "Australia"))

# 8.7 Album: Write a function called make_album that builds a dict
# describing a musical album. The function should take in an artist name
# and an album title, and it return a dict containing these two pieces
# of information. Use the function to make three dict's representing
# different albums. Print each return value to show that the dict's are
# storing the album information correctly

# def make_album(artist_name, album_title):
#     """Returns a dict containing artist name and album title"""
    
#     album = {"Artist Name": artist_name, "Album Title": album_title}
#     return album

# print(make_album("John Jones", "The road back home"))
# print(make_album("Trevor Noah", "Funny is just a concept"))
# print(make_album("Georgie", "No-one likes a winner"))

# User None to add an optional parameter to make_album() that allows
# you to store the number of songs on an album. If the calling line
# includes a value for the number of songs, add that value to the 
# albums dictionary. Make at least one new function call that includes
# the number of songs on an album

# def make_album(artist_name, album_title, songs_num=None):
#     """Returns a dict containing artist name, album title and number
#     of songs on album(optional)"""
    
#     if songs_num:
#         album = {"Artist Name": artist_name, 
#                  "Album Title": album_title,
#                  "Number of Songs": songs_num,
#                  },
#     else:
#         album = {"Artist Name": artist_name,
#                  "Album Title": album_title,
#                  }
#     return album

# print(make_album("John Jones", "The road back home"))
# print(make_album("Trevor Noah", "Funny is just a concept", 10))
# print(make_album("Georgie", "No-one likes a winner", 15))

# 8.8 User Albums: Start with your program from Ex 8.7. Write a while
# loop that allows users to enter an albums artist and title. Once you
# have that information, call make_album() with the users input and print
# the dictionary that's created. Be sure to include a q value in the loop.

# def make_album(artist_name, album_title, songs_num=None):
#     """Returns a dict containing artist name, album title and number
#     of songs on album(optional)"""
    
#     if songs_num:
#         album = {"Artist Name": artist_name, 
#                  "Album Title": album_title,
#                  "Number of Songs": songs_num,
#                  }
#     else:
#         album = {"Artist Name": artist_name,
#                  "Album Title": album_title,
#                  }
#     return album

# while True:
    
#     prompt = "\nTo create the album enter the artist name, album title "
#     prompt += "and number of songs (optional)."
#     prompt += "\nTo quit type 'q'"
#     print(prompt)
    
#     artist_name = input("\nArtist Name: ")
#     if artist_name == "q":
#         break
    
#     album_title = input("Album Title: ")
#     if album_title == "q":
#         break
    
#     songs_num = input("Number of songs: ")
#     if songs_num == "q":
#         break
    
#     album = make_album(artist_name, album_title, songs_num)
    
#     for key, value in album.items():
#         print(f"{key}: {value}")
    
   
# #-------------------------------------------------------------------------------

# # Passing a List

# def greet_users(names):
#     """Print a simple greeting for each user in the list"""
#     for name in names:
#         print(f"Hello, {name.title()}")

# greet_users(["John", "Steve", "Trevor"])

# The first function will have printing t-shirt designs, the second will
# summary the prints that have been made

# def print_models(unprinted_designs, completed_models=[]):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed models after printing
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
        
# def show_completed_models(completed_models):
#     """Show completed models that were printed."""
#     print("\nThe following models have been printed.")
#     for completed_model in completed_models:
#         print(completed_model)
    
# unprinted_designs = ["Phone Case", "Robot Pendant", "Book Case"]
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Preventing a function from modifying a list
# You can send a copy of a list to a function like this:
# function_name(list_name[:])
# You should pass the original list to functions unless you have a specific
# reason to make a copy. Its more efficient for function to work with an
# existing list, because this avoids using time and memory to make a 
# separate copy, especially with large lists.

#-------------------------------------------------------------------------------
#   Try it yourself:
#   8.9: Messages: Make a list containing a series of short text messages.
#   Pass the ist to a function called show_messages() and print each text
#   message
#-------------------------------------------------------------------------------
# def show_messages(messages):
#     """Takes list of short text messages and prints each message."""
    
#     for message in messages:
#         print(f"{message}")
        
# message_list = ["Hey! Just checking in—how’s everything going?",
#                 "Don’t forget our meeting at 3pm. See you then!",
#                 "Running late, be there in 10 mins.",
#                 "Lunch tomorrow? Let me know what time works.",
#                 "Great job today—really impressed with your effort!"]

# show_messages(message_list)

#-------------------------------------------------------------------------------
#   Try it yourself:
#   8.10: Sending Messages: Start with a copy of your program from Ex. 8.9
#   Write a function called send_messages that prints each text message
#   and moves each message to a new list called send_messages as its printed
#   After calling the function, print both of you lists to make sure the
#   messages were moved correctly
#-------------------------------------------------------------------------------

# def send_messages(messages):
#     """
#     Prints each text message and moves each message to a new list called send_messages as its printed
#     """
#     sent_messages = []
#     while messages:
#         new_message = messages.pop()
#         print(f"{new_message}")
#         sent_messages.append(new_message)

# message_list = ["Hey! Just checking in—how’s everything going?",
#                 "Don’t forget our meeting at 3pm. See you then!",
#                 "Running late, be there in 10 mins.",
#                 "Lunch tomorrow? Let me know what time works.",
#                 "Great job today—really impressed with your effort!"]

# send_messages(message_list)
# print(message_list)

#-------------------------------------------------------------------------------
#   Try it yourself:
#   8.11: Archived Messages: Start with your work from Ex. 8.10. Call the
#   function send_messages() with a copy of the list of messages. After
#   calling the function, print both of your lists to show that the original
#   list has retained its messages
#-------------------------------------------------------------------------------

# def send_messages(messages):
#     """
#     Prints each text message and moves each message to a new list called send_messages as its printed
#     """
#     sent_messages = []
#     while messages:
#         new_message = messages.pop()
#         print(f"{new_message}")
#         sent_messages.append(new_message)

# message_list = ["Hey! Just checking in—how’s everything going?",
#                 "Don’t forget our meeting at 3pm. See you then!",
#                 "Running late, be there in 10 mins.",
#                 "Lunch tomorrow? Let me know what time works.",
#                 "Great job today—really impressed with your effort!"]

# send_messages(message_list[:])
# print(message_list)

#-------------------------------------------------------------------------------

# Passing an Arbitrary Number of Arguments
# Python allows a function to collect an arbitrary number of arguments from the
# calling statement.

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    

make_pizza("pepperoni")
make_pizza("Pepperoni", "Just Cheese", "Meat Lovers")

# The asterix in the parameter name *toppings tells python to make a tuple
# called toppings, containing all the values the function recieves

# Mixing Positional Arguments and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed last
# in the function definition.

def make_pizza(size, *toppings):
    """Print the size of the pizza and the list of toppings requested."""
    print(f"Making a {size} inch pizza with the following toppings")
    for topping in toppings:
        print(topping)
        
make_pizza(16, "pepperoni")
make_pizza(22, "Pepperoni", "Just Cheese", "Meat Lovers")

# Using Arbitrary Keyword Arguments
# Sometimes you'll want to accept an arbitrary number of arguments, but you
# won't know ahead of time what kind of information will be passed to the
# function. In this case you can write functinos that accept as many key-value
# pairs as the calling statement provides.
# You will often see the parameter name **kwargs used to collect nonspecific
# keyword arguments

def build_profile(first, last, **user_info):
    """Build a dict containing everything we know about a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = (build_profile("albert", "einstein", location="princeton", field="physics"))
print(user_profile)

#-------------------------------------------------------------------------------
#   Try it yourself:
#   8.12 Sandwhiches: Write a function that accepts a list of items a person
#   wants on a sandwhich. The function should have one parameter that collects
#   as many items as the function call provides. Call the function three times
#   using a different number of arguements each time
#-------------------------------------------------------------------------------

def sandwhiches(*items):
    """
    Accepts a lists of items a person wants on a sandwhich and prints the
    list of items
    """
    for item in items:
        print(item)
        
sandwhiches("cheese", "ham", "tomato")
sandwhiches("cheese", "ham")
sandwhiches("ham")

#-------------------------------------------------------------------------------
#   Try it yourself:
#   8.13 User Profile: Start with a copy of a user profile from page 148.
#   Build a profile of yourself by calling build_profile(), using your first
#   name and last names and three other key-value pairs that describe you.
#-------------------------------------------------------------------------------

def build_profile(first, last, **user_info):
    """Build a dict containing everything we know about a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = (build_profile("andre", "jones", location="perth", 
                field="information technology", university="Murdoch"))
print(user_profile)

#-------------------------------------------------------------------------------
#   Try it yourself:
#   8.14 Cars: Write a function that stores information about a car in a dict.
#   The function should always receive a manufacturer and a model name. It
#   should then accept an arbitrary number of keyword arguments. Call the 
#   function with the required information and two other name-value pairs, 
#   such as color or an optional feature.
#-------------------------------------------------------------------------------

def cars(make, model, **features):
    """
    Stores information about a car in a dict and prints the dict
    """
    features["make"] = make
    features["model"] = model
    return features

print(cars("Volvo", "XL150", color="Blue", tow_package=True))

#-------------------------------------------------------------------------------

# Storing Functions in Models
# An import statement tells python to make the code in a module available in 
# the currently running program file.

import pizzas

pizzas.make_pizza(16, "pepporoni")
pizzas.make_pizza(12, "mushrooms", "green peppers", "ham")

# This first examples makes every function from the module avaiable

# Importing specific functions
# Syntax: from module_name import function_name
# you can import as many functions from the module as you want by
# by separating each function with a comma
# For this scenario you don't need to use the dot notation to call the
# function. Because we have explicitly imported the function in the import
# statement, we can call it by using the name of the function.

# Using as to Give a Function an Alias
# Syntax: from module_name import function_name as fn

# Using as to Give a Module an Alias
# You can also provide an alias for a module name
# Syntax: import module_name as mn

# Importing All Functions in a Module
# You can tell python to import every function in a module by using the
# asterix operator *.
# The asterix in the impport statement tells python to COPY every function
# from the module into the program file. You can call each function by name
# without using the dot notation.
# Syntax: from module_name import *

