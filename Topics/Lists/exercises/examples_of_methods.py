
myList = [
    "Lion",
    "Elephant",
    "Giraffe",
    "Kangaroo",
    "Penguin",
    "Dolphin",
    "Panda",
    "Tiger",
    "Zebra",
    "Koala"
]

# Example of the index() method
# When there are duplicates of the value in the list only the first appearance is returned.

myList.index("Penguin")
print(f"My penguin is at index {myList.index("Penguin")}")

# Example of the enumerate() function which gets index and item
for index, item in enumerate(myList):
    #
    print(f"My {item} is at index {index}")