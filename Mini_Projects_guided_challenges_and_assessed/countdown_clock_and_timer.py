"""
Objective is to create a GUI window, which will set a countdown timer depending on entry by the user. In addition to this, our window will also display the current time at which the window opens up. Once the alarm goes off, we will get a desktop notification. We will also have an option to produce a beep sound once the timer goes off.
"""

# import the time module
from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier
import winsound

window = Tk() # create window
window.geometry("600x600") # giving size
window.title("The Darkness") # giving title
Label(window, text="Countdown Clock and Timer", font=("Calibri 15")).pack(pady=20)# a label

# to print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time).pack()

check = tk.BooleanVar() # check is of Boolean type
hour = tk.IntVar() # Ensure count is of integer type
minus = tk.IntVar() # Ensure count is of integer type
secon = tk.IntVar() # Ensure count is of integer type

# Define the countdown function
def countdown():
    h = hour.get()
    m = minus.get()
    s = secon.get()
    t = h * 3600 + m * 60 + s
    while t:
        mins, secs = divmod(t, 60)
        display = ("{:02d}:{:02d}".format(mins, secs))
        time.sleep(1) # sleep time 1 sec
        t -= 1
        Label(window, text=display).pack()
    
    if (check.get() == True): # if the value of the check is True
        winsound.Beep(440, 1000) # beep sound
        
    Label(window, text="Times-Up", font=("bold", 20)).place(x=250, y=440)
    
    # Display notification on desktop
    toast = ToastNotifier() # create toast variable
    toast.show_toast("Notification", "Timer is Off", duration = 20, icon_path=NONE, threaded = True,) # show toast
    
Label(window, text="Enter time in HH:MM:SS", font=("bold")).pack()
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minus, width=30).pack()
Entry(window, textvariable=secon, width=30).pack()

Checkbutton(text="Check for Music", onvalue=True, variable=check).pack() # creating checkbox
Button(window, text="Set Countdown", command=countdown, bg="yellow").pack() # create buttons
window.update
window.mainloop()