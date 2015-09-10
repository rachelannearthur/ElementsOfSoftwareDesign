#  File: BabyNames.py 

#  Description:  Allows a user to search a data base of 1000 most popular baby names

#  Student Name:  Rachel-Anne Arthur

#  Student UT EID:  ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/12/2015

#  Date Last Modified: 3/14/2015



# Function that determines if a name exists in the dictionary
def is_in_dictionary(name,dictionary):
  return name in dictionary

# Function that finds the decade with the highest ranking for a name
def find_highest_decade(name, dictionary):
   # set highest rank to lowest possible 
   highest_rank = 1001
   # set highest decade to lowest index possible
   highest_decade = 0
   for i in range(len(dictionary[name])):
     # if rank is higher, replace highest_rank and highest_decade
     if dictionary[name][i] > highest_rank:
       highest_rank = dictionary[name][i]
       highest_decade = i
   return highest_decade

# Function that returns all the rankings for a given name
def all_rankings(name, dictionary):
  return dictionary.get(name)

# Function that returns false if a ranking is not in the top 1000
def ranking_in_top(name,dictionary):
  for ranking in dictionary[name]:
    if ranking == 1001:
      return False
  return True

# Function that returns a list of names that have a rank in all the decades sorted by name
def names_in_all_decades(dictionary):
  result = []
  for name in dictionary: 
    if ranking_in_top(name, dictionary):
      result.append(name)
  result.sort()
  return result

# Function that returns a list of all the names that have a rank in a given decade sorted by name
def names_in_decade(decade, dictionary):
  result = []
  for key,value in dictionary.items():
    if value[decade] != 1001:
      result.append(key)
  return result

# Function that determines if a list is strictly ascending
def is_ascending(name, dictionary):
  for i in range(len(dictionary[name])-1): 
    if dictionary[name][i] >= dictionary[name][i+1]:
      return False
  return True 

# Function that determines if a list is strictly descending
def is_descending(name, dictionary):
  for i in range(len(dictionary[name]) - 1):
    if dictionary[name][i] <= dictionary[name][i+1]:
      return False
  return True 

# Function that displays all names in sorted order that are getting more popular every decade
def names_more_popular(dictionary):
  more_pop = []
  for name in dictionary:
    if is_descending(name, dictionary):
      more_pop.append(name)
  more_pop.sort()
  print(str(len(more_pop)) + " names are more popular in every decade.") 
  for elt in more_pop:
    print(elt)

# Function that displays all names in sorted order that are getting less popular in every decade
def names_less_popular(dictionary):
  less_pop = []
  for name in dictionary:
    if is_ascending(name, dictionary): 
      less_pop.append(name)
  less_pop.sort()
  print(str(len(less_pop)) + " names are less popular in every decade.")
  for elt in less_pop:
    print(elt)

def main():
  # open the baby names file for reading
  inFile = open("names.txt", "r")
  
  # initialize and empty dictionary for the baby names
  baby_names = {}
  
  # for each name, add the name as a key in the dictionary and the list of numbers as the value
  for line in inFile:
    line = line.strip()
    line = line.split()
    # if there is a 0 in the baby name ranking, change it to be 1001
    for i in range (1,12):
      # convert rankings into integers
      line[i] = int(line[i])
      if line[i] == 0:
        line[i] = 1001
    baby_names[line[0]] = line[1:]
  
  # create dictionary of decade names for easier output
  decades = {}
  start = 1900
  for j in range(11):
    decades[j] = start
    start += 10

  # Set user choice to arbitrary number for first run of options
  user_choice = 0

  # While user input is not 7, loop through options
  while user_choice != 7:
 
    # Print options and ask user for input
    print()
    print("Options:")
    print("Enter 1 to search for names.")
    print("Enter 2 to display data for one name.")
    print("Enter 3 to display all names that appear in only one decade.")
    print("Enter 4 to display all names that appear in all decadess.")
    print("Enter 5 to display all names that are more popular in every decade.")
    print("Enter 6 to display all names that are less popular in every decade.")
    print("Enter 7 to quit.")
    print()

    user_choice = eval(input("Enter choice: "))

    # Searches for names
    if user_choice == 1:
      name = input("Enter a name: ")
      if is_in_dictionary(name, baby_names):
        print()
        print("The matches with their highest ranking decade are: ")
        print(name, decades[find_highest_decade(name, baby_names)])
      else:
        print()
        print(name + " does not appear in any decade.") 

    # Displays all data for one name
    elif user_choice == 2:
      name = input("Enter a name: ")
      print()
      print(name + ":", end= " ")
      ranks = all_rankings(name, baby_names)
      for i in range(11):
        if ranks[i] == 1001:
          ranks[i] = 0
        print (ranks[i], end = " ")
      print()
      for d in decades:
        print (str(decades[d]) + ": " + str(ranks[d]))
 
    # Displays all names that appear in one decade
    elif user_choice == 3:
      user_decade = eval(input("Enter decade: "))
      print("The names are in alphabetical: ")
      for key in decades: 
        if decades[key] == user_decade:
          decade_names = names_in_decade(key, baby_names)
      decade_names.sort()
      for elt in decade_names:
        print(elt)
    
    # Displays all names that appear in all decades
    elif user_choice == 4:
      all_decades = names_in_all_decades(baby_names)
      all_decades.sort()
      print(str(len(all_decades)) + " names appear in every decade. The names are:")
      for elt in all_decades:
        print(elt)

    # Displays all names taht are more popular in every decade
    elif user_choice == 5:
      names_more_popular(baby_names)
    
    # Displays all names that are less popular in every decade
    elif user_choice == 6:
      names_less_popular(baby_names)

  # If 7 was entered, print "Goodbye."
  print()
  print("Goodbye.")

main()
