# Solutions to the calculator lab

from scrabble import letter_value
import math
import decimal

# Function 1
def add(x, y):
    '''Add Function'''
    if type(x) not in [int, float] or type(y) not in [int, float]:
            raise TypeError("Both inputs must be numbers (int or float)")
    return x + y

# Function 2
def subtract(x, y):
    '''Subtract Function'''
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("Both inputs must be numbers (int or float)")
    return x - y

# Function 3
def multiply(x, y):
    '''Multiply Function'''
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("Both inputs must be numbers (int or float)")
    return x * y

# Function 4
def divide(x, y):
    '''Divide Function'''
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError("Both inputs must be numbers (int or float)")
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

# Function 5
def tip(bill, percent):
    '''Tip function that takes in the bill amount and the percentage tip (ex. 20) and returns the total amount to pay'''
    if type(bill) not in [int, float] or type(percent) not in [int, float]:
        raise TypeError("Both inputs must be numbers (int or float)")
    if percent > 100 or percent < 0:
        raise ValueError('Percent must be a number between 0 and 100')
    if bill < 0:
        raise ValueError('Bill must be a positive number')
    total = bill*(1+percent/100)
    total = round(total, 2)
    return total

# Function 6
def scrabble_value(word):
    '''Function that takes in a word as a string and returns the value of that word in scrabble tiles'''
    if type(word) != str:
        raise TypeError("Word must be a string")
    if len(word) < 2 or len(word) > 15:
        raise ValueError("Word must be at least 2 letters and no more than 15")
    if not word.isalpha():
        raise ValueError("Must be a single word using only letters in the Roman alphabet")
    total = 0
    for letter in word.upper():
        total += letter_value[letter]
    return total

# Function 7
def taxi(distance, stopped_time):
    '''Function that takes in the distance in miles and amount of time spent stopped in minutes and returns the cost of taking a taxi. Taxis cost $2.50 plus 50 cents per 0.2-mile (rounded up) plus 50 cents for each minute of standing (rounded up)'''
    if type(distance) not in [int, float] or type(stopped_time) not in [int, float]:
        raise TypeError("Both inputs must be numbers (int or float)")
    if distance < 0 or stopped_time < 0:
        raise ValueError('Distance and stopped_time cannot be negative')
    base_fee = 2.5
    distance = math.ceil(distance/0.2)*0.2
    stopped_time = math.ceil(stopped_time)
    total = base_fee + distance * 2.5 + stopped_time * 0.5
    return total

# Function 8
def scientific_notation(x):
    '''Function that takes in a number and returns that number expressed in scientific notation'''
    if type(x) not in [int, float]:
            raise TypeError("Input must be a number (int or float)")
    exponent = 0
    while x >= 10:
        x = decimal.Decimal(x /10)
        exponent += 1
    while x < 1:
        x = x*10
        exponent -= 1
    x = round(x, 10)
    significand = float(x)
    return "%s*10**%s"%(str(significand),str(exponent))

#Function 9
def get_numbers():
    '''Gets 2 numbers from the user'''
    x = float(input('Enter your first number: '))
    y = float(input('Enter your second number: '))
    return [x,y]

#Function 10
def get_operation():
    '''Gets the requested operation from the user'''
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
tip to calculate a tip
scrabble to calculat the Scrabble value of a word
taxi to calculate the estimated taxi cost of a trip
sn to convert a number to scientific notation
''')
    operation = operation.lower()
    if operation not in ['+', '-', '*', '/', 'tip', 'scrabble', 'taxi', 'sn']:
        raise ValueError("Input must be one of the requested codes")
    return operation

# Function 11
def calculate():
    operation = get_operation()
    if operation in ['+', '-', '*', '/']:
        numbers = get_numbers()

    if operation == '+':
        return add(numbers[0], numbers[1])

    elif operation == '-':
        return subtract(numbers[0], numbers[1])

    elif operation == '*':
        return multiply(numbers[0], numbers[1])

    elif operation == '/':
        return divide(numbers[0], numbers[1])
    
    elif operation == 'tip':
        x = float(input('Enter your original bill amount: '))
        y = float(input('Enter the percentage you would like to tip as just a number from 1-100: '))
        return tip(x, y)
    
    elif operation == 'taxi':
        x = float(input('Enter the distance you are planning to travel in miles: '))
        y = float(input('Enter your estimate of the amount of minutes spent standing: '))
        return taxi(x, y)
    
    elif operation == 'scrabble':
        word = input('Which word would you like to calculate the Scrabble value for? ')
        return scrabble_value(word)
    
    elif operation == 'sn':
        num = float(input('What number would you like to convert to scientific notation? '))
        return scientific_notation(num)

    else:
        print('You have not typed a valid operator, please run the program again.')
    

# Uncomment the function call below in order to use your calculator!
# run_again = True
# while run_again == True:
#     print(calculate())
#     run_again_yn = input('Would you like to perform another calculation? ')
#     if run_again_yn.lower() == "no" or run_again_yn.lower() == "n":
#         run_again = False