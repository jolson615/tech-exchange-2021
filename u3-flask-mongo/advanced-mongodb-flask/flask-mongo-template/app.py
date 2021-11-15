# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from seed_library import seed_books
from flask_pymongo import PyMongo
from model import genres

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = '<mongo-uri>'
#Initialize PyMongo
mongo = PyMongo(app)

# -- Session data --


# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')

# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    collection = mongo.db.library
    # collection.insert_many(seed_books)
    books = collection.find({})
    return render_template('index.html', books = books, genres = genres)

#SIGNUP Route

#LOGIN Route

#LOGOUT Route

#GENRE Variable Route
@app.route('/genre/<genre>')
def genre_view(genre):
    collection = mongo.db.library
    #find entries whose genre matches the slug
    books = collection.find({"genre":genre})
    genre = genre.capitalize()
    return render_template('index.html', books = books, genres = genres)

#BOOK Variable Route
@app.route('/book/<bookID>')
def book_view(bookID):
    collection = mongo.db.library
    #find a single entry by ObjectId
    book = collection.find_one({"_id":ObjectId(bookID)})
    return render_template('book.html', book = book)

# NEW BOOK Route
@app.route('/new', methods=['GET', 'POST'])
def new_book():
    if request.method == "GET":
        #render the form, with the genre list to populate the dropdown menu
        return render_template('new_book.html', genres = genres)
    else:
        #assign form data to variables
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        publication = request.form['publication']

        #retrieve username from session data if present
        if session:
            user = session['username']
        else:
            user = None

        collection = mongo.db.library
        
        #insert an entry to the database using the varibles declared above
        collection.insert_one({"title":title, "author":author, "genre":genre, "publication": publication, "user": user})

        #redirect to the index route upon form submission
        return redirect('/')
