""""
 Challenge 4 - Random Walk
"""
import turtle as t
import random

turtle1 = t.Turtle()

# our colours
"""
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
"""
t.colormode(255)

# this function is to choose a random color with  RGB
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

# our possible directions
directions = [0, 90, 180, 270]

# this is to define the size of the line
turtle1.pensize(7)

# this is to define the speed of Drawing the line
turtle1.speed("fastest")

for i in range(20):
    turtle1.color(random_color())
    turtle1.forward(20)
    turtle1.setheading(random.choice(directions))