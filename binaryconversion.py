def binary_conversion(n):
    if n == 0:
        return"0"
    Binary = ""
    while n > 0:
        Binary = str(n % 2) + Binary
        n = n // 2
    return Binary
n = int(input("Enter a decimal number: "))
print("Binary representation of", n, "is", binary_conversion(n))
