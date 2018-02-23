#!/usr/bin/python3
import turtle
from turtle import Turtle, Screen

no_of_sides = input("Please enter the number of sides(2-12) you want to draw.\n")
no_of_sides = int(no_of_sides)

# Set Where to start draw
TURTLE_SIZE = 300
screen = Screen()
turtle.penup()
turtle.goto(TURTLE_SIZE - screen.window_width()/2 , screen.window_height()/2 - TURTLE_SIZE/4)
turtle.pendown()


turtle.color('green')
turtle.begin_fill()
turtle.speed(10)

for sides in range(no_of_sides):
    turtle.forward(100)
    turtle.right(360/no_of_sides)
    for side in range(no_of_sides):
        turtle.forward(50)
        turtle.right(360/no_of_sides)
    
# turtle.end_fill()
turtle.done()



# TURTLE_SIZE = 20

# screen = Screen()

# yertle = Turtle(shape="turtle", visible=False)
# yertle.penup()
# yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
# yertle.pendown()
# yertle.showturtle()

# screen.mainloop()