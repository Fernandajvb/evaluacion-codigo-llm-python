import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    return bool(re.search(r'\d', str(number)))
