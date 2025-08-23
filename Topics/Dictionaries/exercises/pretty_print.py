import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message: # loop through characters in the str(message)
    count.setdefault(character, 0) # if the key 'character does not exist create it with value 0. As count dict is empty, it first iteration creates char with value 0. if the key exists it will not update the value with 0.
    count[character] = count[character] + 1
    # get the current character count: count[character] add 1 to it.
    # keeps ongoing count of number of characters in string
pprint.pprint(count)