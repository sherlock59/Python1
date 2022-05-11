#!/usr/bin/env python3

import turtle
import random

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

ekran = turtle.Screen()  # used to control window
strelka = turtle.Turtle()

# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
user_x = 0  # center of screen moving right or left
user_y = 0  # center of screen moving up or down

# previous location of the user's circle used to determine if the user is getting closer or further away
previous_x = 0
previous_y = 0

hidden_x = 100
hidden_y = 100

user_circle_color = 'red'  # the color of the circle
hidden_circle_color = 'black'

circle_size = 50
move_size = 50

center_pos = int(circle_size / 2) * -1


def debug():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global hidden_circle_color
    if hidden_circle_color == ekran.bgcolor():
        hidden_circle_color = 'gray'
    else:
        hidden_circle_color = ekran.bgcolor()
        display_game()


def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_x, user_y
    user_x = 0  # center of screen moving right or left
    user_y = 0  # center of screen moving up or down
    display_game()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_x, user_y
    #user_x -= 20
    user_x -= move_size  # move to the left of center
    display_game()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_x
    #user_x += 20  # move to the right of center
    user_x += move_size
    display_game()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_y, move_size
    #user_y += 20  # move top of center
    move_size = ++user_y
    display_game()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global user_y
    user_y -= move_size  # move down of center
    display_game()


def set_hidden_location():
    global hidden_x, hidden_y, circle_size
    while True:
        hidden_x = random.randint(-400, 400)  # left and right position mix
        hidden_y = random.randint(-450, 450)  # bottom and top position max

        # making sure that the hidden circle isn't too close to the users circle
        # can't be within twice the user's circle size +10
        if abs(hidden_x) > (circle_size * 2 + 10) and abs(hidden_y) > (circle_size * 2 + 10):
            break


def set_center_location():
    global user_x, user_y, center_pos
    user_x = center_pos  # user's circle will be in the center of the screen moving right or left
    user_y = center_pos  # user's circle will be placed in the screen moving up or down


def setup_window():
    """
    Controls how the window looks.

    Returns:
        None
    """

    ekran.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn
    ekran.title('Hot/Cold Game')  # title the title bar of the window
    ekran.bgcolor('black')  # set the window's background color
    ekran.setup(800, 900)  # the size of the window

    set_hidden_location()

    # set up the keys to listen to and what function should be called
    ekran.onkeypress(strelka.clear, "r")
    ekran.onkeypress(debug, "d")
    ekran.onkeypress(move_home, "h")
    ekran.onkeypress(move_up, "Up")
    ekran.onkeypress(move_down, "Down")
    ekran.onkeypress(move_right, "Right")
    ekran.onkeypress(move_left, "Left")
    ekran.listen()  # start listening for keys being pressed


def set_circle_colors():
    global hidden_circle_color, user_circle_color, hidden_y, hidden_x

    # set the amount the user's circle must overlap by the dimension of both circles together minus 10
    overlap = circle_size * 2 - 10

    # if the circle overlap then set both circles to different green colors
    if abs(user_x - hidden_x) < overlap and abs(user_y - hidden_y) < overlap:
        hidden_circle_color = 'green yellow'
        user_circle_color = 'green'
    else:
        # if the user's circle x location has changed then determine if they are closer or further away from previous x
        if previous_x != user_x:
            # if previous x distance is less than current x distance then set red otherwise blue
            if abs(previous_x - hidden_x) > abs(user_x - hidden_x):
                user_circle_color = 'red'
            else:
                user_circle_color = 'blue'

        # if the user's circle y location has changed then determine if they are closer or further away from previous y
        if previous_y != user_y:
            # if previous y distance is less than current y distance then set red otherwise blue
            if abs(previous_y - hidden_y) > abs(user_y - hidden_y):
                user_circle_color = 'red'
            else:
                user_circle_color = 'blue'


def draw_user_circle():
    """
    clear the screen and draw the circle based on the x & y coordinates

    Returns:
        None
    """

    strelka.hideturtle()  # don't show the icon
    strelka.speed('fastest')  # draw quickly

    # write text on the screen
    strelka.penup()  # don't want to see icon moving on the screen
    strelka.goto(-380, 300)  # from the current position which is center after clear, move left 350 up 350
    strelka.pencolor('yellow')  # text color
    strelka.write("Total moves = 'move_size' \n\n"
                  "Use arrows to move:\n"
                  "'d' = debug\n"
                  "'h' = home"
                  "'r' = reset", font=("Verdana", 12, "bold"))
    strelka.pendown()

    # draw circle
    strelka.penup()
    strelka.goto(user_x, user_y)  # move to the updated x (left-right) and y (up-down) location from center
    strelka.pendown()  # start drawing the outline of the circle
    strelka.fillcolor(user_circle_color)  # fill color of the circle
    strelka.begin_fill()  # start the fill of whatever is being drawn
    strelka.circle(circle_size)  # diameter of the circle
    strelka.end_fill()  # done drawing the object to complete the fill


def draw_hidden_circle():
    """
    clear the screen and draw the circle based on the x & y coordinates

    Returns:
        None
    """

    strelka.hideturtle()  # don't show the icon
    strelka.speed('fastest')  # draw quickly

    # draw circle
    strelka.penup()
    strelka.goto(hidden_x, hidden_y)  # move to the updated x (left-right) and y (up-down) location from center
    strelka.pendown()  # start drawing the outline of the circle
    strelka.fillcolor(hidden_circle_color)  # fill color of the circle
    strelka.begin_fill()  # start the fill of whatever is being drawn
    strelka.circle(circle_size)  # diameter of the circle
    strelka.end_fill()  # done drawing the object to complete the fill


def display_game():
    strelka.clear()  # clear the previous screen for the update circle location
    set_circle_colors()  # setting the user's and hidden circle colors
    draw_user_circle()  # draw the initial shape based on diameter
    draw_hidden_circle()  # draw the initial shape  based on diameter


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """

    setup_window()  # configure how the turtle window screen will look like
    set_center_location()
    set_hidden_location()
    display_game()
    ekran.mainloop()  # keep the turtle window open until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
