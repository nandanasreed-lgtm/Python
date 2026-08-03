box1 = {"yogurt", "granola","apple", "apple"}
box2 = {"banana", "chocolate", "crisps", "chocolate"}
print("box 1 : ",box1)
print("box 2 : ",box2)
box1.add("crisps")
print("box 1 : ",box1)
common_snack = box1.intersection(box2)
print("common snack : ",common_snack)
import array as arr
snack_count = arr.array("i", [2, 4, 6])
print("snack count array : ",snack_count)
snack_count.insert(0, 3)
snack_count.append(7)
print("updated snack count array : ",snack_count)
print("count of 4 in snack count array : ",snack_count.count(4))
snack_count.reverse()
print("reversed snack count array : ", snack_count)
