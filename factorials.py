# write a program to find factorial of a given number using recursive function
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x - 1)
print("factorial of 3 is : ",factorial(3))

