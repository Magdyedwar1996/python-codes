"""
065
Write the numbers as shown below,
starting at the bottom of the number
one

"""
from turtle import *
numbers = Turtle()
numbers.pensize(15)

# number one
numbers.left(90)
numbers.forward(150)

# the way between one and two
numbers.right(90)
numbers.penup()
numbers.forward(75)
numbers.pendown()


# number two
numbers.forward(150)
numbers.right(90)

numbers.forward(75)
numbers.right(90)

numbers.forward(150)
numbers.left(90)

numbers.forward(75)
numbers.left(90)

numbers.forward(150)

# the way between two and three
numbers.penup()
numbers.forward(75)
numbers.pendown()

# number three
numbers.forward(100)
numbers.left(90)
numbers.forward(150)
numbers.left(90)
numbers.forward(100)
numbers.penup()
numbers.left(90)
numbers.forward(75)
numbers.left(90)
numbers.pendown()
numbers.forward(75)
done()