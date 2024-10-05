def decicde_winner(computer_choice: str, user_choice: str) -> str:
    """
    decides the winner of the game based on the choices of the computer and the user

    Args:
        computer_choice (str): the choice of the computer
        user_choice (str): the choice of the user
    
    Returns:
        str: the winner of the game
    """

    if (computer_choice == user_choice):
        return "Draw!"
    elif (computer_choice == 'rock' and user_choice == 'scissors'):
        return "Computer wins!"
    elif (computer_choice == 'paper' and user_choice == 'rock'):
        return "Computer wins!"
    elif (computer_choice == 'scissors' and user_choice == 'paper'):
        return "Computer wins!"
    else:
        return "User wins!"
