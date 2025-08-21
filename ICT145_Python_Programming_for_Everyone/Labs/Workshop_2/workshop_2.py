"""Part 2 – Practice Questions
1. Write a python program to calculate the Body Mass Index (BMI) of a person. 
Take the input for weight (kg) and height (m) of the person,
then calculate BMI using: B𝑀𝐼= 𝑤𝑒𝑖𝑔ℎ𝑡 / (ℎ𝑒𝑖𝑔ℎ𝑡2) 
"""

print("Body Mass Index Calculator")
# Get height and weight
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

# Calculate BMI
bodyMassIndex = weight / height**2

# Print results
print(f"Your BMI is {bodyMassIndex:2f}%")

#-------------------------------------------------------------
"""Find and fix the error.
Answer for a. variable z does not have a value assigned
Answer for b. value being assigned to variable c is of type string / type int. Which will raise and error.
"""
#-------------------------------------------------------------
"""
3. Take the input of three numbers a, b, c, and write a program to find the average of these 
three numbers.
"""
print("Find the average of three numbers")
# Get the three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number"))

average = (num1 + num2 + num3) / 3
print(f"The average of {num1}, {num2} and {num3} is: {average:.2f}")

#-------------------------------------------------------------
"""
4. Write a program that takes an input of a 3-digit number and compute the sum of the first 
and last digit of this 3-digit number. 
"""

digits = int(input("Enter a 3 digit number"))
lastDigit = digits % 10
firstDigit = (digits // 10) // 10
sumDigits = firstDigit + lastDigit
print(f"The sum of the first and last digits of {digits} is {int(sumDigits)}")

#-------------------------------------------------------------
"""
5. Given an amount in cents (e.g., 459 cents), write a program to convert it into dollars and 
remaining cents.
Example:
    Input:459 cents Output:
    4 dollars and 59 cents 
"""
#-------------------------------------------------------------
"""
6. Complete the following code snippets.
"""
# a.


# b.

