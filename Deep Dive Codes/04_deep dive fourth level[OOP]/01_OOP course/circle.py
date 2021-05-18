#this project is to calculate the area and circumference of the circle
global radius
PI = 3.14
class circle :
    def __init__(self):
        print("Enter the radius of the circle : ")
        self.radius = int(input())
        if self.radius < 0 :
            print("You entered an invalid value for the radius!")
        else:
            pass

    ###########################
    def Area(self):
         area =PI * self.radius**2
         print("The area of the circle is ",area)

    ##############################################
    def circumference (self ):
        circum= 2*PI*self.radius
        print("the circumference of the circle is  ", circum)

circle1 = circle()
circle1.Area()
circle1.circumference()
