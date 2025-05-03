import random


class RockPaperScissors:
    """Class to play Rock, Paper, Scissors game"""

    def __init__(self, name: str):
        self.options = ['rock', 'paper', 'scissors'] # accepatable options
        self.name = name
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        """Get the user choice for the game"""

        user_choice = input(f"Please enter your choice ({', '.join(self.options)}): ").lower()
        if user_choice == 'q':
            return 'q'
        elif user_choice.lower() in self.options:
            return user_choice.lower()
        else:
            print(f"Invalid input! Your choice must be in ({', '.join(self.options)})")
            return self.get_user_choice() # recursive function call

    def increment_user_score(self):
        """Increment the user score"""
        self.user_score += 1

    def get_computer_choice(self):
        """Get the computer choice for the game"""
        return random.choice(self.options)
    
    def increment_computer_score(self):
        """Increment the computer score"""
        self.computer_score += 1
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decide the winner of the game.
        
        Args:
            user_choice: The choice of the user.
            computer_choice: The choice of the computer.
        """

        if (computer_choice == user_choice):
            return "Draw!"
        # Check all the possible scenarios that the user wins
        user_win_combinations = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")] 
        for win_comb in user_win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                self.increment_user_score()
                return f"{self.name} wins!"

        self.increment_computer_score()    
        return "Computer wins!"

    def play(self):
        """Play the Rock, Paper, Scissors game"""

        while True:
            user_choice = self.get_user_choice()
            if user_choice == 'q':
                print(f"{self.name}'s score: {self.user_score}")
                print(f"Computer's score: {self.computer_score}")
                print(f"Thanks for playing the game {self.name}, Goodbye!")
                break
            computer_choice = self.get_computer_choice()
            print(f"Your choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")
            result = self.decide_winner(user_choice, computer_choice)
            print(result)
            print("-" * 60)
            continue
