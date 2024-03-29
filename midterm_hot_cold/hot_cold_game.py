#!/usr/bin/env python3
import turtle
import random

__author__ = 'Annaberdi Meredov'
__version__ = '1.0'
__copyright__ = "Copyright 2022.05.4, Chapter 4 Assignment"
__github__ = "https://github.com/sherlock59/Python1.git"


# Screen setup
ekran = turtle.Screen()
ekran.colormode(255)
ekran.title("Hot & Cold")  # title bar of the window
ekran.bgcolor("black")     # set the window's background color
ekran.setup(700, 700)      # set the window's size
ekran.tracer(False)        # turn animation off which causes screen flickering as the circle gets redrawn

# setting up the locator
strelka = turtle.Turtle()
circle_size = 100   # set the difficulty of the game by the size of the circles
move_size = 100     # set the difficulty of the game by the size of the circles
num_moves = 0       # running total of the number of moves to find hidden circle
x = 0               # center of screen moving right or left
y = 0               # center of screen moving up or down
fill_color = 'red'  # the color of the circle

# previous location of the user's circle used to determine if the user is getting closer or further away
previous_x = 0
previous_y = 0

# used to control the hidden circle location
hidden_x = 0  # from the center of the screen right (+) left (-)
hidden_y = 0  # from the center of the screen up (+) down (-)

# Display the game instructions
strelka.penup()  # don't want to see icon moving on the screen
strelka.goto(-340, 200)  # from the current position which is center after clear, move left 350 up 350
strelka.pencolor('blue')  # text color
strelka.write("Welcome to the Hot & Cold game \n\n"
              "Instructions:\n\nFind a hidden circle by controlling arrows.\n"
              "The circle that you see, will turn to red(closer) or blue(father) \n"
              "To start a game, please proceed the request below", font=("Verdana", 15, "bold"))
strelka.pendown()


# getting user's input for the size of tte circle and the size of the movement
# if the user closes the input without entering a valid value
# then set the default sizes both to 50

try:
    circle_size = int(turtle.numinput('Circle', 'Size of circles (10 - 100)', minval=10, maxval=100))
    move_size = int(turtle.numinput('Circle', 'Size of move (10-100)', minval=10, maxval=100))
except:
    circle_size = 50
    move_size = 50

ekran.tracer(True)

user_color = 'blue' and 'red'  # the color of the user;s circle (closer) cold = blue , (further) hot=red
hidden_color = 'black'  # the default for the hidden is black to match the screen background color

while True:
    hidden_x = random.randint(-420, 420)  # left and right position mix
    hidden_y = random.randint(-300, 300)  # bottom and top position max

    # making sure that the hidden circle isn't too close to the users circle
    # can't be within twice the user's circle size +10
    if abs(hidden_x) > (circle_size * 2 + 10) and abs(hidden_y) > (circle_size * 2 + 10):
        break

# set the center location

# user's circle will be placed in the middle of the screen based on the circle size
# divide the circle size in half and then move to down (-y) and to the left (-x) by multiplying by -1
center_pos = int(circle_size / 2) * -1

x = center_pos  # user's circle will be in the center of the screen moving right or left
y = center_pos  # user's circle will be placed in the screen moving up or down


# set the amount the user's circle must overlap by the dimension of both circles together minus 10
overlap = circle_size * 2 - 10

# if the circle overlap then set both circles to different green colors
if abs(x - hidden_x) < overlap and abs(y - hidden_y) < overlap:
    hidden_color = 'green yellow'
    user_color = 'green'
else:
    # if the user's circle x location has changed then determine if they are closer or further away from previous x
    if previous_x != x:
        # if previous x distance is less than current x distance then set red otherwise blue
        if abs(previous_x - hidden_x) > abs(x - hidden_x):
            user_color = 'red'
        else:
            user_color = 'blue'

    # if the user's circle y location has changed then determine if they are closer or further away from previous y
    if previous_y != y:
        # if previous y distance is less than current y distance then set red otherwise blue
        if abs(previous_y - hidden_y) > abs(y - hidden_y):
            user_color = 'red'
        else:
            user_color = 'blue'

# store the current x, y to previous x,y to get ready for the new user's move
previous_x = x
previous_Y = y

# getting user's input for the size of tte circle and the size of the movement
# if the user closes the input without entering a valid value
# then set the default sizes both to 50
try:
    circle_size = int(turtle.numinput('Circle', 'Size of circles (10 - 100)', minval=10, maxval=100))
    move_size = int(turtle.numinput('Circle', 'Size of move (10-100)', minval=10, maxval=100))
except:
    circle_size = 50
    move_size = 50

#  Toggles debug mode making it easier to test the game.
#  If the hidden circle color is black (same as the background) change it to gray
#  otherwise change it back to black.
#  The redisplay the game based on current settings.

if hidden_color == ekran.bgcolor():
    hidden_color = 'gray'
else:
    hidden_color = 'black'

# Clearing all turtle drawings
strelka.clear()  # clears the drawings (restore method also could be used)



#   Draw the user's circle and the hidden circle

# draw hidden circle
strelka.goto(hidden_x, hidden_y)  # move to the updated x (left-right) and y (up-down) location from center
strelka.fillcolor(hidden_color)  # fill color of the circle
strelka.begin_fill()  # start the fill of whatever is being drawn
strelka.circle(circle_size)  # diameter of the circle
strelka.end_fill()  # done drawing the object to complete the fill

# draw circle
strelka.goto(x, y)
strelka.fillcolor(user_color)
strelka.begin_fill()
strelka.circle(circle_size)
strelka.end_fill()

# Display the hidden circle based on the circle size, hidden location (x,y) and hidden color

strelka.mainloop()