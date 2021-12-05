from bookshelf import Bookshelf

# Define user class
class User:

    # static list of users
    users = []
    # iterable count of users to give each user a unique id
    idCounter = 1

    def __init__(self, username:str):
        '''
        username (str) identifies this user
        users have a list of shelves to organize their books
        users are given a unique id number
        users are added to a static list of users
        '''
        if (type(username) is not str):
            raise TypeError("username must be a string")
        self.username = username
        self.userid = User.idCounter
        User.users.append(self)
        User.idCounter += 1
        self.shelves = []

    def addShelf(self, newShelf):
        '''
        newShelf(Bookshelf) is added to list of shelves
        '''
        if (not isinstance(newShelf, Bookshelf)):
            raise TypeError("new shelves must be instance of Bookshelf class")
        self.shelves.append(newShelf)

    def removeShelf(self, cutShelf):
        '''
        cutShelf(Bookshelf) is removed from the list of shelves     
        '''
        if (not isinstance(cutShelf, Bookshelf)):
            raise TypeError("cut shelves must be instance of Bookshelf class")
        if (self.shelves.__contains__(cutShelf)):
            self.shelves.remove(cutShelf)
