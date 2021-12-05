import unittest
from user import User, Bookshelf

# data for testing
testUser = User ("Annette")
testUser2 = User ("Ermias")
testBookshelf = Bookshelf("Michael's Picks")

#python3 -m unittest test_user
class TestUser(unittest.TestCase):

    def test_argument_types(self):
        # username must be string
        self.assertRaises(TypeError, User, 0)
        self.assertRaises(TypeError, User, None)

    def test_user_list(self):
        # assert that the test usera were added to the list of users
        self.assertEqual(len(User.users), 2)
        # assert that the test user is an instance of User class
        self.assertIsInstance(User.users[0], User)
        # assert that the usernames are correct and the user ids increment
        self.assertIs(User.users[0].username, "Annette")
        self.assertIs(User.users[0].userid, 1)
        self.assertIs(User.users[1].username, "Ermias")
        self.assertIs(User.users[1].userid, 2)

    def test_addShelf(self):
        # new book must be an instance of Bookshelf class
        self.assertRaises(TypeError, User.addShelf, self, "To Read")
        self.assertRaises(TypeError, User.addShelf, self, None)
        # method successfully updates the list of shelves
        testUser.addShelf(testBookshelf)
        # assert that list is correct length, shelf is type Bookshelf, and title is correct
        self.assertEqual(len(testUser.shelves), 1)
        self.assertIsInstance(testUser.shelves[0], Bookshelf)
        self.assertIs(testUser.shelves[0].shelfName, "Michael's Picks")

    def test_removeBook(self):
        # cut shelves must be an instance of Bookshelf class
        self.assertRaises(TypeError, User.removeShelf, self, "To Read")
        self.assertRaises(TypeError, User.removeShelf, self, None)
        # assert that list is correct length before removal
        self.assertEqual(len(testUser.shelves), 1)
        testUser.removeShelf(testBookshelf)
        # assert that list is correct length after removal
        self.assertEqual(len(testUser.shelves), 0)
