#-----------------------------------------------------------------------------------------------------
#   Chapter 4: Working with Lists
#   
#-----------------------------------------------------------------------------------------------------

# Looping Through an Entire List
#   When you want to do the same action with every item in a list, you can use Pythons for loop

# Use a for loop to print out each name in a list of magicians

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
    
#-----------------------------------------------------------------------------------------------------
#   Try it for Yourself
#   4-1. Pizzas: Think of at least three kinds of your favorite pizza.
#   Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#-----------------------------------------------------------------------------------------------------

pizzas = ["Ham and Cheese", "Hawaiian", "Pepporoni", "Chicken and Bacon"]

# for pizza in pizzas:
#     print(pizza)
    
# Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should have one line

for pizza in pizzas:
    print(f"The name of the pizza is {pizza}")
    
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like
# and then an additional sentence, such as I really love pizza!

print(f"I really like pizza\n")
print(f"My favorite pizzas are {pizzas[0]}, {pizzas[1]} and {pizzas[2]}.\n")
print("I really love pizza!")

#-----------------------------------------------------------------------------------------------------
#   Try it for Yourself
#   Animals: Think of at least three different animals that have a common characteristic. 
#   Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#-----------------------------------------------------------------------------------------------------

animals = ["Bear", "Shark", "Beaver"]
for animal in animals:
    print(animal)
    
# Making Numerical Lists

#   Using the range() Function
#   The range() function makes it easy to generate a series of numbers
#   You can pass range only one argument and it will start the sequence at the number 0
#
#   Using range() to make a List of Numbers
#   If you want to create a list of numbers, you can convert the results of range() directly into a list
#   using the list() function. When you wrap list() around a call to the range() function the output
#   will be a list of numbers

numbers = list(range(1, 11)) # creates a list of numbers from 1 to 10
print(numbers)

#   If you pass a third argument to range(), python uses that value as a step size when generating numbers

even_numbers = list(range(2, 12, 2)) # creates a list of even numbers from 2 to 10
print(even_numbers)

# List Comprehensions

#   A list comprehension combines the for loop and the creation of new elements into one line,
#   and automatically appends each new element

squares = [value ** 2 for value in range(1,11)]
print(squares)


#-----------------------------------------------------------------------------------------------------
#   Try it for Yourself
#   4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive..
#-----------------------------------------------------------------------------------------------------

nums = [value for value in range(1, 21)]
print(nums)

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to 
# print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

for value in range(1, 1_000_001):
    print(value)
    
# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() 
# to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers

count = []
for value in range(1, 1_000_0001):
    count.append(value)
  
print(min(count))
print(max(count))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.

for value in range(1,20, 2):
    print(value)
    
# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
# Use a for loop to print the numbers in your list.

for value in range(3, 31, 3):
    print(value)
    
# 4-8. Cubes: A number raised to the third power is called a cube. 
# For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube.

for value in range(1, 11):
    print(value ** 3)
    
# Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubed = [value ** 3 for value in range(1,11)]
print(cubed)

#-----------------------------------------------------------------------------------------------------
#   Working with a Part of List
#  
#-----------------------------------------------------------------------------------------------------

# Slicing a list
#   To make a slice, you specif the index of the first and last elements you want to work with
#   List[0:3] returns elements at index 0, 1, 2
#   List[2:5] returns elements at index 2, 3, 4
#
#   Without a starting index, python starts the slice at the BEGINNING of the list
#   List[:5] returns elements at index 0, 1, 2, 3, 4
#   
#   Without an ending index, python finishes the slice at the END of the list
#   List[2:] for example if there is a range of 0 to 5, returns elements at index 3, 4
#
# Looping through a Slice
#   You can use a slice in a for loop if you want to loop through a subset of elements in a list
#
players = ["Charles", "Martina", "Michael", "Florence", "Eli"]
print("Here are the first three players on my team")
for player in players[:3]:
    print(player)

# Copying a List
#   To copy a list, you make a slice that includes the entire original list by omitting the first 
#   index and second index [:]

myfoods = ["pizza", "falafel", "carrot cake"]
friends_foods = myfoods[:]

print("My favourite foods are:\n")
print(myfoods)
print(myfoods.index("pizza"))
print("My friends favourite foods are:\n")
print(friends_foods)


#-----------------------------------------------------------------------------------------------------
#   Try It Yourself
#   4-10. Slices: Using one of the programs you wrote in this chapter,
#   add several lines to the end of the program that do the following:
#-----------------------------------------------------------------------------------------------------

# Print the message The first three items in the list are:. 
# Then use a slice to print the first three items from that program’s list

names = ["Charles", "Martina", "Michael", "Florence", "Eli"]
print("The first three names in the list are: \n")
for name in names[:3]:
    print(name)

# Print the message Three items from the middle of the list are:. 
# Then use a slice to print three items from the middle of the list.

print("The first three names in the midde of the list are: \n")
for name in names[1:4]:
    print(name)
    
# Print the message The last three items in the list are:. 
# Then use a slice to print the last three items in the list.

print("The last 3 names in the list are: \n")
for name in names[2:5]:
    print(name)

#-----------------------------------------------------------------------------------------------------
#   Try It Yourself
#   My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
#   Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#-----------------------------------------------------------------------------------------------------

friends_pizzas = pizzas[:]

# Add a new pizza to the original list.
pizzas.append("Meat Lovers")

# Add a different pizza to the list friend_pizzas.
friends_pizzas.append("Cheeseburger")

# Prove that you have two separate lists. Print the message My favorite pizzas are:,
# and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, 
# and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

print("My Favourite pizzas are: \n")
for pizza in pizzas:
    print(pizza)
print("My friends favourite pizzas are: \n")
for pizza in friends_pizzas:
    print(pizza)

#-----------------------------------------------------------------------------------------------------
#   Tuples
#   
#-----------------------------------------------------------------------------------------------------

# A tuple is a list of items that is immutable (cannot change)
# Access elements in the tuple by using each elements index
# Tuples are technically defined by the presence of a comma ','; the parentheses make them look neater
# and more readable. If you want to define a tuple with one element, you need to include a trailing comma e.g. (3,)


dimensions = (200, 10)
print(dimensions)

# Writing Over a Tuple
# Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple

dimensions = (200, 10)
print(f"Orginal dimensions: {dimensions}")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print(f"New Dimensions: {dimensions}")
for dimension in dimensions:
    print(dimension)
    
#-----------------------------------------------------------------------------------------------------
#   Try It Yourself
#   4-13. Buffet: A buffet-style restaurant offers only five basic foods.
#   Think of five simple foods, and store them in a tuple.
#-----------------------------------------------------------------------------------------------------

simple_foods = ("bread", "cheese", "apple", "orange", "pie")

# Use a for loop to print each food the restaurant offers.

for food in simple_foods:
    print(food)
    
# Try to modify one of the items, and make sure that python rejects the change

simple_foods[0] = "Chicken" # TypeError: 'tuple' object does not support item assignment

# The restaurant changes its menu, replacing two of the items with different foods.
# Add a line that rewrites the tuple, and then use a for loop to print each of the items
# on the revised menu

simple_foods = ("chicken", "eggs", "apple", "orange", "pie")
for food in simple_foods:
    print(food)