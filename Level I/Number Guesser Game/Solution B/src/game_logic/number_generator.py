import random


def generate_random_number(start: int, end: int) -> int:
    """
    Generate a random number between the specified range.
    
    args:
        start: int: The lower bound of the range
        end: int: The upper bound of the range

    returns:
        int: A random number between the specified range
    """
    return random.randint(start, end)
