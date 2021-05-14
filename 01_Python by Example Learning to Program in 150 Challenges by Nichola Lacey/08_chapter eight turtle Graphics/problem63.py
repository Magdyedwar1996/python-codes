"""
063
Draw three squares
in a row with a gap
between each. Fill
them using three
different colours
"""
from turtle import *
Squares = Turtle()

# this is the first square
Squares.begin_fill()
for i in range(4):
    Squares.color("blue","GREEN")
    Squares.forward(100)
    Squares.left(90)
Squares.end_fill()

Squares.left(180)
Squares.penup()
Squares.forward(100)
Squares.pendown()
#############################################################

# this is the second square
Squares.begin_fill()
for i in range(4):
    Squares.color("red","yellow")
    Squares.forward(100)
    Squares.right(90)
Squares.end_fill()

Squares.left(180)
Squares.penup()
Squares.forward(300)
Squares.pendown()
##############################################################

# this is the third square
Squares.begin_fill()
for i in range(4):
    Squares.color("black","orange")
    Squares.forward(100)
    Squares.left(90)
Squares.end_fill()

done()