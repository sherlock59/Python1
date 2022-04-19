#!/usr/bin/env python3

LINE_LENGTH = 50
# display a welcome messageeeq
print("Welcome to the Temperature Calculator")
print('=' * LINE_LENGTH)

while True:

    while True:
        user_input = str(input("Enter F to convert C or enter C to convert to F: "))
        conversion_type = user_input[0].lower()
        if conversion_type in ['f','c']:
            break
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

    for temp in range(temp_start, temp_stop + 1, temp_step):
       if conversion_type == 'f':
            c = (temp - 32) * 5 / 9
        #conversion_type = 'f' to 'c' using temp
       elif user_input == 'c':
            f = temp * 9 / 5 + 32
        #conversion_type = 'c' to 'f' using temp
       print(f'{temp} {conversion_type}')
       


     #print(f'| {temp:3.0f]} | {temp_conv:3.0f} |')

    while True:
        user_input = str(input('Do you want to display another temperature chart (y/n)? '))
        if conversion_type in ('y', 'n'):
            break
            print("invalid input.")
            if user_input == 'y':
                continue
            else:
                print("Have a nice day")
                break
