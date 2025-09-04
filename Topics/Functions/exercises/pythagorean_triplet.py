
"""
Find all pythagorean triplets between two numbers
"""

# i = 3
# if i**2 + (i+1)**2 == (i+2)**2:
#     isTriplet = True
# print(isTriplet)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"""
Pythagorean Triplets between {start} and {end} are:
""")
for i in range(start, end+1):
    for j in range(start+1, end+1):
        for k in range(start+1, end):
            if i**2 + j**2 == k**2:
                print(f"{i}, {j}, {k}")


1