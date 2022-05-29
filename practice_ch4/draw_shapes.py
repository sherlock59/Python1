#!/usr/bin/env python3

import global_turtle
"""
This module contains functions related to drawing a cute pink star, 
UCO( unidentified circle object ), rainbow dash, and sharp star with using turtle
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Chapter 4 Assignment"
__github__ = "https://github.com/sherlock59/Python1.git"


def setup_window(bg_color='white'):
    """
    Controls how the window looks.

    Args:
        bg_color (str): the background color of the window

    Returns:
        None
    """

    global_turtle.wn.bgcolor(bg_color)
    global_turtle.wn.title('Star Turtle')
    global_turtle.wn.setup(500, 500)  # the size of the window


def draw_star(length=100, line_color='red', fill_color='blue'):
    """
    the draw_star function is used to draw a star

    Args:
        length (int): the square's side length (default 100)
        fill_color (str): the inside color of the square
        line_color (str): the outside line color of the square

    Returns:
        None
    """

    global_turtle.t.hideturtle()      # make the turtle invisible
    global_turtle.t.width(50)         # make the line width very fat :)
    global_turtle.t.shape("turtle")   # make the cursor look like a turtle instead of an arrow
    global_turtle.t.penup()           # don't draw when turtle moves
    global_turtle.t.goto(-100, -100)  # move the turtle to a location -100 x (left of center) -100 y (down of center)
    global_turtle.t.showturtle()      # make the turtle visible
    global_turtle.t.pendown()         # draw when the turtle moves

    global_turtle.t.color(line_color, fill_color)   # fills the color with turtle.t

    global_turtle.t.begin_fill()  # start the fill based on the next object being drawn

    # draw star
    for i in range(4):                     # loop for 4 times
        global_turtle.t.right(144)         # Turn turtle by 144 degree
        global_turtle.t.forward(length)    # Forward turtle by length units

    global_turtle.t.end_fill()  # stop the fill based on the last object that was drawn


def draw_spiral():
    """
    the draw_spiral function is use to draw a spiral

    Returns:
        None
    """

    global_turtle.t.speed(0)         # speed of the drawing
    global_turtle.t.hideturtle()     # make the turtle invisible
    global_turtle.t.shape("arrow")   # make the cursor look like a turtle instead of an arrow
    global_turtle.t.penup()          # don't draw when turtle moves
    global_turtle.t.goto(100, 100)   # move the turtle to a location -100 x (left of center) -100 y (down of center)
    global_turtle.t.showturtle()     # make the turtle visible
    global_turtle.t.pendown()        # draw when the turtle moves

    global_turtle.t.color('blue', 'orange')  # coloring fill for the arrow and drawings

    global_turtle.t.begin_fill()  # start the fill based on the next object being drawn

    for i in range(7):                   # loop for 7 times
        global_turtle.t.circle(5 * i)    # rotate 5 times
        global_turtle.t.circle(-5 * i)   # rotate -5 times in angle
        global_turtle.t.right(i)         # turn right toward loop

    global_turtle.t.end_fill()  # stop the fill based on the last object that was drawn


def draw_rainbow():
    """
    the draw_rainbow function is use to draw a rainbow dash

    Returns:
        None
    """

    global_turtle.t.speed(0)          # speed of the drawing
    global_turtle.t.hideturtle()      # make the turtle invisible
    global_turtle.t.shape("square")   # make the cursor look like a turtle instead of an arrow
    global_turtle.t.penup()           # don't draw when turtle moves
    global_turtle.t.goto(100, -100)   # move the turtle to a location -100 x (left of center) -100 y (down of center)
    global_turtle.t.showturtle()      # make the turtle visible
    global_turtle.t.pendown()         # draw when the turtle moves

    global_turtle.t.color('blue', 'orange')   # color fillings
    global_turtle.t.begin_fill()  # start the fill based on the next object being drawn
    global_turtle.t.colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']  # rainbow colors

    for x in range(40):                      # loop for 4 times
        global_turtle.t.speed(0)             # speed of the drawings
        global_turtle.t.pencolor(global_turtle.t.colors[x % 6])   # applies 6 ink colors to draw
        global_turtle.t.width(x // 1 + 1)    # width size adjustment
        global_turtle.t.forward(x)           # forwards pen to x position
        global_turtle.t.left(25)             # turns to the left
        global_turtle.t.end_fill()           # stop the fill based on the last object that was drawn


def draw_multiple():
    """
    the draw_multiple function is used to draw a constant star

    Returns:
        None
    """

    global_turtle.t.speed(5)              # speed of the drawing
    global_turtle.t.width(10)             # make the line width very fat :)
    global_turtle.t.shape("classic")      # make the cursor look like a turtle instead of an arrow
    global_turtle.t.penup()               # make a pen invisible
    global_turtle.t.goto(-100, 100)       # move the turtle to a location -100 x (left of center) 100 y (up of center)
    global_turtle.t.showturtle()          # make the turtle visible
    global_turtle.t.pendown()             # draw when the turtle moves
    global_turtle.t.color('black', 'brown')   # color fillings
    global_turtle.t.begin_fill()          # start the fill based on the next object being drawn
    global_turtle.t.end_fill()            # stop the fill based on the last object that was drawn

    for i in range(20):                   # loops 20 times
        global_turtle.t.forward(i * 10)   # forwards 10 times ahead
        global_turtle.t.right(144)        # turns to right 144
        global_turtle.t.reset()           # resets the whole drawings


def main():
    """
    The main function, used to test drawing shapes using the turtle library.

    Returns:
        no value
    """

    global_turtle.turtle_setup()       # create the window & turtle objects
    setup_window('lightblue')          # configure how the turtle window screen will look like
    draw_star(100, 'pink', 'red')      # draw the turtle star (length, outline, fill)
    draw_spiral()                      # draw the arrow spiral
    draw_rainbow()                     # draw the square rainbow
    draw_multiple()                    # draw the classic consistent star
    global_turtle.wn.mainloop()        # keep the turtle running until the user closes it
    global_turtle.screen_recreation()  # recreate the window screen after it's been closed


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
