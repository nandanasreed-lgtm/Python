'''

Step 1: Create a list L holding several integers and print it as the original list.

Step 2: Set a counter, count, to 0 to store the running sum.

Step 3: Loop through every element in L and add it to count.

Step 4: Divide count by len(L) to calculate the average, storing it in avg.

Step 5: Print the total sum and the average.

Step 6: Sort L in ascending order using L.sort().

Step 7: Print L[O] as the smallest element and L[-1] as the largest element.

'''
L = [2, 3, 4, 6, 8, 9, 12]
print("Originial list : ",L)
count = 0
for i in L:
    count += i
avg = count / len(L)
print("Total sum : ",count)
print("average : ",avg)
L.sort()
print("Smallest element : ",L[0])
print("Largest element : ",L[-1])