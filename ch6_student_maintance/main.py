#!/usr/bin/env python3

"""
Student Data System for managing student information (student id, first name, and last name)
This module contains the functions for displaying the main menu and running the menu options
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 6 assignment"
__github__ = "https://github.com/sherlock59/Python1.git"

from validation import valid_int

import student_maint

# two horizontal line
LINE_LENGTH = 40


def display_menu():
    """
    Displays a list of all the valid main menu options
    It also handles for nonnumerical data and invalid menu option selected.

    :return: None
    :rtype: None
    """
    print('Student Menu')
    print('=' * LINE_LENGTH)
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('0 - Exit program')
    print()


def display_students(students):
    """

    :param students:
    :return:
    """
    if len(students) == 0:
        print('There are no students in list.')
        return

    print(f'{"ID":>4s} {"First Name":<15s} {"Last Name":<15s}')
    print('=' * 4, '=' * 15, '=' * 15)

    for student in students:
        idd, first_name, last_name = student
        print(f'{idd:>2d}  {first_name:<15s} {last_name:<15s}')


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

    # student 2D list
    students_ls = []

    # student id is 0 until the user add a student
    student_id = 0

    while True:
        display_menu()

        while True:
            user_input = input('Please enter a Menu # (Valid 0-4): ')
            if not valid_int(user_input):
                continue
            if int(user_input) > 4 or int(user_input) < 0:
                print('Invalid Input: Please enter a number greater or '
                      'equals to 0 and less than or equal to 4.')
            else:
                break

        if int(user_input) == 0:
            print('Bye!')
            break
        elif int(user_input) == 1:
            student_maint.list_students(students_ls)
        elif int(user_input) == 2:
            student_maint.add_student(students_ls, student_id)
            student_id += 1
        elif int(user_input) == 3:
            student_maint.update_students(students_ls)
        elif int(user_input) == 4:
            student_maint.delete_student(students_ls)

        input("Press Enter to continue...")
        print()


if __name__ == "__main__":
    main()
