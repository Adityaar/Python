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
    def print_stack(self):
        print self.items   
        
for line in f:
    st = Stack()
    lst = line.strip().split()
    Mth = int(lst[len(lst)-1])

    #push all the elements to stack except the last one
    for i in range(len(lst)-1):
        st.push(lst[i])

    if st.size() >= Mth :
        for i in range(Mth-1):
            st.pop()
        print st.pop()        
f.close()
