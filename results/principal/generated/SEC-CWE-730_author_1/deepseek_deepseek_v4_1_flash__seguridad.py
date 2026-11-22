import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    if not isinstance(number, str):
        return False
    return bool(re.search(r'\d+', number))
