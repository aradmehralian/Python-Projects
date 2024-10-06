from game import RockPaperScissors
from intro import intro_message


def main():
    name = input("Please enter your name: ").title()
    game = RockPaperScissors(name)
    intro_message(name)
    game.play()


if __name__ == "__main__":
    main()
