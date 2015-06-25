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
        if symbol == '(' :
            s.push(symbol)
        else:
            if s.isEmpty():
                bal = False
                break
            else:
                s.pop()
           
    if bal and s.isEmpty():
        print True            
    else:
        print False
    
for line in f:
    balPar(line.strip())
f.close()                
