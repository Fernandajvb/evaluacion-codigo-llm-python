import logging


def inputConversion():
    user_input = input()
    try:
        return int(user_input)
    except ValueError as e:
        logging.error("Conversion error: %s", e)
        return None
