from game import RockPaperScissors

def main():
    name = input("Please enter your name: ").title()
    game = RockPaperScissors(name)
    print(f"Welcome to our Rock Paper Scissors game {name}!")
    print("Enter your choice in the prompt to see who wins!")
    print("If you wish to quit the game just enter 'q' in the prompt.")
    print("Let's dive into it!")
    print("-" * 60)
    game.play()


if __name__ == "__main__":
    main()