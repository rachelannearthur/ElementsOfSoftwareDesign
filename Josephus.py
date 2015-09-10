#  File: Josephus.py

#  Description: Prints out the solution to the Josephus problem

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/3/2015

#  Date Last Modified: 4/6/2015



class Link(object):
  # constructor
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next


class CircularList(object):
  # Constructor
  def __init__ (self): 
    self.first = None

 # Insert an element in the list
  def insert (self, item):
    newLink = Link(item)
    if self.first == None:
      self.first = newLink
      self.first.next = self.first
    else:
      current = self.first
      while current.next != self.first:
        current = current.next
      current.next = newLink
      newLink.next= self.first

  # Find the link with the given key
  def find (self, key):
    current = self.first
    
    while current.data != key:
      current = current.next

    return current
    
  # Delete a link with a given key
  def delete ( self, key ): 
    current = self.first
    previous = self.first
    
    if current == key:
      while previous.next != key:
        previous = previous.next
      print(self.first.data, end =  " ")
      self.first = self.first.next
      previous.next = self.first
    else:
      while current != key:
        previous = current
        current = current.next
      print(current.data, end = " " )
      previous.next = current.next         

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n ):
    current = self.find(start)
    previous = self.first

    while previous.next != self.find(start):
      previous = previous.next

    for i in range (n-1):
      previous = current
      current = current.next

    #delete current link
    self.delete(current)
    return current.next.data

  # Return a string representation of a Circular List
  def __str__ (self):
    st = "["
    current = self.first
    while current.next != self.first:
      st += str(current.data) + ', '
      current = current.next
    st += str(current.data) + ']'
    return st

def main():

  #open the infile 
  inFile = open('josephus.txt', 'r')
  
  # read in the number of soldiers
  num_soldiers = inFile.readline()
  num_soldiers = num_soldiers.strip()
  num_soldiers = int(num_soldiers)

  # read in the starting position
  start = inFile.readline()
  start = start.strip()
  start = int(start)
  
  # read in the elimination number
  n = inFile.readline()
  n = n.strip()
  n = int(n)

  # create a circular list of the soldiers
  s = CircularList()
  for i in range (1, num_soldiers + 1):
    s.insert(i)

  # print out the killing order
  for i in range(num_soldiers):
    start = s.deleteAfter(start,n)
  print()

  #close the inFile
  inFile.close()

main()



