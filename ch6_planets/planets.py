#!/usr/bin/env python3

"""
This is an application that gives a accurate measurement for galaxy distances. It allows to pick
one particular planet and compare distance of it with rest of planets
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 6 Assignment"
__github__ = "https://github.com/sherlock59/Python1.git"

# Two horizontal lines
LINE_LENGTH = 70


# Defined a 2d tuple planets and their closest distance from the sun in millions of a mile
planets = (('Mercury', 29), ('Venus', 60), ('Earth', 91), ('Mars', 127),
           ('Jupiter', 460), ('Saturn', 839), ('Uranus', 1710), ('Neptune', 2770),
           ('Pluto', 2760))


def print_list(selected_planet, planet_list):
    """
    Displays the generated list for each planet's distance from the selected planet

    :param selected_planet:
    :param planet_list:
    :return:
    """
    for planet_info in planet_list:
        planet, distance = planet_info
        print(planet, 'is', distance, 'million miles from', selected_planet.capitalize())

    # Print empty line after
    print()


def calc_dist(selected_planet):
    """
    Calculating distance from the planets that's selected

    :param selected_planet:
    :return:
    """
    dist_from_planets = []

    # Looping all planets
    for planet_info in planets:
        planet_name, dist_from_sun = planet_info

        # Checking which planet the user selected
        if selected_planet.lower() == planet_name.lower():

            for planet_information in planets:
                planet, distance = planet_information

                # Escape the loop of the same planet
                if planet_name == planet:
                    continue

                # Appending calculated planets to 2D list
                else:
                    dist_from_planets.append([planet, abs(distance - dist_from_sun)])

    return dist_from_planets


def sort(ls):
    """
    Sorting the newly created list by using a lambda function

    :param ls:
    :return: None
    """
    ls.sort(key=lambda sub_ls: sub_ls[1])

    return ls


def display_planets():
    """
    Displays the all planet's names from the tuple list

    :Returns:
    None
    """
    print('=' * LINE_LENGTH)
    print("Planets: Earth Jupiter Mars Mercury Neptune Saturn Uranus Venus")


def main():
    """
    Main function that keeps the program looping until the user enters q for quit

    :return: None
    """
    while True:
        display_planets()
        command = input("Please enter one of the above planet names or q to quit: ")
        print('=' * LINE_LENGTH)

        # Command type q or quit to exit program
        if (command.lower() == 'q') or (command.lower() == 'quit'):
            print('Life is a curious thing, so explore it before GoodByes')
            break

        dist_from_planets = calc_dist(command)

        # If the loop finished and the distance list is empty, this means it's not an existing planet in out 2D tuple
        if len(dist_from_planets) == 0:
            print('Error! Unable to locate', command.capitalize(), 'in list,\n')

        # Print if the distance list is not empty
        if len(dist_from_planets) != 0:
            sorted_planets = sort(dist_from_planets)
            print_list(command.capitalize(), sorted_planets)


if __name__ == "__main__":
    main()
