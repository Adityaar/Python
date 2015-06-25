import sys

f = open(sys.argv[1],'r')

class Stack:
    def __init__(self):
        self.items = []        
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        
for line in f:
    st = Stack()
    lst = line.strip().split()

    for i in range(len(lst)):
        st.push(lst[i])
    s = st.size()
    
    for i in range(s):
        c = st.pop()
        if i%2 == 0:
            print c,
    print
        
f.close()
