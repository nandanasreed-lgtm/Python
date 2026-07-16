price = int(input("Enter the price of the item: "))
if price < 100:
    print("The item is cheap.")
elif price >= 100 and price < 500:
    print("The item is moderately priced.")
elif price >= 500:
    print("The item is expensive.")
else:
    print("Invalid price entered.")
