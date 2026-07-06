# 1) Take a word input from the user and store it in `a`.

# 2) Use a `for` loop to iterate through each character `i` in the word `a`.

# 3) For each character, check if it is equal to 'A':

# a) If `i == 'A'`, print "A is found".

# b) Use `break` to stop the loop immediately after finding 'A'.

# 4) If the current character is not 'A', print "A not found".

# (This message prints for each character until 'A' is found or the loop ends
a = input("Enter a word: ")
for i in a:
    if i == "a":
        print("a is found.")
        break
    print("a is not found.")