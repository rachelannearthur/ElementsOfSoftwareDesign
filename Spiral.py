#  File: Spiral.py

#  Description: Creates a spiral matrix of size dim*dim and returns a target number and 3x3 matrix of surrounding numbers.

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730 

#  Date Created: 1/28/2015

#  Date Last Modified: 1/31/2015


# Function that creates a spiral matrix of size dim * dim
def makeSpiral(dim):

# Make an empty matrix the correct size
  matrix = [[None] * dim for x in range(dim)]
 
# Fill in matrix
# Establish increments and starting coordinate 
  dx = -1
  dy = 0
  x = dim - 1
  y = 0

# Loop through numbers to fill the matrix starting from largest
  for i in range(dim ** 2, 0, -1):
    matrix[x][y] = i 

# Move to new coordinate in matrix
    newX = x+dx
    newY = y+dy

# Check that new point is within boundaries and not filled
    if (0 <= newX < dim) and (0 <= newY < dim) and (matrix[newX][newY] == None):
      x = newX
      y = newY
# If not, change direction of filling and continue
    else:
      dy,dx =-dx, dy
      x = x+dx
      y = y+dy
  return matrix


# Function that returns the location of target number in the matrix  
def findTarget(target, matrix):
  for x in range (len(matrix)):
    for y in range (len(matrix)):
      if matrix[x][y] == target:
        return x, y

# Function that creates 3x3 matrix around the target number
def makeTargetMatrix(x, y, matrix):
  submatrix = [[None] * 3 for x in range(3)]
  x = x-1
  y = y-1
  for i in range (3):
    for j in range (3):
      submatrix[i][j] = matrix[x+i][y+j] 
  return submatrix

def main():

# ask user for dimensions of square spiral
  dim = eval(input("Input dimensions of the square spiral:"))

# ask user for target number
  target = eval(input("Input target number:"))

# Check that dimension is odd
# If not then add 1
  if dim % 2 == 0:
    dim = dim + 1

# Check that target number is within range of spiral
  if (target < 1) or (target > dim**2):
    print ("Number not in range")

# Create spiral matrix of size dim * dim
  matrix = makeSpiral(dim)

# find target number in matrix
  x, y = findTarget(target, matrix)

# check if number is on outer edge
  if (x == dim - 1) or (y == dim - 1):
    print ("Number on Outer Edge.")
  else:
# create 3x3 submatrix around target number 
    submatrix = makeTargetMatrix(x, y, matrix)
# print out submatrix
    for i in range (3):
      for j in range(3):
        print (submatrix[j][i], end = " ") 
      print(end = "\n")

main()
