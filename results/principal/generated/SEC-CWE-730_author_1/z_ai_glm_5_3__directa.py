import re


def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    if re.search(r'\d', number):
        return True
    else:
        return False
