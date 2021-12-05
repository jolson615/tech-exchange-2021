# Unit 2 Project: Build a Back-End

### Student-facing Materials

1. [Objectives](#objectives)
2. [What We’re Building](#building)
3. [Requirements](#requirements)
4. [Exemplar](#exemplar)


### Teacher-facing Materials

5. [Teaching Tips](#teaching-tips)
6. [Launch](#launch)
7. [Recommended Benchmarks](#recommended-benchmarks)

# Student-facing Materials

## Objectives

* Write a command line Python application that could serve as the back end to your front end website
* Practice Test-Driven Development by writing unit tests before writing the code of the application
* Practice collaboration by writing unit tests to be used by a teammate
* Write code to pass another teammate's tests
* Gain practical knowledge of functions and objects in the context of a complex program
* Organize your code, separating concerns whenever reasonable

## What We’re Building <a id="building"></a>

In the first project, you and your team built a front end website for a potential business. Now, you will be building a back end in Python which could be used to support your business. You don't need to actually combine the front and back end, but it can be useful to think about how they relate (for example, "our website shows the different rubber ducks that are available for purchase, so we should design an inventory system that keeps track of their price and how many of each we have currently available"). If your team prefers to pivot to a new business idea, that is fine as well. The goal is to improve your Python skills and use Test Driven Development practices to guide your coding.

There are several routes that you can take for creating a back-end Python program to support a business:
* Creating a product management system for a store
* Creating a social networking program where users can interact with each other (for this project, focus a text-based prototype. A well-written basic framework is relatively easy to transition into a more visual web app if you have rigorous unit testing)
* Creating a simulator (for example, a movie theater might use a simulation of patrons in line to buy tickets in order to determine the optimal way to set up the ticket windows)
* Creating a recommender or matching algorithm (think Netflix show recommendations)
* [STRETCH] Combining any of the above with an API to expand your project scope

In order to adhere to Test Driven Development practices, your team should write unit tests for your key functions and classes BEFORE coding them. Following industry best-practices, you should each write code to be tested by a different team member's tests. 

## Requirements

Each group's project must demonstrate each of the following:
* A functional program that could be used to help a business organize information or serve clients
* Unit tests that verify accuracy, type errors, and value errors, for at least 3 different functions or classes
* Code that satisfies each unit test, written by a different team member
* Proper separation of concerns
* You must make something you're proud of!


## Exemplar

Before launching into your projects, you may want to take a moment to review the exemplar project. Reviewing an exemplar can help you make sure that the expectations you're placing on yourself are in line with the expectations of this course, so that you don't end up accidentally turning significantly more or less than is expected for this unit project.

### Example 1: Bookery Back-end Bookshelf

One great place to start coming up with ideas for the Unit 2 project is to think back to your Unit 1 project and thing about features that business might want to augment with technology. Sure, the business idea is just about getting books in the hands of customers, but this command line application lays the basis for how a user could create and organize their own bookshelf, which could be a powerful next step for the business, especially if the purchases of books could be used to create new books and store them on a user's digital shelf. 

* Unit Project Exemplar Code: [Bookshelf](u2-python-unit-testing/tdd-python-project-exemplar-bookshelf)
* Unit Project Exemplar Deployed Preview: [Deployed Bookshelf](https://replit.com/@jolson615/tdd-python-exemplar-bookshelf#main.py)

Especially if your unit project idea from Unit 1 is the sort of thing that could use an interactive component, you may want to use this as a jumping off point. 

### Exemplar 2: Text-based RPG

While you're encouraged to relate this project to your unit 1 project, you certainly don't have to. Here's an exemplar of a command line application that meets the requirements of this project, but isn't strictly in line with the bookstore app from unit 1. 

* Unit Project Exemplar Code: [Text-based RPG](u2-python-unit-testing/tdd-python-project-exemplar-rpg)
* Unit Project Exemplar Deployed Preview: [Deployed Text-based RPG](https://replit.com/@jolson615/Sample-CLI-text-based-rpg)

NOTE: If you prefer to go this route where your Unit 2 project diverges significantly from your Unit 1 project, you are encouraged to ask either your teacher or project advisor first before beginning work. 


# Teacher-facing Materials


## Teaching Tips

The prompt is for students to create a back end that could support their business website (the previous project), but it is fine for groups to pivot to a new business idea, as long as they create a project that allows them to practice TDD and improve their technical skills in Python. It's important to frame this project as a piece of the puzzle rather than a standalone project. The focus here is to create the underlying logic to organize and utilize key information (such as product stock or user accounts), rather than to create a standalone project that would be accessed by users.

This is students' second time creating a project together, so they should be a little more comfortable working together. On the other hand, any friction that groups experienced in the first project could be exacerbated, so it's especially important to keep a close eye on any groups that struggled with teamwork during the first project. Groups with especially divergent skill levels can also be a challenge to manage. For students with more prior knowledge, it can be helpful to frame the group work as an opportunity to act as a senior developer, whose job is to lead the team and help their teammates learn the skills they need, NOT to code the whole project on their own.

With this project, groups that finish the basic version early may struggle to come up with ideas for how to expand their project. The instructor can be particularly helpful in giving ideas for stretch goals for these groups.

As with the first project, it is very helpful for the instructor to rotate through the breakout rooms to see what students have done so far, and check in with any groups that don't meet benchmark goals. It is essential that each student has a role and is contributing code to the project in order for them to learn as a programmer and feel proud of their accomplishments.

## Launch

Allow groups time to decide whether to continue using their business idea from project 1, or switch to a different idea. Encourage groups to come up with a 1-2 sentence statement of purpose ("This pet playdate system will store user information for different pets and allow them to interact by sending each other messages, barking, meowing, or tail wagging. It will also keep track of the petPoints (in-app currency) for each user and allow them to redeem petPoints for treats.")

Once they have a statement of purpose, teams should identify 3 key functions/classes, as well as a basic idea of how those components would be combined to generate the overall functionality. Guide students through setting up their files and determining who will write each unit test and the corresponding function/class. Students should begin the coding process by writing unit tests.

## Recommended Benchmarks

While it's not required that you collect any student work beyond the project itself, sometimes requiring students to submit one or more of the following before they are allowed to log out of class can be an excellent way of ensuring that students are on track, and that they have a focus for their work on any given day. 

It's ultimately your choice as the instructor whether to communicate any of these as deadlines for your students, but if you find that your students respond well to incremental deadlines and daily expectations, these are good starting points. 

### Statement of Purpose and Key Code Structures

Have students submit their statement of purpose, a list of 3 key functions/classes (name and a docstring that describes the functionality), and a short paragraph explaining how these code structures will fit together to generate the overall program. A Google form can be a great way to collect this information.

### Unit Tests

Have students write unit tests for each of their key code structures. Each student should write at least 1 unit test.

### Passing the Unit Tests

Have students write code that passes each of the unit tests. Each student should write code to pass a different student's test.

### Division of Responsibilities

As with Project 1, this is a good one to do every single day if students are struggling to allocate work equally. Have each student commit to their peers in writing what work they'll do before the next class. For this project, students should evenly divide up the responsibilities for writing unit tests and the accompanying code. Emphasize that the process of each student practicing coding in Python and using TDD is more important than the final product. 

### First Draft Mini-Presentations

Have groups give short presentations to each other on the programs they have written so far. Emphasize that the programs do NOT need to be finished and one of the most important parts of the presentation is outlining "next steps". For groups that finish implementing their basic ideas, this can be a great way to get ideas for stretch goals. 
