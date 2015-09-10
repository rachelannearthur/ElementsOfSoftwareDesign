#  File: Boxes.py

#  Description: Computes the largest subset of nesting boxes for a list of boxes

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 2/26/2015

#  Date Last Modified: 2/26/2015


# Thisfunction computes all subsets of a list
x = []
def subsets (a, b, lo, master_list):
  hi = len(a)
  if (lo == hi):
    if boxesNest(master_list, b, 0):
      x.append(b)
      return x
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1, master_list)
    subsets (a, b, lo + 1, master_list)
  return x

# Function that checks if the values in two subsets nest
def boxesNest(master_list, b, pos):
  if len(b) <= 1:
    return False
  else:
    if pos == len(b) - 1:
      return True
    else:
      if master_list[b[pos]][0] < master_list[b[pos + 1]][0] and master_list[b[pos]][1] < master_list[b[pos + 1]][1] and master_list[b[pos]][2] < master_list[b[pos + 1]][2]:
        return boxesNest(master_list,b,pos+1)
      else:
        return False
 
# This function prints the boxes in subset by using indices for master_list        
def printBoxes(subset, master_list):
  for idx in range(len(subset)): 
    print("(" + str(master_list[idx][0]) + "," + str(master_list[idx][1]) + "," + str(master_list[idx][2]) + ")")


def main():

# Create a master list of boxes
  master_list = []

# Create a variable to keep track of the size of the largest subset of boxes that fit
  max_size = 0

# Create a list that will hold the list of subset of boxes that do fit having the max_size
  max_subsets = []

# Open file boxes.txt for reading and read first line that gives the number of boxes to follow (n)
  inFile = open("boxes.txt", "r")
  n = inFile.readline()
  n = n.strip()
  n = int(n)

# Read n lines of input
  for i in range (n):
    box = inFile.readline()
    box = box.strip()
    #For each line split and convert the strings to int
    box = box.split()
    for j in range (len(box)):
      box[j] = int(box[j])
    # Sort that list and append to master_list
    box.sort()
    master_list.append(box)

# Close file after reading all inputs
  inFile.close()

# Sort the master_list
  master_list.sort()

# Create a list of the indices of the master_list
  idx_list = [idx for idx in range (n)]
  
# Get all subsets of the indices that nest
  b = []
  nesting_subsets = subsets(idx_list, b, 0, master_list) 
 # If they do nest check against max_size
  for subset in nesting_subsets:  
    # If the length of the subset that nest is greater than max_size replace max_size with the length of the subset and the list max_subsets with the new subset
    if len(subset) > max_size: 
      max_size = len(subset)
      max_subsets = []
      max_subsets.append(subset)    
    # If the length of the subset that nest is equal to the max_size append that subset to the list max_subsets
    elif len(subset) == max_size:
      max_subsets.append(subset)
 
# Sort max subset of boxes max_subsets and print
  max_subsets.sort()
 
  if max_subsets == None:
    print ("No Nesting Boxes")
  else:
    print("Largest Subset of Nesting Boxes")
    for x in range(len(max_subsets)):
      for j in range(len(max_subsets[x])):
        print(master_list[j])
      print() 

main()
  


