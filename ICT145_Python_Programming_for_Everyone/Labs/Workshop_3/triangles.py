import sys
import math

# NOTE: This program does not check if the inputs make a valid triangle or
#  guard against floating point errors which cause negative values.
# In these case it will return a "ValuerError: math domain error'. Code can be
# updated to handle these cases

print("Hello,\nThis program calculates the area of a triangle")
a = int(input("Enter length of side 1: "))
b = int(input("Enter length of side 2: "))
c = int(input("Enter length of side 3: "))

if a == b == c:
    triangleType = "Equilateral"
    area = a ** 2 * math.sqrt(3) / 4
elif a == b or a == c or b == c:
    triangleType = "Isosceles"
    if a == b: # a represents sides of same length
        area = (c / 4) * math.sqrt((4 * a ** 2) - c ** 2)
    elif a == c: # a represents sides of the same length (a, c)
        area = (b / 4) * math.sqrt((4 * a ** 2) - b ** 2)
    else: # b and c are the same length
        area = (a / 4) * math.sqrt((4 * b ** 2) - a ** 2)
elif a != b and b != c and a != c:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    triangleType =  "Scalene"
else:
    print("Input Error")
    sys.exit()

print(f"{triangleType} with an area of {area}")
