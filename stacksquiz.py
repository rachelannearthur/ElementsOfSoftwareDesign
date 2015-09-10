class Stack (object):
  def __init__ (self):
    self.stack = []

 # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

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

def operate (oper1, oper2, token):
  if (token == '+'):
    return oper1 + oper2
  elif (token == '-'):
    return oper1 - oper2
  elif (token == '*'):
    return oper1 * oper2
  else:
    return oper1 / oper2


def rpn (s):
  stack = Stack()

  operators = ['+', '-', '*', '/']

  tokens = s.split()

  for item in tokens:
    if (item in operators):
      oper2 = stack.pop()
      oper1 = stack.pop()
      stack.push (operate (oper1, oper2, item))
    else:
      stack.push (float(item))

  return stack.pop()

def isBalanced(s):
  stack = Stack()
  for i in range (len(s)):
    symbol = s[i]
    if symbol == "(" or symbol == "[" or symbol == "{":
      stack.push(symbol)
    elif symbol == ")" or symbol == "]" or symbol == "}":
      if stack.isEmpty() or not isPaired(stack.peek(), symbol):
        return False
      else:
        stack.pop() 

  return stack.isEmpty()

def isPaired(a,b):
  pair1 = ['(',')']
  pair2 = ['[',']']
  pair3 = ['{','}']
  return (a in pair1 and b in pair1) or (a in pair2 and b in pair2) or (a in pair3 and b in pair3)

      
def main():
  s = input("Enter a series of parenthesis and brackets")
  
  print(isBalanced(s))

main()
