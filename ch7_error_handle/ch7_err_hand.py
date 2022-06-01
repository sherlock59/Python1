#!/usr/bin/env python3
"""
one script that include multiple functions to read an input file
that outputs both valid and invalid data files.
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 7 assignment"
__github__ = "https://github.com/sherlock59/Python1.git"

import re
import csv

INPUT_FILENAME = 'input_data.csv'
VALID_FILENAME = 'valid.csv'
INVALID_FILENAME = 'invalid.csv'


def read_file(filename):
    """
    Reads files and organizes its postion as well as loops for rows to print valid and invalid values accordingly
    :param filename:
    :return:  None
    """
    with open(filename, mode='r', newline='') as input_file, open(VALID_FILENAME, mode='a', newline='') \
             as valid_file, open(INVALID_FILENAME, mode='a', newline='') as invalid_file:
        input_reader = csv.reader(input_file, delimiter='|')
        valid_output = csv.writer(invalid_file, delimiter=',')
        invalid_output = csv.writer(invalid_file, delimiter=',')

        for row in input_reader:
            try:
                id, name, email, phone = row
            except:
                row.insert(0, 'L')
                invalid_output.writerow(row)
                continue

            try:
                # Check id is integer
                int(id)
            except ValueError:
                row.insert(0, 'I')
                invalid_output.writerow(row)
                continue

            try:
                # Check if the name matches the patter "last name, first name"
                last_name, first_name = name.split(',')
            except:
                row.insert(0, 'N')
                invalid_output.writerow(row)
                continue

            try:
                email_pattern = re.compile(r'[a-z.A-Z0-9]+@[a-zA-Z]+\.[eduEDU]{3}')
                email_pattern.match(email)
            except:
                row.insert(0, 'E')
                invalid_output.writerow(row)
                continue

            try:
                phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
                phone_pattern.match(phone)
            except:
                row.insert(0, 'P')
                invalid_output.writerow(row)
                continue
            finally:
                valid_output.writerow(row)


def main():
    """
    This main does the job necessary to validate and show invalid outcome
    :return: None
    """
    try:
        read_file(INPUT_FILENAME)

    except FileNotFoundError:
        print('File not found!')
    except OSError:
        print('Cannot read the file!')
    finally:
        with open(VALID_FILENAME, mode='r') as valid_file, open(INVALID_FILENAME, mode='r') as invalid_file:

             print('----------------- Valid file data ------------------')
             for row in valid_file:
                 print(row)

             print('\n')

             print('----------------- Invalid file data -----------------')
             for row in invalid_file:
                 print(row)


if __name__ == '__main__':
    main()
