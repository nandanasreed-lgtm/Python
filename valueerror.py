#write a program to understnad how the value error exception works.
try:
    num = int(input("Enter a number: "))
    print("Number entered is: ",num)
except ValueError as e:
    print("Exception: ",e)
    