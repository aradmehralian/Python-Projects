import random


def validate_input(user_guess: str) -> bool:
    """checks whether user input is a number and if it is between 1 and 100.
    
    args:
        user_guess: str: user input

    returns:
        bool: True if user input is a number between 1 and 100, False otherwise
    
    """

    if not user_guess.isdigit():
        print("Invalid input. Please try again.")
        return False
    
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print("Your guess is out of range. Your input should be between 1 and 100.")
        return False
    
    return True


def check_guess(user_guess: int, rand_num: int) -> bool:

    """ checks whether user guess is correct, too high or too low.
    
    args:
        user_guess: int: user input
        rand_num: int: randomly generated number

    returns:
        bool: True if user guess is correct, False otherwise
    
    
    """
    if user_guess > rand_num:
        print("Your guess is too high. Try again!")
        return False
    elif user_guess < rand_num:
        print("Your guess is too low. Try again!")
        return False
    else:
        print("Congratulations, You won!")
        print(f"Your guess, {user_guess}, is correct!")
        return True
    

def main():
    rand_num = random.randint(1, 100)

    score = 100
    attempts = 0

    while True:
        user_guess = input("Guess a number between 1 and 100: ")

        if user_guess == "q":
            print("Thank you for playing, Goodbye!")
            break
        
        if not validate_input(user_guess):
            continue
        
        attempts += 1
        user_guess = int(user_guess)
        
        if check_guess(user_guess, rand_num):
            print(f"You had {attempts} attempts and your final score is {score}.")
            repeat_game = input("Would you like to play another round? [y/n]\n")
            if repeat_game == 'y':
                rand_num = random.randint(1, 100)
                score = 100
                attempts = 0
                continue
            else:
                break
        else:
            score -= 10 
            score = max(0, score)


if __name__ == '__main__':
    main()
