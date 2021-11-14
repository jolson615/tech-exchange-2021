# Advanced Flask

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
    * [The Static Folder](#the-static-folder)
    * [Logic In Templates](#logic-in-templates)
    * [Block Content](#block-content)
    * [Redirects](#redirects)
6. [Extensions](#extensions)
7. [Related Resources](#related-resources)

## Context

Even with Flask pared down to the bare essentials, it can still be a lot for students to take in. There's so much new information to process, so this course tries to keep the basic Flask lesson to the bare essentials, and jettisons most other useful content here, to the advanced lesson. 

Some pieces of this lesson are relatively critical. The public folder, for example, is all but necessary to create a viable web application. Some of the other pieces, like internal logic within a template, is really interesting, but often the functions performed by a templated if statement could actually be handled just as easily in the model. 

All of this to say, you should feel empowered to teach as much or as little of this content as you deem necessary for students to move forward. If they're ravenous to learn more, go ahead and cover it all. If they were mostly panicked before, consider narrowing focus to just the public folder. 

## Objectives

* SW make use of the public folder to load in images and CSS files. 
* SW create templates that extend other templates with template blocks. 
* SW add logic / control flow to their templates.
* SW learn to write redirects, e.g. in the situation where someone attempts to reach a slug with an incorrect method. 

## Setup

Depending on how closely you want students to follow along and how well the previous class went, you may choose to continue where you left off from last class. If the basic Flask lesson went tolerably well, that's recommended. 

However, if students really struggled to catch up, or if it's important to review concepts from week 1, you can share out the same starter code from before and do a lightning review of earlier concepts before launching into these more challenging ones. The lesson here is written with the assumption that you'll prefer to start from scratch, but keep everything as simple as possible. 

## Launch

This lesson is a bit of a grab bag - lots of small tools to help supercharge a Flask application. It's a little challenging to launch something like that meaningfully, because the through like is just "ways to make your application better," but if you ask students what features they want, they're most likely to ask for features like account creation, logging in and out, storing/saving your personal data, and social features like posting and following. 

So the best way to launch this lesson is to decide ahead of time what you think is most important and then plan to launch with exactly that - your rationale. If you found the blocks which essentially allow you to componentize your code to be compelling, show students a website with repeated elements and ask them why it would be irritating to need to rewrite code (like a navbar) that appears across multiple pages. As a bonus could even demo instances where a website's navbar is inconsistent across pages to emphasize writing DRY (don't repeat yourself) code isn't just about saving time, it's about avoiding mistakes. 

If the forms library (or really any library) supercharged your code, show them before and after pics of your code and explain why you like it, and then promise students to walk them through the steps. 

## The Lesson

### The Static Folder 

One really interesting thing about the way a Flask application works is that most of the files of the project itself are hidden away from anyone who visits your web application. If they try to see your app.py by requesting the `/app.py` as if it were a route, your application will say "Not Found". The file is there, but Flask doesn't send responses unless you specifically tell it to. 

One way to program the app to send a response is by building a route, which is what we did in the last lesson. But another way is simply place it in the `static` folder. By default, anything in this folder essentially has a route built out for it automatically, and you can subdivide that folder to suit whatever organizational structure you like. There's some additional nuance to what's happening under the hood, but that's the core of what's happening here. 

Go ahead and test it out - try adding an image to the `images` subfolder of the `static` folder, and then requesting it by adding `/static/images/micropig.jpg` - (where "micropig.jpg" is the name of whatever image you've uploaded).

If you look at the HTML template that's pre-built into the template we used, you'll notice that we're *already* using the static folder to connect our CSS to the template. 

```html
<html>
    <head>
        <title>Welcome!</title>
        <link rel="stylesheet" href="../static/css/style.css">
    </head>
    <body>
        <h1>Hello world!</h1>
        <p>We can build a full webpage here</p>
        <form>
            <input type="text" name="nickname" placeholder="Enter your nickname"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
```

As you well know, the `../static/css/style.css` means go up one directory, then locate the static folder, then locate the style folder, and then find the stylesheet called `styles.css`. 

#### Using `url_for`

This is successful, but it's not actually how the Flask documentation recommends you write this route. In order to make this code a bit more error proof, Flask documentation recommends using the built-in `url_for` function. 

```html
<link rel="stylesheet" href={{ url_for("static", filename="css/style.css") }}>
```

The first argument is "static" since we're accessing something housed in this folder, and the named filename argument includes any subdirectories within static you've implemented. In the application's current state, you're not likely to notice any difference between this new way of connecting your CSS and your earlier approach of hard-coding the relative path, but `url_for` can be extremely powerful, so practicing it now can help prepare you for later more complex implementations. 

Feel free to read more about the `url_for` function in the [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/api/?highlight=url_for#flask.url_for).

### Logic in Templates 

Another hugely useful feature of Flask is the ability to add content conditionally. You can embed logic right in the body of an html template with Flask.

#### Using Conditionals

In its simplest form, this might look like telling someone whether they got a question right or wrong. Consider this form that asks the user what the capital of Norway is:

```html
<html>
    <head>
        <title>Geography Quiz!</title>
        <link rel="stylesheet" href={{ url_for("static", filename="css/style.css") }}>
    </head>
    <body>
        <h1>Quick Quiz</h1>
        <p>What's the capital of Norway?</p>
        <form method="POST" action="/scorepage">
            <input type="text" name="capital" placeholder="Answer here"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
```

Previously, we might have needed to do something like this to handle the user's answer:

```python
@app.route('/scorepage', methods=['GET', 'POST'])
def scorepage():
    answer = request.form['capital']
    if answer == "Oslo":
        return render_template("success.html")
    else:
        return render_template("failure.html")
```

This works, but it has a couple of downsides, most critically that you have to maintain two whole templates - a success template and a failure template. 

> Note that checking whether the answer is right or wrong is arguably a job for the `model.py`, not the `app.py`, and as the quiz grows in complexity, we're definitely going to want to separate that concern into another file, but we're keeping it simple to illustrate how conditional logic in templates can help us. 

Consider this other way of writing the route, which is both a bit simpler, and only uses one template:

```python
@app.route('/scorepage', methods=['GET', 'POST'])
def scorepage():
    answer = request.form['capital']
    correct = answer == "Oslo" # will be True if they put Oslo, False otherwise
    return render_template('scorepage.html', correct=correct)
```

In the past when we've passed variables into templates, we've used mostly strings and numbers, which we've displayed directly on the page. This time, though, we're passing in a boolean value `correct` which we won't display on the page. Here's what that looks like in our `scorepage.html` template:

```html
<body>
    <h1>Your Results</h1>
    {% if correct == True %}
        <p>That's right! The capital is Oslo!</p>
    {% else %}
        <p>
            Sorry, that's not quite right.
            <a href="/">Click here to go back and try again.</a>
        </p>
    {% endif %}
</body>
```

You can probably intuit what's happening here. If they get the question right, the first paragraph will show. If they get it wrong, the second paragraph will show. 

> Note that `if correct == True` is the same as just `if correct`, but this more verbose way of writing it is often easier for students to abstract out to other uses. It's ultimately your call how to present this to students, and whether they need to see that more redundant way of writing it first. 

#### Helpful Questions
* Python doesn't usually have `endif` as a keyword. Why is it necessary here?
* Python generally requires a colon `:` after an if statement. Why is that not necessary here?
* Where will the `<a>` link in this example take you? Why will that work?
* Can you think of a situation where we might also need an `elif` branch for logic in a template? In other words, can you think of a situation where there are three distinct possibilities, not just two?

#### Using For Loops

Conditionals aren't the only bit of control flow you can use in a Flask application. If you need to repeat something a few times, a list and a `for` loop can make that happen. 

Imagine a variation of the quiz that keeps track of all the questions you've gotten right so far. Ultimately we'd want to do that sort of thing in a database, but since we haven't gotten to databases yet, we'll skip over storing and retrieving that data, and just assume that the list of three capitals you already got correct are available. 

Here's what the route might look like: 

```python 
@app.route('/scorepage', methods=['GET', 'POST'])
def scorepage():
    previous_corrects = ["Santiago", "Nairobi", "Manila"] # Normally we'd get a user's performance history from a database, but for now we'll use a hard-coded example.
    answer = request.form['capital']
    correct = answer == "Oslo"
    return render_template('scorepage.html', correct=correct, previous_corrects=previous_corrects)
```

This means that we want to display not only the new information about Oslo, but also the older information about the three questions our user got right before this. We could add code to our template to accomplish that with a `for` loop like this: 

```html
<h2>Your Performance History</h2>
{% for capital in previous_corrects %}
    <p> You got 1 point for knowing {{ capital }} </p>
{% endfor %}
```

You can also accomplish other tasks you might use a list for, but just know that the syntax is often a little different. For example, if you wanted to provide a total score so far, you could do that in python by writing `len(previous_corrects) + correct` which will calculate the length of the list and then add either a 1 or a 0 to that number based on whether `correct` is True or False. However, if you try that in a template, it'll need to look a little different. Here's how it's done:

```html
<h3>You have a total of {{ previous_corrects|length + correct }} points so far!</h3>
```

#### Helpful Questions
* What happens if you try a regular `len()` method here?
* As you may remember, the tool that handles templates for Flask is called **jinja2**. What are the major syntax differences you are noticing between how Python usually works and how it works here?
* Are you noticing the difference between how the jinja2 templating engine uses `{{ }}` and `{% %}`? What is the difference?

> Note: this last bit is important, and it's helpful to have a plainwords explanation for both markers:
> * `{{ }}` means "evaluate this Python expression and display the result on the page."
> * `{% %}` means "run this Python code, but do it behind the scenes."

For reference, here's what the entire quiz `scorepage.html` looks like so far:

```html
<html>
    <head>
        <title>Geography Quiz!</title>
        <link rel="stylesheet" href={{ url_for("static", filename="css/style.css") }}>
    </head>
    <body>
        <h1>Your Results</h1>
        {% if correct == True %}
            <p>That's right! You know your capitals</p>
        {% else %}
            <p>
                Sorry, that's not quite right.
                <a href="/">Click here to go back and try again</a>
            </p>
        {% endif %}
        <h2>Your Performance History</h2>
        {% for capital in previous_corrects %}
            <p> You got 1 point for knowing {{capital}} </p>
        {% endfor %}
        <h3>You have a total of {{ previous_corrects|length + correct }} points so far!</h3>
    </body>
</html>
```

### Block Content 

Another super useful feature of Flask is the ability to add base templates with block content to your pages. One of the most easy-to-spot bits of repeated code is on most websites is the navbar at the top of the page, and having a base template can make it such that you don't have to repeat that code - you write it once as a base template, and re-use it wherever you want with child templates. 

In Flask, this way of writing a reusable base template is called [template inheritance](https://flask.palletsprojects.com/en/2.0.x/patterns/templateinheritance/#).

Here's a base template called `base.html` which includes a nav that will take you home at any time:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>{% block title %}Geography Quiz!{% endblock %}</title>
        <link rel="stylesheet" href={{ url_for("static", filename="css/style.css") }}>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
        </nav>
        {% block body %}{% endblock %}
    </body>
</html>
```

Each of these blocks is essentially a blank space that we can fill in later. We've named these blocks really easy-to-remember things that match the HTML elements that they're part of (i.e. `block title` and `block body`), but you could just as easily name them things like `block pineapple`. That said, "pineapple" won't be clear to your other collaborators, so as always, the most important part of naming things is making sure those names make sense to you and to the other developers on your team. 

> Note: Depending on what style of string formatting students are most familiar with, it might be helpful to point out that this type of template is really similar to string formatting in Python. In the same way that `"What's %s got to do with it?" % "love"` evaluates to `"What's love got to do with it?"` - these bits of block content are pieces of the template that will be filled in later. 

So we have our base template, but in order for it to be of any use to us, we need to create a child template that extends it. 

Let's rewrite our `index.html` to use this new base template:

```html
{% extends "base.html" %}

{% block title %}Welcome to the Geography Quiz!{% endblock %}

{% block body %}
<h1>Quick Quiz</h1>
<p>What's the capital of Norway?</p>
<form method="POST" action="/scorepage">
    <input type="text" name="capital" placeholder="Answer here"/>
    <input type="submit" value="Submit"/>
</form>
{% endblock %}
```

Notice that this basically just fills in the blanks from the base template. 
* The `block title` in the base template had the phrase "Geography Quiz!" in it. Since we've included the title block here, that original string will be overwritten with the "Welcome to the Geography Quiz!" that's included here. 
* The `block body` in the base template had nothing in it, so the content we've included here will get added to the base template before it's rendered. 

In order to get any real benefit from the base template, we really do need to use it twice, so here's what our `scorepage.html` page would look like if it were refactored to extend the base page. 

```html
{% extends "base.html" %}

{% block body %}
    <h1>Your Results</h1>
    {% if correct == True %}
        <p>That's right! You know your capitals</p>
    {% else %}
        <p>
            Sorry, that's not quite right.
            <a href="/">Click here to go back and try again</a>
        </p>
    {% endif %}
    <h2>Your Performance History</h2>
    {% for capital in previous_corrects %}
        <p> You got 1 point for knowing {{capital}} </p>
    {% endfor %}
    <h3>You have a total of {{ previous_corrects|length + correct }} points so far!</h3>
{% endblock %}
```

By now the `scorepage.html` doesn't look much like HTML, so be patient with yourself as you adjust to writing your templates in this new way. It's more efficient in the long-term, but it's not critical that your application be done in this way. 

#### Helpful Questions
* What part of Flask template inheritance do you like most?
* What part of Flask template inheritance do you think will be most challenging?
* Do you think your Flask application could benefit from templates that use inheritance in this way?


### Redirects 

One last super useful thing to know is how to redirect someone to another page. There are dozens of reasons why you might want to do this - websites will commonly redirect you to a dashboard after you log in, or to a homepage after a certain screen times out. 

In the context of our quiz app, we'll use a redirect to handle a situation where a user tries to navigate our page in an unintended way. For example, we don't really want a user to just jump into the `scorepage.html` template by adding `/scorepage` to their URL - they're supposed to answer the question first! 

We could just specify that the route is only for 'POST' methods, but it's entirely possible that a friend sends them a URL to take the quiz that includes that `/scorepage` slug, and they click on it innocently. This is a really likely user behavior, even if it's not intended, so we need to be prepared for it. 

Without redirects, we could try something like this:

```python
@app.route('/scorepage', methods=['GET', 'POST'])
def scorepage():
    if request.method == 'POST':
        ... # code for intended POST behavior, omitted here for readability
    else:
        return "Please go back and use the form!"
```

This will print a plaintext message, which works, but definitely isn't best. We could improve that with `return render_template('index.html')` so that it actually renders the entire homepage, but the trouble is that the user will look at their browser and it will still show `/scorepage` in the address. They'll get a really confusing impression of what lives at different parts of the site. 

So the best solution is a redirect. In order for this to work, you need to change `from flask import request` to `from flask import request, redirect` at the top of your `app.py` file. If you skip this step, you'll get an error when you try to use a redirect function which you never imported.

The following tiny bit of Flask code sends what's called a [302 response](https://en.wikipedia.org/wiki/HTTP_302) by default, which basically sends sends the user to a whole different route automatically. Here's what that looks like in context:

```python
@app.route('/scorepage', methods=['GET', 'POST'])
def scorepage():
    if request.method == 'POST':
        ... # code for intended POST behavior, omitted here for readability
    else:
        return redirect('/')
```

This code is really simple, and it allows us to account for some unintended (but likely) user behavior where they try to access information that isn't there yet. 

> Note: now is probably not the best time to get deep into the nitty gritty of 301 v 302 v 303 v other redirect codes - the default 302 is fine for now, and depending on where students are at, might be worth glossing over entirely. 

#### Helpful Questions
* When have you encountered redirects in your own web browsing?
* Do you generally find redirects to be helpful for frustrating?

## Extensions

Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 

Try each of the following for the Flask application you're currently working on:
* Add some content to the static folder, and implement it in your app using `url_for`.
* Add some control flow (code using `if` or `for`) to one of your templates.
* Try implementing a base HTML template for things like a header and a footer, and use it on all the templates currently in place. 
* Try adding a redirect in case anyone tries to use your application in an unintended way. 


## Related Resources

* [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/) - The best place to learn Flask is right at the source. The documentation has detailed explanations about how everything here works. 
* [Flask Macros](https://uniwebsidad.com/libros/explore-flask/chapter-8/creating-macros) - If you're familiar with the React style of creating pages out of component parts, macros could scratch that exact itch for you. 
* [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) - If you want a super-comprehensive exploration of Flask that doesn't even start with a template, this is a really great place to start. The code is a little out of date, but the core concepts are the same. It will take a long time to work through, but you'll emerge on the other side with a pretty comprehensive understanding of how Flask works. 
