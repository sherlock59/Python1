#!/usr/bin/env python3

"""
Student Data System for managing student information (student id, first name, and last name)
This module contains the functions for displaying the main menu and running the menu options
"""

#import student_maint

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 6 assigment"
__github__ = "https://github.com/sherlock59/Python1.git"

# two horizontal line
LINE_LENGTH = 40

# Color variables
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def display_menu():
    """
    Displays a list of all the valid main menu options
    It also handles for nonnumerical data and invalid menu option selected.

    :return: None
    :rtype: None
    """
    print(HEADER + 'Student Menu' + ENDC)
    print(OKGREEN + '=' * LINE_LENGTH + ENDC)
    print(OKGREEN + '1 - List all students' + ENDC)
    print(OKGREEN + '2 - Add a student' + ENDC)
    print(OKGREEN + '3 - Update a student' + ENDC)
    print(OKGREEN + '4 - Delete a student' + ENDC)
    print(OKGREEN + '0 - Exit program' + ENDC)
    print()


def main():
    """
    Main keeps the program looping until the user enters 0 to exit the program
    then based on the user's selected, will call the corresponding function option
    Local scoped students is a 2D list that is pass as an argument to each menu option function
    Local scoped max_student_id is the last student id used, and is passed to the add_student function,
    and this function will return the last added student id

    :return: None
    :rtype: None
    """

    while True:
        display_menu()

        while True:
            user_input = input(OKGREEN + 'Please enter a Menu # (Valid 0-4): ' + ENDC)
            if not validate_int(user_input):
                continue
            if int(user_input) > 4 or int(user_input) < 0:
                print(FAIL + 'Invalid Input: Please enter a number greater or '
                             'equals to 0 and less than or equal to 4.' + ENDC)
            else:
                break

            if int(user_input) == 0:
                print('Bye!')
                break
            elif int(user_input) == 1:
                list_students()


if __name__ == '__main__':
    main()