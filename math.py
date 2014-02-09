import sys

class Evaluator(Object):
	"""Evaluator class evaluates rpn strings"""

	def operate(x, y, op):
		if op == '*':
			return x * y
		elif op == '+':
			return x + y
		elif op == '/':
			return y / x
		elif op == '-':
			return y - x
		
	def evaluate(rpn_string):
		stack = []
		for x in rpn_string:
			if x.isdigit():
				stack.append(x)
			elif rpn.isOperator(x):
				if len(stack) < 2:
					raise RuntimeError('Improper placement of values')
				val1 = int(stack.pop())
				val2 = int(stack.pop())
				result = operate(val1, val2, x)
				stack.append(result)
		return stack[0]

class RPN(object):
  operators = ['+','%','-','*','/']
  parens = ['(','[','{',')',']', '}']

  def isOperator(x):
      return x in operators

  def isParen(x):
      return x in parens

  def format(equation = ' '):
      spaced = []
      for x in equation:
          if x != ' ':
              spaced.append(x)
              spaced.append(' ')
      spaced.pop()
      prevprev = ''
      prev = ''
      for counter, x in enumerate(spaced):
          ##check for standard numbers
          if prev.isdigit() and x.isdigit():
              spaced.pop(counter - 1)
              
          ##check for negative numbers
          if isOperator(prevprev) and (prev == '-' and x.isdigit()):
              spaced.pop(counter - 1)
              
          ## Check for lack of operator in variable/digit combo "2x"
          if prev.isdigit() and x.isalpha():
              spaced.insert(counter, '*')
              spaced.insert(counter+1, ' ')
              spaced.insert(counter+2, x)
              spaced.insert(counter+3, ' ')
              
          ##ignore spaces
          if x != ' ':
              prevprev = prev
              prev = x
              
      fin = ''.join(spaced).split(' ')
      return fin
              


  def assoc(operator):
      if operator in ['+','-']:
          return 1
      elif operator in ['*','/','%']:
          return 2
      elif operator in ['^']:
          return 3
      else:
          raise RuntimeError('Operator specified does not exist: "' + operator + '"')
      
  def ToPoland(val):
      infix = val
      rpn = ''
      stack = []
      
      #operators = ['+','%','-','*','/']
      left = ['(','[','{']
      right = [')',']', '}']
      for x in infix:
          if x.isdigit() or x.isalpha():
              rpn += x + ' '
          elif x in operators:
              temp = ''
              if stack:
                  temp = stack[len(stack)-1]
              while stack and temp in operators:
                  if assoc(x) <= assoc(temp):
                      rpn += stack.pop() + ' '
                      if stack:
                          temp = stack[len(stack)-1]
                  else:
                      break
              stack.append(x)
          elif x in left:
              stack.append(x)
          elif x in right:
              if stack:
                  temp = stack[len(stack)-1]
                  while stack and temp not in left:
                      rpn += stack.pop() + ' '
                      if stack:
                          temp = stack[len(stack)-1]
                  if stack:
                      stack.pop()
                  else:
                      raise RuntimeError('Paren out of place')
          else:
              rpn += x + ' '
      while stack:
          rpn += stack.pop() + ' '
      rpn = rpn[:len(rpn)-1]
      ##print 'The RPN version is:', rpn
      return rpn

if __name__=='__main__':
    
