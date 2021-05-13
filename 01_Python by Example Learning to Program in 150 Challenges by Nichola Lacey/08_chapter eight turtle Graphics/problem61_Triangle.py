"""
061
Draw a triangle.
"""
# import all the libraries from the turtle
from turtle import *
turtle1 = Turtle()

def DrawTriangle(t,n,length):
    for i in range(n):
        t.forward(length)
        t.left(360 / n)

DrawTriangle(turtle1 ,3 , 200)
done()