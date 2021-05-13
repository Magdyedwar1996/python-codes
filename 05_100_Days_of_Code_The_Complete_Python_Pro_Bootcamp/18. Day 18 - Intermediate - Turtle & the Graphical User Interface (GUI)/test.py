from turtle import Turtle, Screen

turtle1 = Turtle()
turtle1.shape("classic")
turtle1.color("Green")
# this is the traditional way to draw the square
"""
# side one
turtle1.forward(200)
turtle1.right(90)
# side two
turtle1.forward(200)
turtle1.right(90)
# side three
turtle1.forward(200)
turtle1.right(90)
# side four 
turtle1.forward(200)
turtle1.right(90)"""

for ____ in range(4):
    turtle1.forward(200)
    turtle1.right(90)
# this should be down the screen as it happens after all is done
screen = Screen()
screen.exitonclick()