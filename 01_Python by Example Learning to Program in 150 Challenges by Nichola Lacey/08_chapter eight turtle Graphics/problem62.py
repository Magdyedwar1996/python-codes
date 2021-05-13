"""
062
Draw a circle
"""
from turtle import *
turtle1 = Turtle()

def DrawCircle(t,n,length):
    for i in range(n):
        t.forward(length)
        t.left(360 / n)

DrawCircle(turtle1,360,3)
done()