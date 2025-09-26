# Topic: Debugging

## 📖 Theory - 

### Automate the Boring Stuff - TextBook

#### **Debugging**

#### Raising Exceptions
- Raising an exception is a way saying "Stop running the code in this function and move the program execution to the except statement
- Exceptions are raised with a **raise** statement. In code, a raise statement consists of the following:
  - The raise keyword
  - A call to the Exception() function
  - A string with a helpful error message passed to the Exception() function
- 
#### Getting the Traceback as a String
- The traceback includes the error message, the line number of the line that caused the error, and the sequence of the function calls that led to the error. This sequence of calls is called the **call stack**.
- python displays the traceback whenever a raised exception goes unhandled. But you can also obtain it as as string by calling *traceback.format_exec()*
  You will need to import pythons traceback module before calling this function

#### Assertions
- An assertion is a sanity check to make sure your code isn't doing something obviously wrong.
- If the sanity check fails, then an AssertionError exception is raised.
- In code an assert statement consists of the following:
  - the *assert* keyword
  - a condition (that is, an expression that evaluates to True or False)
  - a comma
  - a string to display when the condition is false
- In plain english: "I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program"

```python
>>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
>>> ages.sort()
>>> ages
[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
>>> ages.reverse()
>>> ages
[92, 80, 73, 57, 54, 47, 26, 22, 17, 15]
>>> assert ages[0] <= ages[-1] # Assert that the first age is <= the last age
Traceback (most recent call last):
  File "<python-input-9>", line 1, in <module>
    assert ages[0] <= ages[-1]
           ^^^^^^^^^^^^^^^^^^^
AssertionError
```
- Unlike exceptions, your code **should not** handle assert statements with try and except
- Assertions are for programmer errors, not user errors.

#### Logging
- Python's logging module makes it easy to create a record of custom messages that you write