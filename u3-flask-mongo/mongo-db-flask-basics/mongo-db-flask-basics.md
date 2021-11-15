# MongoDB + Flask Basics

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

### Full Stack Development
This is our first project combining MongoDB and Flask for a full stack application.  This is an exciting day, and it's worth emphasizing what an accomplishment this is.  That said, there are also a few technical hurdles students could face.  Students may get stuck on getting their connection uri to MongoDB.  They may also have difficulty with installing the required libraries for python control of MongoDB.  Plan to spend some time troubleshooting these issues and have students support each other where possible.

## Objectives

* SW create a database for a specific purpose within a Flask application
* SW read from and write to a database.
* SW render data from individual mongoDB records as part of a flask template.
* SW render a list of items from MongoDB use a for loop inside a Flask template. 

## Setup

Change directory (cd) into the 'flask-mongo-template' file

Type 'flask --version' in your terminal to confirm that flask is installed.  If it isn't, run 'pip3 install flask' to install flask.

Copy the following into your terminal to configure your flask app:

    export FLASK_APP=app.py
    export FLASK_DEBUG=1

Run 'flask run' to run your flask app.

Type 'control+c' to close a running flask app.

## Launch

Today we're going to create a full-stack book recommendation app.  We're going to combine the Flask and MongoDB skills we've been developing to create an app that allows users to search for book recommendations by genre, and add their own suggestions to the database.  This process of user interaction with a database is called crud: create, read, update, delete.  Today we're focused just on creating / reading database entries.  We'll get into updating and deleting in the next lesson.

## The Lesson

### Connecting Flask and MongoDB
Open the file seed_library.py.  This contains a list of dictionaries, each representing a book.  This is our starting database.  We could add books to it, but only users on our device could add new entries.  We want to make an app that will allow anyone who visits our site to add entries to the database.

To do that, we'll need to connect our Flask app to MongoDB.

Open app.py and uncomment 'from flask_pymongo import PyMongo'.  This likely raises an error, as you don't have flask_pymoongo installed in your workspace to resolve this, run the following in your terminal:

    pip3 install flask-pymongo  --user
    pip3 install dnspython --user

Next, we'll need to configure the Flask app.  Replace <your-connection-string> with your Mongo URI (from mongodb.com > Databases > Connect > Connect your application).

Now run your app using 'flask run'.  If your database is connected, you will see a new collection in your database on mongodb.com

```python
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
app.config['MONGO_URI'] = <your-connection-string>

mongo = PyMongo(app)

# Comment out this create_collection method after you run the app for the first time
mongo.db.create_collection('library')

```

#### Helpful Questions
* What is useful about connecting a flask app to a database?  Why go through this process?
    We will be able to accept entries from users, resulting in a much more dynamic site.

### Find, Sort, and Limit Recommendations
Now that your 'library' collection is created, comment out 'mongo.db.create_collection('library')' in your code.

You'll need to seed your remote database with the list in seed_library.py.  You can do this by uncommenting 'collection.insert_many(seed_books)' in your index route and then running your Flask app.  You will have to comment this line out after running it once, as it will raise an error if your app attempts to insert duplicate entries.

The next step is to query your database in order to display the recommended books in your Flask app.

Try the following queries in your index route:

    #finds books with the title "Oryx and Crake"
    books = collection.find({"title":"Oryx and Crake"})

    #finds books in the genre "science-fiction"
    books = collection.find({"genre":"science-fiction"})

    #sorts found books by publication (oldest first)
    books.sort('publication')

    #sorts found books by publication (newest first)
    books.sort('publication',-1)

    #limits found books to the first three entries
    books.limit(3)

    #You can also chain queries
    #finds the three most recent science fiction books
    books = collection.find({"genre":"science-fiction"})sort('publication',-1).limit(3)


After you have experimented with these queries, replace them with: 'books = collection.find({})'.

This will render your full list of recommended books on index.html

Note that the render template in your index() function passes the variable 'books' into index.html, where a Jinja for loop populates a list:
    
    {% for book in books %}
        <li>{{ book.title }} by {{ book.author }}</li>
    {% endfor %}

```python
#app.py 

# -- Routes section --
# INDEX ROUTE
@app.route('/')
@app.route('/index')
def index():
    collection = mongo.db.library
    # collection.insert_many(seed_books)
    books = collection.find({})
    return render_template('index.html', books = books)

```

#### Helpful Questions
* How would you find the two oldest fantasy books?
    books = collection.find({"genre":"fantasy"})sort('publication').limit(2)

* What happens if a query yields no results?
    An empty books object is passed into index.html and no list is displayed


### Variable Routes
Right now our Flask app shows all book recommendations.  As our database grows, it would be useful for users to be able to filter results by genre by navigating around the site.  We can do this by creating a variable route, a single route able to filter by any genre.

By wrapping part of a route in angular brackets, you can take in that part as a variable.

Create a second route called: @app.route('/<genre>')

Routes in Flask are positional, meaning that the function called by a route doesn't need the same name as the route itself, but it must directly follow the route.

This route function will be called genre_view() and it has one parameter: the genre provided by the route.

Complete the genre route and try it out by adding the name of a genre to the url slug, for example: http://127.0.0.1:5000/fantasy

```python
# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    collection = mongo.db.library
    # collection.insert_many(seed_books)
    books = collection.find({})
    return render_template('index.html', books = books)

#GENRE Variable Route
@app.route('/<genre>')
def genre_view(genre):
    collection = mongo.db.library
    books = collection.find({"genre":genre})
    return render_template('index.html', books = books)
```

#### Helpful Questions
* What happens when you add a made-up genre like 'test' to the url slug?
    The genre route uses that as a search term for the database query but it yields no results.  An empty books object is passed into index.html and no list is displayed.

* How does @app.route('/<genre>') display different results from @app.route('/index') when they both render the same template, index.html?
    Because they are passingn different lists of books into the template.

* How could you make a second variable route, so that a user could search by genre or author?
    You would need to add a specific path to the url in order to distinguish them, like:
    @app.route('/genres/<genre>')
    @app.route('/authors/<author>')

### App Navigation
It's not very user-friendly to have people type the genre they want into their navigation bar.  We can improve navigation by adding links that will direct users to the genre they are looking for.

We are already importing a list of genres from model.py.  We can use those to populate a for loop of genre links in index.html.  We could make this list manually:

      <div class="nav-bar">
        <a href="/">all books</a>
        <a href='/comedy'>comedy</a>
        <a href='/crime'>crime</a>
        <a href='/fantasy'>fantasy</a>
        ...
      </div>

But this is very repetitive and time-consuming to update.  It's much better to generate the links using a Jinja for loop, as shown below.

```python
# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/index')
def index():
    collection = mongo.db.library
    # collection.insert_many(seed_books)
    books = collection.find({})
    return render_template('index.html', books = books, genres=genres)

#GENRE Variable Route
@app.route('/<genre>')
def genre_view(genre):
    collection = mongo.db.library
    #find entries whose genre matches the slug
    books = collection.find({"genre":genre})
    return render_template('index.html', books = books, genres=genres)

```

```html
<!doctype html>
<html>
    <head>
        <title>Book Recommendations</title>
    </head>
    <body>

      <div class="nav-bar">
        <a href="/">all books</a>
      {% for genre in genres%}
          <a href='/{{ genre }}'>{{ genre }}</a>
      {% endfor %}
      </div>

      <h1>Recommendations</h1>
      <div class="book-list">
        <ul>
          {% for book in books %}
            <li>{{ book.title }} by {{ book.author }}</li>
          {% endfor %}
        </ul>
      </div>

    </body>
</html>
```

#### Helpful Questions
* When should you use a Jinja for loop rather than hard-coding part of your template?
    When a similar component is repeated several times.

* What determines the route the links redirect to?
    The genre is interpolated into the hypertext reference of the anchor tag.  This redirects app.py to the <genre> route.


### Flask Form Methods
Our app now allows the user to filter results from the database using links.  However, the user still has no way to add new books.  We'll have to do something about that!

We're going to create a route.  Try out the code below then navigate to '/new' and try submitting the form.

```python
# NEW BOOK Route
@app.route('/new')
def new_book():
    return render_template('new_book.html', genres = genres)
```

When you hit submit, the response you get is:
    Method Not Allowed
    The method is not allowed for the requested URL.

That's because you have attempted a different http method.  Submitting a form that sends information to the database requires a post method.  If you add a conditional to this route function, you can render the form when you navigate to the page and post an entry to the database when that form is submitted.

Revise the new route in app.py and try submitting a few books using the provided form.

Congratulations, you have built a full stack application!

```python
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

        collection = mongo.db.library
        
        #insert an entry to the database using the variables declared above
        collection.insert_one({"title":title, "author":author, "genre":genre, "publication": publication})

        #redirect to the index route upon form submission
        return redirect('/')
```

#### Helpful Questions
* What input types are the forms using?
    Text, number, and dropdown

* Why redirect?
    It communicates to the user that their form has been submitted and allows them to see the updated database entries

## Extensions
* Add at least two books to each genre
* Edit index.html to show the year of each book's publication
* Replace you genre navigation links with a dropdown menu
* Add another dropdown to filter by author
* Create a button that recommends a random book from the database

## Related Resources
* [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/) - Full PyMongo Documentation
* [Flask Documentation URL Route Registration](https://flask.palletsprojects.com/en/2.0.x/api/#url-route-registrations) - Details on variable part routes
* [w3 Schools HTMl Forms](https://www.w3schools.com/html/html_forms.asp) - What it is

