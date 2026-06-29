# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
def add(p, q):
    return p + q
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
def subtract(p, q):
    return p - q
# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
def multiply(p, q):
    return p * q
# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
def divide(p, q):
    return p / q
# 5) Display a menu to the user showing the available operations:

# a) Add

# b) Subtract

# c) Multiply

# d) Divide
print("Select from the given operations: ")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
# 6) Take the user's choice as input and store it in `choice`.
choice = int(input("Enter your choice: "))
# 7) Take two integer inputs from the user:

# a) Store the first number in `num_1`

# b) Store the second number in `num_2`
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
# 8) Use conditional statements to perform the chosen operation:

# a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.

# b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.

# c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.

# d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.

# 9) If the user enters anything other than a/b/c/d, print an invalid input message.
if choice == 1:
    result = add(num1, num2)
    print("Sum is: ",result)
elif choice == 2:
    result = subtract(num1, num2)
    print("Difference is: ",result)
elif choice == 3:
    result = multiply(num1, num2)
    print("Product is: ",result)
elif choice == 4:
    result = divide(num1, num2)
    print("quotient is: ",result)
else:
    print("Invalid operator")