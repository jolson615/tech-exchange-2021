from currencies import currencies

def cad_converter(usd):
    '''Converts a non-negative value of USD (int or float) to CAD (float)'''
    if type(usd) not in [int,float]:
        raise TypeError("The currency amount must be a non-negative real number")
    if usd < 0:
        raise ValueError("The currency amount cannot be negative")
    return float(usd) * 1.2397

def usd_converter(country, amount):
    '''Converts a non-negative currency value (int or float) of a specified country (string) to USD (float)'''
    if type(country) is not str:
        raise TypeError("The country must be a string")
    else:
        country = country.upper()
    if country not in currencies.keys():
        raise ValueError("Country not listed in currency dictionary")
    if type(amount) not in [int,float]:
        raise TypeError("The currency amount must be a non-negative real number")
    if amount < 0:
        raise ValueError("The currency amount cannot be negative")
    return float(amount) / currencies[country]

def two_currency_converter(input_country, input_amount, output_country):
    '''Converts a non-negative currency value (int or float)
    of a specified input country (string) to the equivalent value (float) of
    the currency of a specified output country (string)'''
    if type(input_country) is not str:
        raise TypeError("Input country must be a string")
    else:
        input_country = input_country.upper()
    if input_country not in currencies.keys():
        raise ValueError("Input country not listed in currency dictionary")
    if type(output_country) is not str:
        raise TypeError("Output country must be a string")
    else:
        output_country = output_country.upper()
    if output_country not in currencies.keys():
        raise ValueError("Output country not listed in currency dictionary")
    if type(input_amount) not in [int,float]:
        raise TypeError("The currency amount must be a non-negative real number")
    if input_amount < 0:
        raise ValueError("The currency amount cannot be negative")
    usd = float(input_amount) / currencies[input_country]
    return usd * currencies[output_country]
