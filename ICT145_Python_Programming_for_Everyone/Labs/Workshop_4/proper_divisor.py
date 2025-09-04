"""
A perfect number is a number that is equal to the sum of its proper divisors, excluding itself
Write a python program to check if a number is perfect.
Keep asking the user to enter a number until the number is perfect
A positive proper divisor is a positive divisor of a number n, excluding n itself. For example, 1, 2, and 3 are positive proper divisors of 6, but 6 itself is not. 
"""

# while True:
    
#     total = 0
#     try:
#         n = input("Enter a number: ")
#         if not n.isdigit(): continue
#         n = int(n)
#     except ValueError: continue
    
#     for i in range(1, n):
#         if n % i == 0:
#             total += i
#         else:
#             continue

#     if total == n:
#         print(f"{n} is a perfect number\nGood Job! You did it this time!")
#         break
#     else:
#         print(f"{n} is not a perfect number. Try Again!")
#         continue



while True:
    
    total = 0
    try:
        n = input("Enter a number: ")
        if not n.isdigit(): continue
        n = int(n)
    except ValueError: continue
    
    for i in range(1, n):
        if n % i == 0:
            total += i
    else:
        if total == n:
            print(f"{n} is a perfect number\nGood Job! You did it this time!")
            break
        else:
            print(f"{n} is not a perfect number. Try Again!")
            continue
    

