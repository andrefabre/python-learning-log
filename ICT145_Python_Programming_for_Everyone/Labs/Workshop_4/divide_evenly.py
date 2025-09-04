"""
Given a positive integer n, count the number between range 1 and 10 inclusive.
tha e divide n evenly. Print the count of such numbers. 
"""

n = int(input("Enter the number: "))
count = 0

for i in range(1, 11):
    if n % i == 0:
        print(f"{i} divides {n}")
        count += 1
    else:
        print(f"{i} does not divide {n}")
print(f"Count of numbers between 1 and 10 that divides {n} is: {count}")