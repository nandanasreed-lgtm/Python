from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Text Editor")
window.geometry("600x500")
frame = Frame(window, bd= 2, relief= "raised")
frame.grid(row= 0, column= 0, sticky= "ns")
textbox = Text(window)
textbox.grid(row= 0, column= 1, sticky= "nsew")
def openfile():
    filepath = askopenfilename(filetypes= [("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    textbox.delete(1.0, END)
    with open(filepath, "r") as inputfile:
        text= inputfile.read()
        textbox.insert(END, text)
        inputfile.close()
    window.title(f"Text Editor - {filepath}")
btnopen = Button(frame, text= "open", command= openfile)
btnopen.grid(row= 0, column= 0, padx= 5, pady= 5)
def savefile():
    filepath = asksaveasfilename(defaultextension= "txt", filetypes= [("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    textbox.delete(1.0, END)
    with open(filepath, "w") as outputfile:
        text= textbox.get(1.0, END)
        outputfile.write(text)
        outputfile.close()
    window.title(f"Text Editor - {filepath}")
btnsave = Button(frame, text= "save", command= savefile)
btnsave.grid(row= 1, column= 0, padx= 5)
window.mainloop()