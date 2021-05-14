""""
 Challenge 4 - Random Walk
"""
import turtle as t
import random

turtle1 = t.Turtle()

# our colours
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# our possible directions
directions = [0, 90, 180, 270]

# this is to define the size of the line
turtle1.pensize(5)

# this is to define the speed of Drawing the line
turtle1.speed("fastest")

for i in range(2000):
    turtle1.color(random.choice(colours))
    turtle1.forward(20)
    turtle1.setheading(random.choice(directions))