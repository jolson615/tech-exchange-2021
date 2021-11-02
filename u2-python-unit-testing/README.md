# Test-driven Python Functions

## Objectives
* SW write functions that pass the pre-written unit tests that come with the lab. 
* SW review all the core concepts in the Python basics lab in the context of functions. 
* SW raise valueType errors.

## Context
You have been hired by Sandshark Capital to develop a currency conversion program for their in-house portfolio management software.  Their existing codebase has some unresolved errors so it’s especially important that this currency converter can handle multiple error types in a predictable way.  See the email from Sandshark’s lead developer Aurelia Clarke for more details on the project specifications.

```
Hi Tech Exchange team,

I’m glad to hear you’ll be taking over the currency converter functions.  We’ve had some challenges with these functions in the past because of errors elsewhere in our code base.  The key challenge here is that it’s not enough for our currency converters to get the math right.  There should be sufficient error handling that if the functions are called incorrectly elsewhere, the error won’t be passed on.

I developed a set of unit tests for you to use in writing these functions.  Our team is shifting toward fully test-driven development, meaning that we write our unit tests before writing the code.  This practice has helped us prevent unhandled errors and has shifted our mindset around development.  We are w

You can run these unit tests from the command line by name:
python -m unittest test_cad_converter

Or you can run unittest and python test and python test discovery will identify the relevant test based on the file name:
python -m unittest
	
Most of our international business is with Canada, so our first priority is a USD to CAD converter.  After that, we need a flexible converter that accepts all the currency types in our dictionary and converts them to USD.  If it’s possible, we also want a universal converter that can exchange between any of the currencies in the countries we operate in.

Don’t hesitate to reach out if you have questions.

Cheers,
Aurelia
```

## The Setup
Students will need to clone down the lab files and open them in their IDE.  Complete the functions in converters.py until all functions pass the relevant unit tests.

## The Lab

### CAD Converter
Complete the function cad_converter() such that it passes all relevant unit tests.
Run the following test command from your terminal:
python -m unittest test_cad_converter

### USD Converter
Complete the function usd_converter() such that it passes all relevant unit tests.
Run the following test command from your terminal:
python -m unittest test_usd_converter

### Two Currency Converter
Complete the function two_currency_converter() such that it passes all relevant unit tests.
Run the following test command from your terminal:
python -m unittest test_two_currency_converter

