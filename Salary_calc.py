#!/usr/bin/env python3

(''' Description: This project calculates invoice total with discount included based on user's input'
 * Written by: Anaberdi Meredov
 * Date Written: 2022.01.31
 * GitHub: https://github.com/sherlock59/InvoiceApp.git ''')


print("Welcome to the Salary Hours Calculator") # displays a welcome message
print("This calculator allows the user to determine hours worked for a whole year")  # explain what does this program do
print("")

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))

# calculate and round miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# display the result
print()
print("Miles Per Gallon:\t\t{mpg}")
print()
print("Bye!")



