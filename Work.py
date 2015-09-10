
#  File: Work.py 

#  Description:  Computes the c lines of code that Vyasa has to write

#  Student Name:  Rachel-Anne Arthur

#  Student UT EID:  ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/28/2015

#  Date Last Modified: 3/28/2015



# function that computes the sum of a series
def compute_series(v, k):
  total = v
  p = 1
  lines_code = v // (k ** p)
  while (lines_code > 0):
    total += lines_code
    p += 1
    lines_code = v // (k**p)
  return total

# function that finds the lowest number of v lines of code he has to write
def find_lowest_v (n,k):
  lo = 0
  hi = n
  # initializes min_v to find lowest v that writes at least n lines of code
  min_v = n 
  while (lo <= hi):
    v = (lo + hi) // 2
    if (compute_series(v, k) > n):
      if v < min_v:
        min_v = v
      # continues binary search for ideal v (sum is = to n) 
      hi = v - 1
    elif (compute_series(v, k) < n):
      lo = v + 1
    else:
      return v
  # ideal v not found so returns minimum v
  return min_v

def main():

  # open the input file
  inFile = open("work.txt", "r")

  # read the number of test cases 
  num_cases = inFile.readline()
  num_cases = num_cases.strip()
  num_cases = int(num_cases)

  # go through each of the test cases
  for i in range (num_cases):
    
    # read the next line containing n and k 
    line = inFile.readline()
    line = line.strip()
    line = line.split()

    n = int(line[0])
    k = int(line[1])

    print(find_lowest_v(n, k))
    
main()




