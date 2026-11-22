import re


def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    if not isinstance(number, str):
        raise TypeError("Input must be a string")

    if not number:
        return False

    pattern = re.compile(r'[+-]?(?:\d+(?:\.\d+)?|\.\d+)')
    return bool(pattern.fullmatch(number))
