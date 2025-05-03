def provide_hint(user_guess: int, actual_number: int) -> None:

    """
    Provide a hint to the user based on their guess and the actual number.

    args:
        user_guess: int: The user's guess
        actual_number: int: The actual number to guess

    returns:
        None
    """
    
    if user_guess < actual_number:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")
