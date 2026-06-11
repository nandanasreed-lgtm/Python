# 1) Ask the user to enter a word or sentence and store it in `string`.

# 2) Create an empty string called `string2`.

# (This will store the reversed version.)

# 3) Loop through each character `i` in `string`:

# - Add the character `i` in front of `string2`

# - This builds the reversed string step by step.

# 4) Print the original string (`string`).

# 5) Print the reversed string (`string2`).
word = input("Enter a word or sentence: ")
string2 = ""
for i in word:
    string2 = i+string2
print("original string: ",word)
print("reverse string: ",string2)