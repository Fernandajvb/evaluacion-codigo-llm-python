import logging


def inputConversion():
    user_input = input()
    try:
        return int(user_input)
    except ValueError:
        logging.error("Conversion error: could not convert input to integer")
        return None
