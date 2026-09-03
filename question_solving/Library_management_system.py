class Library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def addBooks(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)
    def showsBooks(self):
            print(f"The no of books in library is {self.no_of_books}.")
            for book in self.books:
                print(book)

l=Library()
l.addBooks("Harry Potter1")
l.addBooks("Harry Potter2")
l.addBooks("Harry Potter3")
l.addBooks("Harry Potter4")
l.showsBooks()

