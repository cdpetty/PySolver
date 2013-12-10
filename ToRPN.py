import sys


operators = ['+','%','-','*','/']
parens = ['(','[','{',')',']', '}']

def isOperator(x):
    return x in operators

def isParen(x):
    return x in parens


def parseUserInput(equation = ' '):
    spaced = []
    #for x in equation:
    #    if x != ' ':
    #        spaced.append(x)
    #        spaced.append(' ')
    #spaced.pop()
    prevprev = ''
    prev = ''
    counter = 0
    for x in spaced:
        if prev.isdigit() and x.isdigit():
            spaced.pop(counter - 1)
        if isOperator(prevprev) and (prev == '-' and x.isdigit()):
            spaced.pop(counter - 1)
        if x != ' ':
            prevprev = prev
            prev = x
        counter += 1
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
        raise RuntimeError('Operator specified does not exist: ' + operator)
    
def ToPoland(val):
    infix = val
    rpn = ''
    stack = []
    
    operators = ['+','%','-','*','/']
    left = ['(','[','{']
    right = [')',']', '}']
    for x in infix:
        if x == ' ':
            pass
        elif x.isdigit():
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
    print 'The RPN version is:', rpn

if __name__=='__main__':
    ToPoland(parseUserInput(sys.argv[1]))