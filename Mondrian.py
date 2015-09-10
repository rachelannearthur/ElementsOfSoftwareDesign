import turtle, random

def drawLine(ttl, size, level_rec):

  # randomly decide if the line will be horizontal or vertical or there will be no line
  if level_rec <= 2:
    r = random.randint(1, 3)
  else:
    r = random.randint(0, 3)
  # randomly determine pen width
  w = random.randint(4,15)
  # randomly determine the position of the line
  d = random.randint(0,2)
  # set x and y coordinates to 0
  x = 0
  y = 0
  
  # if r is 0, draw no line
  if r == 1:
    return 
  # if r is 1, draw a vertical line
  elif r == 0:
    ttl.penup()
    ttl.goto(-1 *(size/1.618)-(size/2), -size/2)
    ttl.seth(90)
    ttl.width(w)
    ttl.pendown()
    ttl.forward(size)
  # if r is 2, draw a horizontal line
  else:
    ttl.penup()
    ttl.goto(-(size/2), -1 * (size/1.618)+(size/2))
    ttl.seth(0)
    ttl.width(w)
    ttl.pendown()
    ttl.forward(size)

def mondrian_Comp(ttl, level_rec, size):
  if level_rec < 1:
    return
  else: 
    drawLine(ttl,size, 1)


def main():

# print title
  print("Mondrian Composition")

# ask user for level of recursion
  level_rec = eval(input("Enter a level of recursion between 1 and 6: "))

# setup screen size
  turtle.setup(800,800,0,0)

# create Turtle object
  ttl = turtle.Turtle()
  size = 800
  mondrian_Comp(ttl, 1, size)

main()





