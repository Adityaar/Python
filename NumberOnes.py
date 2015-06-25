import sys

f = open(sys.argv[1],'r')

'''
Decimal to Binary conversion
'''
class Stack:

    def __init__(self):    
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []

s = Stack()        
    
for line in f:
    cnt = 0    
    st = ""

    n = int(line.strip())
        
    '''if n == 0:
        st = str(n)
        print n
    else:
    '''        
    while n > 0:        
        rem = n % 2
        s.push(rem)
        n = n // 2        
        
    while not s.isEmpty():
        if s.pop() == 1:
            cnt += 1
    print cnt    
f.close()        