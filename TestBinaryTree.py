
#  File: TestBinaryTree.py

#  Description: Tests various functions of the Tree class

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/16/2015

#  Date Last Modified: 4/19/2015

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      self.inOrder (aNode.lChild)
      print (aNode.data)
      self.inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      preOrder (aNode.lChild)
      preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      postOrder (aNode.lChild)
      postOrder (aNode.rChild)
      print (aNode.data)

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
        isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
        successor.rChild = deleteNode.rChild

    return True

  # returns true if two binary trees are similar
  def isSimilar (self, otherTree):
    list1 = traversal(self.root)
    list2 = traversal(otherTree.root, a = [])
    return list1 == list2
        
  # prints out all nodes at the given level 
  def printLevel(self, level):
    if level == 0:
      return
    listLevel(level, self.root)
    print()
    return
    
  # Returns the height of the tree
  def getHeight(self):
    # subtract 1 because height includes the root
    return height(self.root) - 1
     
  # method that returns the number of nodes in the left subtree from the root and number of nodes in the right subtree from the root
  def numNodes(self):
    lStart = self.root.lChild
    rStart = self.root.rChild
    lCount = countNodes(lStart)
    rCount = countNodes(rStart)
    return lCount, rCount

# returns the height of a tree
def height(node):
  if node == None:
    return 0
  else:
    return max(height(node.lChild), height(node.rChild)) + 1
    
# counts all nodes of a tree starting with a parent node    
def countNodes(pNode):
  if (pNode == None):
    return 0
  return 1 + countNodes(pNode.lChild) + countNodes(pNode.rChild) 
    
# prints the nodes in a target level in the tree, helper for printLevel
def listLevel(level, node):
  if node == None:
    return None
  elif level == 1 and node.data != None:
    print(node.data, end = ' ' )
    
  listLevel(level-1,node.lChild)
  listLevel(level-1,node.rChild)
       
# returns a list of the inorder traversal of a tree
def traversal (aNode, a = []):
  if (aNode != None):    
    traversal (aNode.lChild, a)
    a.append (aNode.data)
    traversal (aNode.rChild, a)
  return a 
   
def main():
  # create 3 trees - two are the same and the third is different
  tree1 = Tree()
  tree1.insert(50)
  tree1.insert(30)
  tree1.insert(70)
  tree1.insert(10)
  tree1.insert(40)
  tree1.insert(60)
  tree1.insert(80)
  tree1.insert(7)
  tree1.insert(25)
  tree1.insert(38)
  tree1.insert(47)
  tree1.insert(58)
  tree1.insert(65)
  tree1.insert(77)
  tree1.insert(96)
  
  tree2 = Tree()
  tree2.insert(50)
  tree2.insert(30)
  tree2.insert(70)
  tree2.insert(10)
  tree2.insert(40)
  tree2.insert(60)
  tree2.insert(80)
  tree2.insert(7)
  tree2.insert(25)
  tree2.insert(38)
  tree2.insert(47)
  tree2.insert(58)
  tree2.insert(65)
  tree2.insert(77)
  tree2.insert(96)
 
  tree3 = Tree()
  tree3.insert(50)
  tree3.insert(30)
  tree3.insert(10)
  tree3.insert(40)
  tree3.insert(58)
  tree3.insert(55)
  tree3.insert(77)
  
  # tests the method isSimilar()
  print(tree1.isSimilar(tree2)) #check and print the boolean of tree1 == tree2
  print(tree1.isSimilar(tree3)) #check and print the boolean of tree1 == tree3
  
  # tests the method printLevel()
  # print various levels of 2 of the trees that are different
  tree1.printLevel(2) 
  tree1.printLevel(3) 
  tree1.printLevel(4) 
  tree3.printLevel(2)
  tree3.printLevel(3) 
  
  # tests the method getHeight()
  # gets the height of 2 trees that are different
  print(tree1.getHeight()) 
  print(tree3.getHeight()) 
  
  # test the method numNodes()
  # get the number of nodes in the left and right subtree of tree1
  l, r = tree1.numNodes()
  print(l)
  print(r)
  # get the number of nodes in the left and right subtree of tree3
  l2, r2 = tree3.numNodes()
  print(l2)
  print(r2)

main()

