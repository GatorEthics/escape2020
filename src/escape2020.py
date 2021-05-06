"""Main file for the Escape 2020 game, which runs the project."""

import story

class color:
    """Defines different colors and text formatting settings to be used for CML output printing."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

def main():
    """Runs the game."""
    print_welcome_message()

    q_directions = input(color.BOLD + "Do you want to view the game's directions? Y/N: " + color.END)
    if q_directions.upper() == "Y":
        print_directions()
    else:
        pass

    q_user_ready = "N"
    while q_user_ready.upper() != "Y":
        q_user_ready = input(color.BOLD + "\nAre you ready to begin the game? Y/N: " + color.END)

    print(color.YELLOW + color.BOLD + "\nAlrighty then, lets begin " + color.END + color.END)
    story.intro()

def print_welcome_message():
    """Prints the program welcome message and information."""
    print(
        "\n\n   -----------------------------------------------"
        + "\n   |                                             |\n"
        + color.BOLD
        + color.GREEN
        + "   |       Welcome to the Escape 2020 Game!      |"
        + color.END
        + "\n   |                                             |"
        + "\n   |       \"Can you survive the pandemic?\"       |"
        + "\n   |                                             |"
        + color.END
        + "\n   -----------------------------------------------\n\n"
    )

def print_directions():
    """Prints game directions."""
    
    print("\n\n" + color.BOLD + color.UNDERLINE + "Directions:" + color.END + color.END)
    print("- This is a story-based game, while including some side mini games.\n- The goal is to make it to the end of the day without being infected, so you may be vaccinated.")

main()
