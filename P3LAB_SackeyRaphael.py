# P3LAB_SackeyRaphael
# Author: Raphael Sackey
# Date: 11/23/2025
# Description:
#   This program asks the user for a money amount (with two decimal places)
#   and then calculates the most efficient number of dollars, quarters,
#   dimes, nickels, and pennies needed to make that amount. It prints only
#   the coins that are used, with correct singular/plural names.

# Read the amount of money from the user
amount = float(input("Enter amount of money: "))

# Convert dollars to cents (integer) to avoid floating-point issues
total_cents = int(round(amount * 100))

# If there is no money, print "No change"
if total_cents == 0:
    print("No change")
else:
    # Calculate number of each denomination using floor division (//)
    dollars = total_cents // 100
    total_cents -= dollars * 100

    quarters = total_cents // 25
    total_cents -= quarters * 25

    dimes = total_cents // 10
    total_cents -= dimes * 10

    nickels = total_cents // 5
    total_cents -= nickels * 5

    pennies = total_cents  # whatever is left are pennies

    # Print results only if that denomination is used,
    # and use correct singular / plural wording.

    if dollars > 0:
        if dollars == 1:
            print("1 dollar")
        else:
            print(f"{dollars} dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 quarter")
        else:
            print(f"{quarters} quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 dime")
        else:
            print(f"{dimes} dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 nickel")
        else:
            print(f"{nickels} nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 penny")
        else:
            print(f"{pennies} pennies")
