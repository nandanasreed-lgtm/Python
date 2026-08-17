"""

1) Create the parent class.

a) Create a class named `FamilyMember`.

b) Use `__init__()` to store shared traits like eye colour and height.

c) Store the values using `self`.

2) Add a parent class method.

a) Create `show_traits()` inside `FamilyMember`.

b) Print the eye colour.

c) Print the height in centimetres.

3) Create the child class.

a) Create a class named `Kid`.

b) Inherit from `FamilyMember`.

c) Allow the child class to use the parent class features.

4) Add child class details.

a) Create `__init__()` inside the `Kid` class.

b) Store the kid's name and age.

c) Use `super().__init__()` to call the parent class constructor.

d) Pass eye colour and height to the parent class.

5) Override the parent method.

a) Create another `show_traits()` method inside `Kid`.

b) Print the kid's name and age.

c) Use `super().show_traits()` to also show inherited traits.

6) Add a new child class method.

a) Create `favorite_hobby()`.

b) Take a hobby as input.

c) Print the kid's favourite hobby.

7) Create an object.

a) Create a `Kid` object named `child`.

b) Add values for name, age, eye colour, and height.

8) Call the methods.

a) Use `child.show_traits()` to display all details.

b) Use `child.favorite_hobby()` to display the hobby.

9) Check inheritance.

a) Use `issubclass()` to check if `Kid` is a subclass of `FamilyMember`.

b) Print the result.

"""
class FamilyMember:
    def __init__(self, eyecolour, height):
        self.eyecolour = eyecolour
        self.height = height
    def show_traits(self):
        print("eye colour : ",self.eyecolour)
        print("height in centimeters : ",self.height)
class Kid(FamilyMember):
    def __init__(self, name, age, eyecolour, height):
        self.name = name
        self.age = age
        super().__init__(eyecolour, height)
    def show_traits(self):
        print("name : ",self.name)
        print("age : ",self.age)
        super().show_traits()
    def favorite_hobby(self, hobby):
        print(self.name ,"loves", hobby)
child = Kid("Jimmy", 8, "brown", 150)
child.show_traits()
child.favorite_hobby("crafting")
print(issubclass(Kid, FamilyMember))

