# Test-Writing Lab: Python Calculator

## Objectives

* Write unit tests to catch errors in pre-written code
* Write unit tests to check for value errors and type errors
* Create a functional command-line calculator

**Core requirement:** Unless your teacher communicates otherwise, you must complete at least the first 6 functions.

## Context

We're trying to program a python calculator by creating functions that can add, subtract, multiply, divide, and perform other useful calculations. However, some of our functions are not working! Your job is to write unit tests for each function. Make sure to test both the accuracy of the functions and the proper raising of value and type errors.

## The Setup

Clone or import this lab to the coding environment of your choice.

Open calculator.py and test_calculator.py. You will need to write unit tests in test_calculator.py to test each of the calculator functions. Based on the results of your unit tests, edit the functions in calculator.py to give accurate answers and raise appropriate errors.

## The Lab

### Function 1: Addition
* Write unit tests in test_calculator.py to check the accuracy of the add function
* Write unit tests to check that a type error is raised when an input is not an integer or a float
* Edit the add function in calculator.py in order to pass all tests

### Function 2: Subtraction
* Write unit tests to check the accuracy of the subtract function
* Write unit tests to check that a type error is raised when an input is not an integer or a float
* Edit the subtract function in order to pass all tests

### Function 3: Multiplication
* Write unit tests to check the accuracy of the multiply function
* Write unit tests to check that a type error is raised when an input is not an integer or a float
* Edit the multiply function in order to pass all tests

### Function 4: Division
* Write unit tests to check the accuracy of the divide function
* Write unit tests to check that a type error is raised when an input is not an integer or a float
* Write unit tests to check that a value error is raised when dividing by zero
* Edit the divide function in order to pass all tests

### Function 5: Tip Calculator
* The tip function should take in a bill amount and a tip percentage and return the total amount to be paid, but it isn't quite working properly. Write unit tests to check the accuracy of the tip function
* Write unit tests to check that a type error is raised when an input is not an integer or a float
* Edit the tip function in order to pass all tests

### Function 6: Scrabble Word Value
* The scrabble_value function should take in a word as a string and return the value of that word in scrabble tiles (tile values are given in the letter_value dictionary in scrabble.py). Write unit tests to check the accuracy of the scrabble_value function
* Write unit tests to check that a type error is raised when an input is not a string
* Write unit tests to check that a value error is raised when the word length is impossible
* Edit the scrabble_value function in order to pass all tests

### Function 7: Taxi Cost Estimator
* The taxi function should take in a distance (in miles) and and a time spent stopped (in minutes) and return the cost of taking a taxi. Taxis cost $2.50 plus 50 cents per 0.2-mile plus 50 cents for each minute of standing. The pre-written function is giving some strange results. Write unit tests to check the accuracy of the taxi function
* Write unit tests to check that a type error is raised when the input types are incorrect
* Edit the taxi function in order to pass all tests

### Function 8: Scientific Notation Converter
* The scientific_notation function should take in a number and convert it into scientific notation. However, it's returning values in standard notation! Write unit tests to check the accuracy of the scientific_notation function
* Write unit tests to check that a type error is raised when the input type is incorrect
* Edit the scientific_notation function in order to pass all tests

### Function 9: Getting Numbers from the User
* The get_numbers function should ask the user to input two different numbers and return those numbers as a list of numbers, which can be input into one of the previously-defined functions. Right now it's not working properly with the otehr functions. Write unit tests to check the accuracy of the get_numbers function
* Write unit tests to check that a type error is raised when the input type is incorrect
* Edit the get_numbers function in order to pass all tests

### Function 10: Getting Numbers from the User
* The get_numbers function should ask the user to input two different numbers and return those numbers as a list of numbers, which can be input into one of the previously-defined functions. Right now it's not working properly with the otehr functions. Write unit tests to check the accuracy of the get_numbers function
* Write unit tests to check that a type error is raised when the input type is incorrect
* Edit the get_numbers function in order to pass all tests

### Check your calculator!
* Uncomment the function call at the end of calculator.py and run "python calculator.py" to see your calculator in action!
* The calculator works, but using the tip and taxi functions is confusing. Edit your calculate() function to improve the user experience.
* Edit the code so that after a calculation, the calculator asks the user if they would like to perform another calculation