from .characters import _DIGITS, _LETTERS, _SYMBOLS


def build_char_pool(include_digits=False, include_symbols=False) -> str:
    """
    Create character pool to indicate which characters to be in the passwords.
    """
    pool = _LETTERS

    if include_digits:
        pool += _DIGITS
    if include_symbols:
        pool += _SYMBOLS

    return pool