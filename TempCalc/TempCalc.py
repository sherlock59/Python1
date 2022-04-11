#!/usr/bin/env python3

LINE_LENGTH = 50
#display a welcome message
print("Welcome to the Temperature Calculator")
print('=' * LINE_LENGTH)


while True:

    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if 0 < monthly_investment <= 1000:
            break
        else:
            print("Entry must be greater than 0. Please try again.")
