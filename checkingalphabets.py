enteredvalue = str(input("Enter a character: "))

if (enteredvalue>= 'A' and enteredvalue<= 'Z') or (enteredvalue>= 'a' and enteredvalue<= 'z'):
    print("Entered character is an alphabet")
else:
    print("Entered character is not an alphabet")