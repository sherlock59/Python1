#!/usr/bin/env python3

import turtle
import random

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Anaberdi Meredov'
__version__ = '2.0'
__copyright__ = "Copyright 2022.05.12, Midterm assignment"
__github__ = "https://github.com/sherlock59/Python1.git"

ekran = turtle.Screen()           # used to control window
strelka = turtle.Turtle()         # used to control pointer
user_x = 0                        # center of screen moving right or left
user_y = 0                        # center of screen moving up or down
previous_x = 0                    # location of the user's circle if the user is getting closer or further away
previous_y = 0                    # location of the user's circle if the user is getting closer or further away
hidden_x = 100                    # hidden circle for right and left directions
hidden_y = 100                    # hidden circle for up and down directions
user_circle_color = 'red'         # the color of user's circle
hidden_circle_color = 'black'     # the color of the hidden circle
circle_size = 50                  # default circle size of 50 if user decides not to pick the size
move_size = 50                    # default move size of 50  if user decides not to pick the move size

center_pos = int(circle_size / 2) * -1  # assigns center position for user's circle


def debug():
    """
    The function allows to find hidden circle by turning its original color into user visible color

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
    user_x -= move_size  # move to the left of center
    display_game()


def move_right():
    """
    Adding move_size to the x coordinate which will be used move the circle to the right
    then call display_game to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_x
    user_x += move_size  # move to the right of center
    display_game()


def move_up():
    """
    Add move_size to the y coordinate which will be used move the circle up
    then call display_game to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_y, move_size
    user_y += move_size  # move top of center
    display_game()


def move_down():
    """
    Subtract move_size from y coordinate which will be used move the circle to the down
    then call display_game to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_y
    user_y -= move_size  # move down of center
    display_game()


def set_hidden_location():
    """
    Randomizing hidden circle locations and initializing that the hidden circle
    must be +10 size apart from the user's circle

    Returns:
        None
    """
    global hidden_x, hidden_y, circle_size
    while True:
        hidden_x = random.randint(-400, 400)  # left and right position mix
        hidden_y = random.randint(-450, 450)  # bottom and top position max

        # making sure that the hidden circle isn't too close to the users circle
        if abs(hidden_x) > (circle_size * 2 + 10) and abs(hidden_y) > (circle_size * 2 + 10):
            break


def set_center_location():
    """
    Setting user's circle location to the center upon starting a game

    Returns:
        None
    """

    global user_x, user_y, center_pos  # changing value of user's circle, requires to declare global
    user_x = center_pos  # user's circle will be in the center of the screen moving right or left
    user_y = center_pos  # user's circle will be placed in the screen moving up or down


def setup_window():
    """
    Controls how the window looks.

    Returns:
        None
    """

    ekran.tracer(False)           # turn animation off which causes screen flickering as the circle gets redrawn
    ekran.title('Hot/Cold Game')  # title the title bar of the window
    ekran.bgcolor('black')        # set the window's background color
    ekran.setup(800, 900)         # the size of the window
    set_hidden_location()         # setting up hidden location of a circle into display to show

    # Below are setting up the keys to listen to and what function should be called
    ekran.onkeypress(display_game, "r")
    ekran.onkeypress(debug, "d")
    ekran.onkeypress(move_home, "h")
    ekran.onkeypress(move_up, "Up")
    ekran.onkeypress(move_down, "Down")
    ekran.onkeypress(move_right, "Right")
    ekran.onkeypress(move_left, "Left")
    ekran.listen()  # start listening for keys being pressed


def set_circle_colors():
    """
    Setting up hidden and user circles' color.
    The user's color will turn red if user gets closer to hidden circle and blue displays for opposite.
    If user's circle touches hidden color, then both will have similar color "yellow hidden and green yellow user's"

    Returns:
        None
    """

    global hidden_circle_color, user_circle_color, hidden_y, hidden_x

    # setting the amount the user's circle must overlap by the dimension of both circles together minus 10
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
    clear the screen and draw the circle based on the user_x & user_y coordinates

    Returns:
        None
    """

    strelka.hideturtle()      # don't show the icon
    strelka.speed('fastest')  # draw quickly

    # writing a text on the screen
    strelka.penup()             # don't want to see icon moving on the screen
    strelka.goto(-380, 300)     # from the current position which is center after clear, move left 350 up 350
    strelka.pencolor('yellow')  # text color
    strelka.write("Total moves = 'move_size' \n\n"
                  "Use arrows to move:\n"
                  "'d' = debug\n"
                  "'h' = home\n"
                  "'r' = reset", font=("Verdana", 12, "bold"))
    strelka.pendown()           # will begin drawing the outline above

    # drawing a user's circle
    strelka.penup()                       # don't want to see icon moving on the screen
    strelka.goto(user_x, user_y)          # move to the updated x (left-right) and y (up-down) location from center
    strelka.pendown()                     # start drawing the outline of the circle
    strelka.fillcolor(user_circle_color)  # fill color of the circle
    strelka.begin_fill()                  # start the fill of whatever is being drawn
    strelka.circle(circle_size)           # diameter of the circle
    strelka.end_fill()                    # done drawing the object to complete the fill


def draw_hidden_circle():
    """
    clear the screen and drawing hidden circle based on the hidden_x & hidden_y coordinates

    Returns:
        None
    """

    strelka.hideturtle()                    # don't show the icon
    strelka.speed('fastest')                # drawing quickly without slow motion

    # draw circle
    strelka.penup()                         # don't want to see icon moving on the screen
    strelka.goto(hidden_x, hidden_y)        # move to the updated x (left-right) and y (up-down) location from center
    strelka.pendown()                       # start drawing the outline of the circle
    strelka.fillcolor(hidden_circle_color)  # fill color of the circle
    strelka.begin_fill()                    # start the fill of whatever is being drawn
    strelka.circle(circle_size)             # diameter of the circle
    strelka.end_fill()                      # done drawing the object to complete the fill


def display_game():
    """
    Combines relevant functions declared above to make it easier and organized

    Returns:
        None
    """

    strelka.clear()       # clear the previous screen for the update circle location
    set_circle_colors()   # setting the user's and hidden circle colors
    draw_user_circle()    # draw the initial shape based on diameter
    draw_hidden_circle()  # draw the initial shape  based on diameter


def main():
    """
    The main function, used to test "Hot & Cold_Game"

    Returns:
        None
    """

    setup_window()         # configure how the turtle window screen will look like
    set_center_location()  # calling set center location to start the circle from the middle screen
    set_hidden_location()  # calling hidden circle function
    display_game()         # displaying game to make it visible for user to play
    ekran.mainloop()       # keeps the turtle window open until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
