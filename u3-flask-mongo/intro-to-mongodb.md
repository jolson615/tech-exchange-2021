# Intro to MongoDB

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

### Why Databases?

So far we have developed front-end applications in Flask, which have no way to take in and store data persistently across devices and users.  Front end applications are useful!  You can make an informational site with information from Flask templates or access an existing api (application programming interface) in order to use data from a database.

Today we are taking our first steps toward creating a full-stack application.  In order to allow users to input information to our site (like logging into a news site, favoriting a show on Netflix, or posting content to social media) we need to create a database that users can access.

### Why MongoDB

We will be building databases with MongoDB, a document database that is highly accessible, easy to deploy, and scalable to larger projects.  When we develop our projects, we will focus on deploying our databases to a cloud-based server so the data storage will not be limited to a single machine (we want to be able to turn off our laptops without shutting our apps down).  Using a cloud database also minimizes software installation and troubleshooting.

## Objectives

* SW understand what a cloud database service is and what new functionality it affords our web applications. 
* SW create MongoDB free accounts
* SW understand the way MongoDB labels different parts of its data storage system (e.g. cluster, collection, and database)
* SW add themselves as authorized users of their database, and whitelist appropriate IP addresses
* SW write basic MongoDB queries
* SW read from and write to a MongoDB database

## Setup

Students will navigate to mongodb.com and create a new account.  Instructors should follow the installation steps on their own so they are familiar with the process.

## Launch

Today we're making a database of computer programming languages.  We'll be creating a new database on MongoDB Atlas and inserting a few entries.  We'll be building on this database in the next lab.

## The Lesson

### Setting Up MongoDB
<img width="1241" alt="mongodb" src="https://user-images.githubusercontent.com/37776449/140630209-5221a82e-97d6-4cc0-8c43-455c61f20f1f.png">

Navigate to mongodb.com and click 'Try Free' on the homepage.  After you create an account, select 'Create New Cluster'.
* Select a shared server, rather than a paid dedicated server.
* Select a cloud provider that is geographically close to you that supports the free cluster tier.
* Select the M0 sandbox tier, as this is free forever.
* Give your cluster a name (Cluster0 is a good default).
* Create the cluster and wait a few minutes will the server is provisioned.
<img width="943" alt="cluster" src="https://user-images.githubusercontent.com/37776449/140630212-52265fe7-0569-4a78-9025-9f559c24afc2.png">

Once you have created the cluster, you will need to add a database.
* From your database deployments page, select Browse Collections
* Create a new database named 'database' with a collection named 'programming_languages'
<img width="1403" alt="Screen Shot 2021-11-06 at 9 23 47 PM" src="https://user-images.githubusercontent.com/37776449/140630195-409ce990-d747-4a32-b436-bb5ba7d94236.png">

Next, you will need to create a user with access to this database.  On your database deployments page, select 'Database Access' from the Security nav bar.
* Click 'Add New Database User'.
* Give your user the username 'admin' and save the password you use somewhere local (like in a text file.)
* Give the user read/write privileges to your user.
* Click 'Add User'

Finally, you need to approve your IP address for access to this database.  On your database deployments page, select 'Network Access' from the Security nav bar.
* Click 'Add IP Address'.
* Select 'Allow access from anywhere'.
* Add a common noting that access to this database is open to any IP.
* Click 'Confirm'.

#### Helpful Questions
* What's the relationship between a database and a collection?
It's a parent-child relationship: a database may contain many connections.
* Why would you want to limit which IP addresses can access your databases?
It could contain internal documents for a business or protected personnel data.

### Intro to PyMongo
In order to access our collections from a python file, you will need a library called PyMongo.  As the name suggests, PyMongo contains a set of tools specific to MongoDB.

In your terminal, type:
    python3 -m pip install "pymongo[srv]"

Next, you will need to get the connection url from your MongoDB dashboard.
* Click 'Connect'
* Select 'Connect your application'
* Set Driver to Python version 3.6 or later (type python3 --version in your terminal to check your version if unsure)
* Select 'Include full driver code example'
* Copy the example code and close the modal

Create a new python file named languages.py.  You will need to import PyMongo and include the connection code.  Initialize the variable db and assign it the value client.database.  This will allow you to modify the database in your cluster named database (it will create a database if it does not yet exist).  Then add a collection named languages using db.create_collection().  This and other helpful methods are included in PyMongo.

Run the file by typing 'python3 languages.py' in your terminal.

```PYTHON
import pymongo

client = pymongo.MongoClient("mongodb+srv://feedbackLoop:TestUserPassword1!@cluster0.0nsou.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.database
db.create_collection('languages')
```

#### Helpful Questions
* How do you know if this worked?
Check your MongoDB dashboard (refreshing if necessary).  Look for a collection named languages.

### Writing Entries to a Database

Now you're going to add some programming languages to this collection.  The database isn't very useful without any entries.  First, comment out the create_collection method.  The collection already exists.  Next, declare a variable langs and assign it the value db.languages.  This will allow us to use PyMongo methods to read and write to that collection.

The first PyMongo method is .insert_one.  Insert three programming languages to your collection following the example below.

```PYTHON
import pymongo

#mongo client connection
client = pymongo.MongoClient("mongodb+srv://feedbackLoop:TestUserPassword1!@cluster0.0nsou.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#initialize variable to access database
db = client.database

#Comment out this create_collection method
#db.create_collection('languages')

#initialize variable to access collection
langs = db.languages

#Insert three programming languages to the database
langs.insert_one({"Language":"Python", "Designer":"Guido van Rossum", "Year Created":1991})
langs.insert_one({"Language":"JavaScript", "Designer":"Brendan Eich", "Year Created":1995})
langs.insert_one({"Language":"Java", "Designer":"James Gosling", "Year Created":1995})
```

#### Helpful Questions
* What happens if you don't comment out db.create_collection('languages')?
raise CollectionInvalid("collection %s already exists" % name)
* What data type are these entries?
You can try it by wrapping one in a type() function.  Python reads them as dictionaries.
* What happens if you run this file twice?
You create duplicate entries.

### Reading Entries in a Database
You can read your entries directly in the collections tab of your MongoDB dashboard.  You can even edit entries directly in this interface.  If you have any duplicate entries, float over them and select the trash icon to delete them now.
<img width="1392" alt="Screen Shot 2021-11-06 at 10 37 33 PM" src="https://user-images.githubusercontent.com/37776449/140630259-84b56256-701e-4215-8d4c-7e4251949c67.png">


Users of our apps can't view this dashboard, so we want a way to retrieve results in our Python file.  We can do this with PyMongo's .find() method

Including an empty pair of curly brackets as the argument for the find method will return all entries in the collection.  You can include one or more key:value pairs in the find method to return only the entries matching your specifications.

Keep in mind that Python accesses these entries as dictionaries, so you can reference specific values in the same way you would a dictionary.

```PYTHON
#return all entries in the collection
all_langs = langs.find({})
#print each entry
for l in all_langs:
    print(l)
    #references specific values of the entry to create a formatted string
    print(f"{l['Language']} was created by {l['Designer']}")

#return all entries in the collection, sorted by the oldest
sorted_langs = langs.find({}).sort("Year Created", -1)
for l in sorted_langs:
    print(l)

#return the first two entries in the collection
two_langs = langs.find({}).limit(2)
for l in two_langs:
    print(l)

#return one entry in the collection where the designer is Guido van Rossum
guido = langs.find_one({"Designer":"Guido van Rossum"})
print(guido)

#return one entry in the collection where the designer is Brendan Eich
brendan = langs.find_one({"Designer":"Brendan Eich"})
print(brendan)
```
#### Helpful Questions
* When multiple entries match the criterion of a find_one search, which is returned?  Is it always the same?
The first entry is always returned.
* What are some advantages of find_one over find?
More predictable output (always a single object) that's easier to print (no need to iterate through a list)


## Extensions
Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* Add three more languages to the collection.
* Find the three most recently created languages.
* Write a function that accepts a count as a parameter and returns a formatted string listing that many designer names.
* Write a function that accepts a year as a parameter and returns a formatted string listing all programs released that year.

## Related Resources
* [Mongo DB](https://www.mongodb.com/) - Document Database with cloud service
* [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/) - Documentation for PyMongo installation and syntax
