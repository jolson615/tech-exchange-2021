# Lesson Title

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

Students should be familiar with the basics of python, and have been introduced to unit testing. In this lesson, we will introduce a more advanced python topic: Object Orientation.  

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

Explain to students that today's class is focused on classes, which are one of the most useful and versatile parts of the Python language. Classes are a way of packaging together information and functions in a way that is easy to use, reuse, and modify.

Show students the launch code. Explain that we have defined a class for Netflix original TV shows.

#### Helpful Questions

* Predict what will happen when the code runs.

Run the code. It prints "thriller", which is the genre of Squid Game. Try chaging the command to print bridgerton.genre and tiger_king.genre.
* How can we print out "Tiger King"?
* What do you think the number "9" represents?

## The Lesson

### Basic Class Walkthrough

Let's dive a little deeper into the code. Share the code with all of the students so that they can see it on their screens and code along with you. It can be helpful to annotate the code with comments as you explain it.

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

To define a class, we start with the word "class", the name of the class (usually capitalized, unlike python variables), and the word "object" in parentheses. Inside the class, we can define data (called "attributes") and fuctions (called "methods" if they are inside a class). This is a pretty basic class, so we have one method, called init, which stands for initialize. The init method is special-- it's the method that runs every time we create an instance of the class. It's like the boot-up code for each new Netflix show. Notice that the init method has 2 underscores before and after the word "init".

Every method is going to take in "self", which stands for the particular instance that we are creating. So for example, when we create squid_game, self represents squid_game. In this case, each method takes in 3 more attributes: the name of the Netflix Original show, the genre, and the number of episodes. Inside the init method, we set self dot each attribute equal to the attribute. This is basically a way of storing all of the information together in one object.

```python
# Defining the Netflix class
class Netflix(object):
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes

# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8)
```

After defining the class, we can use the class "Netflix" to initialize (create) specific instances of the class for specific shows. 

#### Helpful Questions
* How many instances have we created so far?
* How many attributes does each instance have?

#### Practice
Ask students to:
* Create at least 2 more instances of Netflix shows.
* Challenge: Modify the class to accept an additional attribute, recommend, a Boolean representing whether or not you would recommend the show. You will need to modify each of the instances of the class as well.

Some examples of additional instances are:
```python
bojack_horseman = Netflix("Bojack Horeseman", "cartoon", 49)
stranger_things = Netflix("Stranger Things", "sci-fi", 25)
too_hot_to_handle = Netflix("Too Hot to Handle", "reality TV", 19)
```
### Updating Values
What if Netflix releases a new season of Squid Game? We will need to update the number of episodes.

```python
print(squid_game.episodes)
squid_game.episodes += 10
print(squid_game.episodes)
```

 ### Methods

So far, class objects are a cute way to store data, but we could easily store the same information in dictionaries instead. The real advantage of classes is that they can perform actions (called methods) in addition to storing info. For example, if we want to print a bunch of recommendations for friends to try a certain show, we can define a method to do this:

```python
# Defining the Netflix class
# Defining the Netflix class
class Netflix(object):
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes
    def friend_rec(self, friend):
        return ("I really think that " + friend + " would love " + self.name)   

# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8)

print(tiger_king.friend_rec("Daphne"))
print(bridgerton.friend_rec("Joe"))
        
```

Note that we define our method inside of the class. The first parameter for the method is self, meaning that it applies to the particular instance of the class (aka one specific Netflix show). In this case, we are defining the method to also take a second parameter, the friend who we think should watch the show. 


#### Helpful Questions
* What do you think will happen when I run this code?
* How could I recommend Squid Game to Carole?
* Where have you seen this type of notation before?
Common answers: list/string methods! In python, lists and strings are class object that comes with predefined methods like list.append(), list.pop(), string.lower(), etc.

#### Practice
Ask students to:
* Write a method that returns "___ is my favorite show!" using the name of the show
* Write a method that returns a message based on the genre of the show (ex. if the genre is horror, return "This is too scary for me!!" and if the show is comedy, return "lol", etc.)
* Write a method that returns a randomly-selected episode number to watch


### Class Variables
So far, we have used the init function to assign a name, genre, and number of episodes to each Netflix show object when we create it. However, sometimes we have a variable that is the same for all or nearly all instances of the class. In that case, it would be tedious to have to type the same thing every time we create a new instance. Instead, we can define a class variable. For example, all of the shows we are looking at are on the Netflix network:

```python
# Defining the Netflix class
class Netflix(object):
    network = "Netflix"
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes
    def friend_rec(self, friend):
        return ("I really think that " + friend + " would love " + self.name)   

# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8)

print (squid_game.network)
print (bridgerton.network)
print (tiger_king.network)
```

### STRETCH: Dunders

This topic is not essential content, but it can be a great stretch topic for advanced students.

Most variables can be accessed and updated using dot syntax. For example, if a new season of Squid Game adds 10 more episodes, we can update the episode count:

```python
print(squid_game.episodes)
squid_game.episodes += 10
print(squid_game.episodes)
```

However, sometimes you want to make a variable that is not so easily manipulable, such as user data. In this case, we can use dunders (which stands for double underscores). Let's use dunders to hide an easter egg.

```python
class Netflix(object):
    network = "Netflix"
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes
        self.__easter = "secret message"
    
# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)

print(squid_game.__easter)
```

Running this code produces an error saying "'Netflix' object has no attribute '__easter'". In other words, we cannot read this dunder variable like we can a normal variable.

In order to read the secret message, we need a getter method, and to update it, we need a setter method:

```python
# Defining the Netflix class
class Netflix(object):
    network = "Netflix"
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes
        self.__easter = "secret message"
    def friend_rec(self, friend):
        return ("I really think that " + friend + " would love " + self.name)   

    def get_easter(self):
        return self.__easter

    def set_easter(self, value):
        self.__easter = value

print(squid_game.get_easter())
squid_game.set_easter("Green light... red light")
print(squid_game.get_easter())
```

#### Helpful Questions
* Why does squid_game.get_easter() end with parentheses?
get_easter() is a method rather than an attribute
* How would you set the Bridgerton easter egg to "I burn for you"?
* What sort of data would you expect to be stored using dunders? 

## Extensions

Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* Define a class called Celebrity that can be used to create objects representing famous people. The class should take at least 3 parameters: first name, last name, and type (actor/actress, politician, athlete, etc)
* Create at least 2 instances of the Celebrity class
* Define a property called "full_name" that combines the first and last names
* Write a method that greets the celebrity by name
* Write a method that returns an Onion (satire) headline based on the type of celebrity and using the celebrity's name
* Create a private variable to store a secret message to the celebrity

## Related Resources

* [Corey Schaffer Tutorial](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=1) - Excellent YouTube playlist that discusses Object Oriented Programming (OOP) including classes
* [Codecademy Tutorial](https://www.codecademy.com/courses/learn-python/lessons/introduction-to-classes) - Tutorial that walks through creating and using classes. You will need to create a free account.
* [W3 Schools Classes/Objects](https://www.w3schools.com/python/python_classes.asp) - Provides examples demonstrating proper syntax for creating and using classes
