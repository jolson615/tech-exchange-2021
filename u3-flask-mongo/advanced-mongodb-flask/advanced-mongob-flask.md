# Advanced MongoDB + Flask

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

### User Auth
User authentication can lead to some unique challenges in app development.  If users are entering a username and password, we need a way to secure that information in our database.  We'll be using a popular encryption tool called bcrypt to store user passwords in our databases.

## Objectives

* SW create a process for users to sign up for individual accounts
* SW add sessions to their Flask applications
* SW create a process for users to sign in and sign out of their application
* SW create a process for checking whether a certain user is logged in before providing access to a page which is unique to a specific user. 
* SW write flexible / variable routes in Flask
* SW hash user passwords before storing them

## Setup

Change directory (cd) into the 'flask-mongo-template' file

Type 'flask --version' in your terminal to confirm that flask is installed.  If it isn't, run 'pip3 install flask' to install flask.

Copy the following into your terminal to configure your flask app:

    export FLASK_APP=app.py
    export FLASK_DEBUG=1

Run 'flask run' to run your flask app.

Type 'control+c' to close a running flask app.

There are possible conflicts between PyMongo versions.  If students are unable to import their app, have them 'pip uninstall pymongo' then 'pip install flask-pymongo user'.

## Launch

We're continuing the Book Recommendation app created in the last lesson.  We'll be adding new functionality to our app by adding a user login and content that is responsive to the current user.  We'll also add the options for users to delete entries that they create.  This is the last step in developing a full-crud app: create, read, update, delete.

## The Lesson

### Variable Routes by ObjectID
The first advanced Flask/MongoDB technique we're going to work on is accessing individual database entries by objectID.  In order to access these, you'll need to install a library called bson.

Run: 'pip3 install bson'.

Once bson is installed, you can use the ObjectID() class to search for books by a specific id.  This is useful, because the id is unique to each database entry.  Create a route named:

    @app.route('/book/<bookID>')
    
This route will render a book.html template, providing a more detailed view of each individual book.

To allow the user to navigate to this book view, you will need to incorporate a link to this route in each entry of index.html: 

    <li><a href='/book/{{ book._id }}'>{{ book.title }}</a> by {{ book.author }

```python
# -- Import section --
from bson.objectid import ObjectId

# -- Routes section --
#BOOK Variable Route
@app.route('/book/<bookID>')
def book_view(bookID):
    collection = mongo.db.library
    #find a single entry by ObjectId
    book = collection.find_one({"_id":ObjectId(bookID)})
    return render_template('book.html', book = book)
```

```html
      <!-- index.html -->
      <div class="book-list">
        <ul>
          {% for book in books %}
            <li><a href='/book/{{ book._id }}'>{{ book.title }}</a> by {{ book.author }}</li>
          {% endfor %}
        </ul>
        
        <!-- book.html -->
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Book</title>
        </head>
        <body>
            <h2>{{ book.title }}</h2>
            <p>By {{ book.author }}</p>
            <p>First published in {{ book.publication }}</p>
            <p>Genre: {{ book.genre }}</p>
            <p><a href="/book/{{ book._id }}/add_image">Add An Image</a></p>
            <p><a href="/">Home</a></p>
        </body>
        </html>
```

#### Helpful Questions
* How does an entry's id differ from its other properties?
    It's not user-created, it requires bson to access in python, and it requires them notation ._id in Jinja. 
* How is the book view different from other templates?
    Most of the page content is variable based on the specific book.

### Updating Database Entries
Now that we have an individual book view, there is space to display images for each book.  Users can already create and read database entries.  This is a good opportunity to allow users to update entries.

Like creating a new entry, updating entries in Flask requires a POST method.  Create an add image route in app.py.  You'll need to extend the bookID route in order to specify which book is associated with this image:

    @app.route('/book/<bookID>/add_image', methods=['GET', 'POST'])

In book.html, create a conditional that shows users the image for entries that have an image property and an 'Add Image' button for entries that don't

```python
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

```

```html
    <!-- book.html -->
    {% if book.image %}
        <img src='{{ book.image }}'/>
    {% else %}
        <p><a href="/book/{{ book._id }}/add_image">Add An Image</a></p>
    {% endif %}
    
<!-- add_image.html -->    
<!DOCTYPE html>
   <html>
    <head>
        <title>Add Image</title>
    </head>
    <body>
        <h1>Upload and Image for {{ book.title }}</h1>
        <form method="post" action="/book/{{ book._id }}/add_image">
            <label for="url">Image Address URL:</label>
            <input type="text" name="url" value="">
          <input type="submit" value="Submit">
        </form>
        <p><a href="/book/{{ book._id }}">Cancel</a></p>
    </body>
</html>
```

#### Helpful Questions
* How is this similar to creating a new database entry?
    Both are put methods interacting with the database.
* How is this different from creating a new database entry?
    This uses .update_one() to update an existing database entry and "$set" to control which property is updated.

### New User Signup
The next advanced technique we're going to apply is allowing users to log in to the site.  This allows recommendations to be linked to a specific user.  In order to preserve the password privacy of our app's users, we're going to use password encryption and hashing.

To add password hashing, install bcrypt with: 'pip3 install bcrypt'.

To track whether a user is currently logged in, we're going to use session data.  Session data tracks information like usernames in the local storage of that user.  It's important for allowing information to persist even when a user refreshes a page or navigates away.

Accessing session data in Flask requires generating a secret key, which we can do by importing the built-in Python library 'secrets'.  The secrets library includes a method called .token_urlsafe(16) that generates safe tokens to prevent outside users from accessing your app's secret key (and therefore session data).

To create a user login, first create a signin route that can accept a username and password from a form, store it in the database, and log the new username in session data.

If the username is not already in use in the database, this route will add a new entry in the 'users' collection.  There are three steps to take before storing the new users password.  The first is to encode it with the .encode("utf-8") method.  Next, bcrypt generates a salt: a random string that will be used to make the hash unpredictable.  Finally, bcrypt uses the salt to hash the password into an encrypted version.  Once the password is hashed, the username and password are added to the database.

You can test this route by entering '/signup' in the navigation bar.  If the signup is successful, you should be able to view the new user on MongoDB.

```python
# -- Import section --
import secrets
# -- Session data --
app.secret_key = secrets.token_urlsafe(16)
# -- Routes section --
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
```

```html
<!-- signup.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
</head>
<body>
    <h1>Sign Up</h1>
    <form method="post" action="/signup">
    <label for="username">username:</label>
    <input type="text" name="username" value="">
    <label for="password">password:</label>
    <input type="password" name="password" value="">
    <input type="submit" value="Submit">
    </form>
    <p><a href="/">Cancel</a></p>
</body>
</html>

```

#### Helpful Questions
* What are the risks of not hashing passwords?
    User information could easily be hacked.  Users may not trust your site.
* Why does signup have both a get and post method?
    Get allows users to view the form.  Post allows them to send information to the database.

### User Login / Logout
Now that users can sign up for your app, the next step is to allow them to login and logout.  The login route will be very similar to the signup route, except that it will be compared to the password the user enters in the form to the hashed password stored in the database; if there is a match, the user is logged in.  This is performed with the method: bcrypt.checkpw()

Creating a logout route is simpler.  Because the login state is tracked in session storage, the user can be logged out by clearing their current session with the method session.clear()

It's not very user-friendly to have users type /login and /logout manually in their navigation bar.  You can provide a login/logout interface by using conditionals in your Jinja template.

    <!-- index.html -->
    {% if session %}
      <p>Logged in as {{ session['username'] }}</p>
      <a href='/logout'>Log Out</a>
    {% else %}
      <a href='/login'>Log In</a>
      <a href='/signup'>Sign Up</a>
    {% endif %}

Add your login and logout routes to app.py, then consider where on your html templates it would be useful to have conditional information based on your login state.

```python
# -- Routes section --
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
```

```html
<!-- login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log In</title>
</head>
<body>
    <h1>Log In</h1>
    <form method="post" action="/login">

      <label for="username">username:</label>
      <input type="text" name="username" value="">

      <label for="password">password:</label>
      <input type="password" name="password" value="">

      <input type="submit" value="Submit">
    </form>
    <p><a href="/">Cancel</a></p>
</body>
</html>

```

#### Helpful Questions
* What makes for a good login interface?
    Easy to find.  Personalized.  Always visible but not intrusive.
* What makes for a good login interface?
    Easy to find.  Personalized.  Always visible but not intrusive.

### User-specific Routes
Now that users can sign in to the Book Recommendation app, we can do more to personalize their experience.

Create a route named: @app.route('/mybooks')

If there is any session data, find all books in the database created by the current session user.  Render the template index.html.

Finally, add a link on index.html allowing users to view their own recommended books.

```python
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
    return render_template('index.html', books = books, genres = genres)

```
```html
    <!-- index.html -->
      {% if session %}
        <p>Logged in as {{ session['username'] }}</p>
        <a href='/mybooks'>My Books</a>
        <a href='/logout'>Log Out</a>
      {% else %}
        <a href='/login'>Log In</a>
        <a href='/signup'>Sign Up</a>
      {% endif %}

```

#### Helpful Questions
* How is this similar to sorting books by genre?
    Both use a specific query to limit the list of books passed to index.html
* How is this different from sorting books by genre?
    It uses session data rather than a variable route to specify a query.

## Extensions
* Create three users and have each recommend a book
* Add images for three books
* Style your book page in CSS
* Allow users to edit recommendations they created
* Allow users to delete recommendations they created

## Related Resources
* [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/) - Full PyMongo documentation
* [Flask Documentation URL Route Registration](https://flask.palletsprojects.com/en/2.0.x/api/#url-route-registrations) - Details on variable part routes
* [w3 Schools HTMl Forms](https://www.w3schools.com/html/html_forms.asp) - HTML Forms tutorial
* [bson](https://pymongo.readthedocs.io/en/stable/api/bson/index.html) - PyMongo bson documentation
* [bcrypt](https://pypi.org/project/bcrypt/) - bcrypt documentation
