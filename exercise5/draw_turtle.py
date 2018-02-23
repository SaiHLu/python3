#!/usr/bin/python3
import turtle
from turtle import *

# turtle.forward(100)
# turtle.right(90)
# turtle.color('green')
# turtle.forward(100)
# turtle.done()

# forward(int) right(int) left(int) color('color_name') backward(int)
# done() => wait until you close the windows

# Drawing Single Rectangle

turtle.color('red', 'green')
turtle.begin_fill()
screen = Screen()
forward = 10
turtle.speed(10)
while True:
    turtle.forward(forward)
    turtle.right(90)
    if forward > screen.window_width()-120 and forward > screen.window_height()-120:
        turtle.right(45)
        turtle.forward(30)
        break
    forward += 10
turtle.end_fill()
turtle.done()
    

# Drawing Flower

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# print(abs(pos()))
# done()

# Draw Over and Over Rectangle 

# for steps in range(4):
#     turtle.forward(10)
#     turtle.right(90)
#     for next in range(4):
#         turtle.forward(50)
#         turtle.right(90)

# turtle.done()

# Draw Flower

# no_of_sides = 20

# # Set Where to start draw
# screen = Screen()
# SIZE = 300
# turtle.penup()
# turtle.goto(SIZE - screen.window_width()/2, screen.window_height()/2 - SIZE/4)
# turtle.pendown()


# turtle.color('green', 'yellow')
# turtle.speed(10)
# turtle.begin_fill()
# for steps in range(no_of_sides):
#     turtle.forward(50)
#     turtle.right(360/no_of_sides)
#     for next in range(no_of_sides):
#         turtle.forward(25)
#         turtle.right(360/no_of_sides)
# turtle.end_fill()
# turtle.done()