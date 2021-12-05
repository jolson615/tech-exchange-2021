import unittest
from book import Book

# data for tests
testAuthor = "Jeff VanderMeer"
testTitle = "Annihilation"
testGenre = "Sci-fi"
testYear = 2014
testRating = 5

#python3 -m unittest test_book
class TestBook(unittest.TestCase):

    def test_argument_values(self):
        # rating must be an int between 0 and 5
        self.assertRaises(ValueError, Book, testAuthor, testTitle, testGenre, testYear, -1)
        self.assertRaises(ValueError, Book, testAuthor, testTitle, testGenre, testYear, 6)
        # publication must be an int between 1000 and 2000
        self.assertRaises(ValueError, Book, testAuthor, testTitle, testGenre, 999, testRating)
        self.assertRaises(ValueError, Book, testAuthor, testTitle, testGenre, 3001, testRating)

    def test_argument_types(self):
        # title, author, and genre must be strings
        self.assertRaises(TypeError, Book, 0, testTitle, testGenre, testYear, testRating)
        self.assertRaises(TypeError, Book, testAuthor, 0, testGenre, testYear, testRating)
        self.assertRaises(TypeError, Book, testAuthor, testTitle, 0, testYear, testRating)
        # rating must be an int
        self.assertRaises(TypeError, Book, testAuthor, testTitle, testGenre, testYear, 2.5)
        self.assertRaises(TypeError, Book, testAuthor, testTitle, testGenre, testYear, "5")
        # publication must be an int
        self.assertRaises(TypeError, Book, testAuthor, testTitle, testGenre, 20.14, testRating)
        self.assertRaises(TypeError, Book, testAuthor, testTitle, testGenre, "2014", testRating)

    def test_updateRating(self):
        # rating must be an int
        self.assertRaises(TypeError, Book.updateRating, self, 2.5)
        self.assertRaises(TypeError, Book.updateRating, self, "5")
        # rating must be an int between 0 and 5
        self.assertRaises(ValueError, Book.updateRating, self, -1)
        self.assertRaises(ValueError, Book.updateRating, self, 6)
        # method successfully updates the rating property
        testBook = Book(testTitle, testAuthor, testGenre, testYear, testRating)
        testBook.updateRating(3)
        self.assertEqual(testBook.rating, 3)
