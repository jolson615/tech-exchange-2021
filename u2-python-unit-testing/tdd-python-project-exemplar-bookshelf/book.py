# Define book class
class Book:
    def __init__(self, title:str, author:str, genre:str, publication:int, rating:int):
        '''
        name, author, genre are strings
        publication (int) is a four digit year
        rating (int) must be between 0 and 5
        '''
        if (type(title) is not str) or (type(author) is not str) or (type(genre) is not str):
            raise TypeError("title, author, and genre must be strings")
        if (type(rating) is not int) or (type(publication) is not int):
            raise TypeError("publication and rating must be integers")
        if (rating<0) or (rating>5):
            raise ValueError("rating must be between 0 and 5")
        if (publication<1000) or (publication>3000):
            raise ValueError("publication must be a valid year")
        self.title = title
        self.author = author
        self.genre = genre
        self.publication = publication
        self.rating = rating

    def updateRating(self, newRating):
        '''
        newRating (int) must be between 0 and 5
        If valid, update the user rating
        '''
        if (type(newRating) is not int):
            raise TypeError("rating must be an integer")
        if (newRating<0) or (newRating>5):
            raise ValueError("rating must be between 0 and 5")
        self.rating = newRating