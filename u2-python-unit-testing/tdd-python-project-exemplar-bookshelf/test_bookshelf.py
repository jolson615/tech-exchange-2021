import unittest
from bookshelf import Bookshelf, Book

# data for testing
testBookshelf = Bookshelf("Michael's Picks")
testBook = Book("Annihilation", "Jeff VanderMeer", "Sci-fi", 2014, 5)

#python3 -m unittest test_bookshelf
class TestBookshelf(unittest.TestCase):
    # data for testing
    testBookshelf = Bookshelf("Michael's Picks")
    testBook = Book("Annihilation", "Jeff VanderMeer", "Sci-fi", 2014, 5)

    def test_argument_types(self):
        # shelf name must be string
        self.assertRaises(TypeError, Bookshelf, 0)
        self.assertRaises(TypeError, Bookshelf, None)

    def test_addBook(self):
        # new book must be an instance of Book class
        self.assertRaises(TypeError, Bookshelf.addBook, self, "Annihilation")
        self.assertRaises(TypeError, Bookshelf.addBook, self, None)
        # method successfully updates the list of books
        testBookshelf.addBook(testBook)
        # assert that list is correct length, book is type Book, and book title is correct
        self.assertEqual(len(testBookshelf.books), 1)
        self.assertIsInstance(testBookshelf.books[0], Book)
        self.assertIs(testBookshelf.books[0].title, "Annihilation")

    def test_removeBook(self):
        # cut book must be an instance of Book class
        self.assertRaises(TypeError, Bookshelf.removeBook, self, "Annihilation")
        self.assertRaises(TypeError, Bookshelf.removeBook, self, None)
        # assert that list is correct length before removal
        self.assertEqual(len(testBookshelf.books), 1)
        testBookshelf.removeBook(testBook)
        # assert that list is correct length after removal
        self.assertEqual(len(testBookshelf.books), 0)
