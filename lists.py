'''

Step 1: Create an empty list called empty_list and print a blank line.

Step 2: Create a list called numbers holding five integers and print it.

Step 3: Use the * operator to repeat [1, 2, 3] three times and store it in triples.

Step 4: Print the triples list.

Step 5: Create a list called aList holding five numbers.

Step 6: Reverse aList using slicing with [ ::- 1] and store it back into aList.

Step 7: Print the reversed aList.

'''
empty_list = []
print()
numbers = [1, 2, 3, 4, 5]
print(numbers)
triples = [1, 2, 3]*3
print(triples)
aList = [6, 7, 8, 9, 10]
aList = aList[ ::-1 ]
print(aList)