# Faces_w_Functions.py
# Using functions, create a program that will create a repeated face
#     of different sizes
# Author: Mike Gilson
# Date: 7/26/19


# import graphics library
from graphics import *

# setting up Graphics window parameters - title, coordinate size and direction,
  # and background color
win = GraphWin("Faces with Functions", 300, 300)
win.setCoords(0.0, 0.0, 20.0, 20.0)
win.setBackground("light gray")

# setting up initial points for the faces to appear at
p1 = Point(5, 15)
p2 = Point(10, 10)
p3 = Point(15, 5)

    
# Creating initial circle to draw the head, based on formal parameters
    # and calling the leftEye, rightEye, and mouth functions.
def drawFace(center, radius, window):
    head = Circle(center, radius)
    head.setFill ("yellow")
    head.setWidth(1)
    head.draw (win)
    leftEye(center, radius)
    rightEye(center,radius)
    mouth(center,radius)

# defining the function to draw the left eye, using the radius for sizing
    # and for moving the eye to a scaleable location
def leftEye(center, radius):
    leftEye = Circle(center, radius*0.2)
    leftEye.move (radius*-0.3, radius*0.2)
    leftEye.draw (win)

# defining the function to draw the right eye, using the radius for sizing
    # and for moving the eye to a scaleable location
def rightEye(center, radius):
    rightEye = Circle(center, radius*0.2)
    rightEye.move (radius*0.3, radius*0.2)
    rightEye.draw (win)

# defining the function to draw the mouth, which required the getX and getY
    # commands to determine placement based off the center parameters.
    # This required defining Point variables for the line to be created.
def mouth(center, radius):
    mouthLength = radius*0.8
    mouthY = (center.getY() - (radius / 2))
    leftX = (center.getX() - (mouthLength / 2))
    rightX = (center.getX() + (mouthLength / 2))
    mouth = Line(Point(leftX, mouthY), Point(rightX,mouthY))
    mouth.draw (win)
    
# calling the drawFace function to draw three repeated faces of different sizes 
def main():
    drawFace(p1, 1, win)
    drawFace(p2, 2, win)
    drawFace(p3, 3, win)
    
main()

