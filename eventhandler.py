# 1) Import everything from `tkinter` to create the GUI.

# 2) Create the main window using `window = Tk()`.

# 3) Set window properties:

# a) Set the title to "Event Handler".

# b) Set the window size to 100x100.

# 4) Define a function `handle_keypress(event)` to handle keyboard events:

# a) This function receives an `event` object automatically.

# b) Print `event.char` to show which key/character was pressed.

# 5) Bind the keypress event to the window:

# a) Use `window.bind("<Key>", handle_keypress)` so every key press triggers the function.

# 6) Define a function `handle_click(event)` to handle button click events:

# a) This function also receives an `event` object automatically.

# b) Print a message when the button is clicked.

# 7) Create a Button widget with the text "Click me!" and display it using `pack()`.

# 8) Bind the left mouse click event to the button:

# a) Use `button.bind("<Button-1>", handle_click)` so left-click triggers the function.

# 9) Start the GUI event loop using `window.mainloop()`

# so the window stays open and responds to user actions.
from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\n The button was clicked")
button = Button(text= "click me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()