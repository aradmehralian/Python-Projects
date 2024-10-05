import random


class RockPaperScissors:
    def __init__(self, name):
        self.options = ['rock', 'paper', 'scissors']
        self.name = name

    def get_user_choice(self):
        user_choice = input(f"Please enter your choice ({', '.join(self.options)}): ")
        if user_choice == 'q':
            return 'q'
        elif user_choice.lower() in self.options:
            return user_choice.lower()
        else:
            print(f"Invalid input! Your choice must be in ({', '.join(self.options)})")
            return self.get_user_choice() # recursive function call

    def get_computer_choice(self):
        return random.choice(self.options)
    
    def decide_winner(self, user_choice, computer_choice):
        if (computer_choice == user_choice):
            return "Draw!"
        
        # Check all the possible scenarios that the user wins
        user_win_combinations = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")] 
        for win_comb in user_win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return f"{self.name} wins!"
            
        return "Computer wins!"

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            if user_choice == 'q':
                print(f"Thanks for playing the game {self.name}, Goodbye!")
                break
            computer_choice = self.get_computer_choice()
            print(f"Your choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")
            result = self.decide_winner(user_choice, computer_choice)
            print(result)
            print("-" * 60)
            continue
