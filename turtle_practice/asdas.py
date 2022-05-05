import turtle
import random
wn = turtle.Screen()  # creen "window"
wn.title('hefra')
t = turtle.Turtle()  # pointer
t.speed(5)
wn.colormode(255)




t.forward(100)
t.right(190)
t.forward(213)

turtle.setup(1000, 1000)

t.clear()  # just leaves it where it was # t.reset brings back to position

for i in range(4):
    t.forward(100)
    t.right(90)   # cubes

t.reset()

t.begin_fill() #fills the color
for i in range(3):
    t.forward(150)
    t.forward(150)
    t.left(120)
t.pencolor('red')
t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))# specify colors
t.width(5)  #"width of the pen"
t.end_fill()   #  will only with end_fill()


t.reset()

sideLen = wn.numinput('Triangle', 'enter side length:', 100, 10) #screen pop and does shaping itslef

t.begin_fill()
t.pencolor('orange')
t.width(60)
for i in range(3):
    t.forward(sideLen)
    t.left(120)

t.end_fill()

t.reset()

t.shape('turtle')  # shape of the icon
for i in range(10): # for if we know the range if not then while in help
    t.forward(random.randint(1, 100))  # moves forward from 1 to 100
    t.left(random.randint(0, 359))

#t.setposition(0, 0) # in the middle
#t.setposition(wn.window_width() / 2, 0)  # draws half screenside
#t.setposition(0, wn.window_height() / 2)
#t.setposition(0, -wn.window_height())












turtle.done() # or wn.exitonclick()