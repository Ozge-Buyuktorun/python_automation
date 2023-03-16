class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
         return f"Bookshelf with {len(self.books)} books."

shelf = BookShelf(300)

class Book(BookShelf):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    
book = Book("Harry Potter")
book2 = Book("Python 101")
book3 = Book("Python 2574")
shelf = BookShelf(book, book2, book3)

print(shelf)