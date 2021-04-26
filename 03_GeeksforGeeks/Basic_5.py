'''
# Python program to find Area of a circle
'''
import math
def area(radius):
    PI = math.pi
    global area
    area = (PI)*(radius**2)
    return  area
radius =int(input("enter the radius : "))
circle_area = area(radius)
print("the area of the circle is %0.6f  "%(circle_area))
if area == circle_area:
    print("True")
else:
    print("False")