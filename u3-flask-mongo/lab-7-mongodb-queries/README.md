# MongoDB Queries Lab

## Objectives

* SW write queries to access information from a public MongoDB database. 
* SW modify queries to access information efficiently using the most context-appropriate queries available.

**Core requirement:** Unless your teacher communicates otherwise, complete at least the first 8 prompts (find and query).  Prompts 9-14 (lists and regular expressions) require advanced techniques and are considered extensions of the core lab.

## Context
A local nonprofit **src_code** is building a website about popular programming languages.  Their mission is to encourage more students to learn to code.  Their web developer, Mariana Reyes, is currently buiding an impeccably styled Flask app to present this information.  She asked your for help querying the database for the information she needs.

    Hi Tech Exchange,

    Thanks so much for volunteering your time to support **src_code!**  The flask app that we're running our site from is coming along nicely but I want to make it more informative by drawing on our database of programming languages.

    First of all, we need help getting the database into the cloud.  Right now our information is just in a file names **language_seed.py**.  There's a file called **reset_collection.py** that can insert all the data to a cloud database, but you need to put in your connection url before your run it.

    Then I have a series of searches and queries I need you to write.  I'll use the results from the queries you write to populate all the views and graphics on our website.  That way, our site will become more informative as our database grows.

    If you have time, I also have some challenging queries for you.  These involve searching for elements in a list or using regular expressions to find partial matches in a string.  Complicated stuff!

    The specific steps are in the file **queries.py**.  You can write each queries right under the relevant prompt.  I'll take it from there.
    
    Thanks,
    -Mariana

## The Setup
Students will need to login to MongoDB.  They will need to retrieve their link to connect their database to a python app.

In addition to this README, students will need access to:
* language_seed.py
* reset_collection.py
* queries.py

## The Lab

### Setup the Database
Open the file **reset_collection.py**.  On line 6, input your PyMongo connection url to connect the file to your database.  (Replace <url> with your url, including your collection's username and password).

Run **reset_collection.py** in your terminal (you may have to cd into **lab-7-mongo-queries** first).  When it asks if you wnt to reset the collection, input **y**.

Check your MongoDB dashboard to confirm that the data is now in your Mongo Atlas database.

Then open the file **queries.py**.  On line 6, input your PyMongo connection url to connect the file to your database.  (Replace <url> with your url, including your collection's username and password).

### Find
In the file **queries.py**, complete prompts 1 through 5.

These prompts ask you to find one or many database entries and print them to the console.

* [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/tutorial.html) 
* [W3 Schools PyMongo Tutorial](https://www.w3schools.com/python/python_mongodb_getstarted.asp)

### Query
In the file **queries.py**, complete prompts 6 through 8.

These prompts ask you to find one or many database entries that match a specific query and print them to the console.

* [MongoDB Query Comparison Documentation](https://docs.mongodb.com/manual/reference/operator/query-comparison/)

### Lists
In the file **queries.py**, complete prompts 9 through 11.

These prompts ask you to find one or many database entries that contain lists matching a specific query and print them to the console.

* [MongoDB Querying Arrays Tutorial](https://docs.mongodb.com/manual/tutorial/query-arrays/)

### Regular Expressions
In the file **queries.py**, complete prompts 12 through 14.

These prompts ask you to find one or many database entries that contain strings matching a specific regular expression.  Regular expressions allow you to compare detailed properties of a string, like individual characters or symbols(like whitespace).

* [Python Documentation - Regular Expressions](https://docs.python.org/3/library/re.html)




