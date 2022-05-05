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