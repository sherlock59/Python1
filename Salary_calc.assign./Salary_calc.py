#!/usr/bin/env python3

(''' Description: This project calculates invoice total with discount included based on user's input'
 * Written by: Anaberdi Meredov
 * Date Written: 2022.01.31
 * GitHub: https://github.com/sherlock59/Python1.git ''')


print("Welcome to the Salary Hours Calculator") # displays a welcome message
print("This calculator allows the user to determine hours worked for a whole year")  # explain what does this program do
print("")

# get input from the user
salary_amount = int(input("Enter salary for per hour:\t\t"))
print('')
hours_worked_per_day = int(input("Enter hours worked per day:\t\t"))
print('')

# calculate and present the result...
sph = salary_amount * hours_worked_per_day
sph = sph * 365

# displays the result
print 'Salary for per year:  ', sph
print('')
print("Bye!")



