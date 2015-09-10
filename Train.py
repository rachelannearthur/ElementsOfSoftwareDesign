#  File: Train.py

#  Description: Draws a train using turtle graphics

#  Student Name: Rachel-Anne Arthur

#  Student UT EID:ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: Feb 20, 2015

#  Date Last Modified: Feb 22, 2015

import turtle, math

# Function that draws a line from (x1, y1) to (x2, y2)
def drawLine(ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto(x1, y1)
  ttl.pendown()
  ttl.goto(x2, y2)
  ttl.penup()
#function that draws a rectangle 
def drawRectangle (ttl, x, y, width, height): 
  ttl.penup()
  ttl.goto(x, y)
  ttl.pendown()
  ttl.goto(x, y - height)
  ttl.goto(x + width, y - height)
  ttl.goto(x + width, y)
  ttl.goto(x, y)
  ttl.penup()
#function that draws a circle
def drawCircle(ttl, x, y, radius):
  ttl.penup()
  ttl.goto(x, y-50)
  ttl.pendown()
  ttl.circle(radius)

#function that draws an arc 
def drawArc(ttl, x, y, radius):
  ttl.penup()
  ttl.goto(x, y)
  ttl.seth(90)
  ttl.pendown()
  ttl.circle(radius, 180)

def drawWheel(ttl, x, y, radius): 
  # draw outer part of wheel
  drawCircle(ttl, x, y, radius)
  # draw inner part of wheel
  drawCircle(ttl, x, y + radius/5, radius * 4/5)
  # draw center part of wheel
  drawCircle(ttl, x, y + radius * 5/6, radius * 1/6)

def drawSpokes(ttl, x, y, radius):
  ttl.penup()
  ttl.goto(x, y)
  ttl.seth(90)
  lengthSpokes = (radius * 4/5 - radius * 1/6) 
  numSpokes = 8
  angle = 360 / 8
  for i in range (numSpokes):
    ttl.pendown()
    ttl.forward(lengthSpokes)
    ttl.back(lengthSpokes)
    ttl.left(angle)

def main():
  
  # Create a turtle object
  ttl = turtle.Turtle()
  ttl.speed(0)
  # Setup a screen size of 800 x 800 
  turtle.setup(800, 800, 0, 0)
  # Change line width
  ttl.width(3)
  
  # Draw train tracks
  drawLine(ttl, -390, -300, 390, -300)
  drawLine(ttl, -390, -285, 390, -285)
  x = -365
  for rectangle in range (13):    
    drawRectangle (ttl, x, -300, 28, 8)
    x += 70

  # Draw wheels 
  ttl.color("red")     # change color to red
  big_x = -260
  big_y = -235
  drawWheel(ttl, big_x, big_y, 70) #draw single large wheel
  small_x = -20
  small_y = -235
  for i in range (2): #draw two small wheels
    drawWheel(ttl, small_x, small_y, 60)
    small_x += 200
  
  drawSpokes(ttl, big_x, big_y, 70)
  drawSpokes(ttl,small_x, small_y,60)
      
  # Draw train body
  # Draw cabin
  ttl.color("blue")    # change color to blue
  drawLine(ttl, -370, -215, -370, 75) 
  drawLine(ttl, -370, 75, -115, 75)
  drawLine(ttl, -115, 75, -115, -215)
  drawRectangle(ttl, -390, 85, 295, 10)
  
  # Draw front of train
  drawLine(ttl, -115, 50, 300, 50)
  drawLine(ttl, 300, 50, 300, -250)
 
  # Draw  bottom of train
  drawLine(ttl, -370, -215, -350, -215)
  drawLine(ttl, -170, -215, -100, -215)   
  drawArc(ttl, -170, -215, 90)
  drawLine(ttl, 60, -215,100 , -215)
  drawArc(ttl, 60, -215, 80)
  drawArc(ttl, 260, -215, 80)
  drawLine(ttl, 260, -215, 300, -215)
 
 # Draw details on outside of train
 # trapezoid on front
  drawLine(ttl, 300, -250, 380, -250)
  drawLine(ttl, 380, -250, 350, -175)
  drawLine(ttl, 350, -175, 300, -175) 
 # two rectangles on front 
  drawRectangle(ttl, 300, 25, 25, 150)
  drawRectangle(ttl, 325, -25, 10, 50)
 # two rectangles on top
  drawRectangle(ttl, 20, 75, 60, 25)
  drawRectangle(ttl, 35, 85, 30, 10)
 # two trapezoids on top
  drawLine(ttl, 185, 50, 170, 110)
  drawLine(ttl, 170, 110, 230, 110)
  drawLine(ttl, 230, 110, 215, 50)
  drawLine(ttl, 170, 110, 178, 130)
  drawLine(ttl, 178, 130, 222, 130)
  drawLine(ttl, 222,130, 230, 110)
 
  # Draw details on inside of train
  drawRectangle(ttl, -115, -50, 415, 10)
  dot_x = -108
  while dot_x < 300:
    ttl.goto(dot_x,-55)
    ttl.dot("black")
    dot_x += 10
  drawRectangle(ttl, 0, 50, 10, 100)
  dot_y = 48
  while dot_y > -50:
    ttl.goto(5, dot_y)
    ttl.dot("black")
    dot_y -= 10
  drawRectangle(ttl, 195, 50, 10, 100)
  dot_y = 48
  while (dot_y > -50):
    ttl.goto(200, dot_y)
    ttl.dot("black")
    dot_y -=10

  # Two filled windows
  ttl.fillcolor("grey")
  window_x = -330
  for j in range (2):
    ttl.begin_fill()
    drawRectangle(ttl,window_x, 45, 73, 90 )
    window_x += 103
    ttl.end_fill()

  # Persist drawing
  turtle.done()

main()

