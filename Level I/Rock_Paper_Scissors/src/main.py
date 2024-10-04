from src.game_logic.computer_choice_generator import RockPaperScissor
from src.game_logic.winner_decider import decicde_winner
from src.utils.user_input_validator import get_valid_input


def main():
    print("Welcome to our Rock Paper Scissors game!")
    print("Enter your choice in the prompt to see who wins!")
    print("If you wish to quit the game just enter 'q' in the prompt.")
    print("Let's dive into it!")
    print("-" * 60)
    computer = RockPaperScissor()

    while True:

        user_choice = get_valid_input()
        if user_choice == 'q':
            print("Thanks for playing the game. Goodbye!")
            break
        computer_choice = computer.play()
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        result = decicde_winner(computer_choice, user_choice)
        print(result)
        print("-" * 35)
        


if __name__ == "__main__":
    main()
