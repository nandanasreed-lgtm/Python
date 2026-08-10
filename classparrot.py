# 1) Create a class named `Parrot`.

# 2) Define a class attribute `species = "bird"`.

# (This attribute is shared by all objects of the class.)

# 3) Define the constructor method `__init__(self, name, age)`:

# a) This method runs when a new object is created.

# b) It takes two inputs: `name` and `age`.

# c) Store these values using instance attributes:

# - `self.name = name`

# - `self.age = age`

# 4) Create (instantiate) two objects of the `Parrot` class:

# a) `blu = Parrot("Blu", 10)`

# b) `woo = Parrot("Woo", 15)`

# 5) Access and print the class attribute `species` using both objects:

# a) Print that Blu is a bird.

# b) Print that Woo is also a bird.

# 6) Access and print the instance attributes (`name` and `age`) for each object:

# a) Print Blu’s name and age.

# b) Print Woo’s name and age.
class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print("Blu is a : ",blu.species)
print("Woo is a : ",woo.species)
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")