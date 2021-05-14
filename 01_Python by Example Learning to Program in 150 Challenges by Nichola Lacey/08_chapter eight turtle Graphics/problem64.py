"""
064
Draw a five-pointed
star.
"""
from turtle import *
five_Star = Turtle()

five_Star.begin_fill()
for i in range(5):
    five_Star.color("red", "yellow")
    five_Star.left(144)
    five_Star.forward(100)
five_Star.end_fill()

done()