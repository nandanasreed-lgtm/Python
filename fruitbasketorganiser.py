"""

1) Create fruit baskets using sets.

a) Create `basket1` with different fruit names.

b) Create `basket2` with another group of fruits.

c) Use sets to automatically remove duplicate fruits.

2) Display both baskets.

a) Print the fruits in basket1.

b) Print the fruits in basket2.

3) Add a new fruit to a set.

a) Use `add()` to add orange to basket1.

b) Print basket1 after adding the new fruit.

4) Find common fruits.

a) Use `intersection()` to find fruits present in both baskets.

b) Store the result in `common_fruits`.

c) Print the shared fruits.

5) Create an array of fruit counts.

a) Import the `array` module as `arr`.

b) Create an integer array using `arr.array('i', [...])`.

c) Store fruit count values inside the array.

6) Add items to the array.

a) Use `insert()` to add a value at the beginning.

b) Use `append()` to add a value at the end.

c) Print the updated array.

7) Count and reverse array values.

a) Use `count()` to check how many times 4 appears.

b) Use `reverse()` to reverse the order of the array.

c) Print the count and reversed array.

8) Print the final summary.

a) Print the class fruit basket organizer heading.

b) Display both baskets, shared fruits, and fruit counts.

c) Print a closing line to complete the summary.

"""
basket1 = {"strawberry", "papaya", "coconut", "coconut"}
basket2 = {"blueberry", "banana", "watermelon", "banana"}
print("basket 1 : ",basket1)
print("basket 2 : ",basket2)
basket1.add("banana")
print("basket 1 : ",basket1)
common_fruit = basket1.intersection(basket2)
print("common fruit : ",common_fruit)
import array as arr
fruit_count = arr.array("i", [1, 2, 3])
print("fruit count array : ",fruit_count)
fruit_count.insert(0, 5)
fruit_count.append(8)
print("updated fruit count array : ",fruit_count)
print("count of 3 in fruit count array : ",fruit_count.count(3))
fruit_count.reverse()
print("reversed fruit count array : ",fruit_count)
