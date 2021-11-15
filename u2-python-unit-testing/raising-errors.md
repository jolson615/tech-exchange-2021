# Raising Errors, Unit Testing, and Separation of Concerns

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context
Our last lesson asked us to write functions that passed pre-written unit tests.  Today we’ll be writing our own unit tests and then writing functions that pass those tests.

### Test-driven Development
The core practice of test driven developments is writing tests before you write the code those tests evaluate.  Connected to this practice are a wider set of principles and mindsets.  Starting the development process with testing means that developers are anticipating errors as part of their process.  Test driven development also encourages programmers to work in smaller, more focused steps, writing just the code they need to pass the next unit test.

### Separation of Concerns
Separation of concerns is a design principle for dividing programs into distinct sections.  On the function level, this means writing functions that perform a distinct operation.  Complex operations with many inputs and outputs should be divided into a series of functions.  On a higher level, functions without a related purpose should be written in separate files.  This practice makes code much easier to read and revise.

## Objectives
* SW Learn to raise additional errors beyond valueType errors. 
* SW understand what unit tests are, why they are written, and how they help teams collaborate effectively. 
* SW understand why large projects are broken up into different files, and how those divisions are decided.
* SW write unit tests for Python functions. 
* SW document their unit tests and provide helpful failure and success messages.

## Setup
Students will need to create a folder in their development environment to hold the various files we will be creating and writing to.

## Launch

Let's play Break the function.  Edit any element of broken_function except its name.  Call it with any arguments you choose.  The goal is to get your development environment to throw as many different errors as you can in the time frame.

```python
def broken_function(string, integer):
return None
```

Discuss the errors you discover.  What do the error messages you read tell you about how Python functions work?

In today's lesson we are going to crowdfund our own board game, but to do so we need to figure out how many backers we will need in order to break even.  We are going to develop cost estimates using a series of functions.  To ensure these functions work as intended, we will follow the principles of Test Driven Development.  Our approach will be similar to playing break the function, except instead of trying to cause errors, we think about what errors are possible and plan to account for them.  We can't prevent all errors, but proper error handling can make errors easier to detect, so that they can be resolved efficiently.

## The Lesson

### Writing Unit Tests
We are going to crowdfund a board game called Python Quest.  In order for our project to be successful, we will need to account for all the material and labor costs and then figure out how to set the price in order to make a profit.

The first function we will need is a function to calculate how much funding we will raise for a given number of backers.  First make two files:
profit_calculator.py will contain our functions that calculate revenue and costs
test_profit_calculator.py will contain our unit tests

We always want to write our tests in a separate file from our code.  This is an example of separation of concerns.  We should organize our code by how and when we will use it.  The tests will be run to develop the code, but not to calculate the costs of our campaign.  Code with a separate purpose goes in a separate file.

Since we are practicing test driven development, we will start in test_profit_calculator.py.

Inside this file, we need to import the library unittest and instantiate a class named TestProfitCalculator with the parameter unittest.TestCase. Note that classes begin with a capital letter as a convention.

Inside this test class, we will define a function that we will specifically use to test our funding calculator.  Call this function test_funding_calculator(self).  The self parameter refers to the parent test class.  We will include the parameter (self) for all our test functions.

In order to write a test for our funding calculator function we need to know its:
* Name : calculate_funding()
* Parameter names (and expected types): backers (int), unit_cost (float)
* Expected output (and type): backers*unit_cost (float)

We are going to test this function for three things:
* Accurate calculations (does it provide the correct output)
* Acceptable range of argument valuers (we don't want to have -1 backers)
* Acceptable type of arguments (backers and unit_cost should both be numbers)

Add the tests below to your test_profit_calculator.py.  Then write a caculate_funding() function that passes all of these tests.

```python
import unittest
from profit_calculator import calculate_funding

class TestProfitCalculator(unittest.TestCase):
    
    def test_funding_calculator(self):
        #test accuracy of calculations
        self.assertAlmostEqual(calculate_funding(backers=100,unit_cost=30.0),3000.0)
        self.assertAlmostEqual(calculate_funding(backers=0,unit_cost=30.0),0.0)
        
       #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_funding, backers=-1, unit_cost=30.0)
        self.assertRaises(ValueError, calculate_funding, backers=100, unit_cost=-1.0)
       
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_funding, backers="test")
        self.assertRaises(TypeError, calculate_funding, unit_cost="test")
```

#### Helpful Questions
Why are we writing tests at all?  What makes this worth the time?
* Code is less likely to throw unexpected or unnoticed errors
* You develop as strong understanding of a code's purpose before writing it, leading to more focused development
* You are encouraged to write small, self-contained segments of code

What's the difference between ValueError and TypeError?  Do you always need both?
* TypeError is common, as arguments almost always are limited in acceptable type
* ValueErrors are only needed when there is a limited acceptable range of arguments of the correct type (eg only nonnegative numbers)

### Raising Errors
If your calculate_funding looks like the snippet below, you are probably failing to raise value and type errors:

```python
def calculate_funding(backers, unit_cost):
    total = backers * unit_cost
    return total
```
To resolve this, we need to Raise Errors when unexpected values or data types are passed into this function as arguments.  We can do this by introducing a conditional to calculate_funcing().  It's also best practice to include a docstring on the first line of the function wrapped in triple quotation marks.  This docstring explains the function's specifications.  Most IDEs display a function's docstring as a popup tooltip when you write the name of the function.

```python
def calculate_funding(backers, unit_cost):
    '''Returns the funding total (float) given a number of backers and cost per unit'''
    if type(backers) not in [int,float]:
        raise TypeError("Backer count must be a non-negative real number")
    if backers < 0:
        raise ValueError("Backer count cannot be negative")
    total = backers * unit_cost
    return total
```

#### Helpful Questions
Why raise these errors at all?  Won't they come up on their own if there is a problem.
* Some errors may go unnoticed.  For example, its possible to multiply a string by an integer (though rarely desirable).  It's preferable to always catch errors.
* You can customize your error message to allow for more accurate tracing.
Why add doc strings to a function?
* Doc strings allow other developers to use functions you create more effectively
* Doc strings make your code easier to read

### Calculate Campaign Costs
Write tests (and then a function) to calculate the costs of running the crowdfunding campaign.  Your test function should be called test_campaign_cost_calculator(self)

Function specifications:
* Name: calculate_campaign_costs
* Parameters: funding_total (nonnegative int or float)
* Calculations:
    * Add a fixed advertising cost of $500
    * Add the crowdfunding site fee: 5% of your funding total
    * Add the fulfillment service's fee: 5% of your funding total (to handle all the * shipping etc)
    * Return the sum of these three values (float)

test_profit_calculator.py:
```python
    def test_campaign_cost_calculator(self):
        #test accuracy of calculations
        self.assertAlmostEqual(calculate_campaign_costs(10000),1500.0)
        self.assertAlmostEqual(calculate_campaign_costs(100),510.0)
        self.assertAlmostEqual(calculate_campaign_costs(0),500.0)
        #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_campaign_costs, -1)
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_campaign_costs, "test")
        self.assertRaises(TypeError, calculate_campaign_costs, None)
        self.assertRaises(TypeError, calculate_campaign_costs, False)
```

profit_calculator.py:
```python
def calculate_campaign_costs(funding_total):
    '''Calculates the advertising costs, site fees, and fulfillment costs of a given funding total'''
    advertising_costs = 500
    crowdfund_site_costs = funding_total*0.05
    fulfillment_costs = funding_total*0.05
    return crowdfund_site_costs + fulfillment_costs + advertising_costs
```

#### Helpful Questions
How can you determine the expected output of functions like this when writing a test?
* Pencil and paper, calculator, etc
How do you decide what to name these variables?
* Generally you want a brief but descriptive name.  Something with just enough information to distinguish from other variables in the same program.

### Calculate Printing Costs
Write tests for a function called calculate_printingl_cost().  Then write the function so that it passes all relevant tests.

Function Specifications
* Name: calculate_printing_costs
* Parameters: units (nonnegative int or float)
* Calculations:
* Add a printing fee of $1000 plus $10 per unit
* Add a shipping fee of $250 plus $2 per unit
* Add the fulfillment service's fee: 5% of your funding total (to handle all the * shipping etc)
* Return the sum of these three values (float)

```python
    def test_printing_cost_calculator(self):
        #test accuracy of calculations
        self.assertAlmostEqual(calculate_printing_costs(1000),13250.0)
        self.assertAlmostEqual(calculate_printing_costs(10),1370.0)
        self.assertAlmostEqual(calculate_printing_costs(0),1250.0)
        #tests that input values are within expected range
        self.assertRaises(ValueError, calculate_printing_costs, -1)
        #test that input values match expected data types
        self.assertRaises(TypeError, calculate_printing_costs, "test")
        self.assertRaises(TypeError, calculate_printing_costs, None)
        self.assertRaises(TypeError, calculate_printing_costs, False)

def calculate_printing_costs(units):
    '''Returns the cost of printing a given number of board game units'''
    printer_fee = 1000.0 + (units * 10.0)
    shipping_fee = 250 + (units * 2)
    return printer_fee + shipping_fee
```

#### Helpful Questions
Why should printing costs have a separate function from the campaign costs?
* They have different parameters (funding vs units).
* There are times you may want to find one and not the other (if you have another * campaign for a digital good, you won't need to find print costs)
* It is easier to write tests for simpler functions

## Extensions
Extensions are generally presented in order of difficulty, and should be * offered to students with that caveat in mind. It's not critical that students * do these activities specifically, but these are a good starting place. 
* Write tests for a function (and then the function) called * calculate_personnel_cost() that calculates the associated personnel costs for a given funding level.  Three friends contributed to this project:
    * Phim chose a variable pay rate of $500 plus 5% of the total campaign funding
    * Ahzam chose a variable pay rate of $500 plus 5% of the total campaign funding
    * Ella chose a fixed payment of $2000
    * Return the sum of all personnel costs
* Write tests for a function (and then the function) called profit_calculator * that calculates funding and subtracts all costs (campaign, printing, personnel) for a given backer_count and unit_price and returns the net profit.
* Create another file named minimum_funding_goal.py
    * Write tests for a function (and then the function) called * calculate_minimum_funding_goal() that:
    * Increments a backer_count (with a for or while loop)
    * Calls profit_calculator with the given backer_count 
    * Repeats the loop until the net_profit is over $2000
    * Prints the funding goal required to generate this profit margin
    * Test your minimum_funding_goal() function with a unit price of:
        * $20
        * $30
        * $40
* Refactor your error code.  Create a new file called raise_error.py and put a series of functions that check data types and acceptable values.  These functions do not need a return statement but should raise Value or Type Errors based on provided criteria.  You will need to import these functions into profit_calculator.py in order to access them.
* Create a deluxe edition of the game.
    * Assume that 20% of backers choose the deluxe edition
    * The cost is double that of the base edition
    * The per unit printing cost is double that of the base edition
    * Shipping costs are unchanged
    * Calculate your minimum funding goal for a campaign with the deluxe edition

## Related Resources

* [Socratica Unit Tests](https://youtu.be/1Lfv5tUGsn8) - Video Tutorial on Unit Tests
* [Wikipedia Overview on Separation of Concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) - Wikipedia entry on separation of concerns
* [Python Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) - Python Documentation on Errors and Exceptions


