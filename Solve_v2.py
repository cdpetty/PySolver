def associativity(operator):
    if operator in ['+','-']:
        return 3
    elif operator in ['*','/','%']:
        return 2
    elif operator == '^':
        return 1
    else:
        raise RuntimeError('Operator ' + operator + ' not valid')
        
def main():
    test = '3 + 4 * 5 / 6'
    rpn = ''
    stack = []
    
    operators = ['+','%','-','*','/']
    left = ['(','[','{']
    right = [')',']', '}']
    
    for x in test:
        print x
        if x == ' ':
            print 'Was a space'
            pass
        if x.isdigit():
            print 'Was a digit'
            rpn += x + ' '
        elif operators.__contains__(x):
            print 'Was an operator'
            if stack:
                while len(stack) == 0 and (operators.__contains__(stack[len(stack)]) and associativity(x) > associativity(stack[len(stack)])):
                    rpn += stack.pop() + ' '
                    if len(stack) == 0:
                        break
            stack.append(x)
        elif left.__contains__(x):
            print 'Left paren'
            stack.append(x)
        elif right.__contains__(x):
            print 'Right paren'
            val = stack.pop()
            while not left.__contains__(val):
                if len(stack) == 0:
                    raise RuntimeError('Missing a paren')
                rpn += val + ' '
                val = stack.pop()
    while stack:
        print 'getting rid of extra operators'
        rpn += stack.pop() + ' '
    print rpn
        
if __name__ == '__main__':
    main()
    
