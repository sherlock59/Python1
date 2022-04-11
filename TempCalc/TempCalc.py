#!/usr/bin/env python3

LINE_LENGTH = 50
#display a welcome message
print("Welcome to the Temperature Calculator")
print('=' * LINE_LENGTH)

# 4 while loop
while True:

    while True:
      input - conversion c or f  # which direction

    while True:
      input - start temp (0)

    while True:
      input - stop tempfile (100)

    while True:
      input - step intervel (10)

    for i in range (0 ,10)

        while True:
            input - y/n ]


while True:

    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if 0 < monthly_investment <= 1000:
            break
        else:
            print("Entry must be greater than 0. Please try again.")

    is_valid = True
    while is_valid == True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = False
        else:
            print("Entry must be greater than 0 and less than or equal to 15. "
                  "PLease try again.")

    is_valid = True
    while is_valid == True:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            is_valid = False
        else:
            print("Entry must be greater than 0 and less than or equal to 50.\t"
                  "Please try again.")

    print()

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 /100
    months = years * 12
