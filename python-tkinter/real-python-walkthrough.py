# Made while working through: https://realpython.com/python-gui-tkinter/

def resetWindow(): # Used to clear the window so something else can be shown
    input("Press anything to go to the next window: ")
    windowWidgets = window.winfo_children()
    for widget in windowWidgets:
        widget.destroy()

import tkinter as tk # Classic widgets
import tkinter.ttk as ttk # Themed widgets

#--- Wildcard import will override all legacy widgets with the themed ones (where possible---
# from tkinter import *
# from tkinter.ttk import * 
# 
# You can then do just Label() (without needing the prefix)
#--------------------------------------------------------------------------------------------

window = tk.Tk()

# Label
#----------
# 1.1
greeting = tk.Label(text="Hello, world!") # Used for displaying text that can't be edited by the user
greeting.pack()

# 1.2
# You can change its colour
greeting = tk.Label(
    text="Hello, world!",
    foreground="white",
    background="black"
)
greeting.pack()

# 1.3
# You can use alternative parameter and argument names/representations
greeting = tk.Label(
    text="Hello, world!",
    fg="#FFFFFF",
    bg="#000000"
)
greeting.pack()

# 1.4
# You can set the width and height (measured in 'text units' based on the H & W of 0)
greeting = tk.Label(
    text="Hello, world!",
    foreground="white",
    background="green",
    width=10,
    height=10
)
greeting.pack()

# Button
#----------
# 2.1
button = tk.Button(
    text="Click me!",
    width=15,
    height=5,
    bg="orange",
    fg="black",
)
button.pack()

# Entry
#----------
# 3.1
entry = tk.Entry(fg="white", bg="blue", width=50)
entry.pack()

#--------------------
# NEXT WINDOW
resetWindow()
#--------------------

# 3.2 - A feature of .pack() is that it will automatically centre the label above the 'Entry' widget
label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()

# .get() is used to retrieve the text from an 'Entry' widget -> text = entry.get()
# .delete() is used to remove a character at a position -> 'entry.delete(0)' removes the first character
    # 'entry.delete(0,4)' removes the first four characters
    # 'entry.delete(0, tk.END)' removes all characters
# .insert() is used to insert text into an 'Entry' widget -> entry.insert(0, "Python")

#--------------------
# NEXT WINDOW
resetWindow()
#--------------------

# Text
#----------
# 4.1
textBox = tk.Text()
textBox.pack()

# .get() works differently for 'Text' widgets. You must give the line number of a character and its position
    # "1.0" would get the first character from the first line
    # To get multiple characters you give a second index -> textBox.get("1.0", "1.5")
    # 'textBox.get("1.0", tk.END)' gets everything
# .delete() works similarly -> 'textBox.delete("1.0")' OR 'textBox.delete("1.0", "1.5")'
# .insert() also works similarly -> textBox.insert("1.0", "Hello")
    # 'textBox.insert("2.0", "\nWorld")' will insert "World" onto the second line
    # 'textBox.insert(tk.END, "Put me on a new line!")' will put the text on at the end of the line

#--------------------
# NEXT WINDOW
resetWindow()
window.destroy()
#--------------------

# Frame
#----------
# Frames are assigned to a window and can be thought of as containers for other widgets
# 5.1
window = tk.Tk() # Make a new window
frame = tk.Frame() # Make a new frame
frame.pack() # Pack the frame into the window
label = tk.Label(master=frame) # Assign the widget to the frame

#--------------------
# NEXT WINDOW
resetWindow()
#--------------------

# 5.2
borderEffects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for reliefName, relief in borderEffects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=reliefName)
    label.pack()

window.mainloop()

#--------------------
# NEXT WINDOW
resetWindow()
#--------------------

# Geometry Managers
#----------
# .pack() is a geometry manager, as well as .place() and .grid()
# Each window or frame can use only one geometry manager

# 6.1 - .pack()
# .pack() computes a rectangular area called a parcel that is just as tall (or wide) enough to hold the widget and then fills the remaining width (or height) in the window with blank space. It then centres the widget in the parcel unless a different location is specified. 
# 'frameOne.pack(fill=tk.X)' will fill the frame horizontally
# 'frameOne.Pack(fill=tk.Y)' will fill the frame vertically
# 'frameOne.Pack(fill=tk.BOTH)' will fill both
#--------------------
# The 'side' keyword argument specifies on which side of the window the widget should be placed
    # 'side=tk.TOP'
    # 'side=tk.BOTTOM'
    # 'side=tk.LEFT'
    # 'side=tk.RIGHT'

# 6.2 - .place()
# .place() is used to control the precise location that a widget should occupy in a window or frame by using a and y co-ordinates (measured in pixels, starting from the top left)
# 'label.place(x=25, y=50)'
# .place() is bad for many reasons: it can be obscured by the window's edge on some OSs, the layout can be difficulty to manage if you have many widgets and .place() is not responsive meaning that it will no change as the window is resized. 

# 6.3 - .grid()
# .grid() works by splitting a window or frame into rows and columns. You then specify the location of a widget by calling .grid() and passing the row and column. 
# You can add external and internal padding using 'padx' and 'pady' 
# '.columnconfigure()' and '.rowconfigure()' can be used to readjust the grid as the window is expanded. They use the three arguments: index, weight, minimum size
# Rather than using 'fill', like .pack(), .grid() uses 'sticky' which uses cardinal directions such as "ne" for North-East. "ns" to force the widget to fill the cell vertically. 

# Events
#----------

# 7.1 - .bind()
# Used to call an event handler when an event occurs on a widget
# 'window.bind("<Key>", handleKeypress)' binds the event "<Key>" to the event handler "handleKeypress". The event handler itself is bound to the window but this can be changed by replacing "window" with the variable name of a widget. For example, 'buttonOne.bind("<Key>", handle_keypress)'
# Events -> https://web.archive.org/web/20190512164300/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/event-types.html 

# 7.2 - 'command'
# The 'command' attribute for a button allows a function to be assigned to the button and called when it is clicked
# 'btn_decrease = tk.Button(master=window, text="-", command=decrease)' will call decrease() when the button is clicked


if __name__ == "__main__":
    window.mainloop()
    