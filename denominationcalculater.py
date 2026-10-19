from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title("Denomination Calculater")
window.geometry("650x400")
window.config(bg= "light blue")
image = ImageTk.PhotoImage(Image.open("app_img.jpg").resize((300, 300)))
lbl = Label(window, image= image, bg= "light blue")
lbl.place(x= 180, y= 20)
lbl1 = Label(window, text= "welcome to the denomination counter application.", bg= "light blue")
lbl1.place(relx= 0.5, y= 340, anchor= "center")
def msg():
    msgbox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if msgbox == "ok":
        topwin()
btn = Button(window, text= "lets get started.", command= msg, bg= "brown", fg= "white")
btn.place(x= 260, y= 360)
def topwin():
    top = Toplevel()
    top.title("Denomination Counter")
    top.geometry("600x350")
    lb = Label(top, text= "Enter total amount:")
    lb.place(x= 230, y= 50)
    entry = Entry(top)
    entry.place(x= 220, y= 80)
    def calculater():
        try:
            amount = int(entry.get())
            note2k = amount//2000
            amount %= 2000
            note500 = amount//500
            amount %= 500
            note100 = amount//100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2k))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("error", "please enter a valid number")
    btn = Button(top, text= "calculate", bg= "brown", fg= "white", command= calculater)
    btn.place(x= 240, y= 120)
    lb1 = Label(top, text= "here are numbers of notes for each denomination:")
    lb1.place(x= 140, y= 170)
    l1 = Label(top, text= "2000")
    l1.place(x= 180, y= 200)
    t1 = Entry(top)
    t1.place(x= 270, y= 200)
    l2 = Label(top, text= "500")
    l2.place(x= 180, y= 230)
    t2 = Entry(top)
    t2.place(x= 270, y= 230)
    l3 = Label(top, text= "100")
    l3.place(x= 180, y= 260)
    t3 = Entry(top)
    t3.place(x= 270, y= 260)
window.mainloop()