"""
Number Guessing Game (CLI)

A simple command-line game where the program selects a random number
and the user attempts to guess it. Demonstrates:
- input validation
- loops and conditionals
- functions and clean program flow
"""

from __future__ import annotations
import random


def choose_range() -> tuple[int, int]:
    """Let the user choose a difficulty range."""
    options = {"1": (1, 10), "2": (1, 100), "3": (1, 1000)}

    while True:
        print("\nChoose difficulty:")
        print("1) Easy   (1-10)")
        print("2) Medium (1-100)")
        print("3) Hard   (1-1000)")
        choice = input("Select 1, 2, or 3: ").strip()

        if choice in options:
            return options[choice]

        print("Invalid choice. Please type 1, 2, or 3.\n")


def get_guess(min_number: int, max_number: int) -> int | None:
    """
    Prompt the user for a guess.

    Returns:
        int: Valid guess within range.
        None: If the user quits (types 'q').
    """
    user_input = input(f"Enter your guess ({min_number}-{max_number}) or 'q' to quit: ").strip()

    if user_input.lower() == "q":
        return None

    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.\n")
        return None

    if not (min_number <= guess <= max_number):
        print(f"Out of range. Please enter a number between {min_number} and {max_number}.\n")
        return None

    return guess


def play_round() -> None:
    """Play one round of the guessing game."""
    min_number, max_number = choose_range()
    secret = random.randint(min_number, max_number)
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")

    while True:
        guess = get_guess(min_number, max_number)

        if guess is None:
            # Could be quit OR invalid; check if they quit by asking last input again is messy,
            # so we treat None as "keep playing" unless they typed q.
            # Easiest clean approach: re-prompt with a small message:
            quit_check = input("Press Enter to keep guessing, or type 'q' to quit: ").strip().lower()
            if quit_check == "q":
                print(f"\nYou quit. The number was {secret}.\n")
                return
            print()
            continue

        attempts += 1

        if guess < secret:
            print("Too low. Try again.\n")
        elif guess > secret:
            print("Too high. Try again.\n")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.\n")
            return


def ask_play_again() -> bool:
    """Return True if the user wants to play again."""
    while True:
        again = input("Play again? (y/n): ").strip().lower()
        if again in {"y", "yes"}:
            return True
        if again in {"n", "no"}:
            return False
        print("Please type 'y' or 'n'.\n")


def main() -> None:
    """Main loop: allows the user to play multiple rounds."""
    while True:
        play_round()
        if not ask_play_again():
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()

