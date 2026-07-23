# 1) Create a tuple `weather` containing 7 values (one for each day of the week).

# Here, 1 represents sunny weather and 0 represents rainy weather.

# 2) Initialize two counters:

# a) `sunny = 0` to count sunny days

# b) `rainy = 0` to count rainy days

# 3) Use a `for` loop to iterate through the 7 days (index 0 to 6):

# a) Check the value at `weather[i]`

# b) If it is 0, increase `rainy` by 1

# c) Otherwise, increase `sunny` by 1

# 4) After counting, compare the number of sunny days and rainy days:

# a) If `sunny > rainy`, print "Good weather"

# b) Else, print "Bad weather"
weather = (0, 1, 1, 1, 0, 0, 1)
sunny = 0
rainy = 0
for i in range(0, 7):
    if weather[i] == 0:
        rainy += 1
    else:
        sunny += 1
if sunny > rainy:
    print("Good weather")
else:
    print("Bad weather")