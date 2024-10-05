import random


class RockPaperScissor:

    """
    This class is responsible for generating the computer's choice of rock, paper, or scissors.
    """

    def __init__(self):
        self.choice = None
        self.options = {1: "rock", 2: "paper", 3: "scissors"} # dictionary to store the options

    def play(self):
        """
        choose a random choice from the options
        """
        self.choice = self.options[random.randint(1, 3)] # choose a random choice from the options
        return self.choice
