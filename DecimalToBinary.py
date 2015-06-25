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
    
    st = ""
    if not line in ['\n','\r\n']:
        n = int(line.strip())
        
        if n == 0:
            st = str(n)
        else:
            while n > 0:        
                rem = n % 2
                s.push(rem)
                n = n // 2        
        
        while not s.isEmpty():
            st = st + str(s.pop())
        print st

f.close()        