"""Learning about tuple unpacking with List
"""

# Assign multiple variables with the values in a list with one line of code
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

# Assign multiple variables with the values in a tuple with one line of code
dog = ('Skinny', 'Mastiff', 5)
size, breed, age = dog
print(size)
print(breed)
print(age)

myPets = [['fat', 'gray', 'loud'], ['Skinny', 'Mastiff', 5], ['Who knows', 'Mum knows', (5, 5)]]
pet1, pet2, pet3 = myPets
print(pet1)
print(pet2)
print(pet3)