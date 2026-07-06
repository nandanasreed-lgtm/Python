# 1) Use a `for` loop to iterate `x` from 0 to 9 using `range(10)`.

# 2) For each value of `x`, check conditions in order:

# 3) If `x % 20 == 0`, print "twist".

# (This is true when `x` is divisible by 20.)

# 4) Else if `x % 15 == 0`, do nothing using `pass`.

# (This is true when `x` is divisible by 15, but no output is required.)

# 5) Else if `x % 5 == 0`, print "fizz".

# (This is true when `x` is divisible by 5.)

# 6) Else if `x % 3 == 0`, print "buzz".

# (This is true when `x` is divisible by 3.)

# 7) Else, if none of the above conditions match, print the value of `x`.
for x in range(10):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print(x)
    
    