def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
try:
    op = input("Choose your operation(+, -, *, /): ")
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
except ZeroDivisionError:
    print("Division by 0: second num cannot be 0")
except ValueError:
    print("Value invalid")
else:
    if op == "+":
        print("result: ",add(num1, num2))
    elif op == "-":
        print("result: ",subtract(num1, num2))
    elif op == "*":
        print("result: ",multiply(num1, num2))
    elif op == "/":
        print("result: ",divide(num1, num2))
    else:
        print("Invalid operator")



    



