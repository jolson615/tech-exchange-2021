from scrabble import letter_value

# Function 1
def add(x, y):
    '''Add Function'''
    return x + y

# Function 2
def subtract(x, y):
    '''Subtract Function'''
    return x - y

# Function 3
def multiply(x, y):
    '''Multiply Function'''
    return x * y

# Function 4
def divide(x, y):
    '''Divide Function'''
    return x // y

# Function 5
def tip(bill, percent):
    '''Tip function that takes in the bill amount and the percentage tip (ex. 20) and returns the total amount to pay'''
    total = bill*(1+percent)
    return total

# Function 6
def scrabble_value(word):
    '''Function that takes in a word as a string and returns the value of that word in scrabble tiles'''
    total = 0
    for letter in word:
        total += letter_value[letter]
    return total

# Function 7
def taxi(distance, stopped_time):
    '''Function that takes in the distance in miles and amount of time spent stopped in minutes and returns the cost of taking a taxi. Taxis cost $2.50 plus 50 cents per 0.2-mile (rounded up) plus 50 cents for each minute of standing (rounded up)'''
    base_fee = 2.5
    total = base_fee + distance * 0.5 + stopped_time * 0.5
    return total

# Function 8
def scientific_notation(x):
    '''Function that takes in a number and returns that number expressed in scientific notation'''
    exponent = 0
    while x > 10:
        x = x /10
        exponent += 1
    significand = x
    return significand * 10**exponent

#Function 9
def get_numbers():
    '''Gets 2 numbers from the user'''
    x = input('Enter your first number: ')
    y = input('Enter your second number: ')
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
    return operation

# Function 11
def calculate():
    operation = get_operation()
    if operation in ['+', '-', '*', '/', 'tip', 'taxi']:
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
        return tip(numbers[0], numbers[1])
    
    elif operation == 'taxi':
        return taxi(numbers[0], numbers[1])
    
    elif operation == 'scrabble':
        word = input('Which word would you like to calculate the Scrabble value for? ')
        return scrabble_value(word)
    
    elif operation == 'sn':
        num = float(input('What number would you like to convert to scientific notation? '))
        return scientific_notation(num)

    else:
        print('You have not typed a valid operator, please run the program again.')
    

# Uncomment the function call below in order to use your calculator!
# print(calculate())