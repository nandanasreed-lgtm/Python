ac=int(input("Actual Cost : "))
sc=int(input("Selling Cost : "))
if sc>ac:
    p=sc-ac
    print("Profit made of: ",p)
else:
    l=ac-sc
    print("Loss made of: ",l)

