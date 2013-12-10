import sys

def assoc(operator):
    if operator in ['+','-']:
        return 1
    elif operator in ['*','/','%']:
        return 2
    elif operator in ['^']:
        return 3
    else:
        return 4
    
def main():
    test = sys.argv[1].split(' ')
    print test
    rpn = ''
    stack = []
    
    operators = ['+','%','-','*','/']
    left = ['(','[','{']
    right = [')',']', '}']
    for x in test:
        if x == ' ':
            pass
        elif x.isdigit():
            print 'A digit was found'
            rpn += x + ' '
        elif x in operators:
            print 'An operator was found'
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
            print 'A left paren was found'
            stack.append(x)
        elif x in right:
            print 'A right paren was found'
            if stack:
                temp = stack[len(stack)-1]
                while stack and temp not in left:
                    rpn += stack.pop() + ' '
                    if stack:
                        temp = stack[len(stack)-1]
                if stack:
                    stack.pop()
        else:
            print 'An unknown character was encountered'
            rpn += x + ' '
    while stack:
        rpn += stack.pop() + ' '
    rpn = rpn[:len(rpn)-1]
    print 'The RPN version is:', rpn

if __name__=='__main__':
    main()