class Library:
    def __init__(self):
        self.books = ["Demon Slayer", "Jujutsu Kaisen", "Spy X Family"]


    def borrow(self, book):
        if book in self.books:
           self.books.remove(book)
           print("Borrowed:", book)
        else:
            print("Not Available")



    def return_book(self, book):
        self.books.append(book)
        print("Returned:", book)



library = Library()
library.borrow("Python")                
library.return_book("Python") 
print(library.books)               
