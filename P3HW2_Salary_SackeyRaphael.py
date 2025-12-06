# Raphael Sackey
# 11/24/2025
# P3HW2 - Salary
# This program asks for an employee's hours and pay rate, then
# calculates overtime pay, regular pay, and gross pay and displays
# the results in a nicely formatted table.

"""
Pseudocode (Algorithm):

1. Ask user to enter employee name and store in employee_name
2. Ask user to enter number of hours worked and convert to float
3. Ask user to enter pay rate and convert to float

4. IF hours_worked > 40:
       overtime_hours = hours_worked - 40
       regular_hours = 40
       overtime_pay = overtime_hours * pay_rate * 1.5
       regular_pay = regular_hours * pay_rate
   ELSE:
       overtime_hours = 0
       regular_hours = hours_worked
       overtime_pay = 0
       regular_pay = regular_hours * pay_rate

5. gross_pay = regular_pay + overtime_pay

6. Display:
     - Employee name
     - A header row with: Hours Worked, Pay Rate, OverTime, OverTime Pay,
       RegHour Pay, Gross Pay
     - A row with the numeric values, formatted to 2 decimals for money
"""

# 1–3. Get input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

print("----------------------------------------")

# 4. Determine regular vs overtime hours and pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
else:
    overtime_hours = 0
    regular_hours = hours_worked
    overtime_pay = 0
    regular_pay = regular_hours * pay_rate

# 5. Gross pay
gross_pay = regular_pay + overtime_pay

# 6. Output
print(f"Employee name:  {employee_name}\n")

# Header row
print(f'{"Hours Worked":<13}{"Pay Rate":<11}{"OverTime":<11}'
      f'{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<10}')
print("-" * 80)

# Data row
print(f'{hours_worked:<13.1f}'
      f'{pay_rate:<11.2f}'
      f'{overtime_hours:<11.1f}'
      f'${overtime_pay:<14.2f}'
      f'${regular_pay:<14.2f}'
      f'${gross_pay:<10.2f}')
