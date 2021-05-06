"""
031
Ask the user to enter the radius of a circle
(measurement from the centre point to the edge). Work
out the area of the circle (π*radius2).
"""
import math
radius = int(input("Enter the radius plz : "))
Area = math.pi * radius**2
print("The Area of the circle is : ", round(Area,2))