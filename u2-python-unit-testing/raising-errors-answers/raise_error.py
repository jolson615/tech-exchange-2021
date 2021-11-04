def check_nonnegative_number(arg):
    '''Raises Type/Value error if argument is not a positive real number'''
    if type(arg) not in [int,float]:
        raise TypeError("Function arguments must be a non-negative real number")
    if arg < 0:
        raise ValueError("Function arguments cannot be negative")