import json
from types import List


def load_vocabulary() -> List[str]:
    """
    Load and return a list of sample words from `data/`
    """

    with open("data/sample words.txt") as f:
        return json.load(f)
