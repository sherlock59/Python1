#!/usr/bin/env python3

(''' Description: This project calculates invoice total with discount included based on user's input'
 * Written by: Anaberdi Meredov
 * Date Written: 2022.01.31
 * GitHub:  ''')


print("Welcome to the Salary Hours Calculator") # displays a welcome message
print("This calculator allows the user to determine hours worked for a whole year")  # explain what does this program do
print("")

# get input from the user
salary_amount = float(input("Enter salary for per hour:\t\t"))
hours_worked = float(input("Enter hours worked:\t"))

# calculate and present the result.
mpg = salary_amount / hours_worked
mpg = round(mpg, 2)

# display the result
print()
print("Salary for per year:\t\t{mpg}")
print()
print("Bye!")



