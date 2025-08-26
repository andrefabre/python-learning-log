# Topic: Input Validation

## 📖 Theory - 

### Python Crash Course - TextBook

### **Input Validation**

#### The PyInputPlus Module

- PyInputPlus module contains functions similar to input() for several kinds of 
  data: numbers, dates, email addresses and more
- If the user enters invalid input, such as a badly formatted date or a number
that is outside of an intended range, PyInputPlus will reprompt the for input.
- PyInputPlus also has other useful features like a limit for the number of times
it reprompts users and a timeout if users are required to respond within a time limit

#### Common Functions
- **inputStr()** is like the built-in input() function that has the general PyInputPlus features.
  You can also pass a custom validation function to it.
- **inputNum()** Ensures the user enters a number and returns an int or float, 
  depending on if the number has a decimal point in it.
- **inputChoice()** Ensures the user enters one of the provided choices
- **inputMenu()** Is similar to inputChoice(), but provides a menu with numbered
  or lettered options
- **inputDateTime()** Ensures the user enters a date or time
- **inputYesNo()** Ensures the user enters a "yes" or "no" response
- **inputBool()** Is similar to inputYesNo(), but takes a "True" or "False" response and returns a Boolean Value
- **inputEmail()** Ensures the user enters a valid email address
- **inputFilepath()** Ensure the user enters a valid file path and filename, and
  can optionally check that a file with that name exists
- **inputPassword()** Is like the built-in input(), but displays * characters as
  the user types so that passwords, or other sensitive information, aren't
  displayed on the screen

These functions will automatically reprompt the user for as long as they enter
enter invalid input
```python
import pyinputplus as pyip
response = pyip.inputNum()
```
To display a prompt
```python
response = pyip.inputNum(prompt="Enter a number: ")
# input 42
response
# 42 - returns an int or float not a string so no need to cast
```

#### The min, max, greaterThan, and lessThan Keyword Arguments
The inputNum(), inputInt(), and inputFloat() functions, which accept int and
float numbers, also have min, max, greaterThan, and lessThan keyword arguments
for specifying a range of values
```python
import pyinputplus as pyip
response = pyip.inputNum("Enter num: ", min=4)
>>>Enter num: 3
>>>Number must be at minimum 4.
>>>Enter num: 4
>>>response
>>>4

response = pyip.inputNum("Enter num: ", greaterThan=4)
>>>Enter num: 4
>>>Number must be greater than 4.
>>>Enter num: 5
>>>response
>>>5

response = pyip.inputNum(">", min=4, lessThan=6)
>>>6
>>>Number must be less than 6.
>>>3
>>>Number must be at minimum 4.
>>>4
```
#### The Blank Keyword Argument
- By default, blank input isn't allowed unless the blank keyword argument is 
  set to True
```python
import pyinputplus as pyip
response = pyip.inputNum("Enter num: ")
>>>Enter num: (*blank input entered here*)
>>>Blank values are not allowed
>>>Enter num: 42
>>>response
>>>42

response = pyip.inputNum(blank=True)
>>>(*blank input entered here*)
>>>response
>>>""
```
#### The limit, timeout, and default Keyword Arguments
- If you'd like a function to stop asking the user for input after a certain
  number of tries or a certain amount of time, you can use the limit and timeout
  keyword arguments.
- Pass an integer for the limit keyword argument to determine the number of attempts
  a PyInputPlus function will make to receive valid input before giving up.
- Pass an integer for the timeout keyword argument to determine how many seconds
  the user has to enter valid input before the PyInputPlus function gives up.
- If the user fails to enter a valid input, these keyword arguments will cause
  the function to raise a RetryLimitException or TimeoutException, respectively.

#### The allowRegexes and blockRegexes Keyword Arguments
- You can also us regular expressions to specify whether an input is allowed or not.
- The allowRegexes and blockRegexes keyword arguments take a list of regular expression
  strings to determine what the PyInputPlus function will accept or reject as valid input

#### Passing a Custom Validation Function to inputCustom()
- You can write a function to perform your own custom validation logic by passing
  the function to inputCustom()