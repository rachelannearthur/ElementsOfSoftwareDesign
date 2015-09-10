#  File: Graph.py

#  Description: create a graph from a file graph.txt Then traverse that graph using dfs, bfs, sssp, and sort topologically and by edge weight 

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 5/1/2015

#  Date Last Modified: 5/8/2015

class Stack(object):
  def __init__ (self):
    self.stack = []
  
  # add an item to the top of the stack
  def push (self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()
  
  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)
  
  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue(object):
  def __init__ (self):
    self.queue = []
  
  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return (self.queue.pop(0))

  def isEmpty(self):
    return len(self.queue) == 0
  
  def size(self):
    return len(self.queue) 

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False
 
 # determine if vertex was visited
  def wasVisited(self):
    return self.visited
 
  # determine the label of the vertex
  def getLabel(self):
    return self.label

  # return string representation of the label
  def __str__(self):
    return str(self.label)


class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
    return self.weight < other.weight

  def __le__ (self, other):
    return self.weight <= other.weight

  def __gt__ (self, other):
    return self.weight > other.weight

  def __ge__ (self, other):
    return self.weight >= other.weight

  def __eq__ (self, other):
    return self.weight == other.weight

  def __ne__ (self, other):
    return self.weight != other.weight 

class Graph (object):
  def __init__(self):
    self.vertices = []
    self.adjMat = []
    self.edges = []  
  # checks if a vertex label already exists
  def hasVertex (self,label):
    nVert = len(self.vertices)
    for i in range (nVert):
      if label == self.vertices[i].label:
        return True
    return False

  # add a vertex with a givel label
  def addVertex (self, label):
    if not self.hasVertex(label):
      self.vertices.append(Vertex(label))
      
      # add a new column in the adjacency matrix for new Vertex
      nVert = len (self.vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append(0)
      
      # add a new row for the new Vertex in adjacency matrix 
      newRow = []
      for i in range (nVert):
        newRow.append(0)
      self.adjMat.append(newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.edges.append(Edge(self.vertices[start], self.vertices[finish], weight))

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight
 
  # return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex (self,v):
    nVert = len(self.vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and not (self.vertices[i].wasVisited()):
        return i
    return -1
  
  # does a depth first search in a graph
  def dfs (self, v):
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.vertices[v]).visited = True
    print (self.vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop() 
      else:
        (self.vertices[u]).visited = True
        print (self.vertices[u])
        theStack.push(u)

    # stack is empty reset the flags
    nVert = len (self.vertices)
    for i in range (nVert):
      (self.vertices[i]).visited = False

  # does a breadth first search in a graph
  def bfs(self,v):
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.vertices[v]).visited = True
    print (self.vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.vertices[v2]).visited = True
        print (self.vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)

    # queue is empty reset the flags
    nVert = len (self.vertices)
    for i in range (nVert):
      (self.vertices[i]).visited = False
  
  # get index from vertex label
  def getIndex (self, label):
    for i in range (len(self.vertices)):
      if self.vertices[i].label == label:
        return i 
    
  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    if self.adjMat[fromVertexLabel][toVertexLabel] != 0: 
      return self.adjMat[fromVertexLabel][toVertexLabel]
    else:
      return -1

  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    neighbors = []
    idx = self.getIndex(vertexLabel)
    for j in range(len(self.adjMat[idx])): 
      if self.adjMat[fr][j] != 0: 
        neighbor = self.vertices[j].label
        neighbors.append(neighbor)
    return neighbors

  # get a copy of the list of vertices
  def getVertices (self):
    vertices = []
    for vertex in self.vertices:
      vertices.append(vertex.label)
    return vertices

  # determine if the graph has a cycle
  def hasCycle (self):
    nVert = len(self.vertices)
    visited = []
    # create a stack
    theStack = Stack()
    # mark the vertex as visited and push on the stack
    (self.vertices[0]).visited = True
    theStack.push(0)
     
    while not theStack.isEmpty():
      # get adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex(theStack.peek())
      if (u == -1): #there are no unvisited vertices
        u = theStack.pop()
      else:
        for i in range (nVert):
          if (self.adjMat[u][i] > 0) and (i in theStack.stack):
            self.vertices[u].visited = False
            return True
        self.vertices[u].visited = True
        theStack.push(u)
        visited.append(u)

    # the Stack is empty and reset the flags
    nVert = len (self.vertices)
    for i in range (nVert):
      (self.vertices[i]).visited = False

    return False
  # determines if a vertex has no incoming edges
  def noIncoming (self, vertexLabel): 
    for e in self.edges:
      if e.v.label == vertexLabel:
        return False
    return True
 
  # return a list of vertices after a topological sort
  def toposort (self):
    if self.hasCycle():
      return None
    # find vertex with no incoming before sorting
    start_vertices = []
    nVert = len(self.vertices)
    for i in range (nVert):
      start_flag = True
      for j in range(nVert):
        if (self.adjMat[j][i] != 0):
          start_flag = False
          break
      if start_flag == True:
        start_vertices.append(i)

    toposort = []
    theStack = Stack()
    for idx in start_vertices:
      theStack.push(idx)
      while not theStack.isEmpty():
        # get an adjacent unvisited vertex
        u = self.getAdjUnvisitedVertex(theStack.peek())
        if u != -1: 
          theStack.push(u)
        else:
          no_next_index = theStack.pop()
          (self.vertices[no_next_index]).visited = True
          toposort.append(self.vertices[no_next_index].label)
      
    # the stack is empty and reset the flags
    nVert = len (self.vertices)
    for i in range (nVert):
      (self.vertices[i]).visited = False
    toposort.reverse()
    return toposort
 
  # prints a list of edges in ascending order of their weights
  # list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
  def edgeList (self):
    for i in range (len(self.edges) - 1): 
      min = self.edges[i]
      minIdx = i
  
      for j in range (i + 1, len(self.edges)):
        if (self.edges[j].weight < min.weight): 
          min = self.edges[j]
          minIdx = j
      
      self.edges[minIdx] = self.edges[i]
      self.edges[i] = min
 
    for edge in self.edges: 
      e = edge.u.label + "--" + edge.v.label + " " + str(edge.weight)
      print (e) 
       

  # determine shortest path from a single vertex
  def shortestPath (self, fromVertexLabel):
    start = self.getIndex(fromVertexLabel)
    nVert = len(self.vertices)
    graphDict = {}
    for i in range (nVert):
      toVertex_indexes = []
      for j in range(nVert):
        if self.adjMat[i][j] != 0:
          toVertex_indexes.append(j)
      graphDict[i] = toVertex_indexes
    for i in range(nVert): 
      possible_paths = self.find_all_paths(graphDict, start, i)
      if possible_paths == []:
        print(fromVertexLabel + "-->" + self.vertices[i].label + " unreachable")
      else:
        cost_list = []
        for path in possible_paths:
          if len(path) == 1: 
            cost_list.append(0)
          else: 
            path_cost = 0
            for j in range(len(path) - 1): 
              path_cost += self.adjMat[path[j]][path[j+1]]
            cost_list.append(path_cost) 
        min_cost = min(cost_list)
        if (fromVertexLabel == self.vertices[i].label):
          print('', end= '')
        else:
          print(fromVertexLabel + "-->" + self.vertices[i].label + " " + str(min_cost))

  def find_all_paths(self,graphDict, start, end, path=[]):
    path = path + [start]
    if start == end:
      return [path]
    if not start in graphDict:
      return []
    paths = []
    for elt in graphDict[start]:
      if elt not in path:
        newpaths = self.find_all_paths(graphDict, elt, end, path)
        for newpath in newpaths:
          paths.append(newpath)
    return paths

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    self.adjMat[fromVertexLabel][toVertexLabel] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    idx = self.getIndex(vertexLabel)
    for v in self.vertices:
      if v.label == vertexLabel:
        self.vertices.remove(v)
    for i in range (len(self.vertices)):
      for j in range (len(self.adjMat[i])):
        if j == idx or i==idx:
          self.adjMat[i][j] = 0
        


def main():
  # create graph object
  cities = Graph()

  # open the file
  inFile = open("graph.txt","r")
  
  # read the vertices
  numVertices = int((inFile.readline()).strip())

  for i in range(numVertices):
    city = (inFile.readline()).strip()
    cities.addVertex(city)
 
  # read the edges
  numEdges = int((inFile.readline()).strip())
  
  for i in range(numEdges):
    edge = (inFile.readline()).strip()
    edge = edge.split()
    start = int(edge[0])
    finish = int(edge[1])
    weight = int(edge[2])
    cities.addDirectedEdge(start,finish,weight)

  # read the starting vertex for dfs,bfs, and shortest path
  startVertex = (inFile.readline()).strip()

  # close file
  inFile.close()

  # test depth first search
  print("DFS from " + startVertex + ":")
  cities.dfs(cities.getIndex(startVertex))
  print()

  # test breadth first search
  print("BFS from " + startVertex + ":")
  cities.bfs(cities.getIndex(startVertex))
  print()

  # test topological sort
  print("Topological Sort:")
  toposort = cities.toposort()
  for city in toposort:
    print (city)
  print()

  # test edge list in ascending order of weights
  print("Ascending Edges:")
  cities.edgeList()
  print()

  # test single source shortest path algorithm
  print("SSSP from " + startVertex + ":")
  cities.shortestPath(startVertex)    
  print()
main()


