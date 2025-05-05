import json

import nltk
from nltk.corpus import words


def save_words():
    """
    Get the words in the NLTK's words corpus and filter based on length.
    Save the filtered list to `data/sample words.txt`
    """

    nltk.download("words")
    words_list = words.words()

    filtered_words = [word for word in words_list if 4 <= len(word) <= 8]

    with open("data/sample words.txt", mode="w") as f:
        json.dump(filtered_words, f)


if __name__ == "__main__":
    save_words()
