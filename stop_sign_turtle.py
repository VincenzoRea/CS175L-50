#Turtle_Graphics
#VincenzoRea1326998
#CS175L50
#Spring2022

import math
import turtle

#Named Constants 
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

#Size the windwo
turtle.setup (400, 400)



s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)
radius = diameter / 2

# Initialize the turtle
turtle.speed(ANIMATION_SPEED)

# Move the turtle to starting point
turtle.penup()
StartX = (radius-x) * (-1)
StartY = WINDOW_HEIGHT / 2 / 2 
turtle.goto(StartX, StartY)
turtle.pendown()
turtle.color("red")

# Draw the octagon
for x in range(8):
    turtle.forward(100)
    turtle.right(45)

# Display 'STOP'
turtle.penup()
turtle.goto(0, -(diameter/2/2))
turtle.write("STOP", align="center", font=("Courier New", 45, "bold"))
turtle.hideturtle()
