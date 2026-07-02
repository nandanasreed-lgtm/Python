# write a program to create a function 'total_calc()' that helps us to calculate and print the total amount paid at a resturant, given amount and the percentage of the bill amount. You decide to pay as a tip.
def total_calc(bill_amount, tip_percent=5):
    tip = bill_amount*(tip_percent/100)
    total = bill_amount + tip
    print(f"Please pay ${total}")
total_calc(45)
total_calc(45, 10)