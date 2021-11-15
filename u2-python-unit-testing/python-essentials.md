# Python Essentials

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

### Why Python?
In our last unit, we used HTML/CSS to build front end products: that is, something that users can see and interact with directly. Now, we’re going to be learning Python, which is commonly used to program the back end of web apps: the internal logic that users don't see (think the Netflix algorithm that decides which shows to recommend you). Python is a high-level object-oriented programming language with several features that make it accessible to beginners.  It's also among the most popular and in-demand languages. For example, Netflix, Instagram, and Spotify are all coded using Python. Python is used for web development, especially for managing a backend database using frameworks like Django or Flask.  Python is commonly used in data analysis and visualization, especially in medicine and financial services.

Python was designed to be highly readable: the syntax is relatively simple, keywords are intuitive (and, or, try, etc), and the use of whitespace means that code is consistently formatted.  Python also has strong documentation and an active community.  It's very likely that a stack overflow search for a Python question will yield multiple relevant results.  Finally, Python supports a large number of libraries that extend its functionality.

### Goals of this Unit
We will be using Python to develop projects that use the Cloud Shell (or local IDE) command line for user interaction.  The unit will focus on three main topics: Python Syntax (how to type Python code), Object Orientation (how to organize Python code), and Test Driven Development (how to leverage unit tests to plan and assess Python code).

The concepts and skills practiced in the unit will directly apply to the following unit, where we will combine our knowledge of python and HTML to build full stack applications.

### Embrace Errors
Working with the Python command line, students will see frequent errors.  It's important to frame this ahead of the lesson: errors are a way for your development environment to give you feedback on what your code is doing.  We will learn a lot about how data types and functions work by carefully reading the error messages in our console.  Responding to errors (and eventually anticipating them) is an important part of learning to code in Python, rather than a sign that you are on the wrong track.

## Objectives
* SW initialize variables with floats, integers, booleans, and strings.
* SW create lists and dictionaries to store related information
* SW use basic control flow (if, elif, else, and for loops) to perform simple tasks
* SW create custom functions to help write DRY (don't repeat yourself) code
* SW learn to raise valueType errors 

## Setup
We will be experimenting with the most common data types and using variables and functions to make a simple state capital quiz.  The first part of this lesson is a code-along interspersed with questions and analysis; we are building a shared vocabulary around Python.  The second part of the lesson is a group coding challenge: to create a state capital quiz using what we know about Python so far.

## Launch
Debugger (or other problem-solving games) are a great launch activity for this topic, because problem-solving games can highlight how errors or incorrect answers can lead you to a solution.

The goal of the lesson is to develop a state capitals quiz using the command line interface.  This is a great introductory project because it touches on a lot of the core concepts (data types, functions, and control flow) that we will be using in all our subsequent Python projects.

## The Lesson

### Variables
To initialize a variable in Python, you write the variable name, an equals sign, and the value you want to assign to it.  Following the example below, create another state profile by initializing variables and assigning them values.

```python
state_name = "Massachusetts"
state_capital = "Boston"
state_population = 7033469
state_land_area_square_miles = 7800.06
international_borders = None
contiguous_state = True
```

#### Helpful Questions
How are the variable names formatted?
The above variable names state_name, state_capital, etc follow the python convention for naming variables: all lowercase letters, with underscores separating words.  This convention is called snake case.

What happens when you remove the "" around Massachusetts?
Note that to assign state_name the value Massachusetts, I had to wrap Massachusetts in quotation marks.  This data type, storing a sequence of characters, is called a string.  In Python, single characters are still considered strings.  Strings can use single and double quotes largely interchangeably (with the exception of strings containing ‘ or " symbols as characters).

Writing state_name = Massachusetts without quotes would throw an error:
NameError: name 'Massachusetts' is not defined

The development environment expects that a series of characters without quotes is a variable name.  Since there is no variable named Massachusetts, the program throws a name error.  The console helpfully notes what line the error occurred on.

What other data types are we assigning to variables besides strings?
Integers, numbers with a decimal (called floats), True/ False (boolean values), and None.  The variables None and True are not strings so they are not wrapped in quotation marks.

### Printing to the console
Python has a built-in function named print() that displays values to the console.  Functions in Python always follow this format, where you type the function name immediately followed by a pair of parentheses.  When a function accepts an argument (in this case, the value to be printed) that argument goes between the parentheses.

To display the value of a variable to the console, type:

```python
print(state_name)
print(state_population)
```

You can label your print statements to make them more readable.
Use + to combine strings (called concatenation).
Use , to separate multiple values to be printed.
Use the keyword f to format other data types into a string, nesting values within {}

```python
print("State Name: " + state_name)
print("State Population: ", state_population)
print(f"The state of {state_name} has {state_population} residents")
```
Print the information from your state profile to the console.

#### Helpful Questions
Which method of adding string labels to your print statements was most intuitive?  Which seems most flexible.
Note the concatenation (+) only works when all values are strings.  The use of multiple comma-separated values is easy, but limits your formatting options.  The use of string formatting (f) is most flexible but is more syntactically complex as it depends on proper placement of f, "", and {}.

What interesting errors did you encounter?  What can we learn from them?
There are many possibilities.  Common errors include attempting to concatenate a data type other than string and not closing " or {

### Data Types and Casting

Python has another built in function named type() which outputs the datatype of a value.
```python
print(type(state_name))
print(f"The variable state_population is a {type(state_population)}")
```
Identify which data types we have seen so far.  There may be instances where you want to change the datatype of a value.  For example, turning an integer into a string to print it or turning a float into an integer.  Changing the data type of a value is called casting.

```python
zipcode = "02101"
numeric_zipcode = int(zipcode)
print("The variable state_population is " + str(state_population))
```
#### Helpful Questions
What happens when you cast a float to an integer?  What effect might this behavior have?
The partial number value is dropped, so you could lose accuracy.

### Lists
Lists are a data type that can store multiple ordered values.  Each value in a list is separated by a comma.  You can reference elements of a list by their index: 0,1,2, etc.  You can also reverse index a list: -1 represents the last element of a list (regardless of its length).

List methods are a set of specialized functions that act on lists.  A few examples:
* .append() adds an element to the end of a list
* .pop() removes an element from the list (either from the end or from a specified index)
* .sort() sorts the list

```python
largest_states = ["Alaska", "Texas", "California", "Montana", "New Mexico"]
print(largest_states)
print(type(largest_states))

print(largest_states[0])
print(type(largest_states[0]))

largest_states.append("Arizona")
print(largest_states)
print(largest_states[-1])
```
Try it out:
* Create a list of the three most populous states.
* Create another list of those states’ capitals.
* Append the fourth most populous state.
* Sort the list.
* Remove the first element from the list.
* Print each of the states in the list.

#### Helpful Questions
How does sort sort?  Did you try it with strings and numbers?
Ascending numerical or alphabetical order.  You can set it to reverse sort and sort by length with optional arguments.

What happens when you attempt to reference index 5 of a list with 5 elements?
You get an index out of range error. The last index in a 5 element list is 4.
What happens if you try to access the index of a string?

Strings can be indexed in Python and iterated through in a manner similar to lists.
What are the risks of accessing states and capitals in two lists?
Since there is no relationship between the two lists, changes in one list are not reflected in the other.  Sorting or editing the lists would throw off all the data. We will need another data type that is able to preserve the state/capital relationship.

### For Loops and Conditionals
In order to print every element in our list of the most populous states, we needed to write repetitive code.  This goes against a principle of effective coding: to write DRY (don't repeat yourself) code.  One way to more efficiently iterate through the elements of a list is with for loops.

```python
largest_states = ["Alaska", "Texas", "California", "Montana", "New Mexico"]
for state in largest_states:
	print(state)
```

For loops are also useful for accessing integers in a given range.

```python
for num in range(100):
	print(num)

for num in range(100,1000,5):
	print(num)
```

When iterating through a list with a for loop, you may not want to access every value the same way.  Conditional statements (if, else, elif) become very useful in this context.

```python
population_counts = [	39538223, 29145505, 21538187, 20201249, 13002700, 12812508, 11799448, 10711908, 10439388, 10077331, 9288994, 8631393]
for count in population_count:
	If count > 30000000:
print("Over thirty million")
elif count > 20000000:
print("Over twenty million")
else:
print("Under twenty million" )
```

Note that indenting is very important in the use of for loops and conditionals.  Everything included in the loop must be indented, and the conditional statements after each if/else statement must be indented.  If a line is not indented, it will be treated independently rather than as part of the for loop.

Using for loops and conditionals:
For each of the most populous states, print the first letter in the state name.
Print every even number from 1 to 50.
For the list of the largest states, print only those in the contiguous United States.

#### Helpful Questions
How would you print every even number between 1 and 50 (including 50)?
for num in range(2,51,2):
	print(num)

How would you decrement with a for loop?
for num in range(100,1,-1):
	print(num)

### Dictionaries
Dictionaries are a changeable data type that stores data as key value pairs.  Like lists, dictionaries are ordered (as of Python version 3.7).  Dictionary keys must be of an immutable type (integer, string, boolean, float) but strings are the most common.  Dictionary values may be of any data type.  Key value pairs are matched with a colon and each pair is separated by a comma.

```python
largest_states_dict = {
"Alaska" : 665384.04,
"Texas" : 268596.46,
"California" : 163694.74
}

largest_states_dict["Montana"] = 147039.71

for state in largest_states_dict:
	print (f"{state} has  {largest_states_dict[state]} residents")
```
Create a dictionary of the three most populous states and their capitals.
Print a formatted string listing the capital of each state in the dictionary.

#### Helpful Questions
What happens if you create two keys with the same value?  Why do you think this happens?
The second instance will override the first.  Since dictionaries are primarily accessed through keys, each key name must be tied to only one value.

When would you prefer to use a dictionary over a list?  When would you want to use a list rather than a dictionary?
You might prefer to use a list to store many similar properties (e.g. months in a year) and a dictionary when organizing two related properties (name:age, state:capital, number:month).

### Functions
So far, the code we have written has run more or less linearly.  The potential for this type of program is limited.  Functions allow us to write code that executes only when called and can be easily repeated.

Functions are defined using the keyword def, followed by the function name, immediately followed by a pair of parenthesis.  Any values that are passed into the function are placed between the parentheses.  These are the function's parameters.  The above function has one required parameter (called this_list) though functions may have none or several (separated by commas).

Functions often have a return value, which can be assigned to a variable.  For example:

```python
numbers_list = [0, 1000, -50, 22, 333]

def sum_values(this_list):
	""""Sums the values of all elements of a list"""
	running_sum = 0
	for var in this_list:
		running_sum += var
		print("Running sum: ", running_sum)
	return running_sum

sum_of_list = sum_values(numbers_list)
print("Sum of List: ", sum_of_list)
```

We are going to need at least two functions for our state capitals quiz: one to select a random state from our dictionary and another to compare a user guess to the random state's capital.

To select random keys from our dictionary, we will need to import a Python library named random, specifically the method random.choice().  The use of libraries is a common way to extend Python's features.  Although dictionaries are ordered in Python, you cannot index them as easily.  One way around this is to cast the keys into a list when you are selecting them at random.

```python
import random

states_dict = {
"Alaska" : 665384,
"Texas" : 268596,
"California" : 163694
}

def random_state():
	"""Returns a randomly selected key from the dictionary states_dict"""
state_list = list(states_dict.keys())
state = random.choice(state_list)
return state

print(random_state())
```

To gather input from the user, we need to use the built-in function input() which is the inverse of print().  input() allows you to take in a string from the command line and assign it to a variable in your code.  Providing a string argument to the input function provides the user a prompt on the command line to respond to.  This highly specific function isn't very flexible.  Try using it as a template to define a function that asks the user to guess the capital of a given state.

```python
def guess_the_population_of_alaska():
	"""Compares a user input to the population of Alaska"""
	pop = states_dict["Alaska"]
	guess = input(f"What is the population of Alaska? ")
	print(f"You guessed {guess}.  The population of Alaska is {pop}")

guess_the_population_of_alaska()
```

#### Helpful Questions
What happens when you assign a function without a return statement to a variable?
Functions without a return statement return None.
Which built in functions [print(), input(), len()] return a value and which do not?
Input and len have a return value but print does not, as its primary function is to display information to the console.
When should a function have a return statement?
When you want to store or otherwise reference the function's output.

### State Capitals Quiz
We are going to use our knowledge of Python dictionaries and functions to create a state capitals quiz game.

To develop the game:
Create a dictionary with state:capital key value pairs.  You can start with only a few state:capital pairs while you test your program.
Create a function that selects a random state from your dictionary.
Create a function that prompts a user to input their guess for the random state's capital and prints a response if the user's guess is correct.

Optional: depending on the level of your students, you may want to show some or all of them this example, or you may choose to have them start pair programming without it. The example below quizzes the user on state populations (an unlikely quiz topic).  Use the structure as a template to get started on your state capitals quiz.

```python
import random
states_dict = {
"Alaska" : 665384,
"Texas" : 268596,
"California" : 163694
}

def random_state():
    state_list = list(states_dict.keys())
    return random.choice(state_list)

def new_question():
    state = random_state()
    guess = input(f"What is the population of {state}? ")
    if guess == states_dict[state]:
        print(f"Correct! {states_dict[state]} is the population of {state}!")

new_question()
```

#### Helpful Questions
Why use a dictionary to store states and capitals rather than a list?
A dictionary preserves the relationship between keys and values even if the contents of the dictionary is changed.

Why use separate functions for retrieving a random state and getting user input?
Programming is easier to read and revise when you maintain separation of concerns: meaning that each element of a program (like a single function) serves a distinct purpose.

## Extensions
* Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* Use if/else statements to print a different response for correct and incorrect guesses.
* Use a for loop to call the new_question() function more than once, so the user can play multiple rounds.
* Use the del keyword to remove states from the dictionary that have been guessed correctly.
* Initialize a score variable that tracks correct guesses.  Report the user's score after the final round of the game.
* By default, string comparisons are case sensitive.  Use the .lower() method to adjust for this.
* Add a hint system that provides the first letter of the state capital when users input "hint".

## Related Resources
[w3 schools python data types](https://www.w3schools.com/python/python_datatypes.asp)
[w3 schools python lists](https://www.w3schools.com/python/python_lists.asp)
[w3 schools python for loops](https://www.w3schools.com/python/python_for_loops.asp)
[w3 schools python dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
[w3 schools python functions](https://www.w3schools.com/python/python_functions.asp)
