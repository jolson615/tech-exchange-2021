# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from seed_library import seed_books
from flask_pymongo import PyMongo
from model import genres

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://feedbackLoop:TestUserPassword1!@cluster0.0nsou.mongodb.net/database?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)

# Comment out this create_collection method after you run the app for the first time
# mongo.db.create_collection('library')

# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    books = []
    return render_template('index.html', books = books)


# NEW BOOK Route
@app.route('/new')
def new_book():
    return render_template('new_book.html', genres = genres)

