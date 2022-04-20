#!/usr/bin/env python3

(''' Description: This project works as calculator and allows users to convert temperature from C to F and F to C'
 * Written by: Anaberdi Meredov
 * Date Written: 2022.04.20
 * GitHub: https://github.com/sherlock59/Python1.git ''')

LINE_LENGTH = 50
# display a welcome message
print("Welcome to the Temperature Calculator")
print('=' * LINE_LENGTH)

while True:

    while True:
        user_input = str(input("Enter F to convert C or enter C to convert to F: "))
        conversion_type = user_input[0].lower()
        if conversion_type in ['f', 'c']:
            break
        else:
            print("Invalid letter entered! Please try again to convert the desired temperature...")

    while True:
        temp_start = int(input(f'{"Enter the starting temperature (-50 to 150)":.<45s}:'))
        if -50 <= temp_start <= 150:
            break
        else:
            print("invalid... Please try again")

    while True:
        temp_stop = int(input(f'{"Enter the stopping temperature (-50 to 150)":.<45s}:'))
        if -50 <= temp_stop <= 150:
            break
        else:
            print("Invalid number... Please input a valid number")

    while True:
        temp_step = int(input(f'{"Enter the step temperature (-50 to 150)":.<45s}:'))
        if -50 <= temp_step <= 150:
            break
        else:
            print("Please provide a valid number")

    for temp in range(temp_start, temp_stop + 1, temp_step):
        if conversion_type == 'f':
            conversion_result = (temp - 32) * 5 / 9
        if conversion_type == 'c':
            conversion_result = temp * 9 / 5 + 32

        print(f'| {temp:3.0f} | {conversion_result:3.0f} |')

    while True:
        user_input = str(input('Do you want to display another temperature chart (y/n)? '))
        if user_input[0].lower() in ['y', 'n']:
            break
        else:
            print("Invalid Input")

    if user_input[0].lower() == 'n':
        break
    else:
        print()

print('Good bye')
