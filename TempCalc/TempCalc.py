#!/usr/bin/env python3
import f as f
import to as to

yes_No = "y"

while yes_No() == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

LINE_LENGTH = 50
# display a welcome message
print("Welcome to the Temperature Calculator")
print('=' * LINE_LENGTH)

while True:

    temp_start = 0
    temp_stop = 0
    temp_step = 0
    yes_No = "y"

    while True:
        user_input = input(
            'Enter F to convert C or enter C to convert to F: ')  # get the first letter and convert to lower case
        conversion_type = user_input[0].lower()
        if conversion_type == 'f':
            f = c * 9 / 5 + 32
        if conversion_type == 'c':
            c = f - 32 * 5 / 9
        else:
            print("Invalid letter entered! Please try again to convert the desired temperature...")

    while True:
        temp_start = int(input('{"Enter the starting temperature (-50 to 150)":.<45s}:'))
        if -50 < temp_start <= 150:
            break
        else:
            print("invalid... Please try again")

    while True:
        temp_stop = int(input('{"Enter the stopping temperature (-50 to 150)":.<45s}:'))
        if -50 < temp_stop <= 150:
            break
        else:
            print("Invalid number... Please input a valid number")

    while True:
        temp_step = int(input('{"Enter the step temperature (-50 to 150)":.<45s}:'))
        if -50 < temp_step <= 150:
            break
        else:
            print("Please provide a valid number")

    for temp in range(temp_start, temp_stop, temp_step):
       if yes_No == 'f':
       conversion_type = 'f' to 'c' using temp
    else:
       conversion_type = 'c' to 'f' using temp
       print (f'{temp} {conversion_type}')

    print(f'| {temp:3.0f]} | {temp_conv:3.0f} |')

    while True:
        yes_No = input('Do you want to display another temperature chart (y/n)? ')
        if yes_No() == "y":





