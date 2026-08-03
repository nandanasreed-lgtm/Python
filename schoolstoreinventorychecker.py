"""

1) Create store item data.

a) Create a list named `items` to store item names.

b) Create a list named `stock_counts` to store stock quantity for each item.

2) Build the inventory dictionary.

a) Use `zip()` to pair each item with its stock count.

b) Use dictionary comprehension to create `inventory`.

c) Print the full inventory.

3) Filter items that are in stock.

a) Use list comprehension to check each item.

b) Keep only items whose stock count is greater than 0.

c) Print the available items.

4) Ask the shopper for an item.

a) Use `input()` to ask which item the shopper wants to buy.

b) Store the answer in `chosen_item`.

5) Check stock availability.

a) Check if the item is not in the inventory.

b) Check if the item stock is 0.

c) Print an out-of-stock message.

d) Use `exit()` to stop the program early.

6) Create prices and markup.

a) Create a list named `prices`.

b) Ask the user to enter a markup amount.

c) Convert the markup input into an integer.

7) Apply markup using `map()`.

a) Use `map()` to update every price.

b) Use a lambda function to add the markup.

c) Convert the result into a list.

d) Print the marked-up prices.

8) Find the selected item price.

a) Use `items.index()` to find the chosen item's position.

b) Use the same index to get the marked-up price.

c) Print the final price of the chosen item.

9) Update the inventory.

a) Reduce the chosen item's stock count by 1.

b) Print the remaining stock after purchase.

10) Print the final store summary.

a) Print the school store inventory checker heading.

b) Show the item bought and price paid.

c) Show the updated inventory.

d) Print a closing line to complete the summary.

"""
items = ["pencils", "eraser", "notebook", "sharpner", "glue"]
stock_counts = [5, 2, 0, 4, 3]
inventory = {item : count for item, count in zip(items, stock_counts)}
print("full inventory : ",inventory)
in_stock = [i for i in items if inventory[i] > 0]
print("items in stock : ",in_stock)
chosen_item = input("which item do you want to buy? : ")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock")
    exit()
price = [3, 1, 5, 2, 4]
markup = int(input("enter the markup amount to add for every price : "))
markup_price = list(map(lambda p: p + markup, price))
print("markup prices : ",markup_price)
item_index = items.index(chosen_item)
chosen_price = markup_price[item_index]
print(f"price of {chosen_item} after markup : {chosen_price}")
inventory[chosen_item] = inventory[chosen_item] -1
print(chosen_item, "purchased. Remaining stock : ",inventory[chosen_item])
print("school store inventory checker")
print("item bought : ",chosen_item)
print("price paid : ",chosen_price)
print("updated inventory : ",inventory)
