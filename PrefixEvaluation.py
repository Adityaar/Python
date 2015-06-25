import sys

f = open(sys.argv[1],'r')

class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []

def compute(op1,opr,op2):
    if opr == "*":
        return op1 * op2
    elif opr == "/":
        return op1 / op2
    elif opr == "+":
        return op1 + op2
    else:
        return op1 - op2
        
for line in f:

    s = Stack()
    valid = True    
    expr = line.strip().split()
    '''
    Start scanning the list from right.
    If it is an operand, push to stack.
    if it is an operator, pop two elements, perform the operation and push the result to stack.
    Repeat until list is exhausted
    '''
    for ch in range(len(expr)-1,-1,-1):
        l = expr[ch] 
        if l not in "/+*":
             s.push(int(l))             
        elif not s.isEmpty() and l in "/*+" :
            oprnd1 = int(s.pop())
            oprnd2 = int(s.pop())
            val = compute(oprnd1,l,oprnd2)
            s.push(val)
        else:
            pass
            valid = False
    if valid:
        print s.pop()
f.close()