from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import Scorer


def main():
    number_to_guess = generate_random_number(1, 100)
    scorer = Scorer()

    while True:
        user_guess = get_valid_input(1, 100)
        if user_guess == 'q':
            break
        scorer.attempts += 1

        if user_guess == number_to_guess:
            print("Congratulations, you win!")
            print(f"Your guess, {user_guess}, is correct!")
            print(f"You took {scorer.attempts} attempts and your final score is {scorer.get_score()}.")
            repeat_game = input("Would you like to play another round? [y/n]\n")
            if repeat_game == 'y':
                number_to_guess = generate_random_number(1, 100)
                scorer = Scorer()
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
