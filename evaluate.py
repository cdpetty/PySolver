import ToRPN as rpn
import sys

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

if __name__ == '__main__':
    if len(sys.argv) == 2:
        formatted = rpn.format(sys.argv[1])
        r = rpn.ToPoland(formatted)
        print 'RPN:', r
        evaluated = evaluate(r)
        print 'Evaluated to be:', evaluated