# 1) Import `ABC` and `abstractmethod` from the `abc` module.

# (These are used to create abstract base classes.)

# 2) Create an abstract base class named `Animal` that inherits from `ABC`.

# 3) Inside `Animal`, define an abstract method `move(self)`:

# a) This method is meant to be implemented by all subclasses.

# b) Use `pass` as a placeholder because the base class does not define the actual behavior.

# 4) Create a subclass `Human` that inherits from `Animal`:

# a) Implement the `move()` method to print "I can walk and run".

# 5) Create a subclass `Snake` that inherits from `Animal`:

# a) Implement the `move()` method to print "I can crawl".

# 6) Create a subclass `Dog` that inherits from `Animal`:

# a) Implement the `move()` method to print "I can bark".

# 7) Create a subclass `Lion` that inherits from `Animal`:

# a) Implement the `move()` method to print "I can roar".

# 8) Create objects of each subclass and call their `move()` methods:

# a) Create `R = Human()` and call `R.move()`.

# b) Create `K = Snake()` and call `K.move()`.

# c) Create `R = Dog()` and call `R.move()`.

# d) Create `K = Lion()` and call `K.move()`.

# (Each object prints its own movement behavior due to method overriding.)
from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can roar")
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()