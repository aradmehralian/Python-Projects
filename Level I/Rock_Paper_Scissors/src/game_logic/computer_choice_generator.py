import random


class RockPaperScissor:

    def __init__(self):
        self.choice = None
        self.options = {1: "rock", 2: "paper", 3: "scissors"}

    def play(self):
        self.choice = self.options[random.randint(1, 3)]
        return self.choice
