"""
066
Draw an octagon that uses a different colour (randomly
selected from a list of six possible colours) for each line
"""
import random
from turtle import *
octagon = Turtle()
octagon.pensize(5)
octagon.begin_fill()
octagon.color("black", "yellow")
def DrawShap(t , n , length ):
    octagon.left(36)
    for i in range(n):
        t.forward(length)
        t.left(360 / n)
#DrawShap(octagon , 8 , 100 )
for j in range(0, 10):
    DrawShap(octagon , 8 , 100 )

octagon.end_fill()
done()
