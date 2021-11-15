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

When teaching about classes, it is tempting to delve into the weeds about _object_, _self_, _init_, and other key components. Inheritance also feels crucial to many veteran programmers. However, these more abstract concepts are usually a really confusing entry point for beginners. 

Instead, focus on walking students through the examples here, which focus narrowly on instances, attributes, and instance methods, and helping them correctly employ the necessary syntax.

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
    """A class used to represent Netflix original series"""
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

Today, we are going to make a database of our favorite Netlfix shows with relevant data like genre and episode count.  However, making a long list of variables or even dictionaries would make it hard to reference all the relevant information for one show. In order to be able to easily organize, access, and use the info for each show, we're going to use Python classes.

Classes are one of the most useful and versatile parts of the Python language, because they let us package together information and functions in a way that is easy to use, reuse, and modify.

Show students the launch code. Explain that we have defined a class for Netflix original TV shows.

#### Helpful Questions

* Predict what will happen when the code runs.

Run the code. It prints "thriller", which is the genre of Squid Game. Try changing the command to print bridgerton.genre and tiger_king.genre.
* How can we print out "Tiger King"?
* What do you think the number "9" represents?
* Why are classes a useful way of organizing this information? 
* How are class objects different from dictionaries?

## The Lesson

### Basic Class Walkthrough

Let's dive a little deeper into the code. Share the code with all of the students so that they can see it on their screens and code along with you. It can be helpful to annotate the code with comments as you explain it.

This code has 2 different parts: first, we defined a class called Netflix in lines 1-5. This is basically a blueprint for Netflix shows. Each show is going to have a name, a genre, and a number of episodes.

Then, we used that class to create different variables representing specific Netflix shows. Each of these is called an "instance" of the class.

```python
# Defining the Netflix class
class Netflix(object):
    """A class used to represent Netflix original series"""
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes

# Creating instances (specific examples) of the class
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8)
```

To define a class, we start with the word "class", the name of the class (usually capitalized, unlike python variables), and the word "object" in parentheses. Inside the class, we can define data (called "attributes") and functions (called "methods" if they are inside a class). This is a pretty basic class, so we have one method, called init, which stands for initialize. The init method is special-- it's the method that runs every time we create an instance of the class. It's like the boot-up code for each new Netflix show. Notice that the init method has 2 underscores before and after the word "init".

Every method takes in the parameter "self", which stands for the particular instance that we are creating. So for example, when we create squid_game, self represents squid_game. In this case, each init method takes in 3 more attributes: the name of the Netflix Original show, the genre, and the number of episodes. Inside the init method, we set self dot each attribute equal to the attribute. This is basically a way of storing all of the information together in one object.

```python
# Defining the Netflix class
class Netflix(object):
    """A class used to represent Netflix original series"""
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
* How is this different from storing information in lists or dictionaries?
* What would happen if you entered the object parameters in a different order (i.e. 8, "Tiger King", "true crime")?

#### Practice
Ask students to:
* Create at least 2 more instances of Netflix shows.
* Modify the class to accept an additional attribute, recommend, a Boolean representing whether or not you would recommend the show. You will need to modify each of the instances of the class as well.
* Challenge: Add a default value for number of episodes, set to 0. Then try creating a new instance of the show without passing in the number of episodes. Print the number of episodes-- it should be 0 without needing to type anything!

Some examples of additional instances are:
```python
bojack_horseman = Netflix("Bojack Horseman", "cartoon", 49)
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

So far, class objects are a cute way to store data, but we could easily store the same information in dictionaries instead. The real advantage of classes is that they can perform actions (called methods) in addition to storing info. For example, we can add an attribute for cast and create a function that will print all of the members of the cast:

```python
# Defining the Netflix class
class Netflix(object):
    """A class used to represent Netflix original series"""
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes, cast=[]):
        self.name = name
        self.genre = genre
        self.episodes = episodes
        self.cast = cast
    def roll_call(self):
        """A method that returns a string that identifies the show's cast members"""
        starring = self.name + " stars: "
        for person in self.cast:
            starring += person
            starring += ", "
        return(starring)  

# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8, ["Joe Exotic", "Carole Baskin", "Doc Antle", "John Finlay"])

print(tiger_king.roll_call())  
```

Note that we define our method inside of the class. The first parameter for the method is self, meaning that it applies to the particular instance of the class (aka one specific Netflix show). When calling the method, we use parentheses after the method name, but we don't need to type "self". 


#### Helpful Questions
* What do you think will happen when I run this code?
* Where have you seen this type of notation before?
Common answers: list/string methods! In python, lists and strings are class objects that come with predefined methods like list.append(), list.pop(), string.lower(), etc.

#### Methods with Additional Parameters
We can also define a method that takes in an additional parameter. For example, let's make a method that adds a cast member:

```python
# Defining the Netflix class
class Netflix(object):
    """A class used to represent Netflix original series"""
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes, cast=[]):
        self.name = name
        self.genre = genre
        self.episodes = episodes
        self.cast = cast
    def roll_call(self):
        """A method that returns a string that identifies the show's cast members"""
        starring = self.name + " stars: "
        for person in self.cast:
            starring += person
            starring += ", "
        return(starring) 
    def add_cast(self, actor):
        """Method that checks if an actor is in the cast and if not, adds them"""
        if actor not in self.cast:
            self.cast.append(actor)

# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8, ["Joe Exotic", "Carole Baskin", "Doc Antle", "John Finlay"])

tiger_king.add_cast("Joe Exotic")
tiger_king.add_cast("Jeff Lowe")
print(tiger_king.roll_call()) 
```

#### Practice
Ask students to:
* Write a method that returns "___ is my favorite show!" using the name of the show
* Write a method that returns a message based on the genre of the show (ex. if the genre is horror, return "This is too scary for me!!" and if the show is comedy, return "lol", etc.)
* Write a method that takes in a friend's name and returns a string recommending that they watch the show
* Write a method that returns a randomly-selected episode number to watch (based on the number of episodes that exist)
* Challenge: Fix the roll_call method so that it doesn't print a comma after the last cast member


### Class Variables
So far, we have used the init function to assign a name, genre, and number of episodes to each Netflix show object when we create it. However, sometimes we have a variable that is the same for all or nearly all instances of the class. In that case, it would be tedious to have to type the same thing every time we create a new instance. Instead, we can define a class variable. For example, all of the shows we are looking at are on the Netflix network:

```python
# Defining the Netflix class
class Netflix(object):
    """A class used to represent Netflix original series"""
    network = "Netflix"
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes, cast=[]):
        self.name = name
        self.genre = genre
        self.episodes = episodes
        self.cast = cast

# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)
bridgerton = Netflix("Bridgerton", "romance", 8)
tiger_king = Netflix("Tiger King", "true crime", 8, ["Joe Exotic", "Carole Baskin", "Doc Antle", "John Finlay"])

print (squid_game.network)
print (bridgerton.network)
print (tiger_king.network)
```

### STRETCH: Dunders & Private Variables

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
    """A class used to represent Netflix original series"""
    network = "Netflix"
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes, cast=[]):
        self.name = name
        self.genre = genre
        self.episodes = episodes
        self.cast = cast
        self.__easter = "secret message"
    
# Creating instances (specific examples) of the class
# The __init__ method runs each time
squid_game = Netflix("Squid Game", "thriller", 9)

print(squid_game.__easter)
```

Running this code produces an error saying "'Netflix' object has no attribute '__easter'". In other words, we cannot read this private variable like we can a normal variable.

In order to read the secret message, we need a getter method, and to update it, we need a setter method:

```python
# Defining the Netflix class
class Netflix(object):
    """A class used to represent Netflix original series"""
    network = "Netflix"
    # The __init__ method runs whenever we create a new instance of the class
    def __init__(self, name, genre, episodes):
        self.name = name
        self.genre = genre
        self.episodes = episodes
        self.cast = cast
        self.__easter = "secret message" 

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
* [Object Documentation Conventions](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings) - Shows how to document code properly using docstrings
