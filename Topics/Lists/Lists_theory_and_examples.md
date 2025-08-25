# Topic: Lists

## 📖 Theory - 

### Python Crash Course - TextBook

### Introducing **Lists**

Syntax for accessing last element in a list [-1]

#### Modifying elements in a list
- To change an element, use the name of the list followed by the index
of the element you want to change, and then provide the new value you want that item to have.

#### Adding elements to a list
- The simplest way to add a new element to a list is to append the item to the list
- Use the append() method - adds element to the end of the list. Remember this creates a **mutated** list

#### Inserting elements into a list
- You can add a new element at any position in a list by using the **insert()** method. This operation shifts every other value in the list one position to the right.

```python
motorcycles = ["Honda", "Yamaha", "Suzuki"]

motorcycles.insert(0, "Ducati")
print(motorcycles)
# ['Ducati', 'Honda', 'Yamaha', 'Suzuki']
```

#### Removing elements from a List
- You can remove an item according to its position in the list or according to its value
- Removing an item using the del statement:
  - Remove an item from any position in a list using the delete statement if you know its index.
  - You can no longer access the value that was removed from the list after the del statement is used.
  
```python
del motorcycles[0]
print(motorcycles)
# ['Honda', 'Yamaha', 'Suzuki']
```
#### Removing an item using the pop() method
  - The pop method removes the last item in a list, but it lets you work with that item after removing it.

```python
print(motorcycles)
# ['Honda', 'Yamaha', 'Suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# ['Honda', 'Yamaha']
# Suzuki

```
#### Popping items from any position in a List

- You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses.

```python
first_owned = motorcycles.pop(1)
print(motorcycles)
print(first_owned)

# ['Honda']
# Yamaha
```

#### Removing an item by Value

- If you only know the value of the item you want to remove, you can use the remove() method.

```python
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

motorcycles.remove("Yamaha")
print(motorcycles)
```
- You can also use the remove() method to work with a value that's being removed from a list.

```python
motorcycles = ["Honda", "Yamaha", "Suzuki", "Ducati"]
print(motorcycles)

too_expensive = 'Ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
```
NOTE: The remove() method only deletes the first occurrence of the value you specify. If there is a possibility the value appears more than once in the list,
#you'll need to use a loop to make sure all occurrences of the value are removed.

#-----------------------------------------------------------------------------------------------------
#### Try It Yourself
**3-4. Guest List:** If you could invite anyone, living or deceased, to dinner, who would you invite?
#-----------------------------------------------------------------------------------------------------
 
```python
# Make a list that includes at least three people you’d like to invite to dinner.

guests = ["John", "Michael", "Cliff"]

# Then use your list to print a message to each person, inviting them to dinner.
for guest in guests:
    print(f"Hi {guest}, would you like to come for dinner?\n")

```
#-----------------------------------------------------------------------------------------------------
**3-5. Changing Guest List:** You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. Start with your program from Exercise 3-4. 
#-----------------------------------------------------------------------------------------------------
```python
# Add a print() call at the end of your program, stating the name of the guest
# who can’t make it.

cancel_guest = guests.pop(0)
print(f"{cancel_guest} is not able to make it\n")

# Modify your list, replacing the name of the guest who can’t make it with the 
# name of the new person you are inviting.

guests.insert(0,"Trevor")
```
#-----------------------------------------------------------------------------------------------------
**3-6. More Guests:** You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or 3-5. 
#-----------------------------------------------------------------------------------------------------
```python
# Add a print() call to the end of your program, informing people that you found
# a bigger table.

print(f"Hi {guests[0]}, {guests[1]} and {guests[2]},\nI have found a bigger table for more people")

# Use insert() to add one new guest to the beginning of your list
guests.insert(0, "Martha")

# Use insert() to add one new guest to the middle of your list.
guests.insert(len(guests)//2, "Penny")

# Use append() to add one new guest to the end of your list
guests.append("Ruth")

# Print a new set of invitation messages, one for each person in your list.
for guest in guests:
    print(f"Hi {guest}, would you like to come for dinner?\n")
```
#-----------------------------------------------------------------------------------------------------
**3-7. Shrinking Guest List:** You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
Start with your program from Exercise 3-6.   
#-----------------------------------------------------------------------------------------------------
```python
# Add a new line that prints a message saying that you can invite only two people for dinner,
print(f"Sorry everyone, I can only now invite two people")

# Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting them know you’re
# sorry you can’t invite them to dinner.

i = len(guests) - 2
while i > 0: 
    cancel_guest = guests.pop()
    print(f"Sorry {cancel_guest}, I am unable to invite you to dinner\n")
    i -= 1

# Print a message to each of the two people still on your list, letting them know they’re still invited
for guest in guests:
    print(f"Hi {guest}, you are still invited for dinner\n")
    
# Use del to remove the last two names from your list, so you have an empty list. 
del guests[1]
del guests[0]

# Print your list to make sure you actually have an empty list at the end of your program.
print(guests)
```
#-----------------------------------------------------------------------------------------------------

#### Organising a List

#### Sorting a list permanently with the sort() Method. 
- The sort method changes the order of the list **permanently**
- You can sort a list in reverse alphabetical order by passing the argument reverse=True. sort(reverse=True)

#### Sorting a list temporarily with the sorted() function
- To maintain the original order of a list but present it in sorted order, you can use the sorted() function
- The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order

#### Printing a List in Reverse Order
- To reverse the order of a list, you can use the reverse() method.
- reverse() doesn't store backward alphabetically; it simply reverse the order of the list
- The reverse() method changes the order of a list **permanently**, but you can revert to the original order anytime by applying reverse() to the same list a second time

#### Finding the Length of a List
- You can find the length of a list by using the len() function

#-----------------------------------------------------------------------------------------------------
#### Try It Yourself
**3-8. Seeing the World:** Think of at least five places in the world you’d like to visit.
#-----------------------------------------------------------------------------------------------------
```python
# Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["Germany", "Austria", "Margaret River", "Europe", "Russia"]

# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
print(places)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places))

# Show that your list is still in its original order by printing it.
print(places)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(sorted(places, reverse=True))

# Show that your list is still in its original order by printing it again.
print(places)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(places)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print(places)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print(places)

# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)

```