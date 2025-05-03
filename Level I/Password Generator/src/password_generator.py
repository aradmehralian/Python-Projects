from abc import ABC, abstractmethod
import json
import random


from utils.characters import _DIGITS
from utils.pools import build_char_pool



__all__ = ["PinCodeGenerator", "RandomPasswordGenerator", "MemorablePasswordGenerator"]


with open("data/sample words.txt") as f:
    filtered_words = json.load(f)


class PasswordGenerator(ABC):
    def __init__(self, length: int):
        self.length = self._validate_length(length)

    def _validate_length(self, length: int) -> int:
        if (not isinstance(length, int)) or (length < 0):
            raise ValueError("Password length must be a non-negative integer")
        if 8 <= length <= 25:
            return length
        raise ValueError("Password length must be between 8 and 25 inclusive")

    @abstractmethod
    def generate(self):
        pass


class PinCodeGenerator(PasswordGenerator):
    def __init__(self, length: int = 4):
        super().__init__(length)

    def _validate_length(self, length: int) -> int:
        if (not isinstance(length, int)) or (length < 0):
            raise ValueError("Pin code length must be a non-negative integer")
        if 4 <= length <= 12:
            return length
        raise ValueError("Pin code length must be between 4 and 12 inclusive")

    def generate(self) -> str:
        random_pin = random.choices(_DIGITS, k=self.length)
        return "".join(random_pin)

    def __call__(self) -> str:
        return self.generate()


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 12):
        super().__init__(length)

    def generate(
        self, include_digits: bool = False, include_symbols: bool = False
    ) -> str:

        pool = build_char_pool(include_digits, include_symbols)

        chars = random.choices(pool, k=self.length)
        return "".join(chars)


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_words: int = 5):
        self.num_words = num_words

    def generate(self, sep: str = "-", capitalized: bool = False) -> str:
        random_words = random.choices(filtered_words, k=self.num_words)

        if capitalized:
            return sep.join(word.capitalize() for word in random_words)  # generator exp

        return sep.join(random_words)
