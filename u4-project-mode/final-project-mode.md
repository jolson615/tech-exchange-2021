# Final Project Mode (instructor-facing)

### Student-facing Materials

1. [Objectives](#objectives)
2. [What We’re Building](#building)
3. [Requirements](#requirements)
4. [Exemplar](#exemplar)
5. [Deployment](#deployment)

### Teacher-facing Materials

6. [Context](#context)
7. [Teaching Tips](#teaching-tips)
8. [Launch](#launch)
9. [Recommended Benchmarks](#recommended-benchmarks)

# Student-facing Materials

## Objectives
 
* Create a fully-functioning web application using Flask
* Connect that Flask application to a MongoDB back-end
* Collaborate effectively with teammates

## What We're Building <a id="building"></a>

For your final projects, you'll be building a full-stack web application which uses HTML, CSS, Flask, and MongoDB. 

The purpose of final projects is for you and your team to get a fresh start, so as you're brainstorming ideas, be sure to start by reflecting on your other projects that led up to this one. If you found that project was too serious, try to brainstorm some more lighthearted ones. If you found the project was a little too straightforward, try brainstorming some projects that will offer you a greater challenge. 

You are highly encouraged to talk with your project advisor about which of your three projects was the weakest up to now, or just getting their input about what you would benefit from focusing on, and then prioritize that piece of the puzzle in final projects. 

## Requirements

This project should integrate all of the skills that students have developed through the entire course, and should demonstrate mastery of all of them. In particular, each group's project must demonstrate each of the following:
* At least three different .html pages, at least one of which contains a form for user input, with Flask routes that direct the user based on whether the request is GET (clicked link) or POST (form filled)
* At least one stylesheet, either custom-made (with at least 10 different rule sets) or connected to a CSS design library like Bootstrap
* An app.py file that contains at least two custom routes, at least one of which can handle POST requests as well as GET requests
* A model.py file that contains logic for storing and processing user input before sending it to a database or rendering it back to the user
* Test files that correspond to the functions created in the model.py file. 
* A Mongo database that is connected to the web app and allows users to update it through the web app and to view elements of the database in the web app
* At least three different branches, or evidence of at least one merge conflict which you have resolved.
* You must make something you're proud of!

## Exemplar

Final projects aren't significantly different in scope from unit 3 projects. After all, we haven't additional material since that project was due, so please reference the unit 3 exemplar again as you prepare for this project. 

* Unit Project Exemplar Code: [Book Store App](u3-flask-mongo/flask-mongodb-project-exemplar)
* Unit Project Exemplar Deployed Preview: [Deployed Book Store App](https://techexchange-book-store.herokuapp.com/)

Even though the exemplars are the same as before, you may notice features of this exemplar that you have a greater appreciation for now that you've gone through the process of building your own. Try to focus on those features as you re-examine these projects.

The biggest difference you should keep in mind between unit 3 projects and final projects is this: final projects are your chance to start from a clean slate. Take the lessons you learned from the unit 3 project (e.g. "I wish we had spent more time on tests" or "I wish we had taken more time to mock up our designs" or "I wish we had organized our database differently") and keep them in mind as you plan your final project. 

## Deployment

As recommended in unit 3, [Heroku](https://www.heroku.com/) is a platform where you can deploy and host your app for free. If deploying to Heroku, be sure to include all necessary requirements (such as gunicorn) in requirements.txt and runtime.txt - examples of these files are available in the project exemplar code.


# Teacher-facing Materials

## Context

You've reached the end of new content for this course! Students are likely overwhelmed; it takes seeing the Flask Framework and using MongoDB multiple times before it starts to make sense. If students are frustrated or confused, there is time during project mode for targeted re-teaching. Here are some suggestions for how to help students manage their panic and ultimately triumph during this final project mode.

Also refer to the Flask Project Guide for additional details and expectations: https://github.com/upperlinecode/tech-exchange-2021/blob/main/u3-flask-mongo/flask-project-guide.md

## Teaching Tips

Use the launch of project mode as an opportunity to get students excited about bringing together everything they've learned so far. Remind students that they should start small, defining an MVP and building things that work every step of the way instead of producing a hairball of code that doesn't work but is too complicated to debug.

Once students have laid out their plan for their MVP, they'll know where they want additional guidance before coding. One option is to have small-group sessions where you re-teach content from Flask and MongoDB. Perhaps one group is implementing user logins but they were confused in the Advanced Mongo lesson. They may choose to attend a re-teach session while other groups are working on their projects. If another group is not sure how to use the CSS grid, they may want a special re-teach session on that, which not all students will attend.

It's important to celebrate bugs and normalize struggle. When students come together at midpoint presentations to share out what they've built thus far, ask them to talk about a particularly gnarly bug they faced and the skills they employed to push through it. 

As the person who sees what everyone is working on (because you're visiting each group as they code), you can also create strategic connections - for example suggesting that one group share a snippet of their code with another group who's working on a similar challenge. When students can work together and use online resources to solve problems, they learn the skills that will make them successful as software developers.

Remind students about the importance of workflow as they code together. They will need to deal with merge conflicts, and it will take time to figure out who has the latest version and how to make sure the main branch on GitHub reflects the code they want integrated. Coding is a process of alternately dividing up responsibilities and then coming together to merge the pieces. If the focus is on process over product, then the product is more likely to end up being something that all students are proud of.

At least one student group will be deeply reluctant to abandon their unit 3 project. Ultimately it's your call to decide whether to allow that. If you do, be extremely clear with students about what additional features you expect them to implement. The rationale for having students start over in final projects is so that they can immediately learn from their mistakes and solidify their stronger understanding, rather than continue down unfruitful rabbit holes. 


## Launch

The main purpose of restarting projects for final project mode is to give students a chance to reflect on their experience leading up to this point, and use that reflection to guide their final project planning. 

Here are some realizations that it could be really helpful for students to have before they get too deep into building projects. 
* Turns out front-end design matters! Projects that were thoughtfully and carefully designed were the best received - HTML and CSS aren't actually less valuable or less important things to spend time on.
* An MVP crucially needs to have the most important feature, so we should build that feature first.
    * Corollary: one critical feature that works really well is much better than five nice-to-have features that are all a little buggy. 
* Almost everything took longer to build than we thought it would take. 
* Our database could have been better organized.

These revelations are less resonant when you simply hand them to students as truths, so you may want to nudge them in that direction with some discussion or reflection questions instead. Here are some examples of questions that can be helpful:
* Was there any other group whose project had features you wish your project had? What features were they? What would you need to learn or who would you need to ask in order to learn the skills you would need to implement those features?
* Is there anything you wanted to be able to do in a prior project that you weren't able to do? What else would you need to learn to be able to implement those features in your final project?
* What took longer than you expected? What was harder than expected?
* What small improvement or feature made the biggest difference to each of your previous projects? Can you plan to implement that small improvement or feature earlier this time around?
* What advice would you give your past selves about project 3 before starting to help make that process easier? Can you give a version of that advice to yourselves now?

Students can reflect on their previous projects before or after brainstorming final project ideas - as long as they reflect before they jump back into building again, the have a chance to save themselves repeating earlier mistakes. 

Brainstorming projects should follow the same general process students have used up to this point. That said here are some reminders and strategies that can help ease and expedite that process:
* Require students to brainstorm and submit a 1-sentence brief for 10-20 project ideas before allowing them pick just one. 
* Allow students to share unused ideas with other groups for those other groups to pick up or draw inspiration from. 
* Require students to plan extensively before allowing them to write their first line of code - tailor this requirement to whatever area you've observed most students struggle with. Often with advanced students, this tends to be front-end and design planning, as these are sometimes unhealthily viewed as lesser disciplines, so requiring students to create prototypes or mockups before starting to code can actually save them a lot of headache in the long run. 

## Recommended Benchmarks

While it's not required that you collect any student work beyond the project itself, sometimes requiring students to submit one or more of the following before they are allowed to log out of class can be an excellent way of ensuring that students are on track, and that they have a focus for their work on any given day. 

It's ultimately your choice as the instructor whether to communicate any of these as deadlines for your students, but if you find that your students respond well to incremental deadlines and daily expectations, these are good starting points. 

### MVP & Feature Road Map

Having students plan out what they can do in a single week as version 1, and then punting additional features to future versions can be a very powerful deliverable. Remember that student ambition is almost always unrealistic, so push them to narrow the scope of their first version as much as possible. 

Narrowing the scope of what students are shooting for is a low-risk proposition, and there aren't many downsides to scoping things too narrowly. If the goals are indeed too easy, then great, students can move on to additional features. On the other hand, scoping a first version that's unrealistically ambitious is really detrimental to team morale.

### Mockups / Design Prototype

Especially for students who proudly declare that they prefer writing back-end code, forcing an early deliverable about what the design of their web application will be can help serve as a reality check for them later. 

Without design goals to aim for and guidelines to get them there, most student projects will look somewhat web 1.0 or unintentionally brutalist. A template can help ease that pain a little bit, but with strong design plans, you can help students who don't want to write tons of front-end code to at least strive for a more intentional minimialism.

### Unit Tests

Requiring students to show off their unit tests early can be a super helpful way to ensure that these tests actually get written before the code does, rather than writing the tests after the fact to get the grade. 

### Database Model

This course assumes the simplest of database structures, but in the event where students are building a more robust back-end, you may want to require them to map that out more clearly and hand it in as a deliverable. 

### Working v1

Have students create a branch called v1 that is a fully functioning version of their application. Requiring students to create that branch and push it to GitHub early can not only help satisfy the requirements around version control, but also serves as a safeguard against students accidentally deleting their work.