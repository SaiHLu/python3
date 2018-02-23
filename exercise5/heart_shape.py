#!/usr/bin/python3
import turtle
from turtle import *

turtle.left(90) # make the turtle face the top of the screen

screen = Screen()
SIZE = 300
turtle.penup()
turtle.goto(SIZE - screen.window_width()/2, screen.window_height()/2 - SIZE/4)
turtle.pendown()




# heart shape

# import matplotlib.pyplot as plt
# import numpy as np

# t = np.arange(0,2*np.pi, 0.1)
# x = 16*np.sin(t)**3
# y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
# plt.plot(x,y)
# plt.show()