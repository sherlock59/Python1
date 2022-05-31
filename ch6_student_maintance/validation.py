#!/usr/bin/env python3

global FAIL, END


def valid_yes_no(phrase):
    """
    Display an input prompt to get a yes/no answer from the user (valid lower cased inputs are y, yes, n, no)

    :param phrase: user's phrase if one is passed otherwise the default is
    :type phrase: string
    :return: true for yes or false for no
    :rtype: bool
    """
    while True:
        user_input = input(phrase)

        if user_input.lower() == 'y' or user_input.lower() == 'yes':
            return True
        elif user_input.lower() == 'n' or user_input.lower() == 'no':
            return False
        else:
            print(FAIL + 'Invalid Input: Please enter a y=yes or n=no!' + END)


def valid_int(num):
    """
    Display an input prompt to get a number from the user, and convert it to int or float
    and loop again if invalid

    param num: #the text that will be used for the user's input prompt#
    :return: None
    """
    if num.isnumeric():
        return True
    else:
        print(FAIL + 'Invalid Input: Please enter a number!' + END)
