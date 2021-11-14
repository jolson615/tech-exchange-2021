# Intro to Flask

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

By this point, students can make websites that allow for user interaction (with HTML/CSS), and users can do meaningful data processing (with Python), but they haven’t yet done both together. Flask is a framework that enables a website coded in HTML/CSS to interact with a Python back end, which means that user input can be processed in Python, and the output can be rendered to the user on the webpage.

It’s good to review the terms “front end” and “back end.” Explain to students that “front end” refers to coding the user’s experience: what they see on the screen and how they interact with it. The term “back end” refers to the behind-the-scenes calculations, which users generally don’t want or need to access directly. The Flask framework enables us to make HTML/CSS our front end and Python our back end. When you are coding from end to end (that is, front end and back end together), it’s called “full-stack development''.”

Image: https://www.seobility.net/en/wiki/Frontend

Ask students: “If you couldn’t get a video you wanted on TikTok, what might be breaking that prevents that from happening?”
Possible answers:
It’s not rendering properly on the screen
The site can’t connect to where the video is housed
The video isn’t there anymore

Getting information to the user is complicated, and so developers tend to separate the pieces into distinct activities. A common structure for these activities is the model-view-controller framework. When something breaks in the code, the first step is to figure out where in the system it broke, and then to debug. Certain coding languages lend themselves better to certain aspects of the process, too. Here are the pieces:
The view refers to what the user sees. We’ll be coding this in HTML and CSS.
The model refers to the back end calculations and manipulation of data. We’ll be coding this in Python, in a file called model.py. When you run your unit tests, you’ll run them on the functions in model.py. The model is also the component of the program that connects with an external database. Later on in this course, you will use MongoDB to store data that your model.py file can interact with.
The controller will also be in Python, in a file called app.py, which sets the rules for what the user sees and how the model is updated as a result of user action.


Image: https://commons.wikimedia.org/wiki/File:MVC_Diagram_(Model-View-Controller).svg

## Objectives

* SW install a Python 3-compatible instance of Flask in Cloud Shell
* SW understand what a basic model-view-controller framework is, and why it is used. 
* SW understand the GET and POST HTTP Request methods, as well as the most common Response types and codes (e.g. 200, 401, and 404)
* SW write routes to handle both GET and POST requests to at least two slugs. (e.g. /index and /search)
* SW use the render_template method and {{}} to customize a template
* SW use at least one python function in a separate file to help emphasize the separation of concerns.

## Setup

It’s time to install Flask in the CloudShell IDE! Ask students to make sure they have auto-save turned off in CloudShell.

Share the following line of code with students and ask them to run it in the command line.

sudo pip3 install flask

Next, have students copy the following into their CloudShell terminal to create a startup script.
touch ~/.customize_environment
echo 'sudo pip3 install flask' >> ~/.customize_environment
echo 'sudo pip3 install python-dotenv' >> ~/.customize_environment

Finally, have students restart their environment using the "..." menu in the top right corner of the Cloud Shell window. When it asks you why you're doing this, select "want clean VM state" as the reason. Your Cloud Shell will probably take about 2 minutes to restart.

Have students confirm that Python and Flask are installed by typing flask --version into their terminal

Now, have students go to the flask template we’re working with, located here: https://github.com/upperlinecode/flaskproject

Ask students to click “Use this template” and name their new repository “Flask practice.” Then they can choose “clone this repository,” copy the URL, and clone it down into the CloudShell folder they’re working in. The terminal command for this is git clone, and then students will paste the URL they copied from GitHub.


## Launch

Ask students to complete the water use survey located here: https://www.watercalculator.org/. Ask: if you were to make a program like this using a combination of HTML/CSS and Python, which aspects would you do in HTML/CSS and which would you do in Python? Likely answers:
The design of the page (colors, moving water, appearance of the forms and buttons) is HTML/CSS
The calculation of water consumption and the numbers that update are in Python

Tell students that this is a great example of something they’ll be able to make using the Flask framework.

## The Lesson

Students will have cloned the Flask template as part of the setup. Ask them to cd into the folder that they just cloned, then type flask run in the command line, and then click the link to preview their page.

This link is a local IP address that enables the coder to view their page as they work on it in their IDE.

Students should see “hello world” in their preview window. Ask students to figure out where in the code the “hello world” comes from.

Students will likely notice “hello world” in line 16 of templates > app.py. Point out that lines 15 and 16 of app.py are a function (just like the functions they’ve already written in Python). The function returns a string, which is “hello world” - and the string is rendered on a webpage.

In the URL of their preview page, ask students to replace the text after and including the question mark with “index”:

Confirm that the website still says “hello world”. Ask students where in the code it says that “/index” is the route that this “hello world” string is connected with. Students will point to line 14. Ask students what else should return “hello world” and students should say that a slash without the word “index” should also return “hello world.” Have students confirm this works. Then ask students to try another ending for the URL, such as “/secret” - and confirm that it returns “Not Found.”

Tell students that HTTP stands for “Hypertext Transfer Protocol.” There are a lot of pieces to HTTP, but we’re going to cover two common methods (or actions) that are used in HTTP: GET and POST. The GET method asks the browser to get information from a particular website. For example, when students visited the water calculator website either by clicking the link or typing the URL in their browser, the browser sent the server a request to get certain information that would be rendered on the page. The response type 200 means that this request has succeeded.

Sometimes the HTTP request does not succeed. Most students will have encountered a 404 error at some point. If a get request is sent by the browser, and the browser was able to connect with the server but unable to find the requested page, then a 404 response type is given. Students may also have encountered 401 and 403 errors, which arise when access to the site is not permitted. Remind students that Googling these errors as they arise is a key way to build their coding knowledge over time and to better understand the ins and outs of HTTP.

Continuing the theme of water conservation, we’re going to write a program where the user can type in a country, and the website tells them the per capita water footprint in that country. (Data sourced from here: https://www.waterfootprintassessmenttool.org/national-explorer/.)

In the flask framework, a route calls a function when the user navigates to a specific url. Let’s write a function for what should happen if the user navigates to the URL of our site with “/purpose” at the end of it. Add the following code to app.py:

```PYTHON
@app.route('/purpose')
def purpose():
    return "This web app tells the user the per capita water footprint for a country they selected."
```

Remind students to always save their code before they reload their preview page. Ask students what they need to type in their preview window to see this purpose page. Have students confirm that appending “/purpose” to the end of the URL does indeed get them to this page.

Ask students to put the text inside an h1 tag, as follows.
```PYTHON
@app.route('/purpose')
def purpose():
    return "<h1>This web app tells the user the per capita water footprint for a country they selected.</h1>"
```

Ask students what happens to the page. Then have them format the page a bit by giving it a title in h1 and smaller text in another h or in a p tag. Point out that the string returned by the function is read as HTML.

Time permitting, students may play for 3-5 minutes by adding their own custom routes to their app.py file.

Ask students why it might be a bad idea to build out an entire HTML page inside the return. Students will likely note that it can be cumbersome and hard to read. Note also that it’s a best practice to keep different functions of our web app separate. Referring back to the MVC framework, the site itself is part of the “view” and the app.py file is the “controller.” So let’s have the return of our function refer to an HTML page that we save somewhere else.

At the top of their app.py file, have students write from flask import render_template

Then ask students to edit their index route as follows:

```PYTHON
def index():
    return render_template('index.html')
```

When students save their code and reload their /index preview page, they will see a whole HTML page. Students will find index.html in the templates folder. Tell students that when using the Flask framework, they should keep their HTML files in the templates folder. When they use the render_template function, it looks for an HTML file in that folder.

Now let’s talk about how to customize the page for an individual user. We’ll ultimately be able to have users log in, and we can pull their information from a database, but to start let’s store their data as a dictionary in Python. Ask students to update their index function as follows:

```PYTHON
def index():
    user = {"name": "Skyla", "status": "platinum"}
    return render_template('index.html', user=user)
```
  
The second argument in the render_template function will allow us to refer to the user variable in the HTML page. Ask students to predict what will change in /index when they save their code and reload the page. The answer: nothing! We haven’t yet put anything in the index.html file that refers to the variable user.

Have students add this code to the body of their index.html file, then see how it appears on the page:

        <h1>Hello {{user["name"]}}</h1>
        <p>You're a {{user["status"]}} user, and it's great to have you back!</p>

This is Jinja3 templating. The double curly braces are used to fill in data that was passed in as arguments of the render_template function.

Now we can get information from Python into an HTML page, but we still need to be able to get information from the user. In the Flask framework, this will be done through forms.

First, in app.py let’s create a route for when the user chooses a country:
```PYTHON
@app.route('/country')
def country():
    return "This page tells you the water footprint of the country you selected."
```

Now, let’s get the information from the user that will be used to generate their message. There is already a form in index.html. Let’s customize it as follows.

        <form method="post" action="/country">
            <input type="text" name="country" placeholder="type a country"/>
            <input type="submit" value="Submit"/>
        </form>

Note that the method here is POST. In a POST method, the user sends information to the server, which can then be processed by the application.

Ask students to try using their form and click “Submit.” What error message do they get? If they hover over the browser tab, they’ll see that it’s a 405 error, which means the method (POST, in this case) is not allowed. To fix this, they need to make POST an allowable method along with GET. They should update their /message route as follows:

```PYTHON
@app.route('/country', methods=['GET', 'POST'])
def country():
    return "This page tells you the water footprint of the country you selected."
```

When we’re on the web, sometimes we arrive at a given URL by clicking a link or typing the address (GET). Other times we arrive at the same URL by submitting information in a form (POST). If we want a single route to render differently based on the method, we need to use requests. Ask students to add

```PYTHON
from flask import request
```
at the top of their app.py file. Then they can update their route to render differently based on whether the user did a GET or POST request.

```PYTHON
@app.route('/country', methods=['GET', 'POST'])
def country():
    if request.method=="GET":
        return "You have not filled out the form."
    else:
        return "This page tells you the water footprint of the country you selected."
```
Ask students to confirm that they get "Here is the message for today.” when they fill out the form and "You have not filled out the form." when they arrive at the /country page by typing the URL in the address bar.

Now it’s time to get the user input into app.py. We do so by using request.form, and referring to the name property of the HTML input.
```PYTHON
@app.route('/country', methods=['GET', 'POST'])
def country():
    if request.method=="GET":
        return "You have not filled out the form."
    else:
        country = request.form['country']
        return "The country you chose is " + country
```
Ask students:
Go to your /index page. When you fill in the form and click “submit,” what data is being captured by your program?
What should happen after the user clicks “Submit”?
What should happen if the user types in the URL /country without filling out the form? Where is this outcome specified in the code?

Students should check that their program works as expected, and use the (very helpful) Flask error messages to debug as they go.

The last part of this lesson is to write Python code in the model, which determines the output that is rendered on the HTML page. Have students write a function in model.py that will take a country as an input and return its per capita water footprint. They’re welcome to use the data from this site: https://www.waterfootprintassessmenttool.org/national-explorer/

Here is some sample code for students to use:
```PYTHON
def waterConsumption(country):
    if country=="United States":
        return "7800 liters per day"
    elif country=="Brazil":
        return "5600 liters per day"
    else:
        return "I don’t have data for " + country + "."
```
Now students need their app.py file to use the function written in model.py. At the top of app.py, write from model import waterConsumption.

Ask students: why did we write the waterConsumption function in a separate Python file? (Answer: this is the separation of concerns idea we talked about earlier. The purpose of app.py is to do the necessary routing based on inputs from the user or a database. The purpose of model.py is to do the calculations that will later be sent to a database or rendered to a user.

In the /country route, students can now return a customized output that depends on user input:
```PYTHON
@app.route('/country', methods=['GET', 'POST'])
def country():
    if request.method=="GET":
        return "You have not filled out the form."
    else:
        country = request.form['country']
        waterAnswer = waterConsumption(country)
        return waterAnswer
```
Have students run their web app, filling out the form with different countries (including ones we haven’t input data for!), to make sure it works. Help them debug.

## Extensions

* Students can add water data from additional countries, besides just the US and Brazil.
* Students can make their model.py function case-insensitive, so it gives the correct output whether the user typed the country in capitals or lowercase.
* Students can add additional fields to their web form, such as asking the user to guess the water consumption (and then later telling them if their guess was too high or too low).
* Students can use a better method (such as a dictionary) to store the country data in model.py.
* Students can build out their output page in a new country.html file that they create in their templates folder.

## Related Resources

* MVC explained: https://www.freecodecamp.org/news/the-model-view-controller-pattern-mvc-architecture-and-frameworks-explained/
* Flask documentation: https://flask.palletsprojects.com/en/2.0.x/
* Python Flask tutorial: https://www.youtube.com/watch?v=QnDWIZuWYW0

