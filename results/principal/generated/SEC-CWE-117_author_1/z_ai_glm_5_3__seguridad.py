import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    user_input = input("Enter an integer: ")
    try:
        converted_value = int(user_input.strip())
    except ValueError:
        logger.error(
            "Conversion error: unable to convert input %r to an integer.",
            user_input,
        )
        return None
    return converted_value
