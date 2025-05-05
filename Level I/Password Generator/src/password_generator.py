from abc import ABC, abstractmethod
from typing import List
import secrets

from utils.characters import _DIGITS
from utils.pools import build_char_pool
from utils.data_loader import load_vocabulary


__all__ = ["PinCodeGenerator", "RandomPasswordGenerator", "MemorablePasswordGenerator"]


class PasswordGenerator(ABC):
    """
    Base Class for all the password generators.
    """

    @abstractmethod
    def _validate_length(self):
        """
        Child classes must implement this method.
        """
        pass

    @abstractmethod
    def generate(self):
        """
        Child classes must implement this method.
        """
        pass


class PinCodeGenerator(PasswordGenerator):
    """
    Class to generate random pin codes.
    """

    def __init__(self, length: int = 4):
        self.length = self._validate_length(length)

    def _validate_length(self, length: int) -> int:
        """
        Validate the length of pin code.

        Args:
            length (int): The length provided by the user
        
        Returns:
            length (int): The validated length.
        
        Raises:
            ValueError: If input length is not a valid number or if input length is not in the limit range.
        """

        if (not isinstance(length, int)) or (length < 0):
            raise ValueError("Pin code length must be a non-negative integer")
        if 4 <= length <= 12:
            return length
        raise ValueError("Pin code length must be between 4 and 12 inclusive")

    def generate(self) -> str:
        """
        Generate numeric pin code.
        """

        return "".join(secrets.choice(_DIGITS) for _ in range(self.length))

    def __call__(self) -> str:
        return self.generate()


class RandomPasswordGenerator(PasswordGenerator):
    """
    Class to generate random passwords.
    """

    def __init__(
        self,
        length: int = 12,
        include_digits: bool = False,
        include_symbols: bool = False,
    ):
        self.length = self._validate_length(length)
        self.pool = build_char_pool(include_digits, include_symbols)

    def _validate_length(self, length: int) -> int:
        """
        Validate the length of password.

        Args:
            length (int): The length provided by the user
        
        Returns:
            length (int): The validated length.
        
        Raises:
            ValueError: If input length is not a valid number or if input length is not in the limit range.
        """

        if (not isinstance(length, int)) or (length < 0):
            raise ValueError("Password length must be a non-negative integer")
        if 8 <= length <= 25:
            return length
        raise ValueError("Password length must be between 8 and 25 inclusive")

    def generate(self) -> str:
        """
        Generate a random password with the given criteria from the characters in `self.pool`
        """

        return "".join(secrets.choice(self.pool) for _ in range(self.length))

    def __call__(self):
        return self.generate()


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate memorable passwords.
    """

    def __init__(
        self,
        num_words: int = 5,
        vocabulary: List[str] | None = None,
        sep: str = "-",
        capitalized: bool = False,
    ):
        self.num_words = self._validate_length(num_words)
        self.sep = sep
        self.capitalized = capitalized

        if vocabulary is None:
            vocabulary = load_vocabulary()
        else:
            vocabulary = self._validate_vocab_size(num_words, vocabulary)
        self.vocabulary = vocabulary

    def _validate_length(self, num_words: int) -> int:
        """"
        Validate the number of words in the password.

        Args:
            num_words (int): The number of words specified by the user.

        Returns:
            num_words (int): The validated number of words.

        Raises:
            ValueError: If the provided `num_words` is not valid or exceeds the maximum limit.
        """

        if (not isinstance(num_words, int)) or (num_words < 0):
            raise ValueError("Number of words must be a non-negative integer")
        if 0 < num_words <= 8:
            return num_words
        raise ValueError("Number of words exceeded maximum limit, 8")

    def _validate_vocab_size(self, num_words: int, vocabulary: List[str]) -> int:
        """
        Validate the size of the user-provided vocabulary.

        Args:
            num_words (int): The number of words in the password.
            vocabulary (List[str]): The vocabulary to choose the words from.
        
        Returns:
            vocabulary (List[str]): The validated vocabulary.
        
        Raises:
            ValueError: If the number of words in the provided vocabulary is less than the number of words in the password.
        """

        if len(vocabulary) >= num_words:
            return vocabulary
        raise ValueError("Not enough words in the vocabulary")

    def generate(self) -> str:
        """
        Generate a memorable password with the given criteria from `self.vocabulary`
        """

        random_words = [secrets.choice(self.vocabulary) for _ in range(self.num_words)]

        if self.capitalized:
            return self.sep.join(word.capitalize() for word in random_words)

        return self.sep.join(random_words)

    def __call__(self):
        return self.generate()
