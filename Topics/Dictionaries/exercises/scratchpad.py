people_ages = {
    "Alice": 25,
    "Bob": 32,
    "Charlie": 41,
    "Diana": 29,
    "Ethan": 37,
    "Fiona": 22,
    "George": 34,
    "Hannah": 28,
    "Ian": 45,
    "Julia": 31
}

# list(people_ages) # creates a list of all the keys in dict
# list(people_ages.keys()) # creates a list of all the keys in dict
# list(people_ages.values()) # creates a list of all values in dict
# tuple(people_ages) # creates a tuple containing  all keys in dict
# tuple(people_ages.values()) # creates a tuple containing all values in dict.
# people_ages.keys()
#     # returns 
#     # dict_keys(['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ian', 'Julia'])
# people_ages.values()
#     # returns
#     # dict_values([25, 32, 41, 29, 37, 22, 34, 28, 45, 31])
# print(people_ages.values())

# print(people_ages.get("TheDarkness", "The key does not exist in the dictionary"))
# # The key does not exist in the dictionary

# # setdefault() method example
# # Counts the number of occurrences of each character in a string
# message = "It was a bright cold day in April, and the clocks were striking thirteen."
# count = {}

# for character in message: # loop through characters in the str(message)
#     count.setdefault(character, 0) # if the key 'character does not exist create it with value 0. As count dict is empty, it first iteration creates char with value 0. if the key exists it will not update the value with 0.
#     count[character] = count[character] + 1
#     # get the current character count: count[character] add 1 to it.
#     # keeps ongoing count of number of characters in string
# print(count)
    
    
    