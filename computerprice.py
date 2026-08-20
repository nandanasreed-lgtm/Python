# 1) Create a class named `Computer`.

# 2) Define the constructor `__init__(self)`:

# a) Initialize a private instance variable `self.__maxprice = 900`.

# (Double underscore makes it private/name-mangled.)

# 3) Define a method `sell(self)`:

# a) Print the current selling price using `self.__maxprice`.

# 4) Define a setter method `setMaxPrice(self, price)`:

# a) Update the private variable `self.__maxprice` with the new value `price`.

# 5) Create an object `c` of the class `Computer`.

# 6) Call `c.sell()` to display the initial selling price (900).

# 7) Try to change the price directly using `c.__maxprice = 1000`:

# a) This does NOT update the private variable `self.__maxprice`.

# b) Instead, it creates a new attribute named `__maxprice` outside the class’s private one.

# 8) Call `c.sell()` again:

# a) It still prints 900 because the original private variable was not changed.

# 9) Update the price properly using the setter method:

# a) Call `c.setMaxPrice(1000)` to modify `self.__maxprice`.

# 10) Call `c.sell()` again:

# a) It now prints 1000 because the private variable was updated using the setter.
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print(f"selling price : {self.__maxprice}")
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
# print(c.__maxprice)
c.setMaxPrice(1000)
c.sell()