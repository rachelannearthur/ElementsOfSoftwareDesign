#  File: BST_Cipher.py

#  Description: A binary tree encryption scheme

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928	

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/28/15

#  Date Last Modified: 4/28/15

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character that character is dropped.
  def __init__ (self, encrypt_str):
    st = ''
    for ch in encrypt_str:
      if  (ch > 'a' or ch < 'z') or ch == ' ': 
        st += ch
    
    self.root = None
    for ch in st:
      self.insert(ch)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    newNode = Node(ch)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ord(ch) < ord(current.data)):
          current = current.lChild
        elif(ord(ch) > ord(current.data)):
          current = current.rChild
        else:
          return
      if (ord(ch) < ord(parent.data)):
        parent.lChild = newNode
      elif (ord(ch) > ord(parent.data)):
        parent.rChild = newNode
      else: 
        return
  # searches for a character in the BST and returns a string containing
  # a series of lefts (<) and rights (>) needed to reach that character.
  # It will return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    st = ''
    current = self.root
    if current.data == ch: 
      st += '*'
    
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        current = current.lChild
        st += '<'
      else:
        current = current.rChild
        st += '>'
    
    if current == None and current.data != ch:
      return ''
    
    return st
  
  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    for i in range(len(st)):
      if st[i] == '*':
        return current.data
      elif st[i] == '<':
        current = current.lChild
      else:
        current = current.rChild
    return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    st = st.lower()
    encrypted_st = ''
    for ch in st:
      encrypted_st += self.search(ch)
      encrypted_st += '!'
    encrypted_st = encrypted_st[:len(encrypted_st) -1]
    return encrypted_st

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    decrypted_st = ''
    characters = st.split('!')
    for ch in characters:
     decrypted_st += self.traverse(ch)

    return decrypted_st

def main():
  f = open('input.txt')
  s=0
  while(s<8):
    
    key = f.readline()
    encode = f.readline()
    encode = encode.strip()
    decode = f.readline()
    decode = decode.strip()
    skip = f.readline()
    s+=1
    t = Tree(key)
    
    print(t.encrypt(encode))
    print(t.decrypt(decode))
    print()

main()
