from tkinter import *
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")
        self.menu_items = {"Fries Meal": 2, "Lunch Meal": 2.50, "Burger Meal": 3.20, "Pizza Meal": 3.99, "Wrap Meal": 2.60, "Drinks": 1}
        self.exchangerate = 127
       # self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx= 0.5, rely= 0.5, anchor= "center")
        ttk.Label(frame, text= "Restaurant Order Management", font= ("Arial", 20, "bold")).grid(row= 0, column= 0, columnspan= 3, padx= 10, pady= 10)
        self.menulabel = {}
        self.menuquantity = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start= 1):
            label = ttk.Label(frame, text= f"{item} (£{price})", font= ("Arial", 12))
            label.grid(row= i, column= 0, padx= 10, pady= 5)
            self.menulabel[item] = label
            quantity_entry = ttk.Entry(frame, width= 5)
            quantity_entry.grid(row= i, column= 1, padx= 10, pady= 5)
            self.menuquantity[item] = quantity_entry
        self.currencyvar = StringVar()
        ttk.Label(frame, text= "Currency: ", font=("Arial", 12)).grid(row= len(self.menu_items) +1, column= 0, padx= 10, pady= 5)
        currencydropdown = ttk.Combobox(frame, textvariable= self.currencyvar, state= "read only", width= 18, values= ["EUR", "INR"])
        currencydropdown.grid(row= len(self.menu_items) +1, column= 1, padx= 10, pady= 10)
        orderbutton = ttk.Button(frame, text= "Place Order", command= self.placeorder)
        orderbutton.grid(row= len(self.menu_items) +2, columnspan= 3, padx= 10, pady= 10)
    def placeorder(self):
        totalcost = 0
        ordersummary = "Order Summary: \n"
        currency = self.currencyvar.get()
        symbol = "₹" if currency == "INR" else "£"
        rate = self.exchangerate if currency == "INR" else 1
        for item, entry in self.menuquantity.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                totalcost += cost
                if quantity > 0:
                    ordersummary += f"{item} : {quantity} x {symbol}{price} = {symbol}{cost} \n"
        if totalcost > 0:
            ordersummary += f"\nTotal Cost : {symbol}{totalcost}"
            messagebox.showinfo("Order Placed", ordersummary)
        else:
            messagebox.showerror("Error", "Please order atleast one item")

window = Tk()
app = RestaurantOrderManagement(window)
window.mainloop()