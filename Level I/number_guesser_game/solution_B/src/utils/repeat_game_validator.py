def repeat_game_validate() -> str:
    """
    Validate user input to ensure it is either 'y' or 'n'.
    """
    while True:
        repeat_game = input("Would you like to play another round? [y/n]\n")
        if repeat_game == 'y' or repeat_game == 'n':
            return repeat_game
        else:
            continue