""""
 Challenge 4 - Random Walk
"""
import turtle as t
import random

# making an object of the Turtle() and give it the name turtle1
turtle1 = t.Turtle()

t.colormode(255)

# this function is to choose a random color with  RGB
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

# this is to define the speed of Drawing the line
turtle1.speed("fastest")
# making the pensize 5
turtle1.pensize(2)


def Draw_Sprigraph(size_of_gape):
    for i in range(int(360/size_of_gape)):
        # choosing a random colour
        turtle1.color(random_color())
        # choosing the radius of the circle
        turtle1.circle(100)
        # changing the heading by adding 10 to the current heading , then draw a circle
        turtle1.setheading(turtle1.heading() + size_of_gape )
        turtle1.circle(100)

Draw_Sprigraph(5)
t.done()