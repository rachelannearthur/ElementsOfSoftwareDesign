def boxesNest(master_list, b, pos):
  if pos == 2:
    return True
  else:
    for i in range (len(b) - 1):
      if (master_list[b[i]][pos] < master_list[b[i+1]][pos]):
        return boxesNest(master_list, b, pos + 1)
      else:
        return False

def main():

  master_list = [[5,2,3],[4,5,6]]
  b = [0,1]
  print (master_list[b[0]][0])
main()







