#!/usr/bin/env python3

import validation
import string
from main import display_students


def list_students(students):
    """
    Display the all student information stored in a 2D list (id, first name, last name)
    It will notify the student if there is no data found.

    param students: student data (id, first_name, last_name)
    :type students: 2d list
    :return: None
    """
    if len(students) == 0:
        print('There are no students in list.')
        return

    display_students(students)


def add_student(students, next_student_id):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.

    type students: 2d list
    :param students: student data (id, first_name, last_name)
    :param next_student_id:
    :return: None
    """

    next_student_id += 1
    print('Add Student')
    print('-----------')
    first_name = input('Please enter the Student\'s First Name: ')
    last_name = input('Please enter the Student\'s Last Name: ')
    print()
    students.append([next_student_id, first_name.capitalize(), last_name.capitalize()])
    print(f'Student ID #{next_student_id} {string.capwords(first_name)} {string.capwords(last_name)} was added.')


def find_student_index(students, student_id):
    """
    Search the 2D list for a specific student ID.

    param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param student_id: student id that they use wants to find
    :return: -1
    """
    for student in students:
        if student_id == student[0]:
            return students.index(student)
    return -1


def update_students(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    param students: student data (id, first_name, last_name)
    type students: 2d list
    return: None
    """
    if len(students) == 0:
        print('There are no students in list.')
        return

    while True:
        student_id = input('Please enter the Student ID to be updated: ')
        if validation.valid_int(student_id):
            break

    student_index = find_student_index(students, int(student_id))
    first_name = students[student_index][1]
    last_name = students[student_index][2]

    if student_index == -1:
        print(f'Student ID #{student_id} was not found.')

    else:
        phrase = f'Do you want to update Student ID #{student_id} {first_name} {last_name} (y/n): '
        valid_res = validation.valid_yes_no(phrase)

        if valid_res:
            students[student_index][1] = string.capwords(
                input(f'Please enter the Student\'s First Name or press enter to keep {first_name}:'))
            students[student_index][2] = string.capwords(
                input(f'Please enter the Student\'s Last Name or press enter to keep {last_name}:'))

            if students[student_index][1] == '':
                students[student_index][1] = first_name
            if students[student_index][2] == '':
                students[student_index][2] = last_name

            first_name_update = students[student_index][1]
            last_name_update = students[student_index][2]
            print()

            if first_name_update == first_name and last_name_update == last_name:
                print('Student\'s name was not changed. Update was cancelled.!')
            else:
                print(f'Student ID #{student_id} {first_name} '
                      f'{last_name} was updated to {first_name_update} {last_name_update}.')

        else:
            print('Student\'s name was not changed. Update was cancelled.!')


def delete_student(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.

    param: students: student data (id, first_name, last_name)
    :type students: 2d list
    :return: None
    """
    if len(students) == 0:
        print('There are no students in list.')
        return

    while True:
        student_id = input('Please enter the Student ID to be deleted: ')
        if validation.valid_int(student_id):
            break

    student_index = find_student_index(students, int(student_id))
    first_name = students[student_index][1]
    last_name = students[student_index][2]

    if student_index == -1:
        print(f'Student ID #{student_id} was not found.')

    else:
        phrase = f'Please confirm deleting Student ID #{student_id} {first_name} {last_name} (y/n): '
        validate_res = validation.valid_yes_no(phrase)

        if validate_res:
            students.pop(student_index)
            print(f'Student ID #{student_id} {first_name} {last_name} was deleted.')

        else:
            print('Student delete cancelled!')
