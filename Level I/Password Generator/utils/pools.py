from .characters import _DIGITS, _LETTERS, _SYMBOLS


def build_char_pool(include_digits: bool = False, include_symbols: bool = False) -> str:
    """
    Create a character pool to draw from for the password.

    Args:
        include_digits (bool): Include digits in the character pool.
        include_symbols (bool): Include symbols in the character pool.

    Returns:
        pool (str): The built character pool based on the given criteria.
    """

    pool = _LETTERS

    if include_digits:
        pool += _DIGITS
    if include_symbols:
        pool += _SYMBOLS

    return pool
