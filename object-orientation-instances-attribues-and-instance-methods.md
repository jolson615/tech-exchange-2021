# Lesson Title

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

Students should be familiar with the basics of python, and have been introduced to unit testing. In this lesson, we will introduce a more advanced python topic: Object Orientation. The suggested breakdown of time for this lesson is:  
 5 min: Intro  
 40 min: Code-Along  
 10 min: Break  
 40 min: Lab  
 15 min: Debrief the lab and close out lesson  

### Teaching Tip

When teaching about classes, it is tempting to delve into the weeds about _object_, _self_, _init_, and other key components. However, this can be confusing for beginners. Instead, focus on walking students through the examples and helping them correctly employ the necessary syntax.

### Lab

This lesson includes a lab in which students will practice writing class definitions and creating instances of a class. The lab contains stretch challenges, but it is not necessary for all students to reach those portions.

## Objectives

* SW understand what Object-oriented programming is and why it is used. 
* SW create instances of a class.
* SW write class definitions, including an __init__, instance variables, and at least one instance method. 
* [STRETCH] SW use dunders to create private variables and write custom getter and setter methods. 

## Setup

Both the instructor and the students should open and work in Google Cloud Shell for this lesson.

Prior to beginning the lesson, the instructor should open a new python file and copy the launch code, below. 

```python
class Netflix(object):
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes

squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8)

print(squid_game.genre)
```

## Launch

Explain to students that today's class is focused on classes, which are one of the most useful and versatile parts of the python language. Classes are a way of packaging together information and functions in a way that is easy to use, reuse, and modify.

Show students the launch code. Explain that we have defined a class for Netflix original TV shows. Ask students to predict what will happen when the code runs.

Run the code. It prints "thriller", which is the genre of Squid Game. Try chaging the command to print bridgerton.genre and tiger_king.genre.

Ask students: how do you think we can print out "Tiger King"? Try the suggestions.

Ask students: What do you think the number "9" represents?
Answer: the number of episodes of Squid Game.


## The Lesson

### Defining Classes

Let's dive a little deeper into the code. Slack the code to all of the students so that they can see it on their screens and code along with you. It can be helpful to annotate the code with comments as you explain it.

This code has 2 different parts: first, we defined a class called Netflix in lines 1-5. This is basically a blueprint for Netflix shows. Each show is going to have a name, a genre, and a number of episodes.

Then, we used that class to create different variables representing specific Netflix shows. Each of these is called an "instance" of the class.

```python

# Defining the Netflix class
class Netflix(object):
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes

# Creating instances (specific examples) of the class
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8)

```

To define a class, we start with the word "class", the name of the class (usually capitalized, unlike python variables), 

#### Helpful Questions
* As many as needed

Repeat the topic-codeblock-questions loop as many times as needed to create the lesson.

## Extensions

Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* List
* At
* Least
* Five
* Extensions (roughly ascending difficulty)

## Related Resources

* [link text](linkurl) - What it is
* [link text](linkurl) - What it is
* [link text](linkurl) - What it is
