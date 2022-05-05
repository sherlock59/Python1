import turtle
import random
telek = turtle.Screen()
telek.colormode(255)
turtle.setup(800, 600)

suka = turtle.Turtle()
suka.forward(50)
print(suka.position()) # shows the position on the terminal


(half_width, half_height) = telek.screensize()

suka.width(5)

(xpos, ypos) = suka.position()

suka.penup()
while xpos > -half_width and xpos < half_width and ypos > -half_height and ypos < half_height:
    suka.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    randColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    suka.pencolor(randColor)
    suka.right(random.randint(0, 359))
    suka.forward(random.randint(0, 359))
    suka.left(random.randint(0, 100))
    suka.stamp()
    (xpos, ypos) = suka.position()
    suka.penup()
    suka.setposition(0, 0) # comes to the middle and keep drawing from the middle
    suka.pendown()




turtle.done()



previous one:




def turtle_setup():


circle_size = 100   # set the difficulty of the game by the size of the circles
move_size = 100     # set the difficulty of the game by the size of the circles
num_moves = 0       # running total of the number of moves to find hidden circle
x = 0               # center of screen moving right or left
y = 0               # center of screen moving up or down
fill_color = 'red'  # the color of the circle


# Screen setup
ekran = turtle.Screen()
ekran.title("Hot & Cold")  # title bar of the window
ekran.bgcolor("white")  # set the window's background color
ekran.setup(width=1000, height=1000)  # set the window's size
ekran.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn
strelka = turtle.Turtle()


# previous location of the user's circle used to determine if the user is getting closer or further away
previous_x = 0
previous_y = 0

# current location of the user's circle
x = 0  # from the center of screen and used to move right (+) or left (-)
y = 0  # start at the center and used to move up (+) or down (-)

# used to control the hidden circle location
hidden_x = 0  # from the center of the screen right (+) left (-)
hidden_y = 0  # from the center of the screen up (+) down (-)

user_color = 'blue' 'red'  # the color of the user;s circle (closer) cold = blue , (further) hot=red
hidden_color = 'black'  # the default for the hidden is black to match the screen background color

while True:
    hidden_x = random.randint(-420, 420)  # left and right position mix
    hidden_y = random.randint(-300, 300)  # bottom and top position max

    # max sure the hidden circle isn't too close to teh users circle
    # can't be within twice the user's circle size +10
    if abs(hidden_x) > (circle_size * 2 + 10) and abs(hidden_y) > (circle_size * 2 +10):
        break

# set the center location

# user's circle will be placed in the middle of the screen based on the circle size
# divide the circle size in half and then move to down (-y) and to the left (-x) by multiplying by -1
center_pos = int(circle_size / 2) * -1

x = center_pos  # user's circle will be in the center of the screen moving right or left
y = center_pos  # user's circle will be placed in the screen moving up or down

# changing the circle color

# set the amount the user's circle must overlap by the dimension of both circles together minus 10
overlap = circle_size * 2 - 10

# if the circle overlap then set both circles to different green colors
if abs(x - hidden_x) < overlap and abs(y - hidden_y) < overlap:
    hidden_color = 'green yellow'
    user_color = 'green'
else:
    # if the user;s circle x location has changed then determine if they are closer or further away from previous x
    if previous_x != x:
        # if previous x distance is less than current x distance then set red otherwise blue
        if abs(previous_x  - hidden_x) > abs(x - hidden_x):
            user_color = 'red'
        else:
            user_color = 'blue'

    # if the user's circle y location has changed then determine if they are closer or further away from previous y
    if previous_y != y:
        # if previous y distance is less than current y distance then set red otherwise blue
        if abs(previous_y) > abs(y - hidden_y):
            user_color = 'red'
        else:
            user_color = 'blue'

# store the current x, y to previous x,y to get ready for the new user's move
previous_x = x
previous_Y = y

# getting user's input for the size of hte circle and the size of the movement
# if the user closes the input wihout entering a valid value
# then set the default sizes both to 50
try:
    circle_size = int(turtle.numinput('Circle', 'Size of circles (10 - 100)', minval=10, maxval=100))
    move_size = int(turtle.numinput('Circle', 'Size of move (10-100)', minval=10, maxval=100))
except:
    circle_size = 50
    move_size = 50


def debug():
    if ekran.bgcolor() == hidden_color:
        hidden_color == 'gray'
    else:
        hidden_color == 'black'


def display_game():
    ekran.clear()    # clears the screen itself
    strelka.clear()  # clears the drawings plus restore method also could be used for Jesus's sake
    user_color = fill_color('red')

def draw_circle():



def up():
     wn.setheading(90)
     wn.forward(100)

def down():
    wn.setheading(270)
    wn.forward(100)

def left():
    wn.setheading(180)
    wn.forward(100)

def right():
    wn.setheading(0)
    wn.forward(100)

turtle.listen()

turtle.onkey(up, 'up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()
