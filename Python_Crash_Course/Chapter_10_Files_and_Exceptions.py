#-------------------------------------------------------------------------------
#   Chapter 10: Files and Exceptions
#-------------------------------------------------------------------------------

# Reading from a File

# Reading the contents of a File

# from pathlib import Path

# path = Path("pi_digits.txt")
# contents = path.read_text().rstrip()
# print(contents)

# read_text() returns an empty string when it reaches the end of a file, this
# empty string should show up as a blank line. We can remove the extra blank 
# line by using rstrip() method

# Relative and Absolute File Paths
# A relative file path tells python to look for a given location relative to
# the directory where the currently running program file is stored.
# Absolute path tells python where the file is on your computer regardless of
# where the program thats being executed is stored. Absolute paths are usually
# longer that relative paths, because they start at your systems root folder.

# Accessing a File's Lines

# You can use the splitlines() method to turn a long string into a set of lines,
# and then use a for loop to examine each line from a file, one at a time.

# from pathlib import Path

# path = Path("pi_digits.txt")
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)
    
# Working with a File's Contents

# from pathlib import Path

# path = Path("pi_digits.txt")
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ""
# for line in lines:
#     pi_string += line

# print(pi_string)
# print(len(pi_string))

# NOTE: When python reads from a txt file, it interprets all text in the file as
# a string. If you read in a number and want to work with that value in a
# numerical context, you'll have to convert it to an integer using the int()
# function or a float using the float() function.

# Writing to a File
# Once you have a path defined you can write to a file using the writetext()
# method.

# from pathlib import Path

# path = Path('writing_to_a_file.txt')
# path.write_text("I love programming in python")

# NOTE: Python can only write strings to a text file. If you want to store
# numerical data in a text file, you'll have to convert the data to string
# format first using the str() function

# Writing Multiple Lines
# To write more than one line to a file, you need to build a string containing
# the entire contents of the file, and then call write_text() with that string

# from pathlib import Path

# contents = "I love programming.\n"
# contents += "I love creating new games\n"
# contents += "I also love working with data."

# path = Path("writing_to_a_file.txt")
# path.write_text(contents)

# NOTE: Be careful when calling write_text() on a path object. If the file already
# exists, write_text() will erase the current contents of the file and write new
# contents to the file.

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   10.4 Guest: Write a program that prompts the user for their name. When
#   they respond, write their name to a file called guest.txt
#-------------------------------------------------------------------------------

# from pathlib import Path

# name = input("Type in your name: ")
# path = Path("guest.txt")
# path.write_text(name)

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   10.5 Guest Book: Write a while loop that prompts users for their name.
#   Collect all the names that are entered, and then write these names to a file
#   called guest_book.txt. Make sure each entry appears on a new line in the
#   file.
#-------------------------------------------------------------------------------

# from pathlib import Path

# flag = True
# guestbook = ""

# while flag:

#     name = input("Enter the guest name: ")
#     if name != "exit":
#         guestbook += name + "\n"
#     else:
#         flag = False

# path = Path("guest_book.txt")
# path.write_text(guestbook)

#-------------------------------------------------------------------------------
#  Exceptions
#-------------------------------------------------------------------------------

# Python uses special objects called exceptions to manage errors that arise
# during a programs execution

# ZeroDivisionError exception

# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
    
# Using Exceptions to Prevent Crashes
# Example of catching an error but keeping the program running

# print("Give me two numbers, and I'll divide them")
# print("Enter q to quit")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == "q":
#         break
#     second_number = input("Second number: ")
#     if second_number == "q":
#         break
    
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# The only code that should go into a try block is code that might cause an
# exception to be raised

# Handling the FileNotFoundError Exception

# from pathlib import Path
# path = Path("alice.txt")
# contents = path.read_text(encoding='utf-8')

# The encoding argument encoding='utf-8' is needed when your systems default
# encoding doesn't match the encoding of the file that's being read. This is
# most likely to happen when reading from a file that wasn't created on your
# system.

# Python can't read from a missing file, so raises an exception

# from pathlib import Path
# path = Path("alice.txt")
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry the file {path} does not exist")

# Analysing Text

# from pathlib import Path
# path = Path("alice.txt")
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry the file {path} does not exist")
# else:
#     # Count the approximate number of words in the file:
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {path} has about {num_words} words.")

# Working with Multiple Files

# from pathlib import Path

# def count_words(path):
#     """Count the approximate number of words in a file."""
#     try:
#         contents = path.read_text(encoding='utf-8')
#     except FileNotFoundError:
#         print(f"Sorry the file {path} does not exist")
#     else:
#         # Count the approximate number of words in the file:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {path} has about {num_words} words.")

# filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
# for filename in filenames:
#     path = Path(filename)
#     count_words(path)

# Storing Data
# The json(Java Script Object Notation) module allows you to convert simple
# python data structures into JSON-formatted strings, and then load the data
# from that file the next time the program runs

# Using json.dumps() and json.loads()

# Saving and Reading User-Generated Data
