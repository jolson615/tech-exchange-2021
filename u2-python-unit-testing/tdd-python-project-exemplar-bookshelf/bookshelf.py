from book import Book
# Define bookshelf class
class Bookshelf:
    def __init__(self, shelfName:str):
        '''
        shelfName (str) is a user input for organizing multiple shelves
        shelves hold a list of books
        '''
        if (type(shelfName) is not str):
            raise TypeError("shelf name must be a string")
        self.shelfName = shelfName
        self.books = []

    def addBook(self, newBook):
        '''
        newBook(Book) is added to list of books on this shelf
        '''
        if (not isinstance(newBook, Book)):
            raise TypeError("new books must be instance of Book class")
        self.books.append(newBook)

    def removeBook(self, cutBook):
        '''
        cutBook(Book) is removed from the list of books on this shelf
        '''
        if (not isinstance(cutBook, Book)):
            raise TypeError("cut books must be instance of Book class")
        if (self.books.__contains__(cutBook)):
            self.books.remove(cutBook)


