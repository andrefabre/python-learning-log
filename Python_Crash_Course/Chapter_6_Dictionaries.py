#-------------------------------------------------------------------------------
#   Chapter 6: Dictionaries
#-------------------------------------------------------------------------------

# Dictionaries allow you to connect pieces of information. 
# A dictionary is a collection of key-value pairs. Each key is connected to a
# value, and you can access the value associated with that key.
# A key-value pair is a set of values associated with each other.
# Accessing values in a dictionary. To get the value associated with a key,
# give the name of the dictionary and then place the key inside a set of 
# square brackets.
# Dictionaries retain the order in which they were defined.

# Simple dictionary

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# Adding New Key-Value Pairs
# To add a new key-value pair, give the name of the dictionary followed by the
# key in square brackets, along with the new value.

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Modifying Values in a Dictionary
# To modify a value in a dictionary, give the name of the dictionary with the
# key in square brackets and then the new value you want associated with that
# key.

alien_0['color'] = "yellow"
print(f"The alien is now {alien_0["color"]}")

# For a more interesting example, let's track the position of an alien that can
# move at different speeds. We'll store a value representing the alien's current
# speed and then use it to determine how far to the right the alien should move.
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")

# Move alien to the right
# Determine how far to move the alien based on it's current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
# You can use the del statement to completely remove a key-value pair. All
# del needs is the name of the dictionary and the key you want to remove.

del alien_0["points"]
print(alien_0)

# Using get() to Access Values
# You can use a the get() method to set a default value that will be returned
# if the requested key doesn't exist.

alien_0 = {"color": "green", "speed": "slow"}

point_value = alien_0.get("points", "No point value assigned")
print(point_value)

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   6.1 Person: Use a dictionary to store information about a person.
#   Store the first name, last name, age, and city. Print each piece of 
#   information stored in the dictionary
#-------------------------------------------------------------------------------

person = {"first_name": "John",
          "last_name": "Mitchell",
          "age": 10,
          "city": "Margaret River",
          }
print(person)

# Looping Through a Dictionary

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "peters",
}

# print key and value pairs
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# print keys
for key in user_0.keys():
    print(f"Key: {key}")

# to view keys in dict
print(user_0.keys())

# print values
for value in user_0.values():
    print(f"Values: {value}")
    
# Sets
# When you wrap set() around a collection of values that contain duplicate
# items, python identifies the unique items in the collection and builds a
# set from those items.
#
# You can build a set directly using braces and separating the elements with
# commas. e.g. mySet = {"John", "Terry", "Steve"}
# When you see braces but no key-value pairs you are probably looking at a
# set

#-------------------------------------------------------------------------------
#   Try it Yourself:
#   6.5 Rivers: Make a dictionary containing three major rivers and the 
#   country each river runs through. One key-value pair might be:
#   "Nile": "Egypt"
#-------------------------------------------------------------------------------

rivers = {
    "Nile": "Egypt",
    "Bourbon": "Africa",
    "Swan Lake": "Australia",
}
# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
for river, country in rivers.items():
    print(f"The {river} runs through {country}")
# User a loop to print the name of each river included in the dict
for river in rivers.keys():
    print(f"{river}")
# Use a loop to print the name of each country included in the dict
for country in rivers.values():
    print(f"{country}")
    
#-------------------------------------------------------------------------------
#   Nesting:
#   You can nest dictionaries inside a list, a list of items inside a
#   dict, or even a dict inside a dict. 
#-------------------------------------------------------------------------------

alien_0 = {
    "color": "green",
    "points": 5,
}

alien_1 = {
    "color": "yellow",
    "points": 10,
}

alien_2 = {
    "color": "red",
    "points": 15,
}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

# Use a range to create a fleet of 30 aliens
aliens = []

for alien_number in range(30):
    if alien_number in range(10):
        new_alien = {"color": "green", "points": 5, "speed": "slow",}
        aliens.append(new_alien)
    elif alien_number in range(11, 20):
        new_alien = {"color": "yellow", "points": 10, "speed": "medium",}
        aliens.append(new_alien)
    else:
        new_alien = {"color": "red", "points": 15, "speed": "fast",}
        aliens.append(new_alien)
    
print(len(aliens))

# List inside a dict

