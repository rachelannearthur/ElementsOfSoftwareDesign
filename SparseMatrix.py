#  File: SparseMatrix.py

#  Description: Tests helper functions of the Sparse Matrix class

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/13/2015

#  Date Last Modified: 4/16/2015


class Link (object):
  def __init__ (self, row, col, data, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = None

class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.num_rows = row      # number of rows
    self.num_cols = col      # number of columns
    self.matrix = None

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create new link
    newLink = Link (row, col, data)

    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      previous.next = newLink
      newLink.next = current
      return

    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next
      
    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
      current.data = data
      return

    # now insert newLink
    previous.next = newLink
    newLink.next = current

  # return a row of the sparse matrix
  def getRow (self, row_num):
    # create a blank list
    a = []

    # search for the row
    current = self.matrix
    if (current == None):
      return a

    while ((current != None) and (current.row < row_num)):
      current = current.next

    if ((current != None) and (current.row > row_num)):
      for i in range (self.num_cols):
        a.append (0)
      return a

    if ((current != None) and (current.row == row_num)):
      for j in range (self.num_cols):
        if (current.col == j):
          a.append (current.data)
          current = current.next
        else:
          a.append (0)

    return a
        

  # returns a column of the sparse matrix
  def getCol (self, col_num):
    # create a blank list
    a = []
    current = self.matrix    
    # search for the column

    while current != None and current.col < col_num: 
      current = current.next
      
    for j in range (self.num_rows):
      if current == None:
        a.append(0)
      elif current.row == j and current.col > col_num:
        a.append(0)
        while current != None and current.col != col_num:
          current = current.next
      elif current.row == j and current.col == col_num:
        a.append(current.data)
        current = current.next
        if current != None and current.col > col_num: 
          current = current.next
        while current != None and current.col < col_num:
          current = current.next
      else: 
        a.append(0)

    return a
    
  # adds two sparse matrices
  def __add__ (self, other):
   if (self.num_rows != other.num_rows) or (self.num_cols != other.num_cols): 
     return None
   new = SparseMatrix(self.num_rows, self.num_cols) 
   for i in range (self.num_rows):
     for j in range (self.num_cols):
       num = (self.getCol(j)[i] + other.getCol(j)[i])
       new.insertLink(i, j, num)
   return new
  # multiplies two sparse matrices
  def __mul__ (self, other):
    if (self.num_cols != other.num_rows):
      return None
    new = SparseMatrix(self.num_rows, other.num_cols)
    for i in range (self.num_rows):
      for j in range (other.num_cols):
        sum = 0
        for k in range (other.num_rows):
          num = other.getCol(j)[k] * self.getRow(i)[k]
          sum += num
        new.insertLink(i,j, sum)
    return new

  # returns a string representation of a matrix
  def __str__ (self):
    s = ''
    current = self.matrix

    # if the matrix is empty return blank string
    if (current == None):
      return s

    for i in range (self.num_rows):
      for j in range (self.num_cols):
        if ((current != None) and (current.row == i) and (current.col == j)):
          s = s + str (current.data) + " "
          current = current.next
        else:
          s = s + "0 "
      s = s + "\n"

    return s

  
# reads the matrix from a file
def readMatrix (inFile):
  line = inFile.readline()
  line = line.strip()
  line = line.split()
  row = int (line[0])
  col = int (line[1])

  mat = SparseMatrix (row, col)

  for i in range (row):
    line = inFile.readline()
    line = line.strip()
    line = line.split()
    for j in range (col):
      data = int (line[j])
      if (data != 0):
        mat.insertLink (i, j, data)
 
  # dummy read
  line = inFile.readline()

  return mat

# def main():
#   # populate the matrix
#   inFile = open ("matrix.txt", "r")
# 
#   print ("Test Matrix Addition")
#   matA = readMatrix (inFile)
#   print (matA)
# 
#   matB = readMatrix (inFile)
#   print (matB)
# 
#   matC = matA + matB 
#   print (matC)
# 
#   print ("\nTest Matrix Multiplication") 
#   matP = readMatrix (inFile)
#   print (matP)
#   matQ = readMatrix (inFile)
#   print (matQ)
# 
#   matR = matP * matQ
#   print (matR)
# 
# 
#   # close file
#   inFile.close()
# 
# main()

