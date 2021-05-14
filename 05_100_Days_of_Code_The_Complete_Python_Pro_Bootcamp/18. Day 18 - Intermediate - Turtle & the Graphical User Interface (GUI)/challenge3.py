import random
from turtle import *
from random import *
colours = ["greenyellow","mediumblue","beige","yellow","darkmagenta",
          "blueviolet","deeppink","mediumpurple","mediumslateblue","dodgerblue"]

One_To_Ten_Shape = Turtle()

def DrawShap( number_sides ):
    for i in range(number_sides):
        One_To_Ten_Shape.forward(100)
        One_To_Ten_Shape.right( 360/number_sides )



for j in range(3 , 11):
   # One_To_Ten_Shape.begin_fill()
    One_To_Ten_Shape.color(choice(colours) , choice((colours)))
    DrawShap(j)
   # One_To_Ten_Shape.end_fill()


done()