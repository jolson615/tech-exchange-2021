# Flask Lab

1. [Objectives](#objectives)
2. [Concept](#concept)
3. [Setup](#setup)
4. [The Lab](#the-lab)
5. [Extensions](#extensions)

## Objectives

* SW write routes to handle both GET and POST requests to at least two slugs. (e.g. /index and /search)
* SW use the render_template method and {{}} to customize a template
* SW use at least one python function in a separate file to help emphasize the separation of concerns.
* SW see an example of custom CSS or a CSS design library (like bootstrap) integrated into a Flask application.

## Concept
You’re a high school history teacher, and you discovered that your students don't actually know the state capitals for the US! You want to make a fun quiz for your high schoolers, which asks them to type in the capitals for each state and then sends them to a webpage where they can see their results (and perhaps also gives them a fun image or GIF that tells them how well they did).

You will go back to the state capitals quiz you made earlier in Python, and you will now turn your code into a web app with an HTML front end. By the end of this lab, you will have made a state capitals quiz web app using the Flask framework!

## Setup

Have students make a copy of the flask template we’re working with, and name their new repository "StateCapitalsQuiz." 

## The Lab

In index.html, customize the form so that the user is inputting capitals for a couple of states:

```html
<form method="post" action="/results">
  <input type="text" name="New York" placeholder="New York's Capital"/>
  <input type="text" name="California" placeholder="California's Capital"/>
  <input type="submit" value="Submit"/>
</form>
```

In `app.py`, create a /results route that takes the user's answers, such as:

```python
answers = {"NY": request.form['New York'], "CA": request.form['California']}
```

In `model.py`, write a function that takes in a dictionary of state capitals (that the user would have generated), and returns a message saying whether the capital the user guessed is correct or incorrect.

Create a `results.html` page that is rendered when the /results route is used in `app.py`. Use Jinja templating to include the output of the function in `model.py` as part of the `results.html` page.

In `app.py`, use `render_template` to send the user to `results.html` when the form has been filled out (POST request). If the form has not been completed (GET request), return a string explaining what went.

Now it's time to style the web app. There are two approaches students can take to styling:
Build custom CSS (which they’ve already done) using the style.css file in their static > css folder. Students should make sure their CSS file is correctly linked in their html, using this tag: <link rel="stylesheet" href="../static/css/style.css">
Use a CSS design library (like Bootstrap). To use Bootstrap, students should navigate to https://getbootstrap.com/ and click "get started." These instructions explain what goes in the html head tag: https://getbootstrap.com/docs/5.1/getting-started/introduction/#css Then students don't need to make their own CSS. They can just copy-paste HTML code from the Layout and Components sections of the Bootstrap menu on the left-hand side of their website. The most common component, and one of the best places to start, is a Card.

## Extensions

* Calculate the user's score (% correct of the state capitals) and include that information in results.html.
* Use the grid in Bootstrap or custom CSS to more elegantly format the page.
* Create a /hints route that lets the user see a list of all the state capitals, which they can choose from.
* Randomize the order of state capital prompts (making sure that questions don't repeat!).
* Implement a "new game" button.
