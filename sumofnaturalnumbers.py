# 1) Ask the user to enter the number of terms and store it in `n`.

# 2) Initialize `sum` to 0.

# (This will store the running total.)

# 3) Initialize `i` to 1.

# (This is the first number we will add.)

# 4) Repeat while `i` is less than or equal to `n`:

# a) Add `i` to `sum`.

# b) Increase `i` by 1 to move to the next number.

# 5) After the loop ends, print the final value of `sum`.
n = int(input("Enter the number of terms: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("sum of natural numbers",sum)