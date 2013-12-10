import sys


operators = ['+','%','-','*','/']
parens = ['(','[','{',')',']', '}']

def isOperator(x):
    return x in operators

def isParen(x):
    return x in parens


def parse(equation = ' '):
    spaced = []
    nospace = equation.replace(' ', '')
    prevprev = ''
    prev = ''
    counter = 0
    prevNums = []
    for x in nospace:
        if (isOperator(prev) and isParen(x)) or (prev.isdigit() and isParen(x)) or (prev.isdigit() and isOperator(x)) or (isParen(prev) and x.isdigit()) or (isParen(prev) and isOperator(x)):
            spaced.append(prev)
            spaced.append(' ')
        elif isOperator(prev) and x.isdigit():
            if isOperator(prevprev):
                spaced.append(prev)
        elif isOperator(prev) and isOperator(x):
            if x == '-':
                spaced.append(prev)
                spaced.append(' ')
            else:
                raise RuntimeError('Incorrect operator usage')
        else:
            if prev:
                spaced.append(prev)
        counter += 1
        prevprev = prev
        prev = x
        if len(nospace) == counter:
            spaced.append(x)
    print spaced
    main(spaced)

def pa(equation = ' '):
    spaced = []
    for x in equation:
        if x != ' ':
            spaced.append(x)
            spaced.append(' ')
    spaced.pop()
    print 'Before:', ''.join(spaced)
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
    print 'After:', fin
    main(fin)
            


def assoc(operator):
    if operator in ['+','-']:
        return 1
    elif operator in ['*','/','%']:
        return 2
    elif operator in ['^']:
        return 3
    else:
        raise RuntimeError('Operator specified does not exist: ' + operator)
    
def main(val):
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
    pa(sys.argv[1])