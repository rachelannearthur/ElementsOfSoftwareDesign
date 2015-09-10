#  File: Geometry.py

#  Description: Program that develops and tests several geometric classes

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: February 11, 2015

#  Date Last Modified: February 15, 2015


import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y
  
  # get distance to another Point object
  def dist (self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  # create a string representation of a Point (x, y)
  def __str__ (self):
    return '(' + str(self.x) + ',' + str(self.y) + ')'

  # test for equality between two points
  def __eq__ (self, other):
    tol = 1.0e-18 
    return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

class Line (object):
  # constructor assign default values if user defined points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    if (abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y)):
      self.p1 = Point(0, 0)
      self.p2 = Point(1, 1)
    else: 
      self.p1 = Point(p1_x, p1_y)
      self.p2 = Point(p2_x, p2_y)

  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol = 1.0e-18
    return (abs(self.p1.y - self.p2.y) < tol)

  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol = 1.0e-18
    return (abs(self.p1.x - self.p2.x) < tol)

  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    if (self.is_parallel_y()):
      return float ('inf')
    else:
      return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  def y_intercept (self):
    return (self.p1.y - (self.p1.x * self.slope()))
 
  # determine the x-intercept of the line
  def x_intercept (self):
    return (-self.y_intercept() / self.slope())

  # determine if two lines are parallel
  def is_parallel (self, other):
    tol = 1.0e-18
    return (abs(self.slope() - other.slope()) < tol)

  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, other):
    tol = 1.0e-18
    return (abs(self.slope() - (-1 / other.slope())) < tol)

  # determine if a point is on the line or on an extension of it
  def is_on_line (self, p):
    tol = 1.0e-18
    return (abs((self.slope() * p.x + self.y_intercept()) - p.y) < tol)

  # determine the perpendicular distance of a point to the line
  def perp_dist (self, p):
    change_in_y = self.p1.y - self.p2.y
    change_in_x = self.p1.x - self.p2.x
    return (abs(change_in_y * p.x + change_in_x * p.y + self.y_intercept()) / (math.sqrt(change_in_y ** 2 + change_in_x ** 2))) 

  # determine the intersection point of two lines if not parallel
  def intersection_point (self, other):
    intersection_x = (other.y_intercept() - self.y_intercept()) / (self.slope() - other.slope())
    intersection_y = self.slope() * intersection_x + self.y_intercept()
    return Point(intersection_x, intersection_y)
   
  # determine if two points are on the same side of the line
  # return False if one or both points are on the line
  def on_same_side (self, p1, p2):
    if self.is_on_line(p1) or self.is_on_line(p2):
      return False
    else:
      change_in_y = self.p2.y - self.p1.y
      change_in_x = self.p2.x - self.p1.x
      side_p1 = change_in_y * p1.x + change_in_x * p1.y + (self.p1.x * self.p2.y - self.p2.x * self.p1.y) 
      side_p2 = change_in_y * p2.x + change_in_x * p2.y + (self.p1.x * self.p2.y - self.p2.x * self.p1.y)
      return (side_p1 < 0 and side_p2 > 0) or (side_p1 > 0 and side_p2 < 0)

  # string representation of the line - one of three cases
  # y = c
  # x = c
  # y = m * x + b
  def __str__ (self):
    if self.is_parallel_x():
      return "y = " + str(self.p1.y)
    elif self.is_parallel_y():
      return "x = " + str(self.p2.y)
    else:
      if (self.y_intercept() > 0):
        return "y = " + str(self.slope()) + " x + " + str(self.y_intercept())
      else:
        return "y = " + str(self.slope()) + " x - " + str(self.y_intercept() * -1)

class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point(x, y)

  # compute circumference
  def circumference (self):
    return 2 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius ** 2

  # determine if a point is inside the circle
  def is_inside_point (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):
    distance = self.center.dist(other.center)
    return (distance + other.radius) < self.radius

  # determine if the other circle intersects self
  def does_intersect_circle (self, other):
    distance = self.center.dist(other.center)
    return (self.radius + other.radius) > distance

  # determine if the line intersects circle
  def does_intersect_line (self, line):
    return line.perp_dist(self.center) < self.radius 

  # determine if the line is tangent to the circle
  def is_tangent (self, line):
    tol = 1.0e-18
    return (line.perp_dist(self.center) - self.radius) < tol

  # string representation of a circle
  # Radius: radius, Center: (x, y)
  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: (" + str(self.center.x) + ", " + str(self.center.y) + ")"    


def main():
  # open file "geometry.txt" for reading
  inFile = open("geometry.txt", "r")

  # read the coordinates of the first Point P
  p_coord = inFile.readline() 
  p_coord = p_coord.strip()
  p_coord = p_coord.split()
  p = Point(float(p_coord[0]), float(p_coord[1]))

  # read the coordinates of the second Point Q
  q_coord = inFile.readline()
  q_coord = q_coord.strip()
  q_coord = q_coord.split()
  q = Point(float(q_coord[0]), float(q_coord[1]))
  
  # print the coordinates of points P and Q
  print("Coordinates of P:", p)
  print("Coordinates of Q:", q)

  # print distance between P and Q
  distance = p.dist(q)
  print("Distance bewteen P and Q:", distance)

  # print the slope of the line PQ
  PQ = Line(p.x, p.y, q.x, q.y)
  print("Slope of PQ:", PQ.slope())

  # print the y-intercept of the line PQ
  print("Y-Intercept of PQ:", PQ.y_intercept())

  # print the x-intercept of the line PQ
  print("X-Intercept of PQ:", PQ.x_intercept())

  # read the coordinates of the third Point A
  a_coord = inFile.readline()
  a_coord = a_coord.strip()
  a_coord = a_coord.split()
  a = Point(float(a_coord[0]), float(a_coord[1]))
 
  # read the coordinates of the fourth Point B
  b_coord = inFile.readline()
  b_coord = b_coord.strip()
  b_coord = b_coord.split()
  b = Point(float(b_coord[0]), float(b_coord[1]))

  # print the string representation of the line AB
  AB = Line(a.x, a.y, b.x, b.y)
  print("Line AB:", AB)

  # print if the lines PQ and AB are parallel or not
  if PQ.is_parallel(AB):
    print ("PQ is parallel to AB")
  else:
    print ("PQ is not parallel to AB")

  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if PQ.is_perpendicular(AB):
    print ("PQ is perpendicular to AB")
  else: 
    print ("PQ is not perpendicular to AB")

  # print coordinates of the intersection point of PQ and AB if not parallel
  if not PQ.is_parallel(AB):
    print("Intersection Point of PQ and AB", PQ.intersection_point(AB))

  # read the coordinates of the fifth Point G
  g_coord = inFile.readline()
  g_coord = g_coord.strip()
  g_coord = g_coord.split()
  g = Point(float(g_coord[0]), float(g_coord[1]))

  # read the coordinates of the sixth Point H
  h_coord = inFile.readline()
  h_coord = h_coord.strip()
  h_coord = h_coord.split()
  h = Point(float(h_coord[0]), float(h_coord[1]))
 
  # print if the the points G and H are on the same side of PQ
  if PQ.on_same_side(g, h):
    print("G and H are on the same side of PQ")
  else:
    print("G and H are not on the same side of PQ")

  # print if the the points G and H are on the same side of AB
  if AB.on_same_side(g, h):
    print("G and H are on the same side of AB")
  else:
    print("G and H are not on the same side of AB")

  # read the radius of the circleA and the coordinates of its center
  circleA_coords = inFile.readline()
  circleA_coords = circleA_coords.strip()
  circleA_coords = circleA_coords.split()
  circleA = Circle(float(circleA_coords[0]), float(circleA_coords[1]), float(circleA_coords[2]))

  # read the radius of the circleB and the coordinates of its center
  circleB_coords = inFile.readline()
  circleB_coords = circleB_coords.strip()
  circleB_coords = circleB_coords.split()
  circleB = Circle(float(circleB_coords[0]), float(circleB_coords[1]), float(circleB_coords[2]))

  # print the string representation of circleA and circleB
  print("circleA:", circleA)
  print("circleB:", circleB)

  # determine if circleB is inside circleA
  if circleA.is_inside_circle(circleB):
    print("circleB is inside circleA")
  else:
    print("circleB is not inside circleA")

  # determine if circleA intersects circleB
  if circleA.does_intersect_circle(circleB):
    print("circleA does intersect circleB")
  else:
    print("circleA does not intersect circleB")

  # determine if line PQ (or extension) intersects circleA
  if circleA.does_intersect_line(PQ):
    print("PQ does intersect circleA")
  else:
    print("PQ does not intersect circleA")
 
  # determine if line AB (or extension) is tangent to circleB
  if circleB.is_tangent(AB):
    print("AB is a tangent to circleB")
  else:
    print("AB is not a tangent to circleB")

  # close file "geometry.txt"
  inFile.close()

main()

