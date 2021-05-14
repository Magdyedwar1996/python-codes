""""
Draw a pattern that will change each time the
program is run. Use the random function to pick
the number of lines, the length of each line and
the angle of each turn
"""
import random
from turtle import *
Random_Shap = Turtle()

lines = random.randint(3, 10)
length = random.randint(25, 200)
for i in range(lines):
    Random_Shap.forward(length)
    Random_Shap.right(360/ lines)

done()