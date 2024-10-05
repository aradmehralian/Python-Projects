def get_valid_input() -> str:
    """
    gets the valid input from the user
    """
    
    options = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Please enter your choice: ")
        if user_choice == 'q':
            return 'q'
        elif user_choice.lower() in options:
            return user_choice.lower()
        else:
            print("Invalid input! Try again")
            continue
