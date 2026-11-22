import re

_NUMBER_LINE_RE = re.compile(r"^[^\n]*\d[^\n]*$", re.MULTILINE)

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    if not isinstance(number, str):
        raise TypeError("number must be a string")
    return _NUMBER_LINE_RE.search(number) is not None
