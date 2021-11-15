# Lesson Title

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

Students have recently learned OOP and practiced writing class definitions and creating instances of a class. In the previous lab, students wrote and modified class definitions based on feedback from pre-existing unit tests. In this lesson, students will learn to write their own unit tests to evaluate classes.

## Objectives

* SW write unit tests for Object-Oriented Python code, with an emphasis on init methods, instance methods, and instance variables.

## Setup

Encourage students to create a new folder for today's files. Students should create and open a students.py file and a test_students.py file.

## Launch

Today, we're going to be making a class to represent students at a college. I've created a basic definition and 3 instances using the characters from the show Community, but there are some problems:

```python
class Student:
    '''A class to store information for college students'''
    def __init__(self, first, last, year=1):
        self.first = first
        self.last = last
        self.year = year

student1 = Student("Jeff", "Winger", 4)
student2 = Student("Britta Perry", 3)
student3 = Student("Pierce", "Hawthorne", 66)

print(student1.first)
print(student2.last)
print(student3.year)
```

What will happen when we run the code?

It looks like when Britta was filling out her paperwork, she accidentally put both her first and last name in the "first name" field, and now her year is accidentally being saved as her last name. And Pierce listed his age rather than his year at the school.

We can use unit testing to catch some of these mistakes!

## The Lesson

### Getting Started Unit Testing Classes 

It is conventional to write our unit tests in a separate file (separation of concerns) that begins with test_ and then the name of the file to be tested. In this case we will create a test_students.py file. Inside this file, we need to import the unittest module and the class that we are trying to test.

Next, we will need to create our test case. Finally we add code so that the unit test runs automatically:

```python
import unittest
from students import Student

class TestStudent(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
```

#### Helpful Questions
* Why is it useful to start writing unit tests before writing class methods?
* How can we write unit tests that will catch the errors we saw?

### Testing the init Method
Let's start by writing some tests to check our basic init method. Let's comment out the faulty class instances in the students.py file and instead create some test instances in our test_students.py file. Then we can verify that these instances are created properly.

```python
class TestStudent(unittest.TestCase):
    def test_init(self):
        student1 = Student("Jeff", "Winger", 4)
        student2 = Student("Annie", "Edison", 2)

        #Check for accuracy
        self.assertEqual(student1.first, "Jeff")
        self.assertEqual(student2.last, "Edison")
        self.assertAlmostEqual(student1.year, 4)
```

Run the test by typing "python test_students.py" in terminal. 

### Testing for Type Errors
It looks like our code passes this basic test, so let's add some tests to check that our faulty students will raise errors. Note that assertRaises doesn't require you to provide all arguments, so it's helpful to name the arguments that you are providing:

```python
    def test_init_types(self):
        # Check for type errors
        self.assertRaises(TypeError, Student, first = "Britta Perry", last = 3)
```

When we run this test, our code fails-- right now, our class is not raising the type error that it should when we pass in the wrong type of data. We can fix this in our students.py file:

```python
class Student:
    '''A class to store information for college students'''
    def __init__(self, first, last, year=1):
        if type(last) != str:
            raise TypeError("Last name must be a string")
        self.first = first
        self.last = last
        self.year = year
```

### Practice
* In the test_students.py file, add tests to check the data type for first name and year
* Edit the students.py to correctly raise type errors when first name or year are the wrong data type
* Edit the test_students.py file to check multiple different data types (boolean, None, string, integer, float)

#### Helpful Questions
* Why is it useful to test multiple different data types?
* Why won't this test catch the problem of Pierce Hawthorne putting his age instead of his year?
* How can we create a test that will catch Pierce's problem?

### Testing for Value Errors
If Pierce Hawthorne inputs 66 for his year, no type error is raised, because the program is expecting an int. We can check for a value error instead. Inside of test_students.py:

```python
def test_init_values(self):
        self.assertRaises(ValueError, Student, first = "Pierce", last = "Hawthorne", year = 66)
```

Our current code fails this test. To pass the test, we must modify students.py:
```python
if year < 1 or year > 10:
            raise ValueError("Year represents the number of years the student has been enrolled (rounded up) and must be an integer from 1 to 9")
```

### Adding Complexity: Email and Full Name
Let's add some complexity to our class. Let's write a test that will check that each student has an email given by first.last@college.edu and a full name that concatenates their first and last names.

```python
    def test_email(self):
        student1 = Student("Jeff", "Winger", 4)
        student2 = Student("Annie", "Edison", 2)
        self.assertEqual(student1.email, "jeff.winger@college.edu")
        self.assertEqual(student2.email, "annie.edison@college.edu")
    
    def test_full(self):
        student1 = Student("Jeff", "Winger", 4)
        student2 = Student("Annie", "Edison", 2)
        self.assertEqual(student1.full, "Jeff Winger")
        self.assertEqual(student2.full, "Annie Edison")
```

Once we have our unit tests, we need to update our students.py file to match:

```python
        self.first = first
        self.last = last
        self.year = year
        self.email = '{}.{}@college.edu'.format(self.first.lower(), self.last.lower())
        self.full = '{} {}'.format(self.first, self.last)
```

#### Helpful Questions
* Do you think it makes more sense to write the unit test or the class first? Why?
* Where are there inefficiencies in our current code?

### Setup and Teardown

Currently our unit test code repeats the creation of student1 and student2 three times. This violates the DRY principle of programming: Don't Repeat Yourself. We can make our code more efficient by combining these 3 sections into one using a setup method. The setup code repeats before every test.

Inefficient original code:
```python
class TestStudent(unittest.TestCase):
    def test_init(self):
        #Check for accuracy
        student1 = Student("Jeff", "Winger", 4)
        student2 = Student("Annie", "Edison", 2)
        self.assertEqual(student1.first, "Jeff")
        self.assertEqual(student2.last, "Edison")
        self.assertAlmostEqual(student1.year, 4)

    def test_init_types(self):
        # Check for type errors
        self.assertRaises(TypeError, Student, first = "Britta Perry", last = 3)
    
    def test_init_values(self):
        # Check for value errors
        self.assertRaises(ValueError, Student, first = "Pierce", last = "Hawthorne", year = 66)

    def test_email(self):
        # Check that the email is created correctly
        student1 = Student("Jeff", "Winger", 4)
        student2 = Student("Annie", "Edison", 2)
        self.assertEqual(student1.email, "jeff.winger@college.edu")
        self.assertEqual(student2.email, "annie.edison@college.edu")
    
    def test_full(self):
        # Check that the full name attribute is created correctly
        student1 = Student("Jeff", "Winger", 4)
        student2 = Student("Annie", "Edison", 2)
        self.assertEqual(student1.full, "Jeff Winger")
        self.assertEqual(student2.full, "Annie Edison")
```

More efficient code:
```python
class TestStudent(unittest.TestCase):
    def setUp(self):
        #This code runs before every test
        print("running setUp")
        self.student1 = Student("Jeff", "Winger", 4)
        self.student2 = Student("Annie", "Edison", 2)

    def tearDown(self):
        #This code runs after every test
        print("running tearDown")

    def test_init(self):
        #Check for accuracy
        self.assertEqual(self.student1.first, "Jeff")
        self.assertEqual(self.student2.last, "Edison")
        self.assertAlmostEqual(self.student1.year, 4)

    def test_init_types(self):
        # Check for type errors
        self.assertRaises(TypeError, Student, first = "Britta Perry", last = 3)
    
    def test_init_values(self):
        # Check for value errors
        self.assertRaises(ValueError, Student, first = "Pierce", last = "Hawthorne", year = 66)

    def test_email(self):
        # Check that the email is created correctly
        self.assertEqual(self.student1.email, "jeff.winger@college.edu")
        self.assertEqual(self.student2.email, "annie.edison@college.edu")
    
    def test_full(self):
        # Check that the full name attribute is created correctly
        self.assertEqual(self.student1.full, "Jeff Winger")
        self.assertEqual(self.student2.full, "Annie Edison")
```

Note that in order to be able to access student1 and student2 from within our other tests, we must add self. in front, turning them into instance attributes of each test.

#### Helpful Questions
* What will be printed when we run the code?
* Right now we are not actually using tearDown. What would be a situation where it would be useful?

Possible answer: tearDown could be useful if each test creates a new file that we don't need to keep. 

### Testing Other Methods
Let's practice testing a method other than init. We want a method called greeting that will say "Welcome to campus!" for freshmen and "Welcome back!" for everyone else. Let's write some unit tests for this method:

```python
    def test_greeting(self):
        self.assertEqual(self.student1.greeting(), "Welcome back!")
        self.student2.year = 1
        self.assertEqual(self.student2.greeting(),"Welcome to campus!")
```

#### Helpful Questions
* Why is it important to test with both a freshmen and another student?

#### Practice
* Edit students.py to add a greeting method that passes our unit test
* Add a docstring to your method so that other programmers can easily figure out how to use it

## Extensions

Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* Modify the class to include a Boolean attribute called lives_on_campus. Add a unit test that verifies that a type error is raised when a new instance of the Student class is created with an incorrect lives_on_campus data type.
* Create a unit test that checks for a class variable called tuition with a value of 20000. Modify the students.py file to pass the test.
* Add an attribute called aid with a default of 0. Create a unit test that checks for a net_cost method calculating the net cost by adding tuition, plus $25000 for room and board if the student lives on campus, minus the amount of financial aid that they receive. Modify the students.py file to pass the test.
* Add an attribute called GPA. Create a unit test that checks for a deans_list function which returns a Boolean value based on whether a student makes the Dean's List (GPA of at least 3.5). Modify the students.py file to pass the test.
* Create unit tests for a class called Faculty which includes attributes for first name, last name, department, and a list of classes taught. Code the class definition in order to pass the tests. Place your code in appropriately-named files, making sure to separate concerns.

## Related Resources

* [Python Unit Testing Documentation](https://docs.python.org/3/library/unittest.html) - The detailed unit testing documentation from python.
* [How to Write a Unit Test in Python](https://codefather.tech/blog/write-unit-test-python/) - Blog post that walks through how to write unit tests for a Python class
* [Corey Schafer Unit Testing Tutorial](https://www.youtube.com/watch?v=6tNS--WetLI) - A YouTube code-along that explains how to write unit tests for functions and classes.
