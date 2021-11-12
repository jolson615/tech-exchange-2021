# LAB TITLE

## Objectives

* Practice writing class definitions (including an __init__, instance variables, and instance methods)
* Modify and improve class definitions based on feedback from unit tests

**Core requirement:** Unless your teacher communicates otherwise, you must edit the pets.py file so that it passes at least the first 5 test_pets.py unit tests. 

## Context

You have just been hired by Pawsome Pets, a local animal shelter, to help all of their pets find forever homes! Currently, their file system is a mess, making it hard to know which pets have been adopted, which will be a good fit for potential owners, and how much food each pet needs. The shelter knows how they want the information to be organized, but they need your help to do it. You will be writing code in the pets.py file in order to pass the pre-written unit tests in test_pets.py.

## The Setup

Clone or import this lab to the coding environment of your choice.

Then, open up pets.py in your editor.

## The Lab

Open up pets.py in your editor. Run the unit tests by typing "python test_pets.py" into your command line. Follow the directions in the failure messages to improve your class definition in order to classify the shelter's pets. Note: be sure to check the top of the failure messages (you may need to scroll up)

For reference, these are some of the pets looking for pet-parents that will be used to test your code:
```python
self.pet1 = Pet("Clifford", "dog", ["brown", "white"], 7)
self.pet2 = Pet("Cleocatra", "cat", ["white", "orange"], 2)
self.pet3 = Pet("Tweetheart", "Bird", ["green"], 1.5)
self.pet4 = Pet("Nemo", "FISH", ["white", "orange"], 0.5)
self.pet5 = Pet("Donatello", "turtle", ["green"], 13)
```