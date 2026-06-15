# 1) Set `i` to 0.

# 2) Start a loop that keeps running as long as `i` is less than or equal to 0.

# 3) Inside the loop, print: "I WILL RUN FOREVER"

# 4) Notice: `i` is never changed inside the loop.

# That means `i` stays 0 forever, so the condition (i <= 0) stays true forever.

# So the loop never stops (infinite loop).
i = 0
while i <= 0:
    print("I WILL RUN FOREVER")
    