class Dog:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age
bluey = Dog("Bluey", 7)
bingo = Dog("Bingo", 5)
print("Bluey is a : ",bluey.species)
print("Bingo is a : ",bingo.species)
print(f"{bluey.name} is {bluey.age} years old")
print(f"{bingo.name} is {bingo.age} years old")
