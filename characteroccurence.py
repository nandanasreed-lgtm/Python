# 1) Ask the user to enter a word and store it in `string`.

# 2) Ask the user to enter a single character and store it in `char`.

# 3) Set `i` to 0.

# (This will be used as the index to move through the string.)

# 4) Set `count` to 0.

# (This will store how many times `char` appears.)

# 5) While `i` is less than the length of `string`:

# a) Check if the character at position `i` in `string` is equal to `char`.

# b) If yes, increase `count` by 1.

# c) Increase `i` by 1 to move to the next character.

# 6) After the loop, print how many times `char` occurred in `string` using `count`.
string = input("Enter a word: ")
char = input("Enter single character: ")
i = 0
count = 0
while i < len(string):
    if string[i] == char:
        count += 1
    i += 1
print(f"The total number of times {char} has occured = {count}")
