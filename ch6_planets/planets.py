#!/usr/bin/env python3

"""
This module contains functions related to drawing a cute pink star,
UCO( unidentified circle object ), rainbow dash, and sharp star with using turtle
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 4 Assignment"
__github__ = "https://github.com/sherlock59/Python1.git"


# Defined a 2d tuple planets and their closest distance from the sun in millions of a mile
planets = (('Mercury', 29), ('Venus', 60), ('Earth', 91), ('Mars', 127),
           ('Jupiter', 460), ('Saturn', 839), ('Uranus', 1710), ('Neptune', 2770),
           ('Pluto', 2760))


def display_planets():
    print("Planets: Earth Jupiter Mars Mercury Neptune Saturn Uranus Venus")


def main():
    planet_list = []

    display_planets()

    while True:
        command = input("Please enter one of the above planet names or q to quit: ")
        if command.lower() == "Earth":
            earth(planet_list)
            break
        elif command.lower() == "Jupiter":
            break
            jupiter(planet_list)
        elif command.lower() == "Mars":
            mars(planet_list)
            break
        elif command.lower() == "Mercury":
            mercury(planet_list)
        elif command.lower() == "Neptune":
            neptune(planet_list)
            break
        elif command.lower() == "Saturn":
            saturn(planet_list)
        elif command.lower() == "Uranus":
            uranus(planet_list)
        elif command.lower() == "Venus":
            venus(planet_list)
        else:
            print("Not a valid command. Please try again.\n")
        if command.lower() == "quit" or "q":
            print("Live long and prosper!")
            break


if __name__ == "__main__":
    main()


