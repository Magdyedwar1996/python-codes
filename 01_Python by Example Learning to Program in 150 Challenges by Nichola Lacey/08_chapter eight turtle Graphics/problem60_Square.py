from turtle import *
turtle1 = Turtle()

# this is the first beginner way to draw a square
"""# first side
turtle1.forward(200)
turtle1.lt(90)

# second side
turtle1.forward(100)
turtle1.lt(90)

# third side
turtle1.forward(200)
turtle1.lt(90)

# fourth side
turtle1.forward(100)
turtle1.lt(90)
"""

# this is to draw a square
"""
for i in range(4):
    turtle1.forward(300)
    turtle1.left(90)
"""
# this is to draw a triangle
"""
for i in range(3):
    turtle1.forward(100)
    turtle1.left(120)
"""

# this function is to draw any geometric shape
def DrawShap(t,n,length):
    for i in range(n):
        t.forward(length)
        t.left(360 / n)


DrawShap(turtle1,4, 150)
done()
#(360/5)