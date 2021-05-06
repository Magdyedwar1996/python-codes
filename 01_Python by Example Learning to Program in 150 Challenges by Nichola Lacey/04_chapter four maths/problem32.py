"""
032
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places
"""
import math
radius = float(input("Enter the radius of the cylinder:"))
length = float(input("Enter the depth of the cylinder  : "))
Area = (radius**2) * math.pi
Total_Volume = Area * length
Total_Volume = round(Total_Volume,3)
print("The total volume of the cylinder is : ", Total_Volume)


