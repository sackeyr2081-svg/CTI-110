# Raphael Sackey
# November 5, 2025
# P1HW2: Travel Budget Calculator
# This program asks the user for their budget and trip expenses, 
# then calculates remaining balance after all costs.

# Pseudocode:
# 1. Ask user for travel budget
# 2. Ask user for travel destination
# 3. Ask user for amount spent on gas
# 4. Ask user for amount spent on accommodation
# 5. Ask user for amount spent on food
# 6. Add all expenses
# 7. Subtract expenses from budget
# 8. Display travel summary and remaining balance

# Ask for user input
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? "))
accommodation = float(input("How much will you spend on accommodation? "))
food = float(input("How much will you spend on food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display summary
print("\n------------ Travel Summary ------------")
print("Destination:", destination)
print("Initial Budget: $", format(budget, ".2f"))
print("Total Expenses: $", format(total_expenses, ".2f"))
print("Remaining Balance: $", format(remaining_balance, ".2f"))
print("----------------------------------------")


