"""
LLM_LAB1 - Number Guessing Game
Generated with help from an AI language model (ChatGPT)
Student: Raphael Sackey

This program lets the user play a number guessing game.
The computer picks a random number between 1 and 100 and
the user tries to guess it. After each guess, the program
tells the user if the guess is too high, too low, or correct.
The game also counts how many guesses it took and lets the
user play again if they want.
"""

import random


def play_game():
    """Play one round of the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'q' to quit at any time.\n")

    # Generate a random secret number between 1 and 100 (inclusive)
    secret = random.randint(1, 100)
    attempts = 0  # Keep track of how many guesses the user makes

    while True:
        guess_input = input("Enter your guess (1-100): ")

        # Allow the user to quit by typing 'q'
        if guess_input.lower() == 'q':
            print("You quit the game. The number was", secret)
            break

        # Make sure the input can be turned into a whole number
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a whole number or 'q' to quit.\n")
            continue

        # Check that the guess is in the valid range
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100. Try again.\n")
            continue

        attempts += 1  # Count this as a valid attempt

        # Compare the guess to the secret number
        if guess < secret:
            print("Too low! Try again.\n")
        elif guess > secret:
            print("Too high! Try again.\n")
        else:
            # The user guessed correctly
            print(f"Correct! You guessed the number in {attempts} attempts.\n")
            break


def main():
    """Main loop: lets the user play multiple rounds."""
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break
        print()  # Blank line between games


# Only run the game if this file is executed directly
if __name__ == "__main__":
    main()