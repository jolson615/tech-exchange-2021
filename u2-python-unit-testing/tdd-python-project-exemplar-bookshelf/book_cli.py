from user import User
from bookshelf import Bookshelf
from book import Book

# Define cli class
class CLI:

    def __init__(self):
        # take username input
        thisUser = input("Enter a username: ")
        # create new user
        self.user = User(thisUser)
        # take shelfName input
        print(f"Welcome, {self.user.username}!")
        thisShelf = input("Name your book shelf: ")
        # create new shelf
        self.user.shelves.append(Bookshelf(thisShelf))
        print(f"Your shelf {self.user.shelves[0].shelfName} has been created")

    def addABook(self, shelfIndex):
        print(f"Add a book to {self.user.shelves[0].shelfName}")
        
        # gather book details
        thisTitle = input("Title: ")
        thisAuthor = input("Author: ")
        thisGenre = input("Genre: ")
        thisYear = input("Publication Year: ")
        thisYear = int(thisYear)
        thisRating = input("Your Rating [0-5]: ")
        thisRating = int(thisRating)

        # add book to current shelf
        thisBook = Book(thisTitle,thisAuthor,thisGenre,thisYear, thisRating)
        self.user.shelves[shelfIndex].addBook(thisBook)
        
        # prompt user to enter another book
        self.next()

    def next(self):
        prompt = input("Do you want to add another book? ")
        prompt = prompt.lower()
        if prompt == 'y' or prompt == 'yes':
            # call addBook again if the user wants to add another
            self.addABook(0)

    def showBooks(self, shelfIndex):
        print("Your shelf:")
        for i in range(0, len(self.user.shelves[shelfIndex].books)):
            thisBook = self.user.shelves[shelfIndex].books[i]
            print(f"{thisBook.title} is a {thisBook.publication} {thisBook.genre} book by {thisBook.author}.")

# Create a CLI instance
newCLI = CLI()

# Add books to instance
newCLI.addABook(0)

# Show books
newCLI.showBooks(0)