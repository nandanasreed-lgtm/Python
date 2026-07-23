# 1) Create a tuple `tuplex` containing different data types (string, boolean, float, integer)

# and print the tuple.

# 2) Create another tuple `tuplex` containing only integer values and print it.

# 3) Demonstrate tuple immutability:

# a) Tuples cannot be modified directly (cannot add/change elements in the same tuple).

# b) Use the `+` operator to merge tuples and create a new tuple.

# c) Add a single element (9) using `(9,)` and store the new tuple back in `tuplex`.

# d) Print the updated tuple.

# 4) Create a tuple `tuple1` and count occurrences of a specific value:

# a) Use `tuple1.count(50)` to count how many times 50 appears.

# b) Print the count.

# 5) Create a tuple `tuplex` with multiple integers to demonstrate slicing.

# 6) Slice a portion of the tuple using indexing:

# a) Use `tuplex[3:5]` to get elements from index 3 up to index 4 (stop index is excluded).

# b) Store it in `_slice` and print it.

# 7) Slice from the beginning when the start index is not provided:

# a) Use `tuplex[:6]` to get elements from index 0 up to index 5.

# b) Store it in `_slice` and print it.
tuplex = ("apple", 5, 2.35, False)
print(tuplex)
tuplex = (1, 2, 3, 4, 5)
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)
tuple1 = (1, 2, 3, 4, 5, 5)
print(tuple1.count(5))
tuplex = (2, 4, 6, 8, 10, 12, 14)
_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)
