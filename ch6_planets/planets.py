#!/usr/bin/env python3

"""
This module contains functions related to drawing a cute pink star,
UCO( unidentified circle object ), rainbow dash, and sharp star with using turtle
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 4 Assignment"
__github__ = "https://github.com/sherlock59/Python1.git"


def earth():
     print("Earth is 25 million miles from Venus\n"
                    "Mercury is 37 million miles from Venus\n"
                    "Mars is 61 million miles from Venus\n"
                    "Jupiter is 394 million miles from Venus\n"
                    "Saturn is 773 million miles from Venus\n"
                    "Uranus is 1644 million miles from Venus\n"
                    "Neptune is 2704 million miles from Venus\n")


def jupiter():
    print("Earth is 25 million miles from Venus\n"
                         "Mercury is 37 million miles from Venus\n"
                         "Mars is 61 million miles from Venus\n"
                         "Jupiter is 394 million miles from Venus\n"
                         "Saturn is 773 million miles from Venus\n"
                         "Uranus is 1644 million miles from Venus\n"
                         "Neptune is 2704 million miles from Venus\n")


def mars():
   print("Earth is 25 million miles from Venus\n"
                         "Mercury is 37 million miles from Venus\n"
                         "Mars is 61 million miles from Venus\n"
                         "Jupiter is 394 million miles from Venus\n"
                         "Saturn is 773 million miles from Venus\n"
                         "Uranus is 1644 million miles from Venus\n"
                         "Neptune is 2704 million miles from Venus\n")


def mercury():
  print("Earth is 25 million miles from Venus\n"
                         "Mercury is 37 million miles from Venus\n"
                         "Mars is 61 million miles from Venus\n"
                         "Jupiter is 394 million miles from Venus\n"
                         "Saturn is 773 million miles from Venus\n"
                         "Uranus is 1644 million miles from Venus\n"
                         "Neptune is 2704 million miles from Venus\n")

def neptune():
    print.command.lower("Earth is 25 million miles from Venus\n"
                         "Mercury is 37 million miles from Venus\n"
                         "Mars is 61 million miles from Venus\n"
                         "Jupiter is 394 million miles from Venus\n"
                         "Saturn is 773 million miles from Venus\n"
                         "Uranus is 1644 million miles from Venus\n"
                         "Neptune is 2704 million miles from Venus\n")


def saturn():
     print("Earth is 25 million miles from Venus\n"
                         "Mercury is 37 million miles from Venus\n"
                         "Mars is 61 million miles from Venus\n"
                         "Jupiter is 394 million miles from Venus\n"
                         "Saturn is 773 million miles from Venus\n"
                         "Uranus is 1644 million miles from Venus\n"
                         "Neptune is 2704 million miles from Venus\n")


def uranus():
    print("Earth is 25 million miles from Venus\n"
                         "Mercury is 37 million miles from Venus\n"
                         "Mars is 61 million miles from Venus\n"
                         "Jupiter is 394 million miles from Venus\n"
                         "Saturn is 773 million miles from Venus\n"
                         "Uranus is 1644 million miles from Venus\n"
                         "Neptune is 2704 million miles from Venus\n")

def venus():
    print("Earth is 25 million miles from Venus\n"
                         "Mercury is 37 million miles from Venus\n"
                         "Mars is 61 million miles from Venus\n"
                         "Jupiter is 394 million miles from Venus\n"
                         "Saturn is 773 million miles from Venus\n"
                         "Uranus is 1644 million miles from Venus\n"
                         "Neptune is 2704 million miles from Venus\n")


def display_planets():
    print("Planets: Earth Jupiter Mars Mercury Neptune Saturn Uranus Venus")


def main():
    display_planets()

    while True:
        command = input("Please enter one of the above planet names or q to quit: ")
        if command.lower() == "Earth":
            earth()
        elif command.lower() == "Jupiter":
            jupiter()
        elif command.lower() == "Mars":
            mars()
        elif command.lower() == "Mercury":
            mercury()
        elif command.lower() == "Neptune":
            neptune()
        elif command.lower() == "Saturn":
            saturn()
        elif command.lower() == "Uranus":
            uranus()
        elif command.lower() == "Venus":
            venus()
            break
        else:
            print("Not a valid command. Please try again.\n")
        if command.lower() == "quit" or "q":
            print("Live long and prosper!")
        break


if __name__ == "__main__":
    main()


