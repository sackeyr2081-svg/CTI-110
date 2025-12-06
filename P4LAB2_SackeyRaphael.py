# Raphael Sackey
# Date
# P4LAB2 - Multiplication Table
# Program displays a multiplication table from 1 to 12 for a user-entered
# non-negative integer. If the integer is negative, it shows an error message.
# After each run, the user can choose to run the program again.
# Uses both a while loop and a for loop.

run_again = "yes"

while run_again == "yes":
    # Ask user for an integer
    number = int(input("Enter an integer: "))

    if number >= 0:
        # FOR loop to print multiplication table 1–12
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")
    else:
        # Negative number case
        print("This program does not handle negative numbers.")

    print()  # blank line for spacing
    run_again = input("Would you like to run the program again? ").lower()

print("Exiting program...")
