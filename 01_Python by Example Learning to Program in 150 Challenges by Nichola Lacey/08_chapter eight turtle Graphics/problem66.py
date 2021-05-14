"""
066
Draw an octagon that uses a different colour (randomly
selected from a list of six possible colours) for each line
"""
import random
from turtle import *
octagon = Turtle()
colours = ["greenyellow","mediumblue","beige","yellow","darkmagenta",
          "blueviolet","deeppink","mediumpurple","mediumslateblue","dodgerblue"]

octagon.pensize(15)
def DrawShap(t , n , length):
    for i in range(n):
        t.color(random.choice(colours))
        t.forward(length)
        t.left(360 / n)

for i in range(5):
    DrawShap(octagon , 8 , 100)
done()
