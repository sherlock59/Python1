#!/usr/bin/env python3

def list(student_list):
    if len(student_list) == 0:
        print("There are no students in the list.\n")
    else:
        for i, student in enumerate(student_list, start=1):
            print(f"{i}. {student[0]} ({student[1]})")
        print()


def add(student_list):
    id = input("ID:  ")
    fname = input("First name: ")
    lname = input("Last name: ")
    student = [id, fname, lname]
    student_list.append(student)
    print(f"{student[0]} was added.\n")


def update(student_list):
    if len(student_list) == 0:
        print('There are no students in the list.')
        return

    id = v.get_pos_num('Enter the ID of the student you would like to update: ')
    index = find_index(student_list, id)

    if index == -1:
        print('There is no student with this ID. Please try again.')
        return

    selected_student = student_list[index]
    id, fname, lname = selected_student

    user_confirm = v.get_yes_no(f'Do you want to update student ID # {id} {fname} {lname}')

    if user_confirm:
       new_fname = input('Please enter the student\s first name or press enter to keep ' +
                          student_list[id - 1][1] + ': '.title())
        return


def delete(student_list):
    number = int(input("Number: "))
    if number < 1 or number > len(student_list):
        print("Invalid student number.\n")
    else:
        student = student_list.pop(number - 1)
        print(f"{student[0]} was deleted.\n")


def display_menu():
    print("STUDENT MENU")
    print("1 - List all students")
    print("2 - Add a student")
    print("3 - Update a student")
    print("4 - Delete a student")
    print("0 - Exit program")
    print()


def main():
    student_list = [["Monty Python and the Holy Grail", 1975],
                  ["On the Waterfront", 1954],
                  ["Cat on a Hot Tin Roof", 1958]]

    display_menu()

    while True:
        command = input("Please enter a Menu # (Valid 0-4): ")
        if command.lower() == "1":
            list(student_list)
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
