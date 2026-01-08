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


MIN_NUMBER = 1
MAX_NUMBER = 100


def get_guess() -> int | None:
    """
    Prompt the user for a guess.

    Returns:
        int: Valid guess within range.
        None: If the user quits.
    """
    user_input = input(f"Enter your guess ({MIN_NUMBER}-{MAX_NUMBER}) or 'q' to quit: ").strip()

    if user_input.lower() == "q":
        return None

    try:
        guess = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.\n")
        return -1  # sentinel for invalid

    if not (MIN_NUMBER <= guess <= MAX_NUMBER):
        print(f"Out of range. Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.\n")
        return -1

    return guess


def play_round() -> None:
    """Play one round of the guessing game."""
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")

    while True:
        guess = get_guess()

        if guess is None:
            print(f"\nYou quit. The number was {secret}.\n")
            return

        if guess == -1:
            continue  # invalid input; prompt again

        attempts += 1

        if guess < secret:
            print("Too low. Try again.\n")
        elif guess > secret:
            print("Too high. Try again.\n")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.\n")
            return


def main() -> None:
    """Main loop: allows the user to play multiple rounds."""
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
