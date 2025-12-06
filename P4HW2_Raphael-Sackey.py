# Rapahel Sackey
# 11/28/2025
# P4HW2 – Payroll
# Program calculates gross pay for multiple employees, including overtime,
# and then displays totals for overtime pay, regular pay, and gross pay.

"""
Pseudocode:

1. Initialize totals:
      total_overtime_pay = 0
      total_regular_pay = 0
      total_gross_pay = 0
      employee_count = 0

2. Ask user for employee name:
      name = input("Enter employee's name or 'Done' to terminate: ")

3. While name is not "Done":
      a. Ask for hours worked (float)
      b. Ask for pay rate (float)

      c. If hours_worked > 40:
             overtime_hours = hours_worked - 40
             regular_hours  = 40
         else:
             overtime_hours = 0
             regular_hours  = hours_worked

      d. regular_pay  = regular_hours * pay_rate
         overtime_pay = overtime_hours * pay_rate * 1.5
         gross_pay    = regular_pay + overtime_pay

      e. Add to totals:
             total_overtime_pay += overtime_pay
             total_regular_pay  += regular_pay
             total_gross_pay    += gross_pay
             employee_count     += 1

      f. Display per-employee breakdown
         (employee name, hours worked, pay rate, overtime, overtime pay,
          regular pay, gross pay)

      g. Ask again for employee name
             name = input("Enter employee's name or 'Done' to terminate: ")

4. After loop ends (user typed "Done"):
      a. Print summary:
             total number of employees
             total overtime pay
             total regular pay
             total gross pay
"""

# -------- Program starts here --------

# Totals
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

# First prompt for name (sentinel)
name = input("Enter employee's name or 'Done' to terminate: ")

while name != "Done":
    # Get hours and pay rate
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))

    # Determine regular vs overtime hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0.0
        regular_hours = hours_worked

    # Pay calculations
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Per-employee output
    print()  # blank line
    print(f"Employee name:  {name}\n")
    print("Hours Worked   Pay Rate   Overtime   Overtime Pay   RegHour Pay   Gross Pay")
    print("-------------------------------------------------------------------------------")
    print(f"{hours_worked:11.1f}   {pay_rate:7.2f}   {overtime_hours:8.1f}   "
          f"{overtime_pay:12.2f}   ${regular_pay:11.2f}   ${gross_pay:9.2f}")
    print()

    # Ask again (sentinel)
    name = input("Enter employee's name or 'Done' to terminate: ")

# After loop – summary totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
