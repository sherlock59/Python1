#!/usr/bin/env python3

"""
This module contains functions related to displaying and modifying student account
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 6 assigment"
__github__ = "https://github.com/sherlock59/Python1.git"


def listings(student_list):
    """
    this function lists if the record has student information if not,
    it allows to add one.

    :param student_list:
    :return: student
    """
    if len(student_list) == 0:
        print("There are no students in the list.\n")
    else:
        for i, student in enumerate(student_list, start=1):
            print(f"{i}. {student[0]} ({student[1]})")
        print()


def add(student_list):
    """
    Asks end user for student information so it could save in its memory

    :param student_list:
    :return: student
    """
    student_id = input("ID:  ")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    student = [student_id, first_name, last_name]
    student_list.append(student)
    print(f"{student[0]} was added.\n")


def update(student_list):
    """
    Updates the student account list if the list is empty

    :param student_list:
    :return:
    """
    if len(student_list) == 0:
        print('There are no students in the list.')
        return

    #id = input('Enter the ID of the student you would like to update: ')
    #index = find_index(student_list)

    if id == -1:
        print('There is no student with this ID. Please try again.')
        return

    student_id, first_name, last_name = student_list

    user_confirm = eval(f"Do you want to update student ID # {student_id}{first_name} {last_name}")
    if user_confirm:
        new_first_name = input('Please enter the students first name or press enter to keep name' +
                               student_list[first_name - 1][1] + ': ' + update())
        return new_first_name


def delete(student_list):
    """
    Allows the user to delete saved data

    :param student_list:
    :return:
    """
    number = int(input("Number: "))
    if number < 1 or number > len(student_list):
        print("Invalid student number.\n")
    else:
        student = student_list.pop(number - 1)
        print(f"{student[0]} was deleted.\n")


def display_menu():
    """
    Displays the multiple options to pick from for the end user

    :return:
    """
    print("STUDENT MENU")
    print("1 - List all students")
    print("2 - Add a student")
    print("3 - Update a student")
    print("4 - Delete a student")
    print("0 - Exit program")
    print()


def main():
    """
    Main menu that tests the whole app

    :return:
    """
    student_list = []

    display_menu()

    while True:
        command = input("Please enter a Menu # (Valid 0-4): ")
        if command.lower() == "1":
            listings(student_list)
        elif command.lower() == "2":
            add(student_list)
        elif command.lower() == "3":
            update(student_list)
        elif command.lower() == "4":
            delete(student_list)
        elif command.lower() == "0":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()
