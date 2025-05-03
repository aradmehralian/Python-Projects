from src.utils.input_validator import get_valid_input
from src.utils.repeat_game_validator import repeat_game_validate
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import Scorer


def main():
    first_number = 1
    last_number = 100
    number_to_guess = generate_random_number(first_number, last_number)
    scorer = Scorer()
    print("Welcome to our number guesser game.")
    print(f"We're going to pick a number between {first_number} and {last_number}. Try to guess it!")
    print("Let's begin !")
    print("-" * 25)


    while True:
        user_guess = get_valid_input(first_number, last_number)
        if user_guess == 'q':
            break
        scorer.attempts += 1

        if user_guess == number_to_guess:
            print("Congratulations, you win!")
            print(f"Your guess, {user_guess}, is correct!")
            print(f"You took {scorer.attempts} attempts and your final score is {scorer.get_score()}.")
            repeat_game = repeat_game_validate()
            
            if repeat_game == 'y':
                number_to_guess = generate_random_number(first_number, last_number)
                scorer.reset_score()
                continue
            else:
                print("Thanks for playing. Hope you had fun!")
                break
        else:
            provide_hint(user_guess, number_to_guess)
            scorer.decrement_score()
            continue


if __name__ == "__main__":
    main()
