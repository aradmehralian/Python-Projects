class Scorer:
    """
    a class to keep track of the user's score and number of attempts
    """

    def __init__(self, initial_score=100, attempts=0):
        self.score = initial_score
        self.attempts = attempts

    def decrement_score(self, penalty=10) -> None:
        """
        Decrement the user's score by the specified penalty.
        """
        self.score -= penalty
        self.score = max(0, self.score)

    def get_score(self) -> int:
        """
        Return the user's current score.
        """
        return self.score
    
    def reset_score(self) -> None:
        """
        Resets the scoring system to its initial state.
        """
        self.__init__()
