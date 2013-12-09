test = '3 + 1 * 4'
rpn = ''
stack = []
final = ''
operators = ['+','%','-','*','/']
opens = ['(','[','{']
closes = [')',']', '}']
for x in test:
    if x == ' ':
        pass
    elif x.isdigit():
        rpn += x + ' '
    elif operators.__contains__(x):
        stack.append(x)
    elif opens.__contains__(x):
        stack.append(x)
    elif closes.__contains__(x):
        while stack[len(stack)] not in opens:
            if len(stack) ==0:
                raise RuntimeError
            else:
                rpn += stack.pop() + ' '
while stack:
    rpn += stack.pop() + ' '
print(rpn)
            
            
        