# Raphael Sackey
# Date: 12/03/2025
# P4HW2 – Pay Calculator (Multiple Employees)
# This program asks the user for multiple employees' names, hours worked, and pay rates.
# It calculates overtime hours, overtime pay, regular pay, and gross pay for each employee.
# The program stops ONLY when the user enters "Done".
# At the end, it displays total overtime paid, total regular pay, and total gross pay.

"""
PSEUDOCODE:
1. Initialize totals:
      total_overtime_pay = 0
      total_regular_pay = 0
      total_gross_pay = 0
      employee_count = 0

2. Start loop:
      Ask for employee_name

3. If employee_name == "Done":
      Exit loop

4. Else:
      Ask for hours_worked
      Ask for pay_rate

5. Calculate:
      If hours_worked > 40:
          overtime_hours = hours_worked - 40
          regular_hours = 40
      Else:
          overtime_hours = 0
          regular_hours = hours_worked

      overtime_pay = overtime_hours * (pay_rate * 1.5)
      regular_pay = regular_hours * pay_rate
      gross_pay = overtime_pay + regular_pay

6. Display employee breakdown

7. Update totals:
      total_overtime_pay += overtime_pay
      total_regular_pay += regular_pay
      total_gross_pay += gross_pay
      employee_count += 1

8. Loop back to step 2

9. After loop:
      Display employee_count, total overtime paid,
      total regular pay, and total gross pay.
"""


# ---------------------- PROGRAM STARTS HERE -------------------------

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    if employee_name.lower() == "done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Determine OT and regular hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculations
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Output for this employee
    print("\nEmployee name: ", employee_name)
    print("--------------------------------------------")
    print(f"Hours Worked:  {hours_worked:.1f}")
    print(f"Pay Rate:      {pay_rate:.2f}")
    print(f"OverTime:      {overtime_hours:.1f}")
    print(f"OverTime Pay:  ${overtime_pay:.2f}")
    print(f"RegHour Pay:   ${regular_pay:.2f}")
    print(f"Gross Pay:     ${gross_pay:.2f}")
    print("--------------------------------------------\n")

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

# Final summary
print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")