# Number Guesser Game

## Description
In this project, a number guesser game is implemented. The program will generate a random number between 1 and 100, and the user will have to guess the number. The program will provide feedback on whether the guess is too high or too low. The user will be given a score based on the number of attempts it took to guess the correct number.

## Directory Structure
- `src/`: Contains the source code for the number guesser game.
    - `game_logic/`: Contains the logic for the number guesser game.
        - `hint_generator.py`: Contains the code to generate hints for the user.
        - `number_generator.py`: Contains the code for the number generation.
        - `scorer.py`: Contains the code to calculate the score of the user.
    - `utils/`: Contains utility functions used in the game.
        - `input_validator.py`: Contains the code to validate the user input.
    - `main.py`: Main script to run the number guesser game.

## How to run the game
1. Navigate to the main directory of the project.(`number_guesser_game`)
2. Add the current directory to the python path.

    ```bash
    export PYTHONPATH="${PYTHONPATH}:$(pwd)"
    ```
3. Run the main script.

    ```bash
    python src/main.py
    ```
4. Follow the instructions on the screen to play the game.