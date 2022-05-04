#!/usr/bin/env python3

import global_turtle

"""
This module contains functions related to drawing a star using turtle
"""

__author__ = 'Annaberdi Merdov'
__version__ = '1.0'
__copyright__ = "Copyright 2022.05.04, Chapter 4 Assignment"
__github__ = ""


def setup_window(bg_color='white'):
    """
    Controls how the window looks.

    Args:
        bg_color (str): the background color of the window

    Returns:
        None
    """

    global_turtle.rusalka.bgcolor(bg_color)
    global_turtle.rusalka.title('Star Turtle')
    global_turtle.rusalka.setup(500, 500)  # the size of the window


def draw_star(length=50, line_color='purple', fill_color='orange'):
    """
    the draw_star_shape function is use to draw a star

    Args:
        length (int): the square's side length (default 150)
        fill_color (str): the inside color of the star
        line_color (str): the outside line color of the star

    Returns:
        None
    """

    global_turtle.zvezda.hideturtle()      # make the turtle invisible
    global_turtle.zvezda.width(30)         # make the line width very fat :)
    global_turtle.zvezda.shape("fish")   # make the cursor look like a fish instead of an arrow
    global_turtle.zvezda.penup()           # don't draw when turtle moves
   # global_turtle.zvezda.goto(-100, -100)  # move the turtle to a location -100 x (left of center) -100 y (down of center)
    global_turtle.zvezda.showturtle()      # make the turtle visible
   # global_turtle.zvezda.pendown()         # draw when the turtle moves

    global_turtle.zvezda.color(line_color, fill_color)

    global_turtle.zvezda.begin_fill()  # start the fill based on the next object being drawn

    # draw star
    for _ in range(0, 6):                # loop for 4 times
        global_turtle.zvezda.forward(length)  # Forward turtle by l units
        global_turtle.zvezda.right(90)         # Turn turtle by 90 degree

    global_turtle.zvezda.end_fill()  # stop the fill based on the last object that was drawn


def main():
    """
    The main function, used to test drawing a star using the turtle library.

    Returns:
        no value
    """

    global_turtle.turtle_setup()       # create the window & turtle objects

    setup_window('lightblue')          # configure how the turtle window screen will look like
    draw_star(200, 'pink', 'black')  # draw the turtle square (length, outline, fill)

    global_turtle.rusalka.mainloop()        # keep the turtle running until the user closes it

    global_turtle.screen_recreation()  # recreate the window screen after it's been closed


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
