def get_valid_input(start: int, end: int) -> (int|str):

    """
    Validate user input to ensure it is an integer within the specified range.
    
    args:
        start: int: The lower bound of the range
        end: int: The upper bound of the range
    
    retruns:
        int|str: The validated user input or 'q' to quit the game
    """

    while True:
        user_input = input("Enter a number: ")
        if user_input == 'q':
            print("Thanks for playing the game, Goodbye!")
            return 'q'
        else:
            try:
                user_input = int(user_input)
                if start <= user_input <= end:
                    return user_input
                else:
                    print(f"Invalid input. Please enter a number between {start} and {end}.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
