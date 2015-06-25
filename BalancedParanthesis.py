import sys

f = open(sys.argv[1],'r')

class Stack:   
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
       
def balPar(symbols):
    s = Stack()   
    bal = True    
    for symbol in symbols:
        if symbol in "({[" :
            s.push(symbol)
        else:
            if s.isEmpty():
                bal = False
                break
            else:
                top = s.pop()
                if not isMatching(top,symbol):
                    bal = False
                    break
    if bal and s.isEmpty():
        print True            
    else:
        print False

def isMatching(o,c):
    s1="({["
    s2=")}]"
    return s1.index(o) == s2.index(c)

for line in f:
    balPar(line.strip())

f.close()                
