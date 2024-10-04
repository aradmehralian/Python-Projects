def decicde_winner(computer_choice, user_choice):
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
