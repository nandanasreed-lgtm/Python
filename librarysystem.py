#1.  Book class      →  __init__ sets title, author, and is_borrowed = False
#2.  borrow()        →  sets is_borrowed to True and prints a confirmation
#3.  return_book()   →  sets is_borrowed to False and prints a confirmation
#4.  3 Book objects  →  demonstrate both borrow() and return_book()
#5.  self            →  used to access and update attributes inside methods

#1.  Book class with __init__ setting title, author, is_borrowed   →   5 marks
#2.  borrow() sets is_borrowed True and prints confirmation         →  10 marks
#3.  return_book() sets is_borrowed False and prints confirmation   →  10 marks
#4.  At least 3 Book objects with both methods demonstrated         →  10 marks
#5.  Program runs without any errors                                →   5 marks
class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        self.is_borrowed = True
        print(self.title, "by", self.author, "has been borrowed")
    def return_book(self):
        self.is_borrowed = False
        print(self.title, "by", self.author, "has been returned")
book1 = Book("Dungeons and Dragons", "Gary Gygax")
book2 = Book("Game of Thrones", "George R.R. Martin")
book3 = Book("The Hunger Games", "Suzanne Collins")
book1.borrow()
book2.borrow()
book3.borrow()
book1.return_book()
book2.return_book()
book3.return_book()



        