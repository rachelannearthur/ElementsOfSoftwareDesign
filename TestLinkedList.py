#  File: TestLinkedList.py

#  Description: Program that tests the helper functions of the Linked List Class

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/8/2015

#  Date Last Modified: 4/13/2015


class Link (object):
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  # constructor
  def __init__(self):
    self.first = None

  # get number of links 
  def getNumLinks (self):
    count = 1
    current = self.first
    if current is None:
      return 0
    else:
      while current.next != None:
        count += 1
        current = current.next
    return count

  # Add data at the beginning of the list
  def addFirst (self, data): 
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink    

  # Add data at the end of a list
  def addLast (self, data): 
    newLink = Link(data)
    
    current = self.first
    if current is None:
      self.first = newLink
      return
    while (current.next != None):
      current = current.next
    current.next = newLink
    
  # Add data in an ordered list in ascending order
  def addInOrder (self, data): 
    newLink = Link(data)
    current = self.first
    prev = self.first
    if current is None:
      self.first = newLink
      return 
    elif self.first.data > data:
      newLink.next = self.first
      self.first = newLink
       
    while current.next != None and current.next.data < data:
      current = current.next 
    newLink.next = current.next
    current.next = newLink

  # Search in an unordered list, return None if not found
  def findUnordered (self, data): 
    current = self.first
    
    if current is None:
      return None
    while current.data != data:
      if current.next is None:
        return None
      else:
        current = current.next
    return current

  # Search in an ordered list, return None if not found
  def findOrdered (self, data): 
     current = self.first
     if current is None:
       return None
     while current.next != None:
       if current.next is None: 
         return None
       else:
         current = current.next
     if data > current.data:
       return None
     else:
       return current

  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
    current = self.first
    previous = self.first

    if current is None:
      return None

    while current.data != data:
      if current.next == None:
        return None
      else:
        previous = current
        current = current.next
    if current == self.first:
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    st = ''
    current = self.first
    count = 0 
    while current != None: 
      if count < 10:
        if current == self.first:
          st += str(current.data)
          current = current.next 
        else:
          st += '  ' + str(current.data)
          current = current.next
      else:
        st += '/n'
        count = 0 
    return st

  # Copy the contents of a list and return new list
  def copyList (self):
    current = self.first
    newList = LinkedList()
    newCurrent = self.first
    newList.first = newCurrent
    
    while current.next != None: 
      newCurrent.next = current.next
      current = current.next
      newCurrent = newCurrent.next

    return newList 

  # Reverse the contents of a list and return new list
  def reverseList (self): 
    newList = LinkedList()
    current = self.first
    while current != None: 
      newList.addFirst(current.data)
      current = current.next

    return newList

  # Sort the contents of a list in ascending order and return new list
  def sortList (self): 
    newList = LinkedList()
    current = self.first
    while current != None:
      newList.addInOrder(current.data)
      current = current.next
    return newList
      

  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
    previous = self.first
    current = self.first.next
    while current.next != None:
      if current.data > previous.data:
        previous = current
        current = current.next
      else: 
        return False
    return True

  # Return True if a list is empty or False otherwise
  def isEmpty (self): 
    return self.first is None

  # Merge two sorted lists and return new list in ascending order
  def mergeList (self, b): 
    newList = LinkedList()
    currentA = self.first
    currentB = b.first
    while currentA != None and currentB != None:
      if currentA.data < currentB.data:
        newList.addLast(currentA.data)
        currentA = currentA.next
      else:
        newList.addLast(currentB.data)
        currentB = currentB.next

    # if self is not empty write it out
    while currentA != None:
      newList.addLast(currentA.data)
      currentA = currentA.next
    # if b is not empty write it out
    while currentB != None: 
      newList.addLast(currentB.data)
      currentB = currentB.next

    return newList

  # Test if two lists are equal, item by item and return True
  def isEqual (self, b):
    if self.getNumLinks() != b.getNumLinks():
      return False
    else:
      currentA = self.first
      currentB = b.first
      while currentA.next != None:
        if currentA.data == currentB.data:
          currentA = currentA.next
          currentB = currentB.next
        else:
          return False
    return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates (self):
    newList = LinkedList()
    current = self.first
    while current != None: 
      if newList.findOrdered(current.data) != None: 
        current = current.next
      else:
        newList.addLast(current.data)
        current = current.next
    return newList 
