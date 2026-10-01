from tkinter import *
from datetime import date
dt = date.today()
window = Tk()
window.title("Getting started with widgets")
window.geometry("300x300")
lbl = Label(window, text= "hello", bg= "blue", fg= "white", height= 1, width= 300)
lbl.pack()
namelbl = Label(window, text= "Enter full name : ")
namelbl.pack()
name_entry = Entry(window)
name_entry.pack()
def start():
    name = name_entry.get()
    message = "Welcome to the application\n"
    greet = "Hello " + name + "\n"
    txt.insert(END, greet)
    txt.insert(END, message)
    txt.insert(END, f"Today's date : {dt}")
btn = Button(window, text= "Start", command= start)
btn.pack()
txt = Text(window, height= 3)
txt.pack()
window.mainloop()