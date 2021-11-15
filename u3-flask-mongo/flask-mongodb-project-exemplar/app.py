# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from seed_library import seed_books
from flask_pymongo import PyMongo
from model import genres
import secrets
from bson.objectid import ObjectId
import bcrypt

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://feedbackLoop:TestUserPassword1!@cluster0.0nsou.mongodb.net/database?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)

# -- Session data --
app.secret_key = secrets.token_urlsafe(16)

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
    return render_template('index.html', books = books, genres = genres,  label="All")

#SIGNUP Route
@app.route('/signup', methods=['GET', 'POST'])
def singup():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        existing_user = users.find_one({'name': request.form['username']})

        #if user not in database
        if not existing_user:
            username = request.form['username']
            #encode password for hashing
            password = (request.form['password']).encode("utf-8")
            #hash password
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password, salt)
            #add new user to database
            users.insert({'name': username, 'password': hashed})
            #store username in session
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        else:
            return 'Username already registered.  Try logging in.'
    
    else:
        return render_template('signup.html')

#LOGIN Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        login_user = users.find_one({'name': request.form['username']})

        #if username in database
        if login_user:
            db_password = login_user['password']
            #encode password
            password = request.form['password'].encode("utf-8")
            #compare username in database to username submitted in form
            if bcrypt.checkpw(password, db_password):
                #store username in session
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            else:
                return 'Invalid username/password combination.'
        else:
            return 'User not found.'
    else:
        return render_template('login.html')

#LOGOUT Route
@app.route('/logout')
def logout():
    #clear username from session data
    session.clear()
    return redirect('/')

#GENRE Variable Route
@app.route('/genre/<genre>')
def genre_view(genre):
    collection = mongo.db.library
    #find entries whose genre matches the slug
    books = collection.find({"genre":genre})
    genre = genre.capitalize()
    return render_template('index.html', books = books, genres = genres, label=genre)

#MYBOOKS Variable Route
@app.route('/mybooks')
def my_books():
    collection = mongo.db.library
    #retrieve username from session data if present
    if session:
        user = session['username']
    else:
        user = None
    #find entries whose user matches the session user
    books = collection.find({"user":user})
    return render_template('index.html', books = books, genres = genres, label="My")

#BOOK Variable Route
@app.route('/book/<bookID>')
def book_view(bookID):
    collection = mongo.db.library
    #find a single entry by ObjectId
    book = collection.find_one({"_id":ObjectId(bookID)})
    return render_template('book.html', book = book)

#DELETE Book Route
@app.route('/book/<bookID>/delete')
def delete(bookID):
    collection = mongo.db.library
    #find a single entry by ObjectId
    book = collection.find_one({"_id":ObjectId(bookID)})
    #delete entry
    collection.delete_one(book)
    return redirect('/')

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

# ADD IMAGE Route
@app.route('/book/<bookID>/add_image', methods=['GET', 'POST'])
def add_image(bookID):
    if request.method == "GET":
        collection = mongo.db.library
        #find a single entry by ObjectId
        book = collection.find_one({"_id":ObjectId(bookID)})
        #render the form, with the genre list to populate the dropdown menu
        return render_template('add_image.html', book = book)
    else:
        #assign form data to variable
        url = request.form['url']
        collection = mongo.db.library

        #set values to update
        book = {"_id":ObjectId(bookID)}
        newvalues = { "$set": { "image": url } }

        #update this book with the new values
        collection.update_one(book, newvalues)

        #redirect to the index route upon form submission
        return redirect('/book/'+bookID)