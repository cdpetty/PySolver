test = '3 + 4'
rpn = ''
stack = []

operators = ['+','%','-','*','/']
left = ['(','[','{']
right = [')',']', '}']

def assoc(operator):
    if ['+','-'].__contains__(operator):
        return 1
    elif ['*','/','%'].__contains__(operator):
        return 2
    elif ['^'].__contains__(operator):
        return 3
    
def main():
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
                temp = stack[len(stack)]
            while stack and operators.__contains__(temp):
                if assoc(x) <= assoc(temp):
                    rpn += stack.pop() + ' '
                temp = stack[len(stack)]
                else:
                    break
            rpn += x + ' '
        elif x in left:
            print 'A left paren was found'
            stack.append(x)
        elif x in right:
            print 'A right paren was found'
            temp = stack[len(stack)]
            while not right.__contains__(temp):
                rpn += stack.pop() + ' '
                temp = stack[len(stack)]
            stack.pop()
        else:
            print 'An unknown character was encountered'
            rpn += x + ' '
    while stack:
        rpn += stack.pop() + ' '
    print 'The RPN version is:', rpn

if __name__=='__main__':
    main()