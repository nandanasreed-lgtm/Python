n = int(input("Enter a digit number: "))
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10
    print(f"The digits of the number in reverse order are: {digit} ")
    

