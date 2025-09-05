#### Tkinter module
- Tkinter is the standard interface in python for creating a GUI that is Graphical User Interface.
- tkinter import * – import everything from the module.
- from tkinter import messagebox – Import message box separately for showing messages on the screen.


#### Example

```python
import tkinter as Tk
# Define the user interface
# --> Tk() contains provisions to handle user events and widgets
password_gen = Tk() 

# --> geometry() method
# Define the dimensions of the frame of the application in the format length x breadth
password_gen.geometry("350x200")

# --> title() method
# An optional parameter to set the title of the application
password_gen.title("Password Generator")
```
#### title_label, length_lable, repeat_label
Use labels to add non-editable text of an application. The parameters are window of the screen, text to display and an optional font styling.
```python
# Mention the title of the app
title_label = Label(password_gen, text="Password Generator", font=("Ubuntu Mono", 12))
title_label.pack()

# Read length
length_label = Label(password_gen, text="Enter length of the password: ")
length_label.place(x=20, y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190, y=30)
```
#### repeat_entry, length_entry
To read user input, we use Entry widget. Alternatively, Text can also be used. To use the widget, pass the following parameters: password_gen-the screen of the python password generator app and the width of the widget.
```python
repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ")
repeat_label.place(x=20, y=60)
repeat_entry = Label(password_gen, width=3)
repeat_entry.place(x=300, y=60)
```
#### widget.place() and widget.pack():
- Any widget or label will be visible only after positioning it on the window or screen of the app. 
- To achieve this, we make use or pack() and place().
- pack() center aligns text along a row. First widget/label is set on row 1, second on row 2 and so on.
- To enable customized positioning of the widget in python password generator and to set to or more labels and widgets on the same row, we can use place().
- place() takes an x and y coordinate which is the row and the column.

#### Password_button:
- Buttons perform a certain function when the user clicks on it.
- Link the generate_password function to the button using command argument along with password_gen and name of the button.
- Place the widget using place().
- password_gen.mainloop(): To close the app when the user clicks on exit