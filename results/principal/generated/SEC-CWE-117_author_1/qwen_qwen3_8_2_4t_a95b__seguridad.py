import logging

logger = logging.getLogger(__name__)

def inputConversion():
    try:
        user_input = input("Enter an integer: ")
        return int(user_input)
    except ValueError:
        logger.error("Conversion error: input is not a valid integer.")
        return None
    except EOFError:
        logger.error("Input stream closed before receiving a value.")
        return None
