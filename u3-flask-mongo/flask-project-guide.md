# Flask Project Guide

1. [Context](#context)
2. [Objectives](#objectives)
3. [Teaching Tips](#teaching-tips)
4. [What We're Building](#what-we're-building)
5. [Requirements](#requirements)
6. [Launch](#launch)
7. [Recommended Benchmarks](#recommended-benchmarks)
8. [Deployment](#deployment)

## Context

This is an exciting time! We have reached the final project of the course. By this point, students can make websites that allow for user interaction (with HTML/CSS), can use functions to do calculations and manipulate data in Python, can integrate Python with HTML/CSS into a web app using the Flask framework, and can connect their web app to a Mongo database that stores data for later retrieval and can be updated by users.

Now, students can integrate these skills and collaboratively produce an exciting web app!

## Objectives
* SW create a fully-functioning web application using Flask and MongoDB
* SW work in teams to create something they're proud of!

## Teaching Tips
The most common challenge that student groups face here is taking on more than they are ready for and then producing a hairball of code that doesn’t work but is too complicated to debug. Often it means starting over, which can be stressful toward the end of project mode.

To prevent this from happening, explain to students the concept of a Minimum Viable Product (MVP). Before starting to code, students should map out what their ideal final product would look like, and they should also design an MVP version that they can code faster (within about half the total time they have for the project). Their MVP should be a working version of what they ultimately want to do, with basic functionality. An example MVP would be a web app that doesn’t yet have styling in Bootstrap, only has one route instead of five, or has hard-coded values in Python instead of being connected to a Mongo database. At any point in the coding process, students should have something that works - even if it doesn’t have all the functionality they ultimately want. This is more effective than writing all the code and then testing later, only to find out it’s too complicated to debug.

While students are working, make sure to visit each project group. Ask them to share their mockups and to tell you which parts they’re working on at a given moment. Ask about a recent debugging success they had. Ask if there’s something they want help on. Ask how the students have organized the work: is one person doing the front end while another does the back end? Are they pair programming? Many styles of collaboration work, as long as everyone in the group is in agreement on how the collaboration should go.

## What We’re Building

You’ll be building a web application that enables users to interact with a Python back end and a Mongo database. The key here is interaction: the user’s experience should depend on choices that the user has made. Here are some options for your final project:
* Something fun and quirky, like a virtual escape room or an app that lets people share their favorite jokes
* Something that improves the world, like a dog adoption app or a platform for sharing climate protest information
* Something practical, like a scheduling app or an investment tracker

## Requirements

This project should integrate all of the skills that students have developed through the entire course. In particular, each group's project must demonstrate each of the following:
* At least two different .html pages, at least one of which contains a form for user input, with Flask routes that direct the user based on whether the request is GET (clicked link) or POST (form filled)
* An app.py file that contains at least two custom routes, at least one of which can handle POST requests as well as GET requests
* A model.py file that contains logic for storing and processing user input before sending it to a database or rendering it back to the user
* A Mongo database that is connected to the web app and allows users to update it through the web app and to view elements of the database in the web app
* At least one stylesheet, either custom-made (with at least 10 different rule sets) or connected to a CSS design library like Bootstrap
* At least three different branches, or evidence of at least one merge conflict which you have resolved.
* You must make something you're proud of!

## Launch

Ask student groups to begin by coming up with ideas. Ask them to write down at least 10 ideas before agreeing on something they’re all excited about.

Once they’ve settled on an idea, they should NOT start coding immediately. Instead, they should map out their ideas in a Google doc or drawing, with a preliminary mock-up of the final web app. They should also define their MVP (versus later nice-to-have functionality) and lay out the steps they’ll need to complete to get their MVP working.

After you approve their plan, help them create a new GitHub repository, add everyone in the team as collaborators, and then clone it down. Note: it will behoove students to use the same Flask template they have been using for the past few classes. They can choose “use this template” in GitHub and then clone it down.

Students have a lot of time to work on this project - by design. It’s worth taking the time to set it up well so that their time spent working is fruitful and results in a web app of which they are proud.

## Recommended Benchmarks

It can be helpful (though not required) to have students report their status at the end of class. Students should generate their own internal group deadlines, such as “By this date we’ll finish the code where the input into the form gets saved in the database.” Make sure that students are on track for an MVP - that is, their code is testable at all times and they continue to build on a working site rather than expecting it to work down the line without testing along the way.

In addition, students should be writing and running unit tests throughout the coding process. Ask students to share their unit tests with you, and ask them what makes them confident that they’ve captured a complete set of possible use cases.

Students should be able to submit:
* First, a plan and mockups. Students should be able to articulate the goal of their web app, the tools they’ll use to achieve it, and a rough sketch of each of the webpages.
* Second, a more detailed outline of the content of each webpage, the routes that connect Python to html, the calculations that will be performed in Python, and the contents of the database.
* Third, an articulation of division of responsibilities wherein everyone has a coding-heavy role and knows which files they’ll be working on in the overall scheme of the GitHub repository.
* Fourth, a presentation of their app where they walk through their process, what they’re proud of, and what they’d add to their app if they had more time.

It can be helpful to have students present their work to each other about halfway through project mode, to share ideas and get suggestions from other groups as they keep coding.

## Deployment

GitHub enables users to host websites, but not when it's an end-to-end web app. If there's a Python back end (which we have here), then we need to use another platform to host the site. If deploying to Heroku, be sure to include all necessary requirements (such as gunicorn) in requirements.txt and runtime.txt
